---
id: pigeonhole
name: Pigeonhole principle
group: Combinatorics
related: [double-counting, modular-arithmetic, extremal, constructive]
---
## What it is
If more than $kn$ objects are placed into $n$ boxes, some box holds at least $k+1$ of them. The simplest case: $n+1$ objects in $n$ boxes force a box with two objects.

It works because a distribution that is "too even" cannot hold more objects than boxes times capacity. If every box held at most $k$, the total would be at most $kn$. The principle proves that something exists without saying which box, or which objects, it is.

The real work is choosing the objects and the boxes. The boxes encode the property you want two objects to share.

## Recognize
- The problem says "show that some two (or $k$) of them have...", or "there exist two with...", with no way to point at them.
- You have more objects than natural categories: $n+1$ numbers, $5$ points, $13$ people.
- You can sort objects into few classes by a remainder, a region, a color, a binary pattern, or the largest odd divisor.
- The conclusion is about a difference, a ratio, or a distance being small or divisible by something.

## Example: Five points in a square
**Problem.** Five points lie in a unit square (side length $1$, boundary included). Show that two of them are at distance at most $\frac{\sqrt2}{2}$.
1. The goal is a pair of points that are close. Close points should land in the same box, so the boxes should be small regions.
2. Cut the square into four squares of side $\tfrac12$ by joining the midpoints of opposite sides.
3. Five points, four small squares: some small square contains two of the points. A point on a shared edge may be assigned to either square, since each point just needs one box.
4. The largest distance inside a square of side $\tfrac12$ is its diagonal, $\tfrac12\sqrt2=\frac{\sqrt2}{2}$.
5. So those two points are at distance at most $\frac{\sqrt2}{2}$.

## Example: Odd parts
**Problem.** Choose $n+1$ distinct numbers from $\{1,2,\dots,2n\}$. Show that one of the chosen numbers divides another.
1. Every positive integer can be written uniquely as $2^a\cdot m$ with $m$ odd. Call $m$ its odd part.
2. The odd parts of numbers in $\{1,\dots,2n\}$ are odd numbers at most $2n$, so there are only $n$ possibilities: $1,3,\dots,2n-1$. These are the boxes.
3. There are $n+1$ chosen numbers and $n$ boxes, so two chosen numbers $x\ne y$ share the same odd part $m$.
4. Write $x=2^a m$ and $y=2^b m$. Since $x\ne y$, $a\ne b$. If $a<b$ then $x$ divides $y$, otherwise $y$ divides $x$.

## Example: A block with sum divisible by $n$
**Problem.** Given integers $a_1,\dots,a_n$, show that some nonempty block of consecutive terms $a_{i+1}+\dots+a_j$ has sum divisible by $n$.
1. A block sum is a difference of two prefix sums. Define $S_0=0$ and $S_k=a_1+\dots+a_k$.
2. The block sum $a_{i+1}+\dots+a_j$ equals $S_j-S_i$, and it is divisible by $n$ exactly when $S_i\equiv S_j\pmod n$.
3. So the objects are $S_0,S_1,\dots,S_n$, which is $n+1$ numbers. The boxes are the $n$ remainders mod $n$.
4. Two of them have the same remainder: $S_i\equiv S_j$ with $i<j$. Then $a_{i+1}+\dots+a_j$ is divisible by $n$, and the block is nonempty because $i<j$.

## Mistakes
- Counting boxes wrong. Always list the boxes explicitly and count them. In the odd-parts example there are $n$ boxes, not $2n$.
- Forgetting an object, like $S_0=0$ in the prefix sums. It supplies the extra object that makes $n+1$.
- Boxes that don't enforce the property. Two points in one region must really be close, so check the maximum distance inside a box.
- Treating the principle as giving a specific box. It does not say which box is crowded.

## Variations
- **Generalized form:** with $N$ objects in $n$ boxes, some box has at least $\lceil N/n\rceil$ objects.
- **Averaging version:** the largest of $x_1,\dots,x_n$ is at least their average, and the smallest is at most it. It is the same idea with numbers.
- **Infinite version:** infinitely many objects in finitely many boxes puts infinitely many in one box.
- **Ramsey flavor:** among any $6$ people, there are $3$ mutual friends or $3$ mutual strangers. Choose one person, and pigeonhole on their $5$ relationships (see [[casework]]).
- **Area and length versions:** if regions inside a set have total area larger than the set, two overlap.
