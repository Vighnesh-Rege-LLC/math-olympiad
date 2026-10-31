---
id: divisibility
name: Divisibility and gcd
group: Number theory
related: [modular-arithmetic, diophantine, descent, polynomials]
---
## What it is
The tools for reasoning about when one integer divides another.

- **Euclid's algorithm:** $\gcd(a,b)=\gcd(b,a-qb)$ for any integer $q$. Subtract multiples to simplify.
- **Bézout:** there are integers $x,y$ with $ax+by=\gcd(a,b)$.
- **Euclid's lemma:** if a prime $p$ divides $ab$, then $p\mid a$ or $p\mid b$. More generally, if $\gcd(a,b)=1$ and $a\mid bc$ then $a\mid c$.
- **Unique factorization:** every integer $>1$ is a product of primes in exactly one way up to order.
- If $d\mid a$ and $d\mid b$ then $d$ divides every combination $ax+by$.

It works because divisibility is preserved by linear combinations. To show a quantity divides something, express it as a combination. To bound a gcd, show it divides a small number.

## Recognize
- "Find all $n$ such that $n+1\mid n^2+1$" and similar.
- A gcd of two expressions that are polynomial or factorial in $n$.
- A statement involving "coprime" or "relatively prime".
- A product $ab$ of coprime positive integers that is a perfect power (each factor is then a perfect power).

## Example: Reduce the divisor
**Problem.** Find all positive integers $n$ such that $n+1\mid n^2+1$.
1. Write $n^2+1=(n+1)(n-1)+2$.
2. Since $n+1\mid(n+1)(n-1)$, we get $n+1\mid n^2+1$ exactly when $n+1\mid2$.
3. For positive $n$, $n+1\ge2$, so $n+1=2$ and $n=1$. Check: $2\mid2$. ✓

## Example: Euclid's algorithm with factorials
**Problem.** Show that $n!+1$ and $(n+1)!+1$ are coprime for every positive integer $n$.
1. Let $d=\gcd(n!+1,\ (n+1)!+1)$.
2. Note $(n+1)!+1=(n+1)(n!+1)-n$. Since $d$ divides $n!+1$ and $(n+1)!+1$, it divides $n$.
3. For $n\ge1$, $n\mid n!$, so $d\mid n!$.
4. But $d\mid n!+1$ too, so $d\mid(n!+1)-n!=1$.
5. So $d=1$.

## Example: Coprime sum and product
**Problem.** If $\gcd(a,b)=1$ show that $\gcd(a+b,ab)=1$.
1. Suppose a prime $p$ divides both $a+b$ and $ab$.
2. Since $p\mid ab$, Euclid's lemma gives $p\mid a$ or $p\mid b$. Say $p\mid a$.
3. Then $p\mid(a+b)-a=b$. So $p$ divides both $a$ and $b$, contradicting $\gcd(a,b)=1$.
4. So no prime divides both, and the gcd is $1$.

## Mistakes
- Concluding $a\mid c$ from $a\mid bc$ without $\gcd(a,b)=1$ ($4\mid2\cdot2$ but $4\nmid2$).
- Treating $n+1\mid f(n)$ as $n+1\mid f(-1)$ without proof. It works for polynomials with integer coefficients: $n+1\mid f(n)-f(-1)$.
- Forgetting trivial cases ($n=1$, or when an expression is zero).
- Assuming a gcd is a prime. It can be composite.

## Variations
- **Perfect powers:** if $a,b>0$, $ab$ is a square and $\gcd(a,b)=1$, both $a$ and $b$ are squares.
- **Linear combinations:** if $d\mid x$ and $d\mid y$, then $d\mid px+qy$.
- **lcm and gcd:** $\gcd(a,b)\cdot\operatorname{lcm}(a,b)=ab$ for positive $a,b$.
- **Valuations:** count the exact power of $p$ in a number, e.g. Legendre's formula for $n!$.
- **Congruence viewpoint:** [[modular-arithmetic]].
