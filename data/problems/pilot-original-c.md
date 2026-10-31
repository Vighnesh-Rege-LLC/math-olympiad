### o25
source: original
type: answer
difficulty: 3
techniques: similar-triangles
statement:
From a point $P$ outside a circle, a tangent $PT$ of length $12$ is drawn. A line through $P$ meets the circle at $A$ and $B$, with $PA=8$ and $A$ between $P$ and $B$. Find $AB$.
asked:
You know the tangent length and the near distance along a secant. Find the length of the chord $AB$.
technique:
Use [[similar-triangles|power of a point]], which comes from a pair of similar triangles.
hint:
For a point outside a circle, the square of the tangent length equals the product of the distances to the two intersection points of a secant.
hint:
Find $PB$ from $PT^2=PA\cdot PB$, then subtract $PA$.
solution:
Triangles $PTA$ and $PBT$ share the angle at $P$, and $\angle PTA=\angle PBT$ (tangent-chord angle), so they are similar and $\frac{PT}{PB}=\frac{PA}{PT}$, i.e. $PT^2=PA\cdot PB$. Hence $144=8\cdot PB$ and $PB=18$. Since $A$ lies between $P$ and $B$, $AB=PB-PA=18-8=\boxed{10}$.

### o26
source: original
type: answer
difficulty: 3
techniques: coordinates
statement:
Points $A=(-1,0)$ and $B=(1,0)$ are given. Describe the set of all points $P$ in the plane with $PA^2+PB^2=10$.
asked:
Find the shape and equation of the set of points whose squared distances to $A$ and $B$ add up to $10$.
technique:
Use [[coordinates]]. Write $P=(x,y)$ and translate the condition into an equation.
hint:
Write $PA^2$ and $PB^2$ with the distance formula in terms of $x$ and $y$.
hint:
Expand and simplify. Recognize the resulting equation.
solution:
Let $P=(x,y)$. Then $PA^2=(x+1)^2+y^2$ and $PB^2=(x-1)^2+y^2$. Adding,
$$2x^2+2y^2+2=10\ \Longrightarrow\ x^2+y^2=4.$$
The set is the circle with center $(0,0)$ and radius $2$.

### o27
source: original
type: answer
difficulty: 5
techniques: cauchy-schwarz
statement:
Positive reals $x,y,z$ satisfy $x+y+z=3$. Find the minimum of $\dfrac1x+\dfrac4y+\dfrac9z$.
asked:
Minimize the sum of the three fractions subject to the constraint, and say where it is attained.
technique:
Titu's form applies: numerators that are squares over denominators that sum to a known value.
hint:
Write the numerators as squares: $\frac{1^2}{x}+\frac{2^2}{y}+\frac{3^2}{z}$.
hint:
Apply $\sum\frac{a_i^2}{x_i}\ge\frac{(\sum a_i)^2}{\sum x_i}$. Then find when equality holds to make sure the bound is reached.
solution:
By Titu's lemma (Cauchy–Schwarz),
$$\frac{1^2}{x}+\frac{2^2}{y}+\frac{3^2}{z}\ge\frac{(1+2+3)^2}{x+y+z}=\frac{36}{3}=12.$$
Equality holds when $\frac x1=\frac y2=\frac z3$. With $x+y+z=3$ this gives $x=\frac12$, $y=1$, $z=\frac32$. Check: $2+4+6=12$. So the minimum is $\boxed{12}$.

### o28
source: original
type: proof
difficulty: 6
techniques: descent, divisibility
statement:
Prove that the equation $x^3+2y^3=4z^3$ has no solutions in positive integers.
asked:
Show that no positive integers $x,y,z$ satisfy $x^3+2y^3=4z^3$.
technique:
If a solution existed, you could build a smaller one, which cannot go on forever.
hint:
Look at the equation modulo $2$. What does it say about $x$? Write $x=2a$ and substitute.
hint:
Repeat the argument: after the substitution, the next variable must be even, then the next. Watch for the equation to return to its original form.
solution:
Suppose positive integers $x,y,z$ satisfy $x^3+2y^3=4z^3$.

Then $x^3=4z^3-2y^3$ is even, so $x=2a$, and $8a^3+2y^3=4z^3$, i.e. $4a^3+y^3=2z^3$. So $y^3$ is even, so $y=2b$, and $4a^3+8b^3=2z^3$, i.e. $2a^3+4b^3=z^3$. So $z^3$ is even, so $z=2c$, and $2a^3+4b^3=8c^3$, i.e. $a^3+2b^3=4c^3$.

