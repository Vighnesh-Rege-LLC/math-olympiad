---
id: extremal
name: Extremal principle
group: Proof methods
related: [induction, pigeonhole, descent, constructive]
---
## What it is
Among finitely many possibilities, there is a largest and a smallest one. Look at the object that is extreme in some quantity (the longest path, the leftmost point, the smallest counterexample, the person with the most wins) and use its extremality to get information.

It works because an extreme object cannot be improved. If it could, it would not be extreme. So the extreme object satisfies conditions the others need not, and "you cannot do better" often forces a contradiction or a structure.

The art is choosing what to maximize or minimize: a length, a distance, an area, a degree, a value.

## Recognize
- The problem asserts that something exists, such as a vertex, a point, or a pair with some property.
- The configuration is finite, or the quantities are positive integers (a minimum always exists).
- You are tempted to start the argument with "take any element" but no element is special.
- Moving or modifying an object seems to always give you a better one, unless it is already optimal.

## Example: The player with the most wins
**Problem.** In a round-robin tournament every pair of players plays once and there are no ties. Let $A$ be a player with the maximum number of wins. Show that for every other player $B$, either $A$ beat $B$, or $A$ beat some player who beat $B$.
1. Take $A$ with the most wins. Let $B$ be another player. If $A$ beat $B$, we are done, so assume $B$ beat $A$.
2. Suppose, for contradiction, that nobody $A$ beat has beaten $B$.
3. Every player $A$ beat then lost to $B$ (there are no ties). Also $B$ beat $A$.
4. So $B$ beat everyone $A$ beat, plus $A$ itself. $B$'s wins are at least $A$'s wins $+1$.
5. This contradicts the maximality of $A$. So some player beaten by $A$ beat $B$.

## Example: A cycle in a graph
**Problem.** In a finite simple graph (no loops or repeated edges) every vertex has degree at least $2$. Show the graph contains a cycle.
1. Take a longest path $P=v_1v_2\dots v_k$ (the vertices are all different). A longest path exists because the graph is finite.
2. Look at the end vertex $v_1$. If it had a neighbor $w$ outside $P$, then $wv_1v_2\dots v_k$ would be a longer path. That contradicts the choice of $P$.
3. So every neighbor of $v_1$ is on $P$. Since the degree of $v_1$ is at least $2$, it has a neighbor $v_j$ with $j\ne2$ (it has at least two neighbors, and only one of them is $v_2$). Therefore $j\ge3$.
4. Then $v_1v_2\dots v_jv_1$ is a cycle.

## Example: Smallest counterexample
**Problem.** Show that $\sqrt2$ is irrational.
1. Suppose $\sqrt2=\frac pq$ with positive integers $p,q$. Among all such representations pick the one with the smallest $q$.
2. Then $p^2=2q^2$, so $p^2$ is even, so $p$ is even. Write $p=2r$.
3. Then $4r^2=2q^2$, so $q^2=2r^2$, which gives $\sqrt2=\frac qr$.
4. Also $r<q$: since $\sqrt2<2$ we have $p<2q$, so $r=\frac p2<q$. So $\frac qr$ is a representation with a smaller denominator $r$.
5. This contradicts the minimality of $q$.

## Mistakes
- Using an extreme without checking it exists. Infinitely many objects may have no maximum. State why the set is finite, or the values are positive integers.
- Choosing an extreme that does not interact with the conditions. If your maximum has no connection to the hypotheses, you cannot use it.
- Forgetting that extremes may be non-unique. Say "an" extreme object, not "the".
- Concluding too early. Often one must show that moving away from the extreme object either improves it or breaks a rule.

## Variations
- **Smallest counterexample / infinite descent:** see [[descent]].
- **Extreme in geometry:** the point closest to a line, the triangle of smallest area, the pair of points at minimal distance, the vertex of the convex hull.
- **Extreme choice inside a proof:** pick the largest root, the minimal element in a set, the longest chain.
- **Optimization (not only existence):** to find the max of a quantity, guess the extreme configuration and prove nothing is larger (see [[constructive]]).
