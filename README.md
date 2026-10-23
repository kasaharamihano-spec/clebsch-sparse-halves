# Sparse halves for Clebsch blow-ups with at most six exceptional classes

**Author / project account:** kasaharamihano-spec  
**Version:** 2026-10-23 research draft. Not peer reviewed; priority not established.

This note proves the sparse-half bound whenever at most six of the sixteen Clebsch blow-up class sizes differ from a common value. The capacities are arbitrary nonnegative numbers in those positions. It does **not** solve the general sparse-half conjecture or arbitrary weighted Clebsch graphs.

- [Full research note](paper.md), readable as Markdown with mathematical notation.
- [LaTeX source](main.tex), including every supporting lemma used in the arguments.
- [Exact finite verifier](verify_families.py), Python 3.10 or newer, standard library only.
- [Verification results](verification_results.json), with the verifier's SHA-256.
- [Literature scope](literature.md), explaining known ingredients and the limits of the priority search.
- [Finite structural census](classification_check.py) and its [results](classification_results.json).
- Direct construction checks for the [extended star](broom_check.py), [pentagon with a leaf](cycle_pendant_check.py), and [theta graph](theta_check.py).

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

Compile main.tex with a standard LaTeX installation. It uses geometry, amsmath, amssymb, amsthm, fontenc, and hyperref.

## AI disclosure and status

The account holder initiated and directed the project. AI agents performed extensive proof development, literature retrieval, drafting, implementation, and cross-checks. Account attribution does not assert that the holder personally derived or independently verified every argument. AI cross-checks are not external expert review or formal verification.

Known inputs are credited. A bounded literature search does not establish that no stronger earlier theorem implies these restricted results. This is a research draft for examination, not a certified original discovery or a prize-qualifying solution.
