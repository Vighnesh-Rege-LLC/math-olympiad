---
id: double-counting
name: Double counting
group: Combinatorics
related: [pigeonhole, parity, graph-theory, cauchy-schwarz]
---
## What it is
Count the same set in two different ways and equate the results. If both counts are correct, the two expressions must be equal, and often that equality is exactly the identity or inequality you want.

It works because a finite set has one size. The only effort is to find a set that is natural to count from two sides, typically pairs $(x,y)$ with some relation between $x$ and $y$: count by fixing $x$ first, or by fixing $y$ first.

## Recognize
- An identity with sums of binomials or products that looks like a count.
- A bipartite relationship (people and clubs, points and lines, numbers and divisors) where you can sum over either side.
- A bound on the number of edges, incidences or pairs.
- A sum over $k$ of floor functions, divisors, or degrees.

## Example: Divisors
**Problem.** Show that $\sum_{k=1}^{n}\left\lfloor\frac nk\right\rfloor=\sum_{m=1}^{n}d(m)$, where $d(m)$ is the number of positive divisors of $m$.
1. Count the pairs $(k,m)$ with $1\le k,m\le n$ and $k\mid m$.
2. Fix $m$ first. The number of choices of $k$ is the number of divisors of $m$, namely $d(m)$. Total: $\sum_{m=1}^nd(m)$.
3. Fix $k$ first. The multiples of $k$ that are at most $n$ are $k,2k,\dots,\lfloor n/k\rfloor k$, so there are $\lfloor n/k\rfloor$ choices of $m$. Total: $\sum_{k=1}^n\lfloor n/k\rfloor$.
4. Both are the number of pairs, so the sums are equal.

## Example: Vandermonde-type identity
**Problem.** Show that $\sum_{k=0}^{n}\binom nk^2=\binom{2n}n$.
1. Consider $n$ men and $n$ women. Count the committees of size $n$.
2. Directly: $\binom{2n}n$.
3. By the number of men $k$ on the committee: choose $k$ men in $\binom nk$ ways and $n-k$ women in $\binom n{n-k}=\binom nk$ ways. This gives $\binom nk^2$ committees for each $k$, for a total of $\sum_k\binom nk^2$.
4. The two counts agree.

## Example: Triangle-free graphs
**Problem.** A simple graph on $n$ vertices has no triangle. Show that it has at most $\frac{n^2}4$ edges.
1. Let $e$ be the number of edges and $d(v)$ the degree of vertex $v$.
2. If $uv$ is an edge, then $u$ and $v$ have no common neighbor (it would form a triangle), so $d(u)+d(v)\le n$.
3. Sum over all edges: $\sum_{uv}\big(d(u)+d(v)\big)\le ne$.
4. In the left side, each vertex $v$ appears once for each of its $d(v)$ edges, so it is counted $d(v)$ times with value $d(v)$. The left side equals $\sum_vd(v)^2$.
5. By Cauchy–Schwarz ([[cauchy-schwarz]]) and $\sum_vd(v)=2e$: $\sum_vd(v)^2\ge\frac{(2e)^2}n$.
6. So $\frac{4e^2}n\le ne$, and $e\le\frac{n^2}4$ (if $e>0$).

## Mistakes
- Counting pairs that are not in bijection between the two methods. Define the set of pairs precisely.
- Double counting ordered versus unordered pairs, and being off by a factor of $2$.
- Not recognizing the set: if one side of the identity looks like a count (a binomial coefficient), the set is often hidden there.
- Weighted counts where the two sides don't use the same weights. Both sides must count the same weighted set.

## Variations
- **Counting incidences:** points and lines, people and groups.
- **Counting with weights:** count with multiplicity to get an inequality.
- **Bijective proofs:** a one-to-one map shows two sets have equal size. A special form of double counting.
- **Averaging:** the average is at most the maximum, at least the minimum ([[pigeonhole]]).
- **Counting both ways, then an inequality:** like the last example.
