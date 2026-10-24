"""Exact construction checks for arbitrary seven-class square-star capacities.

Python standard library only. The unrestricted statement depends on the
analytic proof, not this finite run. In three independence-ratio branches this
checks the premise of Razborov's theorem, rather than claiming to construct
the half supplied by that external theorem.
"""
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import random
import time

HERE = Path(__file__).resolve().parent
D = (1, 2, 4, 8, 15)
V = tuple(range(16))
X = (0, 3, 1, 2, 4, 8, 15)
ALEAVES = (1, 2)
BLEAVES = (4, 8, 15)
EDGES = tuple((u, v) for u in V for v in V if u < v and u ^ v in D)
SIDES = {}
for g in D:
    characters = [m for m in range(1, 16)
                  if all((m & t).bit_count() % 2 == (t != g) for t in D)]
    assert len(characters) == 1
    for bit in (0, 1):
        side = tuple(v for v in V if (v & characters[0]).bit_count() % 2 == bit)
        assert len(side) == 8
        assert all(sum((u ^ v) in D for v in side) == 1 for u in side)
        SIDES[g, bit] = side
WITNESSES = ((0, 7, 9, 10, 12), (0, 3, 5, 9, 14), D)
assert len(EDGES) == 40
assert all(not (u in I and v in I) for I in WITNESSES for u, v in EDGES)


def cost(x):
    return sum((x[u] * x[v] for u, v in EDGES), Q(0))


def fill(x, vertices, capacities, demand):
    assert demand >= 0
    for v in vertices:
        take = min(demand, capacities[v] - x[v])
        assert take >= 0
        x[v] += take
        demand -= take
    assert demand == 0


def choose(d, e, a, b):
    """Choose an analytic branch for c=1; returns construction mode and label."""
    n = d + e + 2 * a + 3 * b + 9
    h = n / 2
    for index, value in enumerate((d + 4, d + e + 3, 2 * a + 3 * b)):
        if 5 * value >= 2 * n:
            return "independence", "independence_" + str(index), index
    assert h > 5 + 5 * d / 4 and h < 15
    if 2 * a + 2 * b + 4 >= h:
        return "proportional_D", "D_heavy", None
    assert d + e + b + 5 > h
    if (d - 1) * (b - 1) <= 0:
        return "proportional_C", "C_straddling", None
    Aheavy = d + a + 6 >= h
    if d < 1 and b < 1:
        if h >= Q(15, 2):
            return "cheap_C", "low_d_b_large_half", None
        if not Aheavy:
            return "cheap_C", "low_d_b_A_light", None
        if a >= 1:
            return "proportional_A", "low_d_b_A_straddling", None
        return ("cheap_A" if a >= b else "cheap_C"), "low_d_b_better_A_C", None
    assert d > 1 and b > 1
    if a <= 1:
        if Aheavy:
            return "proportional_A", "high_d_b_small_a_A_heavy", None
        assert a + e + 3 * b + 3 > h
        if e >= 1:
            return "proportional_B", "high_d_b_small_a_B_straddling", None
        if h >= Q(15, 2):
            return "full_B", "high_d_b_small_a_e_large_half", None
        return "proportional_C", "high_d_b_small_a_e_small_half", None
    if h <= 10:
        return "proportional_C", "high_d_b_large_a_low_half", None
    H = 3 - h / 5
    nu = d + e - h + 6
    assert 0 < H < 1 and abs(nu) < H
    if nu >= 0:
        return "nu_C", "high_half_nonnegative_nu", None
    if e >= 1:
        return "nu_C", "high_half_negative_nu_large_e", None
    if a + e + 3 * b + 3 >= h:
        return "proportional_B", "high_half_negative_nu_B_heavy", None
    return "nu_A", "high_half_negative_nu_A_partial", None


def construction(weights, background):
    w = list(map(Q, weights))
    c = Q(background)
    assert all(w[v] == c for v in V if v not in X)
    assert all(q >= 0 for q in w)
    n = sum(w)
    if not n:
        return [Q(0)] * 16, "zero", None
    if not c:
        part = max(((0, 3), D), key=lambda I: sum(w[v] for v in I))
        x = [Q(0)] * 16
        fill(x, part, w, n / 2)
        return x, "zero_background", None
    w = [q / c for q in w]
    d, e = w[0], w[3]
    a = (w[1] + w[2]) / 2
    b = sum(w[v] for v in BLEAVES) / 3
    n = sum(w)
    h = n / 2
    mode, label, witness_index = choose(d, e, a, b)
    if mode == "independence":
        I = WITNESSES[witness_index]
        assert 5 * sum(w[v] for v in I) >= 2 * n
        return None, label, I
    x = [Q(0)] * 16
    if mode == "proportional_D":
        omitted = min(BLEAVES, key=lambda v: w[v])
        side = SIDES[omitted, 1]
        mass = sum(w[v] for v in side)
        assert mass >= h
        x = [w[v] * h / mass if v in side else Q(0) for v in V]
    else:
        if mode.endswith("A"):
            leaf = max(ALEAVES, key=lambda v: w[v])
            side = SIDES[leaf, 0]
            assert set(side).intersection(X) == {0, leaf}
        elif mode.endswith("B"):
            leaf = max(ALEAVES, key=lambda v: w[v])
            side = SIDES[3 ^ leaf, 1]
            assert set(side).intersection(X) == {3, leaf, *BLEAVES}
        else:
            leaf = max(BLEAVES, key=lambda v: w[v])
            side = SIDES[leaf, 0]
            assert set(side).intersection(X) == {0, 3, leaf}
        if mode.startswith("proportional"):
            capacities = [w[v] if v in side else Q(0) for v in V]
            capacities[leaf] = a if mode.endswith(("A", "B")) else b
            mass = sum(capacities)
            assert mass >= h
            x = [q * h / mass for q in capacities]
        elif mode == "full_B":
            x[leaf], x[3] = a, e
            for v in BLEAVES:
                x[v] = w[v]
            remaining = h - a - e - 3 * b
            assert 0 <= remaining <= 3
            backgrounds = [v for v in side if v not in X]
            assert len(backgrounds) == 3
            for v in backgrounds:
                x[v] = remaining / 3
            assert cost(x) == a * e + b * remaining
        elif mode.startswith("nu_"):
            nu = d + e - h + 6
            for v in side:
                if v not in X:
                    x[v] = 1
            x[0] = d
            if mode == "nu_A":
                x[leaf] = e - nu
                assert 0 <= x[leaf] <= a
            else:
                x[3] = e
                x[leaf] = 1 - nu
                assert 0 <= x[leaf] <= b
        else:
            x[0] = d
            x[leaf] = a if mode == "cheap_A" else b
            remaining_pairs = [(u, v) for u, v in EDGES if u in side and v in side
                               and 0 not in (u, v)]
            completion = []
            for u, v in remaining_pairs:
                if 3 in (u, v):
                    x[u ^ v ^ 3] = 1
                    completion.append(3)
                else:
                    x[u] = 1
                    completion.append(v)
            fill(x, completion, w, h - sum(x))
    assert sum(x) == h
    assert all(0 <= x[v] <= w[v] for v in V), (mode, w, x)
    assert 50 * cost(x) <= n * n, (label, (d, e, a, b), cost(x), n * n / 50)
    return [q * c for q in x], label, None


