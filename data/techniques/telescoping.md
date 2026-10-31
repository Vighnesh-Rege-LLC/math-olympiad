---
id: telescoping
name: Telescoping
group: Algebra
related: [recursion, generating-functions, induction]
---
## What it is
A sum or product **telescopes** when each term can be written so that most pieces cancel with their neighbors. For a sum, write each term as a difference $a_k=b_{k+1}-b_k$; then
$$\sum_{k=1}^{n}a_k=b_{n+1}-b_1.$$
For a product, write each factor as a ratio $\frac{c_{k+1}}{c_k}$; then the product is $\frac{c_{n+1}}{c_1}$.

It works because a long sum of apparently unrelated terms collapses to its two ends. The skill is finding the decomposition, usually by partial fractions, rationalizing, or noticing a factorial identity.

## Recognize
- Sums of fractions with consecutive factors in the denominator, such as $\frac1{k(k+1)}$.
- Square roots, logarithms, or factorials where consecutive terms look alike.
- Products of terms like $1-\frac1{k^2}$ that factor into neighbors.
- An answer that is expected to be short even though the sum has $n$ terms.

## Example: Partial fractions
**Problem.** Evaluate $\displaystyle\sum_{k=1}^{n}\frac1{k(k+1)}$.
1. Split each term: $\dfrac1{k(k+1)}=\dfrac1k-\dfrac1{k+1}$.
2. The sum is $\left(1-\tfrac12\right)+\left(\tfrac12-\tfrac13\right)+\dots+\left(\tfrac1n-\tfrac1{n+1}\right)$.
3. All middle terms cancel, leaving $1-\dfrac1{n+1}=\dfrac n{n+1}$.

## Example: Factorials
**Problem.** Evaluate $\displaystyle\sum_{k=1}^{n}k\cdot k!$.
1. Write $k\cdot k!=\big((k+1)-1\big)\,k!=(k+1)!-k!$.
2. The sum becomes $(2!-1!)+(3!-2!)+\dots+\big((n+1)!-n!\big)$.
3. It telescopes to $(n+1)!-1!=(n+1)!-1$.

## Example: A product
**Problem.** Evaluate $\displaystyle\prod_{k=2}^{n}\left(1-\frac1{k^2}\right)$.
1. Factor: $1-\dfrac1{k^2}=\dfrac{k-1}{k}\cdot\dfrac{k+1}{k}$.
2. The product of the first factors is $\dfrac12\cdot\dfrac23\cdots\dfrac{n-1}n=\dfrac1n$.
3. The product of the second factors is $\dfrac32\cdot\dfrac43\cdots\dfrac{n+1}n=\dfrac{n+1}2$.
4. So the product is $\dfrac{n+1}{2n}$. Check $n=2$: the product is $1-\frac14=\frac34$ and the formula gives $\frac{3}{4}$. ✓

## Mistakes
- Cancelling wrongly: write out the first three and last three terms to see exactly what survives.
- Losing the leftover terms. Sometimes two terms remain at each end, not one.
- Forcing a telescoping decomposition that doesn't hold. Verify $a_k=b_{k+1}-b_k$ for a small $k$.
- Index shifts: the sum equals $b_{n+1}-b_1$, not $b_n-b_1$.

## Variations
- **Rationalizing:** $\dfrac1{\sqrt k+\sqrt{k+1}}=\sqrt{k+1}-\sqrt k$.
- **Partial fractions with a gap:** $\dfrac1{k(k+2)}=\tfrac12\left(\tfrac1k-\tfrac1{k+2}\right)$, where two terms survive at each end.
- **Trigonometric:** $2\sin\tfrac x2\cos kx=\sin\left(k+\tfrac12\right)x-\sin\left(k-\tfrac12\right)x$.
- **Telescoping inequalities:** bound $a_k\le b_k-b_{k+1}$ and sum to bound the total ([[induction]] gives the same strengthening).