So $(a,b,c)=(x/2,y/2,z/2)$ is another positive solution, strictly smaller. Repeating forever gives an infinite sequence of positive integer solutions $x>x/2>x/4>\dots$, which is impossible. Hence there is no solution. $\blacksquare$

### o29
source: original
type: proof
difficulty: 4
techniques: induction, constructive
statement:
Prove that every positive integer can be written as a sum of distinct powers of $2$ (that is, in binary).
asked:
Every positive integer $n$ must be a sum of different numbers from $1,2,4,8,\dots$.
technique:
Use strong [[induction]]. Subtract the largest power of $2$ that fits.
hint:
Given $n$, let $2^k$ be the largest power of $2$ with $2^k\le n$. What can you say about $n-2^k$?
hint:
Show $n-2^k<2^k$, so any representation of $n-2^k$ uses only powers smaller than $2^k$.
solution:
We use strong induction on $n$. For $n=1=2^0$ the claim is true.

Let $n\ge2$ and assume the claim for all smaller positive integers. Let $2^k$ be the largest power of $2$ with $2^k\le n$. If $n=2^k$ we are done. Otherwise $m=n-2^k$ is a positive integer, and $m<2^k$: otherwise $n\ge2\cdot2^k=2^{k+1}$, contradicting the choice of $k$. By the hypothesis, $m$ is a sum of distinct powers of $2$, each at most $m<2^k$, so all are different from $2^k$. Adding $2^k$ gives a representation of $n$. $\blacksquare$

### o30
source: original
type: answer
difficulty: 5
techniques: expectation
statement:
A fair six-sided die is rolled three times. What is the expected number of distinct values that appear?
asked:
Find the average number of different faces seen in three rolls.
technique:
Use [[expectation]]: linearity of expectation with indicator variables, one per face.
hint:
For each face value $v$, let $I_v=1$ if $v$ appears at least once. The number of distinct values is $\sum_vI_v$.
hint:
Compute $P(I_v=1)$ using the complement: $v$ never appears in three rolls. Then add over the six faces.
solution:
Let $I_v=1$ if value $v$ shows up at least once, else $0$. The number of distinct values is $\sum_{v=1}^6I_v$, so by linearity the expectation is $6\,P(I_1=1)$.

The probability that $1$ never shows up is $\left(\frac56\right)^3=\frac{125}{216}$, so $P(I_1=1)=\frac{91}{216}$. The expected number is $6\cdot\frac{91}{216}=\boxed{\dfrac{91}{36}}$.

### o31
source: original
type: answer
difficulty: 4
techniques: recursion
statement:
How many binary strings of length $8$ contain no two consecutive $1$s?
asked:
Count the $0$-$1$ strings of length $8$ in which the digit $1$ is never immediately followed by another $1$.
technique:
Use a [[recursion|recurrence]]: look at the last digit and relate to strings of shorter lengths.
hint:
Let $s_n$ be the count for length $n$. If the last digit is $0$, what can the first $n-1$ digits be?
hint:
If the last digit is $1$, what must the digit before it be? Combine the two cases into a relation between $s_n$ and earlier terms, and compute $s_1,s_2$ directly.
solution:
Let $s_n$ be the number of valid strings of length $n$. A valid string of length $n$ ends in $0$ or $1$.

- Ending in $0$: the first $n-1$ digits form any valid string, so $s_{n-1}$ ways.
- Ending in $1$: the previous digit must be $0$, and the first $n-2$ digits form any valid string, so $s_{n-2}$ ways.

So $s_n=s_{n-1}+s_{n-2}$, with $s_1=2$ ($0,1$) and $s_2=3$ ($00,01,10$). Then $s_3=5$, $s_4=8$, $s_5=13$, $s_6=21$, $s_7=34$, $s_8=\boxed{55}$.

### o32
source: original
type: answer
difficulty: 4
techniques: polynomials
statement:
A monic cubic polynomial $P$ satisfies $P(1)=1$, $P(2)=2$ and $P(3)=3$. Find $P(4)$.
asked:
You know the leading coefficient and three values of the cubic. Find its value at $4$.
technique:
Use [[polynomials]]: consider the polynomial $P(x)-x$, whose roots you know.
hint:
What are the roots of $Q(x)=P(x)-x$?
hint:
$Q$ is a monic cubic with three known roots, so it factors completely. Then evaluate at $4$.
solution:
Let $Q(x)=P(x)-x$. It is a monic cubic with $Q(1)=Q(2)=Q(3)=0$, so $Q(x)=(x-1)(x-2)(x-3)$. Therefore
$$P(4)=4+Q(4)=4+3\cdot2\cdot1=\boxed{10}.$$