def round_selection(w, x):
    initial = cost(x)
    x = x[:]
    excess = sum(x) - sum(w) // 2
    for v in V:
        drop = min(excess, x[v])
        x[v] -= drop
        excess -= drop
    assert excess == 0
    while True:
        interior = [v for v in V if 0 < x[v] < w[v]]
        if len(interior) <= 1:
            break
        i, j = interior[:2]
        lo = max(-x[i], x[j] - w[j])
        hi = min(w[i] - x[i], x[j])
        options = []
        for shift in (lo, hi):
            y = x[:]
            y[i] += shift
            y[j] -= shift
            options.append(y)
        x = min(options, key=cost)
    assert sum(x) == sum(w) // 2
    assert all(q.denominator == 1 for q in x)
    assert cost(x) <= initial
    return x


def main():
    started = time.monotonic()
    counts = Counter()
    samples = {}
    totals = Counter()
    def check(values, c):
        w = [Q(c)] * 16
        for v, q in zip(X, values):
            w[v] = Q(q)
        n = sum(w)
        x, label, I = construction(w, c)
        counts[label] += 1
        totals["examples"] += 1
        samples.setdefault(label, {"capacities_in_X_order": list(map(str, values)),
                                   "background": str(c)})
        if x is None:
            assert I is not None and 5 * sum(w[v] for v in I) >= 2 * n
            totals["published_theorem_premise"] += 1
            return
        assert sum(x) == n / 2 and all(0 <= x[v] <= w[v] for v in V)
        assert 50 * cost(x) <= n * n
        totals["explicit_fractional_construction"] += 1
        if all(q.denominator == 1 for q in w):
            y = round_selection(w, x)
            assert 50 * cost(y) <= n * n
            totals["explicit_integer_rounding"] += 1
            totals["odd_integer_rounding"] += int(n % 2 == 1)
    for d, e, a, b in product((0, 1, 2, 3, 4, 6, 8, 12), repeat=4):
        check((d, e, a, a, b, b, b), 2)
    for values in product(range(3), repeat=7):
        check(values, 1)
        check(values, 0)
    # A narrow small-half branch missed by the coarser grids, and a case near
    # the boundary of the high-a polynomial argument.
    check((33, 0, 0, 0, 43, 43, 43), 30)
    check((604, 0, 201, 201, 398, 398, 398), 200)
    rng = random.Random(1282026102408)
    for _ in range(2000):
        c = rng.randrange(1, 16)
        check([rng.randrange(6 * c + 1) for v in X], c)
    for _ in range(2000):
        # Preserve arbitrary balanced means while making individual leaves very
        # unequal, often crossing the background on different sides.
        d, e, a, b = [Q(rng.randrange(121), 20) for j in range(4)]
        a1 = Q(rng.randrange(101), 100) * 2 * a
        b1 = Q(rng.randrange(101), 100) * 3 * b
        b2 = Q(rng.randrange(101), 100) * (3 * b - b1)
        check((d, e, a1, 2 * a - a1, b1, b2, 3 * b - b1 - b2), 1)
    expected = {"zero", "zero_background", "D_heavy", "C_straddling",
                "independence_0", "independence_1", "independence_2",
                "low_d_b_large_half", "low_d_b_A_light", "low_d_b_A_straddling",
                "low_d_b_better_A_C", "high_d_b_small_a_A_heavy",
                "high_d_b_small_a_B_straddling", "high_d_b_small_a_e_large_half",
                "high_d_b_small_a_e_small_half", "high_d_b_large_a_low_half",
                "high_half_nonnegative_nu", "high_half_negative_nu_large_e",
                "high_half_negative_nu_B_heavy", "high_half_negative_nu_A_partial"}
    assert set(counts) == expected, expected - set(counts)
    report = {"date": "2026-10-24", "program_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
              "status": "PASS", "input_order": X, "totals": dict(totals),
              "branch_counts": dict(counts), "branch_examples": samples,
              "elapsed_seconds": time.monotonic() - started,
              "scope": "Bounded exact checks of explicit full-core constructions and integer rounding; unrestricted capacity theorem relies on the analytic proof; independence branches verify only the premise of the attributed theorem."}
    HERE.joinpath("square_star_full_results.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
