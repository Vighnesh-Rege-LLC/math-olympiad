### o13
source: original
type: answer
difficulty: 3
techniques: polynomials
statement:
The quadratic $x^2-5x+k$ has two roots $r$ and $s$ with $r^2+s^2=13$. Find $k$.
asked:
Find the constant term $k$ so that the sum of the squares of the roots is $13$.
technique:
This uses [[polynomials|Vieta's formulas]], which relate the roots to the coefficients without finding the roots.
hint:
Express $r+s$ and $rs$ using the coefficients of the quadratic.
hint:
Write $r^2+s^2$ in terms of $r+s$ and $rs$.
solution:
By Vieta, $r+s=5$ and $rs=k$. Then
$$r^2+s^2=(r+s)^2-2rs=25-2k.$$
Setting $25-2k=13$ gives $k=\boxed{6}$. (Check: $x^2-5x+6$ has roots $2,3$, and $4+9=13$.)

### o14
source: original
type: answer
difficulty: 3
techniques: diophantine, divisibility
statement:
Find all pairs of positive integers $(x,y)$ with $xy-3x-2y=0$.
asked:
Find every pair of positive integers satisfying the equation.
technique:
It can be rearranged into a product of two factors equal to a constant.
hint:
Add a constant to both sides so that the left side factors as $(x-a)(y-b)$.
hint:
Add $6$. Then list the ways to write the right side as a product of two integers, and keep only the pairs with $x,y>0$.
solution:
Adding $6$ to both sides: $xy-3x-2y+6=6$, i.e. $(x-2)(y-3)=6$.

Factor pairs of $6$: $(1,6),(2,3),(3,2),(6,1)$ and the negatives $(-1,-6),(-2,-3),(-3,-2),(-6,-1)$.

- Positive pairs give $(x,y)=(3,9),(4,6),(5,5),(8,4)$.
- Negative pairs need $x-2<0$; with $x\ge1$ this forces $x=1$, so $x-2=-1$, $y-3=-6$, $y=-3<0$. Rejected.

So the pairs are $\boxed{(3,9),\ (4,6),\ (5,5),\ (8,4)}$.

### o15
source: original
type: proof
difficulty: 3
techniques: induction
statement:
Prove that $n!>2^n$ for every integer $n\ge4$.
asked:
Factorials eventually outgrow powers of $2$. You must prove this from $n=4$ on.
technique:
Use [[induction]], starting at $n=4$ (not at $1$).
hint:
Check $n=4$ directly: compare $24$ with $16$.
hint:
Assume $n!>2^n$. To get $(n+1)!$ multiply by $n+1$. Compare $n+1$ with $2$.
solution:
**Base case.** $4!=24>16=2^4$.

**Step.** Assume $n!>2^n$ for some $n\ge4$. Then
$$(n+1)!=(n+1)\,n!>(n+1)\,2^n\ge2\cdot2^n=2^{n+1},$$
because $n+1\ge5>2$. So the claim holds for $n+1$. $\blacksquare$

### o16
source: original
type: answer
difficulty: 3
techniques: functional-equations
statement:
Does there exist a function $f:\mathbb R\to\mathbb R$ such that $f(x)+f(1-x)=x$ for every real $x$?
asked:
You must decide whether any function at all can satisfy this equation for all real $x$.
technique:
Try substituting a related value of $x$.
hint:
The equation holds for every $x$, so it also holds when $x$ is replaced by $1-x$. Write that version down.
hint:
Compare the two equations. What happens to the left sides?
solution:
**No.** Suppose such an $f$ exists. Replacing $x$ by $1-x$ gives $f(1-x)+f(x)=1-x$. The left side is the same as in the original equation, so $x=1-x$ for every real $x$. But this fails for $x=0$. So no such function exists.

### o17
source: original
type: answer
difficulty: 3
techniques: graph-theory, parity
statement:
Seven people are at a party. Is it possible that each of them shakes hands with exactly three of the others?
asked:
Decide whether seven people can each have shaken hands with exactly three others.
technique:
Model this as a graph ([[graph-theory]]): people are vertices and handshakes are edges. Count the handshakes in two ways.
hint:
Add up the number of handshakes each person took part in. How is that total related to the number of handshakes?
hint:
Each handshake is counted twice in that total. What does that say about whether the total can be odd?
solution:
**No.** If each of the $7$ people shook hands with $3$ others, the total of the individual counts is $7\cdot3=21$. Each handshake involves two people, so it is counted twice, and the total must be twice the number of handshakes. But $21$ is odd. Contradiction.

### o18
source: original
type: proof
difficulty: 4
techniques: double-counting
statement:
Prove that $\displaystyle\sum_{k=1}^{n}k\binom nk=n\,2^{n-1}$.
asked:
Prove the identity for every positive integer $n$.
technique:
Find a set that the left side counts in one way and the right side counts in another.
hint:
Interpret $\binom nk$ as choosing a committee of $k$ people from $n$. What does multiplying by $k$ add?
hint:
Count pairs (committee, chair), where the chair is a member of the committee. Count by choosing the chair first.
solution:
Count the pairs $(C,p)$ where $C$ is a nonempty committee chosen from $n$ people and $p$ is a member of $C$ (the chair).

**By committee size.** For committees of size $k$ there are $\binom nk$ committees and $k$ choices of chair, giving $\sum_{k=1}^nk\binom nk$ pairs.

**By chair.** Choose the chair first: $n$ ways. The remaining $n-1$ people each join the committee or not: $2^{n-1}$ ways. This gives $n\,2^{n-1}$ pairs.

Both counts give the same number of pairs. $\blacksquare$

### o19
source: original
type: answer
difficulty: 4
techniques: symmetry, casework
statement:
Find all triples of positive integers $(a,b,c)$ with $abc=a+b+c$.
asked:
Find every ordered triple of positive integers whose product equals its sum.
technique:
The equation is unchanged when the variables are swapped, so use [[symmetry]]: assume an ordering of the variables.
hint:
Assume $a\le b\le c$. Then $a+b+c\le3c$. What does that say about $ab$?
hint:
From $ab\le3$, list the possible $(a,b)$ and solve for $c$ in each case. At the end, include permutations.
solution:
By symmetry assume $a\le b\le c$. Then $abc=a+b+c\le3c$, so $ab\le3$. The pairs $(a,b)$ with $a\le b$ and $ab\le3$ are $(1,1),(1,2),(1,3)$.

- $(1,1)$: $c=2+c$. Impossible.
- $(1,2)$: $2c=3+c$, so $c=3$. Valid, since $2\le3$.
- $(1,3)$: $3c=4+c$, so $c=2<b$. Not allowed.

So the only ordered solution is $(1,2,3)$, and all triples are the $6$ permutations of $(1,2,3)$.

### o20
source: original
type: proof
difficulty: 4
techniques: extremal
statement:
Let $S$ be a finite set of at least two points in the plane. Prove that it is impossible for every point of $S$ to be the midpoint of two other points of $S$.
asked:
You must show that in any finite set of points, some point is not the midpoint of two other points of the set.
technique:
Look at the point that is most extreme in some direction.
hint:
Among the points of $S$, look at those with the largest $x$-coordinate. Pick the one with the largest $y$-coordinate among them.
hint:
Suppose this point $P$ is the midpoint of $Q$ and $R$, both in $S$ and different from $P$. Compare the coordinates of $Q$ and $R$ with those of $P$.
solution:
Among the points of $S$ take $P=(p,q)$ with the largest $x$-coordinate, and among those the largest $y$-coordinate. Suppose $P$ is the midpoint of two other points $Q=(x_1,y_1)$ and $R=(x_2,y_2)$ of $S$. Then $x_1+x_2=2p$ and $y_1+y_2=2q$.

Since $x_1,x_2\le p$ and $x_1+x_2=2p$, we get $x_1=x_2=p$. Then $Q$ and $R$ have the same $x$-coordinate as $P$, so by the choice of $P$, $y_1,y_2\le q$. With $y_1+y_2=2q$ this gives $y_1=y_2=q$. So $Q=R=P$, contradicting that they are different from $P$. $\blacksquare$

### o21
source: original
type: answer
difficulty: 4
techniques: generating-functions
statement:
How many triples of non-negative integers $(x,y,z)$ satisfy $x+y+z=10$ with each of $x,y,z$ at most $5$?
asked:
Count the solutions of $x+y+z=10$ in non-negative integers in which no variable exceeds $5$.
technique:
Use [[generating-functions]] or complementary counting: first count without the upper bound, then remove the bad cases.
hint:
How many non-negative solutions are there with no upper bound? The standard stars-and-bars count is $\binom{n+2}{2}$ for sum $n$.
hint:
A solution is bad if some variable is at least $6$. Count solutions with $x\ge6$ by shifting $x'=x-6$. Can two variables be at least $6$ at once?
solution:
Without a bound there are $\binom{12}{2}=66$ solutions of $x+y+z=10$.

Bad solutions have some variable $\ge6$. If $x\ge6$, put $x'=x-6$; then $x'+y+z=4$ has $\binom62=15$ solutions. The same holds for $y$ and $z$, giving $45$ bad solutions counted by variable. Two variables $\ge6$ would need a sum of at least $12>10$, so no solution is counted twice.

The answer is $66-45=\boxed{21}$. (Generating-function view: the coefficient of $t^{10}$ in $\left(\frac{1-t^6}{1-t}\right)^3$.)

### o22
source: original
type: answer
difficulty: 3
techniques: complex-numbers
statement:
Compute $(1+i)^{20}$.
asked:
Find the exact value of $(1+i)^{20}$ as a complex number.
technique:
Use [[complex-numbers]]: squaring $1+i$ gives something much simpler.
hint:
Compute $(1+i)^2$.
hint:
Write $(1+i)^{20}$ as a power of $(1+i)^2$, and use $i^2=-1$.
solution:
$(1+i)^2=1+2i+i^2=2i$. So
$$(1+i)^{20}=\big((1+i)^2\big)^{10}=(2i)^{10}=2^{10}i^{10}=1024\cdot i^{10}.$$
Since $i^{10}=(i^2)^5=(-1)^5=-1$, the value is $\boxed{-1024}$.

### o23
source: original
type: answer
difficulty: 3
techniques: trigonometry
statement:
A triangle has side lengths $7$, $8$ and $9$. Find the cosine of its largest angle.
asked:
The triangle is determined by its three sides. Find the cosine of the largest angle.
technique:
Use [[trigonometry]]: the law of cosines links an angle with the three sides.
hint:
The largest angle is opposite the longest side. Which side is that?
hint:
Apply the law of cosines $c^2=a^2+b^2-2ab\cos C$ with $c=9$.
solution:
The largest angle $C$ is opposite the longest side $c=9$. By the law of cosines,
$$81=49+64-2\cdot7\cdot8\cos C,\quad\text{so}\quad\cos C=\frac{113-81}{112}=\frac{32}{112}=\boxed{\frac27}.$$

### o24
source: original
type: answer
difficulty: 3
techniques: angle-chasing
statement:
$ABCD$ is a cyclic quadrilateral (its vertices lie on a circle) with $\angle ABC=100^\circ$ and $\angle CAD=25^\circ$. Find $\angle ACD$.
asked:
Find the measure of angle $ACD$ in the cyclic quadrilateral.
technique:
Use what you know about the opposite angles of a cyclic quadrilateral.
hint:
In a cyclic quadrilateral opposite angles add to $180^\circ$. Find $\angle ADC$.
hint:
Now look at triangle $ACD$ and use the angle sum.
solution:
Opposite angles of a cyclic quadrilateral sum to $180^\circ$, so $\angle ADC=180^\circ-100^\circ=80^\circ$.

In triangle $ACD$: $\angle ACD=180^\circ-\angle ADC-\angle CAD=180^\circ-80^\circ-25^\circ=\boxed{75^\circ}$.
