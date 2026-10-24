"""Portable exact checks of the bounded-ratio matching proposition.

Python standard library only. The elementary unrestricted proof is in
bounded_ratio.tex and paper.md; finite constructions are implementation checks.
"""
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import math
import random
import verify_families as vf


def criterion(m, M):
    return m > 0 and 17 * M * M - 48 * m * M + 3 * m * m <= 0


def check_weights(w):
    n = sum(w)
    assert criterion(min(w), max(w))
    side, pairs = max(vf.SIDES[:2], key=lambda row: sum(w[v] for v in row[0]))
    mass = sum(w[v] for v in side)
    full_cost = sum(w[u] * w[v] for u, v in pairs)
    assert 2 * mass >= n and 25 * full_cost <= 2 * mass * mass
    x = [Q(w[v] * n, 2 * mass) if v in side else Q(0) for v in range(16)]
    assert sum(x) == Q(n, 2) and all(0 <= x[v] <= w[v] for v in range(16))
    assert 50 * vf.cost(x) <= n * n
    y = vf.round_selection(w, x)
    assert 50 * vf.cost(y) <= n * n
    return n % 2


def main():
    # Coefficients of the five corner polynomials, constant term first.
    polynomials = [(8 * (4-k)**2 - 25 * (4-k), 16 * k * (4-k), 8 * k*k - 25 * k)
                   for k in range(5)]
    assert polynomials == [(28, 0, 0), (-3, 48, -17), (-18, 64, -18),
                           (-17, 48, -3), (0, 0, 28)]
    assert tuple(a-b for a, b in zip(polynomials[2], polynomials[1])) == (-15, 16, -1)
    assert tuple(a-b for a, b in zip(polynomials[3], polynomials[1])) == (-14, 0, 14)
    # Substitute r=(24+5sqrt(21))/17 in P1 using rational coefficients
    # in Q(sqrt(21)); both resulting coefficients are exactly zero.
    a, b = Q(24, 17), Q(5, 17)
    assert -17 * (a*a + 21*b*b) + 48*a - 3 == 0
    assert -34*a*b + 48*b == 0
    # 4<sqrt(21)<5 implies 1<r<3; no floating-point check is used here.
    assert 1 < a + 4*b < a + 5*b < 3
    assert criterion(4, 11) and not criterion(1, 3)
    examples = odd = 0
    for w in product((4, 11), repeat=16):
        odd += check_weights(w)
        examples += 1
    rng = random.Random(12820261024)
    for _ in range(500):
        low = rng.randrange(1, 40)
        upper = low
        while criterion(low, upper + 1):
            upper += 1
        w = [rng.randrange(low, upper + 1) for v in range(16)]
        odd += check_weights(w)
        examples += 1
    result = {"date": "2026-10-24", "status": "PASS",
              "program_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
              "corner_polynomial_coefficients": polynomials,
              "exact_quadratic_field_root_check": True,
              "threshold": "(24+5sqrt(21))/17",
              "threshold_approximation_display_only": (24 + 5 * math.sqrt(21)) / 17,
              "constructed_and_rounded": examples, "odd_total": odd,
              "scope": "Exact polynomial identities and finite full-core witnesses; unrestricted theorem and sign arguments are supplied by the written proof."}
    Path(__file__).with_name("ratio_results.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
