---
id: polynomials
name: Polynomials and Vieta
group: Algebra
related: [functional-equations, symmetry, generating-functions, divisibility]
---
## What it is
A polynomial is determined by its coefficients, its roots, or its values, and moving between these views is the main technique.

- **Vieta's formulas:** if $x^3+px^2+qx+r$ has roots $a,b,c$, then $a+b+c=-p$, $ab+bc+ca=q$, $abc=-r$. The same pattern holds in every degree for monic polynomials (divide by the leading coefficient otherwise).
- **Factor theorem:** $P(a)=0$ exactly when $(x-a)\mid P(x)$. **Remainder theorem:** the remainder of $P(x)$ divided by $x-a$ is $P(a)$.
- **Integer coefficients:** if $P$ has integer coefficients then $a-b\mid P(a)-P(b)$ for integers $a,b$.
- **Identity theorem:** two polynomials of degree at most $n$ that agree at $n+1$ points are equal.

It works because a polynomial of degree $n$ has at most $n$ roots, so a small amount of information fixes it, and symmetric functions of the roots can be read off the coefficients without finding the roots.

## Recognize
- You need a symmetric expression in the roots ($a^2+b^2+c^2$, $\frac1a+\frac1b$) of a given polynomial.
- A polynomial with integer coefficients and values at certain integers.
- A remainder on division by a polynomial, or a polynomial with prescribed values.
- An identity that holds for infinitely many values (so it holds as polynomials).

## Example: Symmetric expressions via Vieta
**Problem.** Let $a,b,c$ be the roots of $x^3-2x^2+3x-4=0$. Find $a^2+b^2+c^2$.
1. By Vieta, $a+b+c=2$ and $ab+bc+ca=3$.
2. $a^2+b^2+c^2=(a+b+c)^2-2(ab+bc+ca)=4-6=-2$.
3. The roots are not all real here, which is why the sum of squares can be negative. The computation never needs to find the roots.

## Example: Integer coefficients
**Problem.** Is there a polynomial $P$ with integer coefficients such that $P(7)=5$ and $P(15)=9$?
1. For integer coefficients, $a-b\mid P(a)-P(b)$. (Because $a^k-b^k$ is divisible by $a-b$ for every $k$.)
2. Here $a-b=8$, and $P(15)-P(7)=4$.
3. $8\nmid4$, so no such polynomial exists.

## Example: Remainder by a quadratic
**Problem.** A polynomial $P$ leaves remainder $3$ when divided by $x-1$ and remainder $5$ when divided by $x-2$. What is the remainder when it is divided by $(x-1)(x-2)$?
1. The remainder has degree less than $2$: $R(x)=ax+b$, and $P(x)=(x-1)(x-2)Q(x)+ax+b$.
2. Substitute $x=1$: $P(1)=a+b=3$ (remainder theorem). Substitute $x=2$: $P(2)=2a+b=5$.
3. Subtracting gives $a=2$, then $b=1$.
4. The remainder is $2x+1$.

## Mistakes
- Sign errors in Vieta. Write the polynomial as $x^n-e_1x^{n-1}+e_2x^{n-2}-\dots$ with $e_k$ the elementary symmetric sums.
- Using $a-b\mid P(a)-P(b)$ when coefficients are not integers.
- Forgetting that roots may be complex or repeated (count with multiplicity).
- Dividing by a polynomial that can be zero for some values.

## Variations
- **Newton's sums:** compute power sums $a^k+b^k+c^k$ recursively from the coefficients ([[recursion]]).
- **Lagrange interpolation:** a polynomial of degree $\le n$ with given values at $n+1$ points.
- **Rational root theorem:** a root $\frac pq$ (in lowest terms) of an integer polynomial has $p\mid$ constant term, $q\mid$ leading coefficient.
- **Irreducibility:** Eisenstein's criterion.
- **Roots of unity:** $x^n-1=\prod_{k=0}^{n-1}(x-\omega^k)$ with $\omega=e^{2\pi i/n}$ ([[complex-numbers]]).
