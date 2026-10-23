"""Exact bounded implementation checks for the analytic broom-family proof."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib
import json
import random
import sys

ROOT = Path(__file__).resolve().parent
import verify_families as vf

X = {0, 1, 2, 4, 7, 8}
def side_with_edge(edge):
    return next(side for side, pairs in vf.SIDES if edge in pairs)
A = side_with_edge((0, 1))
C = side_with_edge((0, 8))
F = side_with_edge((7, 8))
B = tuple(v for v in range(16) if v not in A)
D = tuple(v for v in range(16) if v not in C)
E = tuple(v for v in range(16) if v not in F)


def exact_side(w, side):
    pairs = tuple((u, v) for u, v in vf.EDGES if u in side and v in side)
    return vf.match_half(w, side, pairs)


def independent_mass(w):
    return max(sum(w[v] for v in I) for I in vf.INDEPENDENT)


def check_vector(w, x):
    n = sum(w)
    assert len(x) == 16 and sum(x) == Q(n, 2)
    assert all(0 <= x[v] <= w[v] for v in range(16))
    assert 50 * vf.cost(x) <= n * n


def balanced_proof(w):
    w = list(map(Q, w))
    n = sum(w)
    if n == 0:
        return "zero", None
    d, e, t, a, c = (w[v] for v in (0, 8, 7, 1, 15))
    assert w[1] == w[2] == w[4]
    if c == 0:
        assert 2 * independent_mass(w) >= n
        return "zero_background_independent", None
    h = n / 2
    for label, side in (("B_heavy", B), ("D_heavy", D), ("E_heavy", E)):
        mass = sum(w[v] for v in side)
        if mass >= h:
            x = [w[v] * h / mass if v in side else Q(0) for v in range(16)]
            assert 64 * vf.cost(x) <= n * n
            check_vector(w, x)
            return label, x
    witnesses = ((0, 7, 11, 13, 14), (1, 2, 4, 8, 15),
                 (0, 3, 5, 9, 14), (3, 5, 6, 8, 15))
    for I in witnesses:
        assert all(not ((u, v) in vf.EDGES) for u, v in product(I, I) if u < v)
        if 5 * sum(w[v] for v in I) >= 2 * n:
            return "known_independence", None
    dn, en, tn, an, hn = (z / c for z in (d, e, t, a, h))
    nu = (dn + tn - 3 * an - en + 2) / 2
    H = 3 - hn / 5
    assert hn > 7 and hn < 15 and 0 < H and abs(nu) < H
    if hn <= 10:
        x = exact_side(w, C)
        T = (dn + en) / 2
        reference = w[:]
        reference[0] = reference[8] = (d + e) / 2
        y = exact_side(reference, C)
        assert x is not None and y is not None
        U = 3 + (hn - 6) ** 2 / 4
        assert vf.cost(x) <= vf.cost(y) <= c * c * U
        assert n * n / 50 - c * c * U > 0
        check_vector(w, x)
        return "central_edge_low_mass", x
    assert H <= 1
    selections = []
    for side, full, partial, amount in (
        (A, (0, 7), 1, c * (1 - nu)),
        (F, (8, 1, 2, 4), 7, c * (1 + nu)),
    ):
        x = [Q(0)] * 16
        for v in side:
            if v not in X:
                x[v] = c
        for v in full:
            x[v] = w[v]
        x[partial] = amount
        assert all(0 <= x[v] <= w[v] for v in range(16))
        assert sum(x) == h
        selections.append(x)
    cost_A = d * c * (1 - nu) + t * c + 2 * c * c
    cost_F = e * c * (1 + nu) + 3 * a * c
    assert vf.cost(selections[0]) == cost_A
    assert vf.cost(selections[1]) == cost_F
    assert (cost_A + cost_F) / 2 == c * c * (hn - 4 + (en - dn) * nu / 2)
    assert abs(en - dn) < 7 - 3 * H
    assert (cost_A + cost_F) / 2 <= n * n / 50
    x = min(selections, key=vf.cost)
    check_vector(w, x)
    return "two_explicit_halves_high_mass", x


def run():
    counts, balanced_count = {}, 0
    for d, e, t, a, c in product(range(7), range(7), range(7), range(7), range(4)):
        w = [c] * 16
        w[0], w[8], w[7] = d, e, t
        w[1] = w[2] = w[4] = a
        if not sum(w):
            continue
        branch, x = balanced_proof(w)
        balanced_count += 1
        counts[branch] = counts.get(branch, 0) + 1
        if x is not None:
            vf.round_selection(w, x)
    original_count, reduction_checks, rounded = 0, 0, 0
    rng = random.Random(12820261025)
    vectors = []
    for values in product(range(3), repeat=7):
        c, d, e, t, a1, a2, a3 = values
        w = [c] * 16
        for v, value in zip((0, 8, 7, 1, 2, 4), (d, e, t, a1, a2, a3)):
            w[v] = value
        if sum(w):
            vectors.append(w)
    for _ in range(400):
        w = [rng.randrange(20)] * 16
        for v in X:
            w[v] = rng.randrange(150)
        vectors.append(w)
    for w in vectors:
        original_count += 1
        mean = Q(w[1] + w[2] + w[4], 3)
        wb = list(map(Q, w))
        wb[1] = wb[2] = wb[4] = mean
        assert sum(w) == sum(wb)
        assert independent_mass(w) >= independent_mass(wb)
        branch, x = balanced_proof(wb)
        if x is None:
            assert 5 * independent_mass(w) >= 2 * sum(w)
            continue
        actual = [y for side, pairs in vf.SIDES
                  if (y := vf.match_half(w, side, pairs)) is not None]
        averaged = [y for side, pairs in vf.SIDES
                    if (y := vf.match_half(wb, side, pairs)) is not None]
        x_actual = min(actual, key=vf.cost)
        x_mean = min(averaged, key=vf.cost)
        assert vf.cost(x_actual) <= vf.cost(x_mean) <= vf.cost(x)
        check_vector(w, x_actual)
        vf.round_selection(w, x_actual)
        reduction_checks += 1
        rounded += 1
    report = {
        "date": "2026-10-23", "balanced_grid_cases": balanced_count,
        "balanced_branches": counts, "arbitrary_leaf_vectors": original_count,
        "exact_matching_reduction_comparisons": reduction_checks,
        "arbitrary_vectors_constructed_and_rounded": rounded,
        "status": "all exact bounded checks passed; universal claim uses the analytic proof",
        "program_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    Path(__file__).with_name("broom_check_results.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    run()
