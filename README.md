# Sparse halves for Clebsch blow-ups: six exceptional classes and a star extension

**Author / project account:** kasaharamihano-spec  
**Version:** 2026-10-24 research draft. Not peer reviewed; priority not established.

This note proves the sparse-half bound whenever at most six of the sixteen Clebsch blow-up class sizes differ from a common value. The capacities are arbitrary nonnegative numbers in those positions. It does **not** solve the general sparse-half conjecture or arbitrary weighted Clebsch graphs.

It also proves the bound for **seven arbitrary class sizes on a vertex, its five neighbours, and one further vertex**, with the other nine sizes equal. This treats one seven-position shape, a four-cycle with three pendant leaves. It does not assert the general seven-exception theorem.

A separate elementary criterion allows all sixteen positive sizes to vary if their maximum-to-minimum ratio is at most `(24+5sqrt(21))/17`, approximately 2.75958. The six-exception and seven-class theorems permit zero capacities and unrestricted ratios.

- [Full research note](paper.md), readable as Markdown with mathematical notation.
- [LaTeX source](main.tex), including every supporting lemma used in the arguments.
- [Exact finite verifier](verify_families.py), Python 3.10 or newer, standard library only.
- [Verification results](verification_results.json), with the verifier's SHA-256.
- [Literature scope](literature.md), explaining known ingredients and the limits of the priority search.
- [Finite structural census](classification_check.py) and its [results](classification_results.json).
- Direct construction checks for the [extended star](broom_check.py), [pentagon with a leaf](cycle_pendant_check.py), and [theta graph](theta_check.py).
- The [seven-class proof source](seven_star.tex), [full-core construction checker](square_star_full_check.py) and [results](square_star_full_results.json).
- The [bounded-ratio proof](bounded_ratio.tex), [portable checker](ratio_check.py) and [results](ratio_results.json).

The proof reduces the six exceptional positions to these shapes:

1. A star with five leaves.
2. A double star with two adjacent centres of degree three.
3. A star with one leaf edge extended.
4. A pentagon and an isolated vertex.
5. A pentagon with a pendant vertex.
6. Two pentagons sharing a path of three edges.

If an exceptional set misses a generator colour, a direct matching bound suffices. A short analytic classification handles the remaining sets. The structural argument does not rely on sampling capacity vectors.

The principal existing ingredients are the weighted pentagon construction of Norin and Yepremyan and the independence-ratio theorem of Razborov. The rounding mechanism is classical. An explicit square identity supplies the pentagon construction with a prescribed edge avoided. See the note for precise attributions and full statements.

## Reproduce

Run Python on verify_families.py. The verifier uses rational arithmetic, reconstructs all graph edges, checks its selected masses and costs, and rounds matching certificates to actual integer selections. In the independent-set branch it checks the hypothesis of the cited published theorem. Finite examples are implementation checks; the unrestricted parameter claims rely on the proofs.

Run classification_check.py to reconstruct every six-position set. Run broom_check.py, cycle_pendant_check.py, and theta_check.py for the direct construction and reduction checks. All use the Python standard library. Each writes its own results file with its program hash.

Run square_star_full_check.py for the seven-class family. Its 12,472 bounded examples exercise every construction branch; 4,644 return explicit fractional halves and 4,509 perform integer rounding. The other 7,828 check the independent-set premise of Razborov's theorem, rather than claiming to construct that theorem's half. Run ratio_check.py for exact corner identities and bounded-ratio constructions. These scripts also use only the standard library.

Compile main.tex with a standard LaTeX installation. It uses geometry, amsmath, amssymb, amsthm, fontenc, and hyperref.

## AI disclosure and status

The account holder initiated and directed the project. AI agents performed extensive proof development, literature retrieval, drafting, implementation, and cross-checks. Account attribution does not assert that the holder personally derived or independently verified every argument. AI cross-checks are not external expert review or formal verification.

Known inputs are credited. A bounded literature search does not establish that no stronger earlier theorem implies these restricted results. This is a research draft for examination, not a certified original discovery or a prize-qualifying solution.
