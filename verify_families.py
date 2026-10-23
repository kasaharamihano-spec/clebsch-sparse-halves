"""Exact finite implementation checks for the accompanying research draft.

Python 3.10+, standard library only. No network, credentials or private files.
This verifies bounded examples, not the unrestricted mathematical theorem.
The independent-set branch invokes the published theorem cited in the paper.
"""
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json
import random

D = (1, 2, 4, 8, 15)
EDGES = tuple((u, v) for u in range(16) for v in range(u + 1, 16)
              if u ^ v in D)
ADJ = tuple(sum(1 << v for v in range(16) if u ^ v in D)
            for u in range(16))


def independent_sets():
    out = []
    for mask in range(1 << 16):
        if all(not (ADJ[v] & mask) for v in range(16) if mask >> v & 1):
            out.append(tuple(v for v in range(16) if mask >> v & 1))
    return out


INDEPENDENT = independent_sets()


def parity(x):
    return x.bit_count() % 2


def matching_sides():
    result = []
    for d in D:
        characters = [k for k in range(1, 16)
                      if all(parity(k & s) == (s != d) for s in D)]
        assert len(characters) == 1
        k = characters[0]
        for bit in (0, 1):
            side = tuple(v for v in range(16) if parity(v & k) == bit)
            pairs = tuple((u, v) for u, v in EDGES
                          if u in side and v in side)
            assert len(side) == 8 and len(pairs) == 4
            assert len({v for e in pairs for v in e}) == 8
            result.append((side, pairs))
    return result


SIDES = matching_sides()


def cost(x):
    return sum((x[u] * x[v] for u, v in EDGES), Q(0))


def match_half(w, side, pairs):
    h = Q(sum(w), 2)
    if sum(w[v] for v in side) < h:
        return None
    x = [Q(0)] * 16
    oriented = [((u, v) if w[u] >= w[v] else (v, u))
                for u, v in pairs]
    left = h
    for large, small in oriented:
        take = min(left, w[large])
        x[large] = take
        left -= take
    for large, small in sorted(oriented, key=lambda pair: w[pair[0]]):
        take = min(left, w[small])
        x[small] = take
        left -= take
    assert left == 0
    assert all(0 <= x[v] <= w[v] for v in range(16))
    assert sum(x) == h
    return x


def round_selection(w, x):
    x = x[:]
    initial_cost = cost(x)
    excess = sum(x) - sum(w) // 2
    for v in range(16):
        drop = min(excess, x[v])
        x[v] -= drop
        excess -= drop
    assert excess == 0
    while True:
        internal = [v for v in range(16) if 0 < x[v] < w[v]]
        if len(internal) < 2:
            break
        i, j = internal[:2]
        low, high = max(-x[i], x[j] - w[j]), min(w[i] - x[i], x[j])
        candidates = []
        for t in (low, high):
            y = x[:]
            y[i] += t
            y[j] -= t
            candidates.append(y)
        x = min(candidates, key=cost)
    assert all(z.denominator == 1 for z in x)
    assert all(0 <= x[v] <= w[v] for v in range(16))
    assert sum(x) == sum(w) // 2
    assert cost(x) <= initial_cost
    return x


def verify(w, counts):
    n = sum(w)
    if n == 0:
        return
    counts["examples"] += 1
    counts["odd_total"] += n % 2
    alpha = max(sum(w[v] for v in ind) for ind in INDEPENDENT)
    if 5 * alpha >= 2 * n:
        # This branch checks the hypothesis of Razborov's published theorem.
        counts["published_independence_theorem"] += 1
        return
    candidates = [x for side, pairs in SIDES
                  if (x := match_half(w, side, pairs)) is not None]
    assert candidates, w
    x = min(candidates, key=cost)
    assert 50 * cost(x) <= n * n, (w, cost(x), Q(n * n, 50))
    y = round_selection(w, x)
    assert 50 * cost(y) <= n * n
    counts["constructed_and_rounded"] += 1


def new_counts():
    return dict(examples=0, odd_total=0, published_independence_theorem=0,
                constructed_and_rounded=0)


def family_grid(vertices, grid=range(3)):
    for values in product(grid, repeat=len(vertices) + 1):
        c, *free = values
        w = [c] * 16
        for v, val in zip(vertices, free):
            w[v] = val
        yield w


def main():
    assert len(EDGES) == 40
    assert all(len([v for v in range(16) if u ^ v in D]) == 5
               for u in range(16))
    assert all(not (ADJ[u] & ADJ[v]) for u, v in EDGES)
    star = (0,) + D
    cycle_isolate = (0, 1, 3, 7, 15, 10)
    cycle = cycle_isolate[:5]
    assert all(cycle[i] ^ cycle[(i + 1) % 5] in D for i in range(5))
    assert all((10 ^ v) not in D for v in cycle)
    output = {}
    double_star = (6, 9, 2, 4, 1, 8)
    for name, vertices in (("star", star), ("cycle_plus_isolate", cycle_isolate),
                           ("double_star", double_star)):
        counts = new_counts()
        for w in family_grid(vertices):
            verify(w, counts)
        rng = random.Random(12820261023 + len(output))
        for _ in range(100):
            c = rng.randrange(50)
            w = [c] * 16
            for v in vertices:
                w[v] = rng.randrange(250)
            verify(w, counts)
        output[name] = counts
    counts = new_counts()
    # Every labelled five-position set, with fixed asymmetric positive capacities.
    for vertices in combinations(range(16), 5):
        w = [2] * 16
        for v, val in zip(vertices, (0, 1, 3, 5, 8)):
            w[v] = val
        verify(w, counts)
    output["five_exception_position_sets"] = counts
    output["status"] = "all finite checks passed; see paper for universal proofs"
    output["script_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    destination = Path(__file__).with_name("verification_results.json")
    destination.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
