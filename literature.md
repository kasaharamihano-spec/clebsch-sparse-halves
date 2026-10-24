# Literature scope and attribution

Checked on 24 October 2026. This is a bounded primary-source review, not a certification of priority.

The project has not located a primary theorem explicitly asserting the complete six-exception capacity statement or the seven-class star-extension statement in this note. This does not exclude an unindexed manuscript, an earlier implicit consequence, or a stronger theorem not found in the search.

## Existing ingredients and overlapping cases

- **Norin–Yepremyan, Sparse halves in dense triangle-free graphs**, [author manuscript](https://arxiv.org/abs/1311.5818v2). The proof of Theorem 3.1, d=2, already gives the arbitrary weighted pentagon construction used here. That branch explicitly does not require the minimum-degree assumption. Lemma 2.2 transfers weighted sparse halves along valid homomorphisms with the actual pushforward weights. Neither fact alone asserts every nonuniform Clebsch case.
- **Razborov, More about sparse halves in triangle-free graphs**, [author manuscript](https://arxiv.org/abs/2104.09406v2), [published DOI](https://doi.org/10.1070/SM9615). Corollary 3.7 is the independence-ratio-at-least-two-fifths input. Theorem 3.5 covers triangle-free strongly regular graphs; Section 4.4 treats uniform Clebsch weights. Arbitrarily unequal blow-up class sizes generally do not yield a strongly regular graph.
- **Brandt, The local density of triangle-free graphs**, Freie Universität Berlin Preprint A 95-14, June 1995, [official archive](https://ftp.mi.fu-berlin.de/pub/math/publ/pre/1995/index.html). The full public PostScript preprint was downloaded and its text read. Proposition 1 contains the classical two-coordinate rounding mechanism. The appendix gives the local-density function of the uniform Clebsch graph, allowing a fractional selected vertex of the uniform core; it does not assert our variable-capacity sparse-half families. This source therefore strengthens the attribution of old tools rather than certifying a new weighted theorem.
- **Bedenknecht–Mota–Reiher–Schacht, On the local density problem for graphs of given odd-girth**, [author manuscript](https://www.math.uni-hamburg.de/home/schacht/2019/Andrasfai.pdf). Theorem 1.2 covers graphs homomorphic to an Andrásfai graph. Those targets are three-colourable, whereas a full-support Clebsch blow-up is four-chromatic. Boundary cases can still fall under prior work.

## Contemporary author repositories inspected

- [cormundus/erdos-128-census](https://github.com/cormundus/erdos-128-census) discusses uniform strongly regular graph certificates and numerical weighted searches.
- [aimir/erdos-128-sparse-halves](https://github.com/aimir/erdos-128-sparse-halves) states a general bound of 131/5000 in its inspected manuscript, larger than 1/50. Its Clebsch configuration appears in a different certificate, not an identified theorem for all capacities in the present families.
- Pablo Miguel Argudo's [9 September 2026 draft](https://github.com/pma1999/erdos-128-sparse-halves/blob/2193a4a06a4ec288a53ae986cdca5c1082abf1bb/outputs/cut-independent.tex) claims a general bound of 2587/100000, using an external max-cut theorem. Its scope is broader but its constant is larger than 1/50. This project has not independently verified the full argument or confirmed journal acceptance.
- komeiji shiki's [5 September 2026 draft](https://github.com/Komeiji-Shiki/erdos-128-sparse-halves/blob/9a66f297c1502f6f7904224efd39d8f9323a218f/paper/sparse-halves.tex), *Sparse-set extension and degree-sensitive perturbations for halves of triangle-free graphs*, claims the general constant 2543/100000. The inspected source states this at its main theorem and credits the max-cut inputs and Sarid's four-cycle certificate. Its README says it has not been accepted by a journal. This is a source/scope check, not a full proof endorsement; the constant remains above 1/50 and does not directly subsume our local exact bound.

Searches included combinations of Clebsch, sparse half, weighted blow-up, exceptional classes, pentagon, isolated vertex, neighbours, double star, and the cited papers. All boundary cases, tools, and already known uniform results remain attributed to their sources. The square-identity variant of the pentagon argument is explicitly proved here, but its prior appearance has not been ruled out. No claim of first discovery, external peer review, or eligibility for the original problem's prize is made.

The seven-class review additionally searched closed neighbourhood plus one vertex, seven exceptional classes, square with three leaves, and star extension. Norin--Yepremyan's balanced-neighbourhood theorems have further hypotheses, and the homomorphism results above do not automatically cover a full-support four-chromatic Clebsch blow-up. No direct overlap was located; this is still not a certification of originality.

The bounded-ratio proposition is elementary. Existence of some neighbourhood of the uniform weighting already follows from strict slack and continuity; the explicit ratio here is only a sufficient criterion, not an optimal radius for the conjecture.

Exact symbolic work used SymPy and its procedural skill from [Scientific Agent Skills](https://doi.org/10.48550/arXiv.2609.00065), checked against the current arXiv record on 24 October 2026. This is software-workflow attribution, not an external mathematical premise.
