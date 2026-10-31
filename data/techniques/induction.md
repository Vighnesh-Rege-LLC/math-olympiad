---
id: induction
name: Induction
group: Proof methods
related: [extremal, constructive, recursion, invariants]
---
## What it is
To prove a statement $P(n)$ for all integers $n\ge n_0$:
1. **Base case:** prove $P(n_0)$.
2. **Step:** prove that $P(n)$ implies $P(n+1)$ for every $n\ge n_0$.

Then $P(n_0)$ holds, so $P(n_0+1)$ holds, and so on forever. **Strong induction** lets the step assume $P(k)$ for every $k$ with $n_0\le k\le n$, which is useful when $n+1$ depends on much smaller cases.

Induction works because the natural numbers are built by repeatedly adding one. Any claim that transfers from $n$ to $n+1$ climbs the entire ladder.

The skill is in choosing the statement. Often the claim you want is too weak to carry itself through the step, and you must prove something stronger.

## Recognize
- The statement depends on a positive integer $n$ (sums, sequences, board sizes, number of points).
- A configuration of size $n+1$ can be reduced to size $n$ by deleting one object, merging two, or cutting along something.
- A sequence is defined recursively.
- A direct attack at general $n$ is messy, but $n=1,2,3$ are easy and show a pattern.

## Example: Induction with an inequality
**Problem.** Prove that $2^n>n^2$ for all integers $n\ge5$.
1. Base case $n=5$: $2^5=32>25=5^2$.
2. Assume $2^n>n^2$ for some $n\ge5$. Then $2^{n+1}=2\cdot2^n>2n^2$.
3. We want $2n^2\ge(n+1)^2$. This is equivalent to $n^2\ge2n+1$, i.e. $(n-1)^2\ge2$, which holds for $n\ge3$, hence for $n\ge5$.
4. So $2^{n+1}>2n^2\ge(n+1)^2$, which completes the step.

## Example: Strong induction
**Problem.** Show that every integer $n\ge8$ can be paid exactly with coins of values $3$ and $5$.
1. Base cases: $8=3+5$, $9=3+3+3$, $10=5+5$.
2. Take $n\ge11$ and assume the claim for all values from $8$ up to $n-1$.
3. Since $n\ge11$, we have $n-3\ge8$, so $n-3$ can be paid by the assumption.
4. Add one coin of value $3$ to get $n$.
5. Three base cases are needed because the step reaches back $3$ values. With only the base case $8$, the values $9$ and $10$ would never be reached, and neither would anything that depends on them.

## Example: Strengthening the statement
**Problem.** Prove that $1+\frac1{2^2}+\frac1{3^2}+\dots+\frac1{n^2}<2$ for all $n\ge1$.
1. Try induction on the claim as stated. The step would give $S_n<2$ and need $S_n+\frac1{(n+1)^2}<2$, but knowing only $S_n<2$ leaves no room. The hypothesis is too weak.
2. Strengthen: prove $S_n\le2-\frac1n$. This implies $S_n<2$, and it gives the induction room.
3. Base case $n=1$: $S_1=1=2-\frac11$.
4. Step: assume $S_n\le2-\frac1n$. Then $S_{n+1}\le2-\frac1n+\frac1{(n+1)^2}$.
5. We need $-\frac1n+\frac1{(n+1)^2}\le-\frac1{n+1}$, i.e. $\frac1{(n+1)^2}\le\frac1n-\frac1{n+1}=\frac1{n(n+1)}$. This is true since $(n+1)^2\ge n(n+1)$.
6. So $S_{n+1}\le2-\frac1{n+1}$, completing the induction, and $S_n<2$ follows.

## Mistakes
- Forgetting the base case, or checking only one when the step reaches back further.
- A step that quietly assumes what it is proving, or that works only for $n$ large enough without saying so.
- Applying the hypothesis to a different object than the one the step produces. When reducing a size-$(n+1)$ configuration, check the smaller one satisfies all the conditions of $P(n)$.
- A step that is valid only for $n\ge2$ but is used from $n=1$. The classic false "all horses have the same color" proof fails exactly this way: $P(1)$ is true, but the step $P(1)\Rightarrow P(2)$ is invalid because the two groups of one horse do not overlap.

## Variations
- **Strong induction:** assume all earlier cases (coin problems, divisibility, recursion on both halves).
- **Two-step induction:** for sequences like Fibonacci, assume $P(n)$ and $P(n+1)$ and prove $P(n+2)$.
- **Induction on a different parameter:** the number of points, the number of vertices, or the largest element.
- **Backward (Cauchy) induction:** prove for infinitely many $n$ (such as powers of $2$) and step down. This is how AM-GM is proved for all $n$.
- **Strengthening the hypothesis:** see the third example. Also called "loading" the induction.
