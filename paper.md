# Some sparse-half bounds for nonuniform Clebsch blow-ups

**Author / project account:** kasaharamihano-spec  
**23 October 2026 — research draft, not peer reviewed.**

## Abstract

Let $H$ be the Clebsch graph, and replace each vertex $v$ by an independent
set of size $w_v$, with complete bipartite graphs on the edges of $H$.
We give explicit arguments for the sparse-half bound $N^2/50$ in four
restricted families: at most five class sizes differing from a common
value; arbitrary sizes on a vertex and its five neighbours with the other
ten classes equal; and arbitrary sizes on an induced pentagon and a
vertex nonadjacent to it with the other ten classes equal; and arbitrary
sizes on a specified induced double star with the other ten classes equal.
The arguments use matching cuts, a known weighted pentagon construction,
and Razborov's independence-ratio theorem.
These statements do not settle arbitrary Clebsch blow-ups or the
general sparse-half conjecture. The priority of these particular restricted
consequences has not been established.

## Statements and scope

Use the model

$$

 V(H)=\mathbb{F}_2^4,\qquad
 D=\{1,2,4,8,15\},\qquad uv\in E(H)\ \Longleftrightarrow\ u+v\in D ,

$$

where integers encode four-bit vectors and addition is bitwise XOR.
The only nonempty subset of $D$ with sum zero is $D$ itself. In particular
$H$ is triangle-free. For capacities $w_v\geq0$, put $N=\sum_v w_v$.
A fractional half is a vector $x$ with

$$

 0\leq x_v\leq w_v,\qquad \sum_vx_v=N/2,\qquad
 \mathcal{E}(x)=\sum_{uv\in E(H)}x_ux_v .

$$

For integer capacities this is the natural relaxation of selecting vertices
from the corresponding blow-up.

**Theorem 1.**

There is a fractional half of cost at most $N^2/50$ in each of the following
families of nonnegative real capacities.

1. There is $c\geq0$ such that at most five capacities differ from $c$.

2. The capacities on $\{z\}\cup N_H(z)$ are arbitrary, and all other
ten capacities equal $c\geq0$.

3. The capacities on an induced $C_5=P$ and a vertex $z$ nonadjacent
to every vertex of $P$ are arbitrary, and all other ten capacities equal
$c\geq0$.

4. The capacities on an automorphic image of
$\{1,2,4,6,8,9\}$ are arbitrary, and all other ten capacities equal
$c\geq0$. These six vertices induce a double star with adjacent centres
$6,9$, left leaves $2,4$, and right leaves $1,8$.

For integer capacities, the blow-up has a set of $\lfloor N/2\rfloor$
vertices inducing at most $N^2/50$ edges.

