---
id: symmetry
name: Symmetry and WLOG
group: Proof methods
related: [casework, am-gm, double-counting, functional-equations]
---
## What it is
When a problem treats several objects the same way (swapping $a$ and $b$ leaves the statement unchanged, or reflecting the figure gives the same figure), you can use that sameness in two ways:
- **Without loss of generality (WLOG):** assume an ordering such as $a\le b\le c$. This is valid only if every other ordering is a relabeling of this one, so it loses nothing.
- **Pairing:** pair each term with its mirror image, so that two copies of a sum can be added into something simple.

It works because symmetry removes redundancy. A problem with $6$ equivalent orderings needs only one of them, and a sum equal to its own mirror can be computed as half of their combined total.

## Recognize
- The statement is unchanged under swapping variables, such as $x+y+z$, $xyz$, or $\frac1a+\frac1b+\frac1c$.
- A geometric figure has a line or center of symmetry, or the answer must be symmetric.
- A sum has terms $f(k)$ and $f(n-k)$ related to each other.
- You need to bound all variables and an ordering would give you a bound on the smallest.

## Example: WLOG ordering
**Problem.** Find all positive integers $a,b,c$ with $\dfrac1a+\dfrac1b+\dfrac1c=1$.
1. Since the equation is symmetric, any solution can be reordered so that $a\le b\le c$. So we may assume this order and find all such triples. (Other orders are rearrangements.)
2. The smallest denominator gives the largest fraction, so $\frac3a\ge\frac1a+\frac1b+\frac1c=1$, hence $a\le3$.
3. $a=1$ is impossible, since $\frac1b+\frac1c>0$ would give a sum greater than $1$.
4. $a=2$: $\frac1b+\frac1c=\frac12$ with $2\le b\le c$. Similarly $\frac2b\ge\frac12$ gives $b\le4$, and $b>2$ (otherwise $\frac1c=0$). If $b=3$ then $c=6$. If $b=4$ then $c=4$.
5. $a=3$: $\frac1b+\frac1c=\frac23$ with $b\ge3$. Then $\frac2b\ge\frac23$ gives $b\le3$, so $b=3$ and $c=3$.
6. The solutions are $(2,3,6),\ (2,4,4),\ (3,3,3)$ and their permutations.

## Example: Pairing terms
**Problem.** Evaluate $S=\sum_{k=0}^{n}k\binom nk$.
1. Use the symmetry $\binom nk=\binom n{n-k}$. Reindex the sum by $k\mapsto n-k$: $S=\sum_{k=0}^n(n-k)\binom nk$.
2. Add the two expressions for $S$: $2S=\sum_{k=0}^n\big(k+(n-k)\big)\binom nk=n\sum_{k=0}^n\binom nk=n\,2^n$.
3. So $S=n\,2^{n-1}$.

## Mistakes
- Using WLOG when the symmetry is not complete. Assuming $a\le b$ is fine for a symmetric statement in $a,b$, but if the conditions treat $a$ and $b$ differently, ordering loses cases.
- Ordering too much. After assuming $a\le b\le c$ you can no longer also assume another independent order condition among $a,b,c$.
- Forgetting to rebuild all solutions at the end: the answer includes all permutations.
- Assuming an expression is symmetric when only part of it is.

## Variations
- **Symmetric polynomials:** express things through $a+b+c$, $ab+bc+ca$, $abc$ (see [[polynomials]]).
- **Geometric symmetry:** reflect a point over a line to turn a shortest-path problem into a straight line.
- **Cyclic symmetry:** the statement is unchanged by $a\to b\to c\to a$ but not by every swap. You may rotate so that the maximum is first, but not sort fully.
- **Averaging over symmetry:** replace a quantity by its average over all relabelings (see [[am-gm]]).
