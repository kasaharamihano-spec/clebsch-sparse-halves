# Some sparse-half bounds for nonuniform Clebsch blow-ups

**Author / project account:** kasaharamihano-spec  
**Version:** 2026-10-23 research draft. Not peer reviewed; priority not established.

This note gives complete arguments for the sparse-half bound in four specified families of Clebsch blow-ups. It does **not** solve the general sparse-half conjecture or arbitrary weighted Clebsch graphs.

- [Full research note](paper.md), readable as Markdown with mathematical notation.
- [LaTeX source](main.tex), including every supporting lemma used in the arguments.
- [Exact finite verifier](verify_families.py), Python 3.10 or newer, standard library only.
- [Verification results](verification_results.json), with the verifier's SHA-256.
- [Literature scope](literature.md), explaining known ingredients and the limits of the priority search.

The four families allow:

1. At most five class sizes to differ from a common value.
2. Arbitrary sizes on a vertex and its five neighbours, with the other ten classes equal.
3. Arbitrary sizes on an induced pentagon and a common nonneighbour, with the other ten classes equal.
4. Arbitrary sizes on the specified induced double star and its automorphic images, with the other ten classes equal.

The principal existing ingredients are the weighted pentagon construction of Norin and Yepremyan and the independence-ratio theorem of Razborov. The rounding mechanism is classical. See the note for precise attributions and full statements.

## Reproduce

Run Python on verify_families.py. The verifier uses rational arithmetic, reconstructs all graph edges, checks its selected masses and costs, and rounds matching certificates to actual integer selections. In the independent-set branch it checks the hypothesis of the cited published theorem. Finite examples are implementation checks; the unrestricted parameter claims rely on the proofs.

Compile main.tex with a standard LaTeX installation. It uses geometry, amsmath, amssymb, amsthm, fontenc, and hyperref.

## AI disclosure and status

The account holder initiated and directed the project. AI agents performed extensive proof development, literature retrieval, drafting, implementation, and cross-checks. Account attribution does not assert that the holder personally derived or independently verified every argument. AI cross-checks are not external expert review or formal verification.

Known inputs are credited. A bounded literature search does not establish that no stronger earlier theorem implies these restricted results. This is a research draft for examination, not a certified original discovery or a prize-qualifying solution.