Our external inputs are explicitly identified below. In particular,
the weighted $C_5$ construction is already present in
Norin–Yepremyan [Norin–Yepremyan](https://arxiv.org/abs/1311.5818v2) (proof of Theorem 3.1, $d=2$).
The independence-ratio input is Razborov [Razborov](https://arxiv.org/abs/2104.09406v2) (Corollary 3.7).
No numerical experiment is used as a proof of a continuous statement.

## Preliminaries

**Lemma 2 (Matching cuts).**

For each $d\in D$ there is a linear functional $\ell_d:\mathbb{F}_2^4\to\mathbb{F}_2$
that takes value $0$ on $d$ and value $1$ on $D\setminus\{d\}$.
Each fibre induces four disjoint edges, all of difference $d$.

**Proof.** 
Prescribing the values is consistent with the unique relation
$\sum_{s\in D}s=0$, since four prescribed values are $1$.
The functional is nonzero. Each fibre has eight vertices; the only
generator preserving it is $d$.

QED.

Call the ten fibres in Lemma 2 matching sides.
The case $N=0$ is immediate; henceforth assume $N>0$.
If a side has total capacity $b\geq N/2$ and full cost $Q\leq b^2/16$,
scaling all its capacities by $N/(2b)$ gives a half with cost at most
$N^2/64$. We will repeatedly use this sufficient condition.

**Lemma 3 (Capacitated matching).**

For disjoint edges with capacities $(L_j,S_j)$, $L_j\geq S_j$,
a minimum-cost selection of prescribed total mass is obtained by first
using the larger endpoints at cost zero, then filling smaller endpoints
in increasing order of $L_j$, at cost $L_j$ per unit.
Moreover, at fixed total selection mass the minimum cost is nonincreasing
when any capacity increases.

**Proof.** 
On a single edge, fixing its selected mass $t$ gives a concave quadratic
$x(t-x)$. An endpoint of its feasible interval minimizes this expression.
The resulting minimum is zero for $0\leq t\leq L_j$ and
$L_j(t-L_j)$ for $L_j\leq t\leq L_j+S_j$.
Allocation over the edges is then a linear filling problem.
The last assertion follows directly by inclusion of feasible sets:
the objective does not depend on the capacities.

QED.

**Lemma 4 (Known independence-ratio input).**

If an independent set in a triangle-free weighted core has total capacity
at least $2N/5$, the weighted core admits a fractional half of cost at most $N^2/50$.

**Proof.** 
For integer capacities, double every capacity. The resulting graph has
$2N$ vertices and independence number at least $4N/5$.
Razborov's theorem [Razborov](https://arxiv.org/abs/2104.09406v2) (Corollary 3.7), including its weighted-half
formulation, gives a half of cost at most $(2N)^2/50$.
Dividing the selected class masses by two proves the claim.
Rational capacities follow by clearing denominators.
For real capacities, normalize $N=1$ and approximate within the rational
polytope defined by nonnegativity and the specified independent-set
inequality. Compactness of the selected vectors and continuity of the
cost give the conclusion. The case $N=0$ is immediate.

QED.

**Lemma 5 (Rounding).**

For integer capacities, a fractional half of cost at most $N^2/50$
implies the integer assertion in Theorem 1.

**Proof.** 
The two-coordinate mechanism is classical; see, for example,
Brandt [Brandt](https://ftp.mi.fu-berlin.de/pub/math/publ/pre/1995/index.html) (Proposition 1). We include the capacitated argument.
If $N$ is odd, delete mass $1/2$; all cost coefficients are nonnegative,
so cost cannot increase. The target mass is now $\lfloor N/2\rfloor$.
Given two coordinates strictly between zero and their integer capacities,
vary them as $x_i+t,x_j-t$. The cost is concave in $t$, its quadratic
coefficient being $-a_{ij}\leq0$. Some feasible endpoint does not increase
cost and makes at least one more coordinate integral.
Repeat until at most one coordinate is internal.
Its integrality follows from the integer total mass.

QED.

**Lemma 6 (Known pentagon construction).**

For nonnegative capacities $b_0,\ldots,b_4$ on a cycle, with sum $T$,
there is a half of cost at most $T^2/50$ supported in
$\{i,i+1,i+3\}$ for some $i$ (indices are modulo five).

**Proof.** 
This is the $d=2$ construction in [Norin–Yepremyan](https://arxiv.org/abs/1311.5818v2) (proof of Theorem 3.1),
where the authors observe that the minimum-degree hypothesis is not
used in this branch. We recall its short proof in cycle order.
If a nonadjacent pair has mass at least $T/2$, use it at zero cost.
Every such pair lies in a triple of the required form.
Otherwise fill $b_i,b_{i+3}$ and take
$T/2-b_i-b_{i+3}$ from $i+1$. All five choices are feasible because
both the filled nonadjacent pair and the omitted nonadjacent pair
have mass less than $T/2$. Their costs $q_i$ satisfy

$$

 \sum_iq_i=\frac{T^2}{2}
   -\frac12\sum_i(b_i+b_{i+3})^2
 \leq \frac{T^2}{10},

$$

by Cauchy--Schwarz.

QED.

## At most five exceptional classes

Let $X=\{v:w_v\ne c\}$. If a generator $d$ is absent from the differences
of edges internal to $X$, every $d$-edge has an endpoint of capacity $c$.
Take the heavier matching side, of capacity $b\geq N/2$.
Its full cost is $Q=cb-4c^2$, so

$$

 b^2-16Q=(b-8c)^2\geq0.

$$

The scaling observation proves the required bound, including $c=0$.

If $|X|\leq5$ and all five differences occur, choose one edge of each
difference within $X$. This gives five edges on at most five vertices,
so it contains a cycle. The distinct differences of that cycle sum to
zero and hence comprise all of $D$. Thus $X$ is exactly an induced
pentagon. It remains to treat arbitrary capacities $p_0,\ldots,p_4$ on
a pentagon and common capacity $c$ on the other eleven vertices.
Put $W=\sum p_i$ and $N=W+11c$.

Along an induced pentagon each generator occurs once.
For its edge $\{i,i+1\}$, the corresponding matching cut splits the
pentagon into $\{i,i+1,i+3\}$ and $\{i+2,i+4\}$.
If some $p_0\leq c$, one of the nonadjacent pairs
$\{1,3\},\{2,4\}$ has capacity $s\geq(W-c)/2$.
The matching side meeting the pentagon in that pair has

$$

 b=s+6c\geq N/2,\quad Q=cs+2c^2,\quad
 b^2-16Q=(s-2c)^2 .

$$

It therefore gives cost at most $N^2/64$.

Otherwise put $b_i=p_i-c\geq0$ and $T=\sum b_i$, so $N=T+16c$.
Use Lemma 6, and take the matching side containing its
support triple. Select $c$ at each of the eight vertices of this side
and add the half from the $b_i$. The mass is $N/2$ and the cost is at most

$$

 4c^2+\frac{cT}{2}+\frac{T^2}{50}\leq\frac{N^2}{50},

$$

since the difference is $28c^2/25+7cT/50$.
This proves part (1).

## A vertex and its five neighbours

Translate the centre to $0$, give it capacity $d$, give its five neighbours
capacities $a_1,\ldots,a_5$, and give the remaining ten vertices capacity $c$.
Write $S=\sum a_i$, $a=S/5$, and $N=d+S+10c$.
The matching side $A_i$ containing the centre and leaf $i$ consists of

$$

 (d,a_i),(c,c),(c,c),(c,c).

$$

Its complement $B_i$ consists of $(a_j,c)$, $j\ne i$.
Two independent-set witnesses have capacities $S$ and $d+4c$.

We first give the symmetric calculation needed in the proof.

**Lemma 7 (Symmetric matching-side bound).**

Assume $a>0$, $N=d+5a+10c$,

$$

 5a<2N/5,\qquad d+4c<2N/5,\qquad d>3a-2c .

$$

The matching with capacities $(d,a)$ and three copies of $(c,c)$
contains a half of cost at most $N^2/50$.

**Proof.** 
Set $x=d/a$, $t=c/a$, $n=N/a=x+5+10t$.
The assumptions imply

$$

 0\leq x<10/3,\qquad x>15/2-10t,\qquad x>3-2t. \tag{R}

$$

The last inequality makes the side heavier than $N/2$.
Let $H$ be its exact minimum cost divided by $a^2$, and
$\Delta=n^2-50H$.

If $t\geq\max(x,1)$, fill both star endpoints before paying for background
small endpoints. The remaining background demand is $(3+4t-x)/2>0$,
and Lemma 3 gives

$$

 H=x+t(3+4t-x)/2,\quad
 \Delta=x^2-40x+25+(45x+25)t .

$$

For $0\leq x\leq1$, use $t\geq1$ to get
$\Delta\geq x^2+5x+50>0$.
For $1\leq x<10/3$, use $t\geq x$ to get
$\Delta\geq46x^2-15x+25>0$.

Now suppose $t\leq\max(x,1)$. If $x\leq1$, then
$t\leq1$ contradicts $x>3-2t$. Hence $1<x<10/3$ and $t\leq x$.
The remaining demand after the larger endpoints is
$r=(5+4t-x)/2>0$.
If $r\leq3t$, then $H=tr$ and

$$

 \Delta=(x+5)^2+(45x-25)t>0.

$$

Otherwise

$$

 H=3t^2+x(5-x-2t)/2,\quad
 \Delta=26x^2-115x+25+(70x+100)t-50t^2 .

$$

Here $\partial_t\Delta=70x+100-100t\geq100-30x>0$.
By (R) it suffices to substitute
$t_0=\max((15-2x)/20,(3-x)/2)$.
For $1<x\leq15/8$ the resulting expression is
$(-43x^2+30x+125)/2$, a concave quadratic whose endpoint values
on $[1,15/8]$ are $56$ and $1925/128$.
For $15/8\leq x<10/3$ it is

$$

 \frac{148x^2-520x+575}{8}
 =\frac{37}{2}\left(x-\frac{65}{37}\right)^2+\frac{4375}{296}>0 .

$$

All cases have been covered.

QED.

To prove part (2), apply Lemma 4 if
$S\geq2N/5$ or $d+4c\geq2N/5$.
Otherwise $S>0$, so $a>0$.
Put $m=\min a_i$.
For $B_i$, with $u=S-a_i$, its mass and cost are
$b=u+4c$, $Q=cu$, and $b^2-16Q=(u-4c)^2$.
If any $B_i$ is heavy enough, scaling suffices.
In the remaining case,

$$

 d>S-2m-2c\geq3a-2c.

$$

Replace all leaves by their mean $a$, preserving $N$ and both
independent-set inequalities. Lemma 7 gives a half on
the symmetric side $(d,a)+3(c,c)$.
Choose an actual largest leaf $M=\max a_i\geq a$.
The side $A_i$ for this leaf has capacities $(d,M)+3(c,c)$ and
contains that same selected vector: only one capacity has increased.
Its cost and mass are unchanged.
This proves the result without any further case split.
The case $S=0$ was already covered by $d+4c\geq2N/5$.

## A pentagon and a common nonneighbour

Let $P=(v_0,\ldots,v_4)$ be an induced pentagon, let $z$ be nonadjacent
to all of $P$, and assign capacities $p_i,d,c$ as in part (3).
Put $W=\sum p_i$, $N=d+W+10c$, $h=N/2$.

### Geometry and direct cases

Translate $z$ to $0$. Its ten nonneighbours correspond to the two-element
subsets $\{s,t\}$ of $D$, via the vertex $s+t$,
with adjacency given by disjointness: this is the Petersen
graph. For each $s\in D$, the four pairs containing $s$ are independent.
Their intersections with $P$ each have size at most two.
Each vertex of $P$ belongs to exactly two of these five four-sets,
so every intersection has size exactly two.
Consequently $z$ is in the three-point side of every pentagon matching cut.

For each $i$, that side $A_i$ consists of the four pairs

$$

 (p_i,p_{i+1}),\quad(p_{i+3},c),\quad(d,c),\quad(c,c).

$$

Set $s_i=p_{i+2}+p_{i+4}$.
Its complementary side has mass $s_i+6c$ and full cost $cs_i+2c^2$.
If it is heavy enough, scaling gives cost at most $N^2/64$.
Otherwise, for every nonadjacent pair of $P$,

$$

 s_i<(W+d-2c)/2. \tag{B}

$$

The independent set $N_H(z)$ has capacity $5c$.
Also one of the five independent four-sets above, together with $z$,
has capacity at least $d+2c+2W/5$.
Lemma 4 therefore applies if $d+W\leq5c/2$ or
$d\geq10c/3$. This covers $c=0$.
In all remaining cases assume

$$

 c>0,\qquad 0\leq d\leq10c/3,\qquad W>5c/2-d. \tag{I}

$$

### Low centre capacity: $0\leq d\leq2c$

Let $k=(W-d+2c)/2$.
Condition (B) implies every nonadjacent pair has mass less than $k$,
and every matching triple of $P$ has mass greater than $k$:
the omitted pair is less than $W-k=(W+d-2c)/2$.
In $A_i$, fill $z$, all four background classes, $p_i$, and $p_{i+3}$,
then take $k-p_i-p_{i+3}$ from $p_{i+1}$.
This is feasible and has mass $h$ and cost

$$

 q_i=p_i(k-p_i-p_{i+3})+cp_{i+3}+cd+c^2 .

$$

Cauchy--Schwarz gives the average bound

$$

 \frac15\sum_iq_i\leq H_{\rm low}
 =\frac{W^2}{50}-\frac{Wd}{10}+\frac{2cW}{5}+cd+c^2.

$$

The gap to the target is

$$

 G=\frac{N^2}{50}-H_{\rm low}
   =\frac{7Wd}{50}+\frac{d^2}{50}-\frac{3dc}{5}+c^2.

$$

The average pair mass is $2W/5$, so (B) implies $W>10c-5d$.
Set $r=d/c$, $w=W/c$.
Thus $w>\max(10-5r,5/2-r)$ and $0\leq r\leq2$.
The coefficient of $w$ in $G/c^2$ is nonnegative.
For $r\leq15/8$, substituting $w=10-5r$ gives
$1+4r/5-17r^2/25$, positive by concavity and endpoint values
$1,7/64$.
For $15/8\leq r\leq2$, substituting $w=5/2-r$ gives
$1-r/4-3r^2/25\geq1/50$.
Some $q_i$ therefore satisfies the target.

### Middle capacity and $W\geq c/2$

Assume $2c\leq d\leq10c/3$.
In a suitable $A_i$, take $u=d/2+c\leq d$ from $z$, all four
background classes, and a half of the pentagon capacities.
The total is $h$ and the fixed cost is $cd/2+2c^2$.

If a nonadjacent pentagon pair has mass at least $W/2$, choose
mass $W/2$ within it. Each such pair lies in two matching triples,
with either member as the isolated vertex of the triple.
Explicitly, the pair $\{i,i+2\}$ lies in
$\{i+2,i+3,i\}$ and $\{i+4,i,i+2\}$, with isolated vertices
$i$ and $i+2$, respectively.
Make the smaller selected member the isolated vertex, so its mass
is at most $W/4$. The total cost is at most

$$

 H_{\rm pair}=cd/2+2c^2+cW/4 .

$$

A direct identity yields

$$

 \frac{N^2}{50}-H_{\rm pair}
 =\frac{(d-2c)^2}{50}
 +(W-c/2)\left(\frac W{50}+\frac d{25}+\frac{4c}{25}\right)\geq0 .

$$

If all nonadjacent pairs have mass less than $W/2$, the five explicit
constructions of Lemma 6 are feasible.
Their pentagon costs average at most $W^2/50$, and their background
attachment costs average $cW/5$. Some selection has cost at most

$$

 H_{\rm cycle}=W^2/50+cW/5+cd/2+2c^2.

$$

Here

$$

 \frac{N^2}{50}-H_{\rm cycle}
 =\frac{(d-2c)^2+c^2}{50}
 +(W-c/2)\left(\frac d{25}+\frac c5\right)>0 .

$$

### Middle capacity and $W\leq c/2$

Retain (B) and (I).
In $A_i$ fill the three pentagon classes, $z$, and three background
classes. From the background partner of $z$ take

$$

 b_i=(4c-d-W)/2+s_i .

$$

It is positive because $d+W\leq23c/6<4c$, and is less than $c$ by (B).
The selection has mass $h$ and exact cost

$$

 F_i=p_ip_{i+1}+cp_{i+3}+c^2+
             d\big((4c-d-W)/2+s_i\big).

$$

Using $\sum s_i=2W$ and $\sum p_ip_{i+1}\leq W^2/2$, the average is
at most

$$

 H_{\rm small}=W^2/10+cW/5+c^2+d(4c-d-W)/2+2dW/5.

$$

With $r=d/c\in[2,10/3]$, $w=W/c\in[0,1/2]$, the normalized gap is

$$

 D=\frac{N^2/50-H_{\rm small}}{c^2}
  =\frac{13r^2}{25}+\frac{7rw}{50}-\frac{8r}{5}
   -\frac{2w^2}{25}+\frac w5+1.

$$

Its derivative in $w$ is at least $2/5$.
For $2\leq r\leq5/2$, use $w>5/2-r$ from (I) to get
$D\geq3r^2/10-21r/20+1\geq1/10$.
For $5/2\leq r\leq10/3$, use $w\geq0$ to get
$D\geq13r^2/25-8r/5+1\geq1/4$.
This proves part (3).

## An induced double star

Use the representative in part (4), with centre capacities $d,e$,
left leaf capacities $a_1,a_2$, right leaf capacities $b_1,b_2$,
and common background capacity $c$.
Let $B(w)$ be the least cost of a half among the ten matching sides,
with infeasible sides assigned cost $+\infty$.

**Lemma 8 (Two matching-edge comparisons).**

For a fixed selection mass, averaging the two capacities of one matching
edge cannot decrease its minimum cost. For two disjoint edges
$(a,c),(b,c)$, averaging $a,b$ while keeping $c$ fixed also cannot
decrease the minimum cost.
These comparisons remain valid when other disjoint matching edges
are added.

**Proof.** 
For a single edge of total capacity $u$, put $L=\max(a,b)\geq u/2$.
At selected mass $t\leq u$, the cost is $L\max(0,t-L)$.
In its positive region its derivative in $L$ is $t-2L\leq0$.

For the second assertion fix $u=a+b$, write $a=u-b\geq b$, and increase
$b$ towards $u/2$. Let $g_b(t)$ be the minimum on these two edges.
If $a,b\leq c$, then $g_b(t)=c\max(0,t-2c)$, independent of $b$.
If $a,b\geq c$, put $q=\max(0,t-u)\leq2c$; then

$$

 g_b(t)=b\min(q,c)+(u-b)\max(0,q-c),

$$

whose coefficient of $b$ is nonnegative.
In the remaining region $b\leq c\leq a$, put $q=t-u-c\leq c$.
For $q\leq0$, the formula is $c\max(0,q+b)$.
For $q\geq0$, it is $cb+(u-b)q$, with coefficient $c-q\geq0$.
The formulas agree on their boundaries.
Thus $g_b(t)$ is nondecreasing throughout.
The compared component total capacities are unchanged. Taking the
infimum over mass allocations between this component and the remaining
disjoint edges preserves each comparison.

QED.

Put $\ell=(a_1+a_2)/2$, $r=(b_1+b_2)/2$ and let $\bar w$ replace
the respective leaf pairs by $\ell,\ell$ and $r,r$.
Then

$$

 B(w)\leq B(\bar w),\qquad \alpha_w\geq\alpha_{\bar w}. \tag{S}

$$

For the matching comparison, the ten sides have four types:
the centre edge plus three background edges; all four leaf--background
edges; a centre--background edge, an opposite leaf--background edge,
and two background edges; or a centre--leaf edge, two opposite
leaf--background edges, and one background edge.
The first type is unchanged. For the second, apply
Lemma 8 to both leaf pairs.
For each side of the third type in $\bar w$, choose the larger actual
opposite leaf and use capacity inclusion.
For the fourth, first use the smoothing comparison on the two opposite
leaf--background edges, then choose the larger actual leaf on the centre
edge. Thus each side for $\bar w$ has a side for $w$ of no larger cost.
For the independence comparison, swapping bit coordinates $2,4$ fixes
both centres and the right leaves, and swapping coordinates $1,8$ fixes
both centres and the left leaves. They are automorphisms of $H$.
Averaging $w$ over these four automorphisms gives $\bar w$;
the maximum independent-set mass is a convex invariant function.

It suffices by (S) to treat the pair-balanced family.
The case $c=0$ is bipartite on its positive support, so an independent
half suffices. For $c>0$ scale to $c=1$, with

$$

 N=d+e+2\ell+2r+10,\qquad h=N/2 .

$$

The four-leaf matching side has mass $M=2\ell+2r+4$ and cost
$Q=2\ell+2r$, with $M^2-16Q=(2\ell+2r-4)^2$.
The two-exception side with centre $d$ and opposite leaf $r$ has
$M=d+r+6$, $Q=d+r+2$, and $M^2-16Q=(d+r-2)^2$.
The analogous side uses $e,\ell$.
If any is heavy enough, scaling proves the result.
Otherwise

$$

 d+e>2\ell+2r-2,\quad d-e<2\ell-2,\quad e-d<2r-2.

$$

Define positive parameters

$$

 k=(d-e)/2,\quad x=\ell-1-k,\quad y=r-1+k,\quad
 s=x+y,\quad z=(d+e)/2-1-s .

$$

Then $x,y,z>0$ and

$$

 \ell=1+x+k,\quad r=1+y-k,\quad
 d=1+s+z+k,\quad e=1+s+z-k,\quad h=8+2s+z.

$$

The independent sets $\{1,6,8,11,13\}$ and $\{2,4,7,9,14\}$
have masses $d+2r+2$ and $e+2\ell+2$.
Unless Lemma 4 applies, with

$$

 \nu=x-y+k,\qquad H=(7-2s-z)/5=3-h/5

$$

their masses $h-3-\nu,h-3+\nu$ imply $|\nu|<H$ and $H>0$.

If $2s+z\leq2$, the centre-edge side has no greater minimum cost
than after averaging $d,e$ to $t=1+s+z$, by
Lemma 8.
In $(t,t)+3(1,1)$, fill the large endpoints, the three background
small endpoints, and mass $1+s\leq t$ on the centre small endpoint.
Its cost is $3+(1+s)(1+s+z)$, and

$$

 N^2-50[3+(1+s)(1+s+z)]
 =56+28s+14z-34s(s+z)+4z^2
 \geq56-40s\geq16 .

$$

Here $s\leq1$ and $s+z\leq2$.

If $2s+z\geq2$, then $0<H\leq1$.
On the side meeting the double star in $\{1,2,6,8\}$, fill centre $d$,
the two opposite leaves $r,r$, and all four background classes.
Take $1+\nu=\ell-y$ on the remaining leaf of capacity $\ell$.
This quantity is positive and less than $\ell$, and the total is $h$.
Its cost is $F_L=d(1+\nu)+2r+1$.
The side meeting the double star in $\{1,2,4,9\}$ similarly gives
$F_R=e(1-\nu)+2\ell+1$, since $1-\nu=r-x$ is feasible.
Their average is

$$

 (F_L+F_R)/2=h-4+k\nu .

$$

As $k=\nu-x+y$, $|\nu|<H$, and $s\leq(7-5H)/2$,

$$

 k\nu\leq H^2+sH\leq H^2+\frac{H(7-5H)}2 .

$$

Since $h=15-5H$,

$$

 \frac{N^2}{50}-(h-4)=7-7H+2H^2 .

$$

Subtracting the preceding upper bound leaves
$\tfrac72(H-1)(H-2)\geq0$.
At least one of the two halves has cost at most $N^2/50$.
This completes the balanced family and hence part (4).
Lemma 5 proves all integer assertions.

## Verification and limitations

The supplied exact-arithmetic verifier reconstructs the core, matching
cuts, and independent-set witnesses. It checks bounded examples of the
four families and verifies returned selections against all core edges.
Such finite checks support reproducibility; the proofs above establish
the unrestricted parameter claims.

The general sparse-half problem remains outside the scope of this note.
Uniform Clebsch graphs are covered by Razborov's strongly regular graph
result [Razborov](https://arxiv.org/abs/2104.09406v2) (Theorem 3.5 and Section 4.4); the present text concerns
specified nonuniform families. Known ingredients are attributed explicitly.
A bounded literature search has not located these exact restricted-family
statements, but this does not establish priority or exclude a stronger
prior theorem implying them. There is no claim of a prize-qualifying solution.

**AI-use and contribution disclosure.**

This project was initiated and directed by the account
`kasaharamihano-spec`.
Proof development, literature retrieval, drafting, implementation, and
cross-checks were performed extensively with OpenAI Codex and multiple
AI agents. The listed account attribution must not be read as a claim that
the account holder personally derived or independently verified every step.
AI cross-checks are not external expert review or formal verification.
This draft is shared for examination with these limitations explicit.
No AI system is listed as a human author.

## References

1. S. Norin and L. Yepremyan, *Sparse halves in dense triangle-free graphs*, Journal of Combinatorial Theory, Series B **115** (2015), 1–25. [Author version](https://arxiv.org/abs/1311.5818v2).

2. A. Razborov, *More about sparse halves in triangle-free graphs*, Sbornik: Mathematics **213** (2022), 109–128. [DOI](https://doi.org/10.1070/SM9615); [author version](https://arxiv.org/abs/2104.09406v2).

3. S. Brandt, *The local density of triangle-free graphs*, Freie Universität Berlin, Preprint A 95-14, June 1995, Proposition 1. [Official archive](https://ftp.mi.fu-berlin.de/pub/math/publ/pre/1995/index.html).