### o33
source: original
type: proof
difficulty: 3
techniques: modular-arithmetic, casework
statement:
Prove that $n^2+n+1$ is never divisible by $5$.
asked:
For every integer $n$, show that $n^2+n+1$ leaves a nonzero remainder when divided by $5$.
technique:
Use [[modular-arithmetic]]: only the remainder of $n$ mod $5$ matters, so there are five cases to check.
hint:
Write the possible remainders of $n$ mod $5$: $0,1,2,3,4$.
hint:
Compute $n^2+n+1$ mod $5$ for each remainder.
solution:
The value of $n^2+n+1$ mod $5$ depends only on $n$ mod $5$:

| $n\bmod5$ | $0$ | $1$ | $2$ | $3$ | $4$ |
|---|---|---|---|---|---|
| $n^2+n+1\bmod5$ | $1$ | $3$ | $2$ | $3$ | $1$ |

(For example $n=2$: $4+2+1=7\equiv2$; $n=3$: $9+3+1=13\equiv3$; $n=4$: $16+4+1=21\equiv1$.) None is $0$. $\blacksquare$

### o34
source: original
type: proof
difficulty: 4
techniques: pigeonhole, parity
statement:
Five points with integer coordinates are given in the plane. Show that the midpoint of some two of them also has integer coordinates.
asked:
Among any five lattice points, find two whose midpoint is a lattice point.
technique:
Use [[pigeonhole]], sorting the points by the parity of their coordinates.
hint:
The midpoint of $(a,b)$ and $(c,d)$ is $\left(\frac{a+c}2,\frac{b+d}2\right)$. When are both coordinates integers?
hint:
Classify each point by the parities of $(x,y)$. How many classes are there?
solution:
The midpoint of $(a,b)$ and $(c,d)$ has integer coordinates exactly when $a+c$ and $b+d$ are both even, i.e. when $a,c$ have the same parity and $b,d$ have the same parity.

Classify each point by the parities of its two coordinates: (even, even), (even, odd), (odd, even), (odd, odd). These are four boxes. Five points go into four boxes, so two points share a class, and their midpoint is a lattice point. $\blacksquare$

### o35
source: original
type: answer
difficulty: 4
techniques: constructive, parity
statement:
Can plus and minus signs be placed in front of each of the numbers $1,2,\dots,2024$ so that the total is $0$?
asked:
Decide whether a choice of signs exists making $\pm1\pm2\pm\dots\pm2024=0$.
technique:
First check [[parity]] to see if it is ruled out. If not, find an explicit [[constructive]] pattern, perhaps on blocks of consecutive numbers.
hint:
The sum $1+2+\dots+2024$ is even. So parity does not forbid it. Try small cases: can you get $0$ from four consecutive numbers?
hint:
For four consecutive numbers $k,k+1,k+2,k+3$ choose signs $+,-,-,+$. What is the total?
solution:
**Yes.** For any four consecutive integers, $k-(k+1)-(k+2)+(k+3)=0$. Split $1,\dots,2024$ into $506$ blocks of four consecutive numbers, and use the signs $+,-,-,+$ on each block. Each block contributes $0$, so the total is $0$.

### o36
source: original
type: answer
difficulty: 3
techniques: modular-arithmetic, casework
statement:
Find all primes $p$ such that $8p^2+1$ is also prime.
asked:
Find every prime $p$ for which $8p^2+1$ is prime too.
technique:
Use [[modular-arithmetic]] with [[casework]]: look at $p$ modulo $3$.
hint:
Check $p=2$ and $p=3$ directly. What is $8p^2+1$ mod $3$ for a prime $p\neq3$?
hint:
If $3\nmid p$ then $p^2\equiv1\pmod3$. Deduce that $3\mid8p^2+1$.
solution:
If $p=3$: $8\cdot9+1=73$, which is prime. ✓

If $p\ne3$: then $p^2\equiv1\pmod3$ (as $p\equiv\pm1$), so $8p^2+1\equiv8+1=9\equiv0\pmod3$. And $8p^2+1>3$, so it is composite. (This includes $p=2$: $33=3\cdot11$.)

So the only such prime is $\boxed{p=3}$.
