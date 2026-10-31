---
id: generating-functions
name: Generating functions
group: Algebra
related: [recursion, telescoping, double-counting, polynomials]
---
## What it is
A sequence $a_0,a_1,a_2,\dots$ is packaged as a power series $A(x)=a_0+a_1x+a_2x^2+\dots$. Multiplying series convolves the sequences: the coefficient of $x^n$ in $A(x)B(x)$ is $\sum_{k}a_kb_{n-k}$. Counting problems with independent choices turn into products of series.

Key series:
- $\dfrac1{1-x}=1+x+x^2+\dots$
- $\dfrac1{(1-x)^m}=\sum_{n\ge0}\binom{n+m-1}{m-1}x^n$
- $(1+x)^n=\sum_{k}\binom nkx^k$

It works because algebra on series does the bookkeeping for counting. You never need to find the sequence term by term; you find a closed form for $A(x)$ and read the coefficients.

## Recognize
- Counting the number of ways to choose with restrictions: each type of item contributes a factor.
- Identities with convolution sums like $\sum_ka_kb_{n-k}$.
- Sums over a subset defined by a residue (even-indexed, multiples of $3$).
- A recurrence that is hard to solve directly.

## Example: Counting solutions
**Problem.** How many non-negative integer solutions does $x+y+z=n$ have?
1. Each variable contributes the series $1+t+t^2+\dots=\dfrac1{1-t}$, where the exponent records its value.
2. The coefficient of $t^n$ in $\left(\dfrac1{1-t}\right)^3$ counts the solutions.
3. By the formula for $\dfrac1{(1-t)^m}$ with $m=3$, this coefficient is $\binom{n+2}2$.

## Example: A binomial identity
**Problem.** Prove that $\displaystyle\sum_{k=0}^{r}\binom mk\binom n{r-k}=\binom{m+n}r$.
1. Expand $(1+x)^m(1+x)^n=(1+x)^{m+n}$.
2. The coefficient of $x^r$ on the right is $\binom{m+n}r$.
3. On the left, the coefficient of $x^r$ in the product is $\sum_k\binom mk\binom n{r-k}$ by the convolution rule.
4. Equating the two gives the identity.

## Example: Roots of unity filter
**Problem.** Show that for $n\ge1$, $\displaystyle\sum_{k\text{ even}}\binom nk=2^{n-1}$.
1. Let $f(x)=(1+x)^n=\sum_k\binom nkx^k$.
2. Then $f(1)+f(-1)=\sum_k\binom nk\big(1+(-1)^k\big)$. Odd $k$ contribute $0$ and even $k$ contribute $2\binom nk$.
3. So $\sum_{k\text{ even}}\binom nk=\dfrac{f(1)+f(-1)}2=\dfrac{2^n+0^n}2=2^{n-1}$, since $n\ge1$ gives $0^n=0$.

## Mistakes
- Forgetting that the factors must be independent. If the choices interact, a simple product does not work.
- Wrong closed form for a series. Test by expanding the first few terms.
- Treating series as functions without caring about convergence. In olympiad counting problems you work with formal series, where convergence is not an issue, but substituting numbers (like $x=-1$) needs a polynomial, or a series that converges at that value.
- Off-by-one errors in the exponent that records the quantity.

## Variations
- **Exponential generating functions:** for labelled structures (permutations, set partitions), where choices combine with binomial coefficients.
- **Roots of unity filter:** extract terms with exponents in a residue class ($x=\omega$, a primitive cube root of unity, for mod $3$).
- **Solving recurrences:** multiply the recurrence by $x^n$ and sum ([[recursion]]).
- **Partial fractions of series:** to read off coefficients of $\dfrac1{(1-ax)(1-bx)}$ when $a\ne b$.
- **Polynomial viewpoint:** a polynomial identity can be checked by values at many points ([[polynomials]]).
