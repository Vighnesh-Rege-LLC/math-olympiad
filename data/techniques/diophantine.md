---
id: diophantine
name: Diophantine equations
group: Number theory
related: [modular-arithmetic, divisibility, descent, casework]
---
## What it is
Equations whose solutions must be integers (or positive integers). The main strategies:
- **Factor:** rewrite as $(\text{something})(\text{something else})=\text{constant}$, then list the divisor pairs.
- **Bound:** show variables are small by size arguments, then check the finite list.
- **Reduce mod $n$:** show there are no solutions, or restrict their form ([[modular-arithmetic]]).
- **Parametrize:** describe all solutions by a formula, as for Pythagorean triples.
- **Descent:** show a smallest solution leads to a smaller one ([[descent]]).

It works because integrality is a strong constraint: a product of integers equal to $36$ has only finitely many possibilities.

## Recognize
- "Find all integer / positive integer solutions".
- An equation that rearranges to $xy+ax+by=c$ (use Simon's favorite factoring trick).
- A difference of squares or a quadratic that completes to a square.
- An exponent equation like $2^a+1=b^2$.

## Example: Simon's favorite factoring trick
**Problem.** Find all ordered pairs of positive integers $(x,y)$ with $\dfrac1x+\dfrac1y=\dfrac16$.
1. Multiply out: $6y+6x=xy$, i.e. $xy-6x-6y=0$.
2. Add $36$ to both sides to factor: $(x-6)(y-6)=36$.
3. Since $\frac1x<\frac16$, we have $x>6$, and likewise $y>6$. So both factors $x-6$ and $y-6$ are positive.
4. The positive divisors of $36$ are $1,2,3,4,6,9,12,18,36$, giving nine ordered pairs.
5. The solutions are $(7,42),(8,24),(9,18),(10,15),(12,12),(15,10),(18,9),(24,8),(42,7)$.

## Example: Completing the square
**Problem.** Find all integer solutions of $x^2=y^2+2y+13$.
1. Complete the square: $x^2=(y+1)^2+12$, so $x^2-(y+1)^2=12$.
2. Factor: $(x-y-1)(x+y+1)=12$. Let $d=x-y-1$ and $e=x+y+1$, so $de=12$.
3. Their sum $d+e=2x$ is even, so $d$ and $e$ have the same parity. Since $12$ is even, both must be even.
4. Even factor pairs of $12$: $(2,6),(6,2),(-2,-6),(-6,-2)$.
5. Use $x=\frac{d+e}2$ and $y+1=\frac{e-d}2$:
   - $(2,6)$: $x=4$, $y=1$. Check: $16=1+2+13$. ✓
   - $(6,2)$: $x=4$, $y=-3$. Check: $16=9-6+13$. ✓
   - $(-2,-6)$: $x=-4$, $y=-3$.
   - $(-6,-2)$: $x=-4$, $y=1$.
6. The solutions are $(x,y)=(\pm4,1)$ and $(\pm4,-3)$.

## Mistakes
- Missing negative factor pairs when the variables can be negative.
- Missing the symmetric (swapped) pairs, or counting ordered and unordered pairs inconsistently.
- Not checking each candidate in the original equation.
- Dividing by something that could be $0$.
- Forgetting parity constraints on the factors.

## Variations
- **Pythagorean triples:** all primitive solutions of $a^2+b^2=c^2$ are, up to swapping $a$ and $b$, $a=m^2-n^2$, $b=2mn$, $c=m^2+n^2$ with $m>n>0$, $\gcd(m,n)=1$ and opposite parity.
- **Pell equations:** $x^2-Dy^2=1$, with $D$ a positive non-square, has infinitely many solutions generated from a smallest one.
- **Exponential equations:** compare sizes and use mod arguments to limit exponents.
- **Linear equations:** $ax+by=c$ is solvable exactly when $\gcd(a,b)\mid c$ ([[divisibility]]).
