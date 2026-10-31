---
id: constructive
name: Constructive arguments
group: Proof methods
related: [induction, pigeonhole, extremal, invariants]
---
## What it is
To prove that something exists, build it. A constructive argument gives an explicit object (a number, a tiling, a sequence, a graph, an arrangement) and then checks that it has every required property.

It is the right tool when a statement says "there exist", "it is possible", "for every $n$ there is...". A pure existence argument ([[pigeonhole]], [[extremal]]) can also work, but if an object can be named you also learn what it looks like.

Constructions are found by experiment: try small $n$, find a pattern, then prove the pattern works. A good construction often arrives by induction ([[induction]]), where you build the $(n+1)$ object from the $n$ one.

## Recognize
- "Prove that for every $n$ there exist $n$ numbers such that...".
- "Is it possible to arrange / color / tile / schedule...?" and you suspect yes.
- An optimization problem: you need an example to show the bound is attained.
- Small cases suggest a pattern you can extend.

## Example: Long runs of composite numbers
**Problem.** Show that for every positive integer $n$ there are $n$ consecutive positive integers, all composite.
1. Take the numbers $(n+1)!+2,\ (n+1)!+3,\ \dots,\ (n+1)!+(n+1)$. There are $n$ of them and they are consecutive.
2. For $2\le k\le n+1$, $k$ divides $(n+1)!$ and divides $k$, so $k$ divides $(n+1)!+k$.
3. Also $(n+1)!+k>k$ and $k\ge2$, so each number has a divisor strictly between $1$ and itself. It is composite.

## Example: Using the Chinese remainder theorem
**Problem.** Show that for every $n$ there are $n$ consecutive positive integers, each divisible by a perfect square greater than $1$.
1. Choose $n$ distinct primes $p_1,\dots,p_n$.
2. The moduli $p_1^2,\dots,p_n^2$ are pairwise coprime, so by the Chinese remainder theorem there is a positive integer $x$ with $x\equiv-i\pmod{p_i^2}$ for every $i=1,\dots,n$.
3. Then $p_i^2$ divides $x+i$ for every $i$. The numbers $x+1,\dots,x+n$ are consecutive and each is divisible by a square greater than $1$.

## Example: Tiling with L-trominoes
**Problem.** From a $2^n\times2^n$ board one square is removed, anywhere. Show that the rest can be tiled by L-shaped trominoes (three squares in an L).
1. Induct on $n$. For $n=1$ the $2\times2$ board minus one square is exactly one L-tromino.
2. For $n\ge2$ cut the board into four $2^{n-1}\times2^{n-1}$ quadrants. The removed square lies in one quadrant, call it $Q$.
3. Place one L-tromino at the center of the board, covering one square from each of the three quadrants other than $Q$. The three squares are those adjacent to the center point.
4. Now each quadrant is a $2^{n-1}\times2^{n-1}$ board with exactly one square missing: $Q$ has the original removed square, and each other quadrant has the square covered by the central L.
5. By the induction hypothesis each quadrant can be tiled. Together with the central tromino this tiles the board.

(The area $4^n-1$ is divisible by $3$, which is a necessary condition. The construction shows it is sufficient here.)

## Mistakes
- Giving an example for small $n$ and claiming it works for all $n$. A general construction needs a proof that it satisfies every condition.
- Checking some conditions of the construction but not all.
- Describing the construction vaguely ("and so on"). Define it precisely, usually with a formula or a recursion.
- Confusing "possible" with "for every $n$". A construction for even $n$ doesn't settle odd $n$.

## Variations
- **Inductive construction:** build the $n+1$ object from the $n$ one (third example).
- **Explicit formulas:** factorials, CRT, geometric progressions.
- **Optimization:** show an upper bound by an argument, and attain it by a construction.
- **Algorithmic construction:** a procedure that provably terminates ([[invariants|monovariants]]).
- **Probabilistic existence:** show a random object works with positive probability ([[expectation]]).
