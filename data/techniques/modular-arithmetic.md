---
id: modular-arithmetic
name: Modular arithmetic
group: Number theory
related: [parity, divisibility, diophantine, casework, descent]
---
## What it is
$a\equiv b\pmod n$ means $n\mid a-b$. Congruences can be added, subtracted and multiplied like equations: if $a\equiv b$ and $c\equiv d\pmod n$ then $a+c\equiv b+d$ and $ac\equiv bd$. Division is allowed only by numbers coprime to $n$.

Useful facts:
- Squares mod $3$ are $0,1$. Squares mod $4$ are $0,1$. Squares mod $8$ are $0,1,4$. Cubes mod $9$ are $0,1,8$.
- **Fermat's little theorem:** if $p$ is prime and $p\nmid a$ then $a^{p-1}\equiv1\pmod p$.
- **Euler's theorem:** if $\gcd(a,n)=1$ then $a^{\varphi(n)}\equiv1\pmod n$.

It works because an integer equation, reduced mod $n$, becomes a finite check. If the reduced equation has no solution, neither does the original.

## Recognize
- An equation in integers claimed to have no solutions, with a left side made of squares, cubes or powers.
- A divisibility question about a large expression (a huge power, a factorial, a polynomial).
- "Find the last digits" or "the remainder when..." appear.
- The problem has a clean statement for each residue class, so you can split [[casework|into cases]] by remainder.

## Example: A sum of two squares
**Problem.** Show that no integers $x,y,z$ satisfy $x^2+y^2=4z+3$.
1. Reduce mod $4$. Squares mod $4$ are $0$ (even numbers) or $1$ (odd numbers).
2. So $x^2+y^2\equiv0,1,$ or $2\pmod4$.
3. But the right side is $4z+3\equiv3\pmod4$.
4. No residue matches, so there are no solutions.

## Example: Choosing the modulus
**Problem.** Show that $x^3+y^3+z^3=2020$ has no integer solutions.
1. Cubes mod $9$: it is enough to cube the residues $0,\dots,4$ and use $(-x)^3=-x^3$. We get $0,\ 1,\ 8,\ 27\equiv0,\ 64\equiv1$. So $x^3\bmod9\in\{0,1,8\}$.
2. Sums of three elements from $\{0,1,8\}$ give: $0,1,2,3,6,7,8$ (for example, $1+1+1=3$, $8+8+8=24\equiv6$, $8+8+0=16\equiv7$, $8+8+1=17\equiv8$). Residues $4$ and $5$ never appear.
3. $2020=9\cdot224+4\equiv4\pmod9$.
4. So no solution exists.

## Example: Product of consecutive integers and Fermat
**Problem.** Show that $n^5-n$ is divisible by $30$ for every integer $n$.
1. $30=2\cdot3\cdot5$, so it is enough to check divisibility by $2$, $3$ and $5$ separately.
2. Factor: $n^5-n=n(n-1)(n+1)(n^2+1)$. The product $(n-1)n(n+1)$ contains a multiple of $2$ and a multiple of $3$.
3. For $5$: if $n\equiv0,1,4\pmod5$ then one of $n,\ n-1,\ n+1$ is divisible by $5$.
4. If $n\equiv2$ or $3\pmod5$ then $n^2\equiv4$, so $n^2+1\equiv0\pmod5$.
5. In every case $5$ divides it. So $30\mid n^5-n$. (This is also Fermat's little theorem for $p=5$.)

## Mistakes
- Dividing a congruence by a number not coprime to the modulus. $2a\equiv2b\pmod 6$ does not give $a\equiv b$.
- Picking a modulus that doesn't separate the values. Try $3,4,5,7,8,9$ and look at the residues of squares, cubes, fourth powers.
- Using Fermat/Euler when $\gcd(a,n)\ne1$.
- Missing residue classes. List all residues, including negative ones, and check each.

## Variations
- **Chinese remainder theorem:** compatible congruences mod coprime moduli combine into one mod the product.
- **Orders:** the smallest $d$ with $a^d\equiv1\pmod n$ divides $\varphi(n)$.
- **Lifting the exponent:** for the exact power of a prime dividing $a^n-b^n$.
- **Quadratic residues:** which numbers are squares mod $p$. Useful for $x^2+y^2$ and similar forms.
