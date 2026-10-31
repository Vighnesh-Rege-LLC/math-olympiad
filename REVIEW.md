# Review sample

40 problems drawn at random (seed 40) from 60. Check the statement, the hints, and above all the solution.

## o06 · difficulty 2 · AM-GM and mean inequalities
*original*

**Statement**

For positive real $x$, what is the minimum value of $x+\dfrac9x$?

**Hint 1: What is being asked**

Over all positive $x$, find the smallest value that $x+\frac9x$ can take.

**Hint 2: The technique**

The two terms multiply to a constant.

**Hint 3: The key idea**

Apply the inequality "arithmetic mean $\ge$ geometric mean" to the two positive numbers $x$ and $\frac9x$.

**Hint 4: The next step**

Compute their product. Then find the $x$ at which the two terms are equal, and check that the bound is actually reached.

**Solution**

By AM-GM, $\dfrac{x+\frac9x}{2}\ge\sqrt{x\cdot\frac9x}=3$, so $x+\frac9x\ge6$.

Equality holds when $x=\frac9x$, i.e. $x=3$, which is allowed. So the minimum is $\boxed{6}$.

---

## o14 · difficulty 3 · Diophantine equations, Divisibility and gcd
*original*

**Statement**

Find all pairs of positive integers $(x,y)$ with $xy-3x-2y=0$.

**Hint 1: What is being asked**

Find every pair of positive integers satisfying the equation.

**Hint 2: The technique**

It can be rearranged into a product of two factors equal to a constant.

**Hint 3: The key idea**

Add a constant to both sides so that the left side factors as $(x-a)(y-b)$.

**Hint 4: The next step**

Add $6$. Then list the ways to write the right side as a product of two integers, and keep only the pairs with $x,y>0$.

**Solution**

Adding $6$ to both sides: $xy-3x-2y+6=6$, i.e. $(x-2)(y-3)=6$.

Factor pairs of $6$: $(1,6),(2,3),(3,2),(6,1)$ and the negatives $(-1,-6),(-2,-3),(-3,-2),(-6,-1)$.

- Positive pairs give $(x,y)=(3,9),(4,6),(5,5),(8,4)$.
- Negative pairs need $x-2<0$; with $x\ge1$ this forces $x=1$, so $x-2=-1$, $y-3=-6$, $y=-3<0$. Rejected.

So the pairs are $\boxed{(3,9),\ (4,6),\ (5,5),\ (8,4)}$.

---

## o33 · difficulty 3 · Modular arithmetic, Casework
*original*

**Statement**

Prove that $n^2+n+1$ is never divisible by $5$.

**Hint 1: What is being asked**

For every integer $n$, show that $n^2+n+1$ leaves a nonzero remainder when divided by $5$.

**Hint 2: The technique**

Use [[modular-arithmetic]]: only the remainder of $n$ mod $5$ matters, so there are five cases to check.

**Hint 3: The key idea**

Write the possible remainders of $n$ mod $5$: $0,1,2,3,4$.

**Hint 4: The next step**

Compute $n^2+n+1$ mod $5$ for each remainder.

**Solution**

The value of $n^2+n+1$ mod $5$ depends only on $n$ mod $5$:

| $n\bmod5$ | $0$ | $1$ | $2$ | $3$ | $4$ |
|---|---|---|---|---|---|
| $n^2+n+1\bmod5$ | $1$ | $3$ | $2$ | $3$ | $1$ |

(For example $n=2$: $4+2+1=7\equiv2$; $n=3$: $9+3+1=13\equiv3$; $n=4$: $16+4+1=21\equiv1$.) None is $0$. $\blacksquare$

---

## o10 · difficulty 3 · Invariants and monovariants
*original*

**Statement**

The numbers $1,2,3,\dots,10$ are written on a board. A move erases two numbers $a$ and $b$ and writes $a+b-1$ in their place. After nine moves one number remains. What is it?

**Hint 1: What is being asked**

Whatever order of moves is used, find the single number left at the end.

**Hint 2: The technique**

Look for a quantity that does not change with any move.

**Hint 3: The key idea**

Each move replaces two numbers by one. Look at the sum of the numbers together with how many numbers are on the board.

**Hint 4: The next step**

Find how the sum changes and how the count changes in one move. Combine them so that the change cancels.

**Solution**

In one move, the sum $S$ of the numbers decreases by $1$ (since $a+b$ is replaced by $a+b-1$), and the count $k$ of numbers decreases by $1$. So $S-k$ never changes.

At the start, $S=55$ and $k=10$, so $S-k=45$. At the end, $k=1$, so $S=45+1=\boxed{46}$.

---

## m03 · difficulty 7 · Extremal principle, Graph theory basics, Pigeonhole principle
*53. Bulgarian Mathematical Olympiad (Bulgaria), MathNet 032t*

**Statement**

Let $m\ge3$ and $n\ge2$ be integers. Prove that in a group of $N=mn-n+1$ people such that there are two familiar people among any $m$, there is a person who is familiar with $n$ people. Does the statement remain true if $N<mn-n+1$?

**Hint 1: What is being asked**

Among $N$ people, any $m$ contain an acquainted pair. Show someone knows at least $n$ people, and decide whether that still holds for smaller groups.

**Hint 2: The technique**

Model the group as a graph ([[graph-theory]]) and use an [[extremal]] choice: take the largest set of people who all pairwise do not know each other.

**Hint 3: The key idea**

The condition says there are never $m$ mutual strangers. Take a largest group of mutual strangers, of size $l\le m-1$.

**Hint 4: The next step**

By maximality, every outside person knows someone in the group. Count how many outside people the members of the group know in total, and use pigeonhole.

**Hint 5: The next step**

For the second question, try $m-1$ cliques of people who know exactly their own clique.

**Solution**

Take a largest set $S$ of people who pairwise do not know each other, with $|S|=l$. Among any $m$ people two know each other, so $l\le m-1$.

By maximality of $S$, each of the other $N-l$ people knows at least one member of $S$ (otherwise we could add them). So the members of $S$ together know at least $N-l$ people outside $S$, and by pigeonhole one member knows at least $\frac{N-l}{l}=\frac Nl-1$ of them. Since $l\le m-1$,
$$\frac Nl-1\ge\frac{mn-n+1}{m-1}-1=n-1+\frac1{m-1}>n-1.$$
The number of people known is an integer greater than $n-1$, so it is at least $n$.

**Smaller $N$: not true.** Let $N\le(m-1)n$. Split the people into $m-1$ groups of at most $n$ people each, where people know exactly those in their own group. Among any $m$ people two lie in the same group (pigeonhole), so they know each other. But everyone knows at most $n-1$ people. So the statement fails for $N\le(m-1)n=mn-n$, i.e. for every $N<mn-n+1$.

---

## m16 · difficulty 5 · Trigonometry in geometry
*2nd ASU (Soviet Union), MathNet 0ew4*

**Statement**

$ABCD$ is any convex quadrilateral. Construct a new quadrilateral as follows. Take $A'$ so that $A$ is the midpoint of $DA'$; similarly, $B'$ so that $B$ is the midpoint of $AB'$; $C'$ so that $C$ is the midpoint of $BC'$; and $D'$ so that $D$ is the midpoint of $CD'$. Show that the area of $A'B'C'D'$ is five times the area of $ABCD$.

**Hint 1: What is being asked**

Show that the new quadrilateral built by doubling each side outward has exactly five times the area of the original.

**Hint 2: The technique**

Break $A'B'C'D'$ into $ABCD$ plus four triangles at the corners, and compute each triangle's area with $\frac12ab\sin C$ ([[trigonometry]]).

**Hint 3: The key idea**

Look at triangle $A'B'A$. How do its two sides at $A$ compare with $AD$ and $AB$?

**Hint 4: The next step**

What is the angle between them, compared with $\angle DAB$?

**Hint 5: The next step**

Express the area of each of the four corner triangles through triangles such as $ABD$, and add.

**Solution**

Since $ABCD$ is convex, each corner triangle such as $A'B'A$ lies on the far side of line $AB$ from $ABCD$, so the pieces do not overlap. The quadrilateral $A'B'C'D'$ consists of $ABCD$ together with the four triangles $A'B'A$, $B'C'B$, $C'D'C$, $D'A'D$.

In triangle $A'B'A$: $AA'=AD$ (as $A$ is the midpoint of $DA'$) and $AB'=2AB$ (as $B$ is the midpoint of $AB'$). The ray $AA'$ is opposite to ray $AD$ and the ray $AB'$ is ray $AB$, so $\angle A'AB'=180^\circ-\angle DAB$, which has the same sine as $\angle DAB$. Hence
$$[A'B'A]=\tfrac12\cdot AD\cdot2AB\cdot\sin\angle DAB=2\cdot\tfrac12AD\cdot AB\sin\angle DAB=2[ABD].$$
In the same way, $[B'C'B]=2[BCA]$, $[C'D'C]=2[CDB]$, $[D'A'D]=2[DAC]$.

Since the diagonals split $ABCD$ in two ways, $[ABD]+[CDB]=[ABCD]$ and $[BCA]+[DAC]=[ABCD]$. So the four triangles have total area $2\cdot2[ABCD]=4[ABCD]$, and $[A'B'C'D']=[ABCD]+4[ABCD]=5[ABCD]$. $\blacksquare$

---

## m19 · difficulty 6 · Cauchy–Schwarz and Titu's lemma, AM-GM and mean inequalities
*2008 Shortlist JBMO (JBMO), MathNet 08l7*

**Statement**

Show that
$$(x+y+z)\left(\frac1x+\frac1y+\frac1z\right)\ge4\left(\frac x{xy+1}+\frac y{yz+1}+\frac z{zx+1}\right)^2$$
for all positive real numbers $x,y,z$.

**Hint 1: What is being asked**

Prove the inequality for all positive reals.

**Hint 2: The technique**

Use [[cauchy-schwarz]] to bound the left side from below by a perfect square, and [[am-gm]] to bound each fraction on the right.

**Hint 3: The key idea**

Find an expression whose square sits between the two sides. Try $\sqrt{x/y}+\sqrt{y/z}+\sqrt{z/x}$.

**Hint 4: The next step**

For the left side, apply Cauchy–Schwarz to $(\sqrt x,\sqrt y,\sqrt z)$ and $(1/\sqrt y,1/\sqrt z,1/\sqrt x)$.

**Hint 5: The next step**

For the right side show $\sqrt{x/y}\ge\frac{2x}{xy+1}$ by AM-GM.

**Solution**

Let $S=\sqrt{\frac xy}+\sqrt{\frac yz}+\sqrt{\frac zx}$.

**Left $\ge S^2$.** By Cauchy–Schwarz with the vectors $(\sqrt x,\sqrt y,\sqrt z)$ and $\left(\frac1{\sqrt y},\frac1{\sqrt z},\frac1{\sqrt x}\right)$,
$$(x+y+z)\left(\frac1y+\frac1z+\frac1x\right)\ge\left(\sqrt{\tfrac xy}+\sqrt{\tfrac yz}+\sqrt{\tfrac zx}\right)^2=S^2.$$
**$S\ge$ the bracket.** AM-GM gives $xy+1\ge2\sqrt{xy}$, so
$$\frac{2x}{xy+1}\le\frac{2x}{2\sqrt{xy}}=\sqrt{\frac xy}.$$
Adding the three cyclic versions, $S\ge2\left(\frac x{xy+1}+\frac y{yz+1}+\frac z{zx+1}\right)$, and squaring (both sides positive) gives $S^2\ge4(\dots)^2$.

Combining, the left side is at least $S^2\ge4\left(\frac x{xy+1}+\dots\right)^2$. $\blacksquare$

---

## o19 · difficulty 4 · Symmetry and WLOG, Casework
*original*

**Statement**

Find all triples of positive integers $(a,b,c)$ with $abc=a+b+c$.

**Hint 1: What is being asked**

Find every ordered triple of positive integers whose product equals its sum.

**Hint 2: The technique**

The equation is unchanged when the variables are swapped, so use [[symmetry]]: assume an ordering of the variables.

**Hint 3: The key idea**

Assume $a\le b\le c$. Then $a+b+c\le3c$. What does that say about $ab$?

**Hint 4: The next step**

From $ab\le3$, list the possible $(a,b)$ and solve for $c$ in each case. At the end, include permutations.

**Solution**

By symmetry assume $a\le b\le c$. Then $abc=a+b+c\le3c$, so $ab\le3$. The pairs $(a,b)$ with $a\le b$ and $ab\le3$ are $(1,1),(1,2),(1,3)$.

- $(1,1)$: $c=2+c$. Impossible.
- $(1,2)$: $2c=3+c$, so $c=3$. Valid, since $2\le3$.
- $(1,3)$: $3c=4+c$, so $c=2<b$. Not allowed.

So the only ordered solution is $(1,2,3)$, and all triples are the $6$ permutations of $(1,2,3)$.

---

## o17 · difficulty 3 · Graph theory basics, Parity
*original*

**Statement**

Seven people are at a party. Is it possible that each of them shakes hands with exactly three of the others?

**Hint 1: What is being asked**

Decide whether seven people can each have shaken hands with exactly three others.

**Hint 2: The technique**

Model this as a graph ([[graph-theory]]): people are vertices and handshakes are edges. Count the handshakes in two ways.

**Hint 3: The key idea**

Add up the number of handshakes each person took part in. How is that total related to the number of handshakes?

**Hint 4: The next step**

Each handshake is counted twice in that total. What does that say about whether the total can be odd?

**Solution**

**No.** If each of the $7$ people shook hands with $3$ others, the total of the individual counts is $7\cdot3=21$. Each handshake involves two people, so it is counted twice, and the total must be twice the number of handshakes. But $21$ is odd. Contradiction.

---

## o29 · difficulty 4 · Induction, Constructive arguments
*original*

**Statement**

Prove that every positive integer can be written as a sum of distinct powers of $2$ (that is, in binary).

**Hint 1: What is being asked**

Every positive integer $n$ must be a sum of different numbers from $1,2,4,8,\dots$.

**Hint 2: The technique**

Use strong [[induction]]. Subtract the largest power of $2$ that fits.

**Hint 3: The key idea**

Given $n$, let $2^k$ be the largest power of $2$ with $2^k\le n$. What can you say about $n-2^k$?

**Hint 4: The next step**

Show $n-2^k<2^k$, so any representation of $n-2^k$ uses only powers smaller than $2^k$.

**Solution**

We use strong induction on $n$. For $n=1=2^0$ the claim is true.

Let $n\ge2$ and assume the claim for all smaller positive integers. Let $2^k$ be the largest power of $2$ with $2^k\le n$. If $n=2^k$ we are done. Otherwise $m=n-2^k$ is a positive integer, and $m<2^k$: otherwise $n\ge2\cdot2^k=2^{k+1}$, contradicting the choice of $k$. By the hypothesis, $m$ is a sum of distinct powers of $2$, each at most $m<2^k$, so all are different from $2^k$. Adding $2^k$ gives a representation of $n$. $\blacksquare$

---

## m14 · difficulty 5 · Coordinate geometry
*Canadian Mathematical Olympiad (Canada), MathNet 03gy*

**Statement**

Consider all line segments of length $4$ with one end-point on the line $y=x$ and the other end-point on the line $y=2x$. Find the equation of the locus of the midpoints of these line segments.

**Hint 1: What is being asked**

Describe, by an equation in $x$ and $y$, the path traced by the midpoints.

**Hint 2: The technique**

Use [[coordinates]]: parametrize the two endpoints, express the midpoint, and eliminate the parameters.

**Hint 3: The key idea**

Let the endpoints be $(a,a)$ and $(b,2b)$. Write the midpoint $(x,y)$ in terms of $a$ and $b$.

**Hint 4: The next step**

Solve for $a$ and $b$ in terms of $x$ and $y$, then substitute into the length condition.

**Solution**

Let the endpoints be $A=(a,a)$ and $B=(b,2b)$. The midpoint is $(x,y)=\left(\frac{a+b}2,\frac{a+2b}2\right)$. Solving $a+b=2x$, $a+2b=2y$ gives $b=2y-2x$ and $a=4x-2y$.

The length condition is $(b-a)^2+(2b-a)^2=16$. Now $b-a=4y-6x$ and $2b-a=6y-8x$, so
$$(4y-6x)^2+(6y-8x)^2=16\ \Longrightarrow\ 100x^2-144xy+52y^2=16\ \Longrightarrow\ \boxed{25x^2-36xy+13y^2=4}.$$

---

## m09 · difficulty 4 · Constructive arguments, Modular arithmetic
*62nd Ukrainian National Mathematical Olympiad, Third Round, First Tour (Ukraine), MathNet 0hgo*

**Statement**

Does there exist a trinomial $f(x)=ax^2+bx+c$ with integer coefficients such that $a$ isn't divisible by $2022$ and all numbers $f(1),f(2),\dots,f(2022)$ give different remainders under division by $2022$?

**Hint 1: What is being asked**

Decide whether a quadratic with integer coefficients, whose leading coefficient is not a multiple of $2022$, can take $2022$ distinct values modulo $2022$ at $x=1,\dots,2022$.

**Hint 2: The technique**

This asks for a [[constructive]] example; use [[modular-arithmetic]] and the idea that $x(x+1)$ is always even.

**Hint 3: The key idea**

The simplest map that hits every remainder is $x\mapsto x$. Try to add a term that is always a multiple of $2022$.

**Hint 4: The next step**

Since $x(x+1)$ is even, which multiple of $x(x+1)$ is divisible by $2022=2\cdot1011$?

**Solution**

**Yes.** Take $f(x)=1011x^2+1012x=1011\,x(x+1)+x$. The product $x(x+1)$ is even, so $1011\,x(x+1)$ is divisible by $2\cdot1011=2022$. Hence $f(x)\equiv x\pmod{2022}$, so $f(1),\dots,f(2022)$ have the remainders $1,2,\dots,2021,0$, all different. And $a=1011$ is not divisible by $2022$.

---

## m23 · difficulty 4 · Cauchy–Schwarz and Titu's lemma
*Estonian Mathematical Olympiad (Estonia), MathNet 05bw*

**Statement**

Anna, Berta and Carol make fruit drinks from syrup. Anna makes $a$ litres of drink by mixing water and syrup in the proportion of $a:1$. Berta makes $b$ litres of drink by mixing water and syrup in the proportion of $b:1$. Carol makes $c$ litres of drink by mixing water and syrup in the proportion of $c:1$. (It is not known if $a$, $b$ and $c$ are integers.) They make $6$ litres of drink in total. Prove that they use at most $2$ litres of syrup.

**Hint 1: What is being asked**

Translate to an inequality in $a,b,c$ with $a+b+c=6$ and prove it.

**Hint 2: The technique**

After translating, apply [[cauchy-schwarz]] (Titu's form) to the sum of reciprocals.

**Hint 3: The key idea**

In $a$ litres of drink with water : syrup $=a:1$, what fraction is syrup? So how much syrup is in Anna's drink?

**Hint 4: The next step**

You want $\sum\frac a{a+1}\le2$. Rewrite it using $\frac a{a+1}=1-\frac1{a+1}$.

**Hint 5: The next step**

Apply Titu's lemma to $\sum\frac1{a+1}$ with $\sum(a+1)=9$.

**Solution**

In Anna's drink the syrup is $\frac1{a+1}$ of the volume, so she uses $\frac a{a+1}$ litres of syrup; similarly for the others. We must show that $a+b+c=6$ with $a,b,c>0$ implies
$$\frac a{a+1}+\frac b{b+1}+\frac c{c+1}\le2.$$
Since $\frac a{a+1}=1-\frac1{a+1}$, this is equivalent to $\frac1{a+1}+\frac1{b+1}+\frac1{c+1}\ge1$. By Cauchy–Schwarz (Titu's lemma),
$$\frac1{a+1}+\frac1{b+1}+\frac1{c+1}\ge\frac{(1+1+1)^2}{(a+1)+(b+1)+(c+1)}=\frac9{6+3}=1.\ \blacksquare$$

---

## m18 · difficulty 4 · Parity, Invariants and monovariants
*22nd ASU (Soviet Union), MathNet 0f80*

**Statement**

A book contains $30$ stories. Each story has a different number of pages under $31$. The first story starts on page $1$ and each story starts on a new page. What is the largest possible number of stories that can begin on odd page numbers?

**Hint 1: What is being asked**

The stories have $1,2,\dots,30$ pages in some order. Maximize how many start on an odd page.

**Hint 2: The technique**

Track how the parity of the starting page changes from one story to the next.

**Hint 3: The key idea**

When does the starting page of the next story have the same parity as the current one, and when does it flip?

**Hint 4: The next step**

Compare stories with an even number of pages to those with an odd number. How must the odd-length stories alternate?

**Hint 5: The next step**

How many of each kind are there, and can all even-length stories start on odd pages?

**Solution**

A story with an even number of pages leaves the parity of the next starting page unchanged, and a story with an odd number of pages flips it. The page counts $1,\dots,30$ contain $15$ odd and $15$ even numbers.

Before the first odd-length story only even-length stories occur, so it starts on page $1+(\text{even})$, an odd page. Between two consecutive odd-length stories only even-length ones occur, so the parity of their starting pages alternates: odd, even, odd, ... Hence among the $15$ odd-length stories exactly $8$ start on odd pages (the 1st, 3rd, ..., 15th), whatever the order.

The even-length stories can all start on odd pages: place all of them first, since $1+(\text{sum of even numbers})$ is odd. So the maximum is $15+8=\boxed{23}$.

---

## o05 · difficulty 2 · Casework
*original*

**Statement**

How many integers $n$ satisfy $|n-3|+|n+2|=9$?

**Hint 1: What is being asked**

Count the integers $n$ for which the sum of the distances from $n$ to $3$ and to $-2$ equals $9$.

**Hint 2: The technique**

An absolute value behaves differently on either side of the point where its inside changes sign.

**Hint 3: The key idea**

The expressions $n-3$ and $n+2$ change sign at $n=3$ and $n=-2$. These two points split the number line into three regions.

**Hint 4: The next step**

In each region, remove the absolute values and solve the resulting linear equation. Then check that the solution lies in that region.

**Solution**

Split the line at $-2$ and $3$.

- **$n\ge3$:** the equation is $(n-3)+(n+2)=9$, so $2n-1=9$ and $n=5$. This is $\ge3$, so it is valid.
- **$-2\le n\le3$:** the equation is $(3-n)+(n+2)=5\ne9$. No solutions.
- **$n\le-2$:** the equation is $(3-n)+(-n-2)=9$, so $1-2n=9$ and $n=-4$. This is $\le-2$, so it is valid.

There are $\boxed{2}$ integers: $n=5$ and $n=-4$.

---

## m02 · difficulty 5 · Double counting, Invariants and monovariants
*Singapore Mathematical Olympiad (SMO) (Singapore), MathNet 0dsa*

**Statement**

Consider a polygon with $m+n$ sides where $m,n$ are positive integers. Colour $m$ of its vertices red and the remaining $n$ vertices blue. A side is given the number $2$ if both its end vertices are red, the number $\frac12$ if both its end vertices are blue and the number $1$ otherwise. Let the product of these numbers be $P$. Find the largest possible value of $P$.

**Hint 1: What is being asked**

Over all ways of coloring the vertices, find the largest value of the product of the edge numbers.

**Hint 2: The technique**

The answer turns out not to depend on the coloring. This is a [[double-counting]] problem: count red endpoints of edges in two ways.

**Hint 3: The key idea**

Write $P=2^{R-B}$, where $R$ is the number of red-red sides and $B$ the number of blue-blue sides. You need $R-B$.

**Hint 4: The next step**

Count pairs (vertex, side at that vertex) where the vertex is red. Each red vertex lies on exactly two sides.

**Hint 5: The next step**

Do the same for blue vertices, and subtract the two counts.

**Solution**

Let $R,B,M$ be the numbers of red-red, blue-blue and mixed sides. Then $P=2^{R}\cdot2^{-B}=2^{R-B}$.

Count pairs (red vertex, side through it). Each of the $m$ red vertices lies on $2$ sides, so there are $2m$ such pairs. A red-red side contributes $2$ pairs and a mixed side $1$, so $2m=2R+M$. Similarly for blue vertices, $2n=2B+M$.

Subtracting: $2(m-n)=2(R-B)$, so $R-B=m-n$ for every coloring. Hence $P=2^{m-n}$ always, and the largest value is $\boxed{2^{m-n}}$.

---

## o34 · difficulty 4 · Pigeonhole principle, Parity
*original*

**Statement**

Five points with integer coordinates are given in the plane. Show that the midpoint of some two of them also has integer coordinates.

**Hint 1: What is being asked**

Among any five lattice points, find two whose midpoint is a lattice point.

**Hint 2: The technique**

Use [[pigeonhole]], sorting the points by the parity of their coordinates.

**Hint 3: The key idea**

The midpoint of $(a,b)$ and $(c,d)$ is $\left(\frac{a+c}2,\frac{b+d}2\right)$. When are both coordinates integers?

**Hint 4: The next step**

Classify each point by the parities of $(x,y)$. How many classes are there?

**Solution**

The midpoint of $(a,b)$ and $(c,d)$ has integer coordinates exactly when $a+c$ and $b+d$ are both even, i.e. when $a,c$ have the same parity and $b,d$ have the same parity.

Classify each point by the parities of its two coordinates: (even, even), (even, odd), (odd, even), (odd, odd). These are four boxes. Five points go into four boxes, so two points share a class, and their midpoint is a lattice point. $\blacksquare$

---

## o25 · difficulty 3 · Similar triangles and power of a point
*original*

**Statement**

From a point $P$ outside a circle, a tangent $PT$ of length $12$ is drawn. A line through $P$ meets the circle at $A$ and $B$, with $PA=8$ and $A$ between $P$ and $B$. Find $AB$.

**Hint 1: What is being asked**

You know the tangent length and the near distance along a secant. Find the length of the chord $AB$.

**Hint 2: The technique**

Use [[similar-triangles|power of a point]], which comes from a pair of similar triangles.

**Hint 3: The key idea**

For a point outside a circle, the square of the tangent length equals the product of the distances to the two intersection points of a secant.

**Hint 4: The next step**

Find $PB$ from $PT^2=PA\cdot PB$, then subtract $PA$.

**Solution**

Triangles $PTA$ and $PBT$ share the angle at $P$, and $\angle PTA=\angle PBT$ (tangent-chord angle), so they are similar and $\frac{PT}{PB}=\frac{PA}{PT}$, i.e. $PT^2=PA\cdot PB$. Hence $144=8\cdot PB$ and $PB=18$. Since $A$ lies between $P$ and $B$, $AB=PB-PA=18-8=\boxed{10}$.

---

## m04 · difficulty 5 · Similar triangles and power of a point
*Baltic Way 2013 (Baltic Way), MathNet 01ai*

**Statement**

Let $ABC$ be a triangle, and let $X,Y,Z$ be points on $BC,CA,AB$ respectively. Suppose that $AX$, $BY$ and $CZ$ intersect in a point $P$. Prove that
$$\frac{AP}{AX}+\frac{BP}{BY}+\frac{CP}{CZ}=2.$$

**Hint 1: What is being asked**

Three lines from the vertices meet at one point $P$ inside the triangle. Each ratio compares $AP$ with the full length $AX$ of the line from the vertex through $P$ to the opposite side. Show that the three ratios add to $2$.

**Hint 2: The technique**

Convert the segment ratios into ratios of areas: triangles on a common base have areas proportional to their heights, and the heights are in the ratio of segments along a line through the vertex ([[similar-triangles]]).

**Hint 3: The key idea**

Write $\frac{AP}{AX}=1-\frac{PX}{AX}$.

**Hint 4: The next step**

Triangles $PBC$ and $ABC$ share the base $BC$. Their heights above $BC$ are in the ratio $PX:AX$.

**Solution**

Write $\frac{AP}{AX}=1-\frac{PX}{AX}$. Triangles $PBC$ and $ABC$ have the same base $BC$, and their heights from $P$ and $A$ to $BC$ are in the ratio $PX:AX$ (because $A$, $P$, $X$ are collinear and $X$ is on $BC$). So
$$\frac{PX}{AX}=\frac{[PBC]}{[ABC]}\quad\text{and}\quad\frac{AP}{AX}=1-\frac{[PBC]}{[ABC]}.$$
Similarly $\frac{BP}{BY}=1-\frac{[PCA]}{[ABC]}$ and $\frac{CP}{CZ}=1-\frac{[PAB]}{[ABC]}$. Adding,
$$\text{sum}=3-\frac{[PBC]+[PCA]+[PAB]}{[ABC]}=3-1=2.\ \blacksquare$$

---

## m13 · difficulty 6 · Angle chasing and cyclic quadrilaterals
*Estonian Mathematical Olympiad (Estonia), MathNet 05cw*

**Statement**

In an isosceles triangle $ABC$ with $AB=AC$, the bisector of the angle $BAC$ intersects $BC$ at $D$. The bisector of the angle $ABC$ intersects the perpendicular bisector of $AD$ at $E$. Prove that the bisector of the angle $ACB$ is perpendicular to $DE$.

**Hint 1: What is being asked**

Show that the line $DE$ meets the bisector from $C$ at a right angle.

**Hint 2: The technique**

First prove $A,B,D,E$ are concyclic, then chase angles at $D$ and at the incenter.

**Hint 3: The key idea**

In an isosceles triangle the bisector $AD$ is also an altitude, so $\angle ADB=90^\circ$. Which circle passes through $A,B,D$?

**Hint 4: The next step**

Let the bisector of $\angle ABC$ meet that circle again at $E'$. Show $E'A=E'D$, so $E'=E$.

**Hint 5: The next step**

Let $I$ be the incenter, on $AD$. Compute $\angle EDI$ using the circle and $\angle CID$ in the right triangle $CDI$, and add them.

**Solution**

Let $\gamma=\angle ABC=\angle ACB$. Since $AB=AC$, the bisector $AD$ is also the altitude, so $\angle ADB=90^\circ$ and $A,B,D$ lie on the circle $\omega$ with diameter $AB$. The incenter $I$ lies on $AD$.

Let the bisector of $\angle ABC$ meet $\omega$ again at $E'$. Since $BE'$ bisects $\angle ABD$, the arcs $AE'$ and $E'D$ are equal, so $E'A=E'D$ and $E'$ is on the perpendicular bisector of $AD$. This line meets $BI$ in one point, so $E'=E$. Thus $ABDE$ is cyclic, with $E$ the midpoint of arc $AD$ not containing $B$, so $E$ and $C$ lie on the same side of $AD$.

Now $\angle EDI=\angle EDA=\angle EBA=\frac\gamma2$ (inscribed angles on arc $EA$). In the right triangle $CDI$, $\angle DCI=\frac\gamma2$ because $CI$ bisects $\angle ACB$, so $\angle CID=90^\circ-\frac\gamma2$.

Since $\angle IDC=90^\circ$ and $E$ is on the same side of $AD$ as $C$ with $\angle EDI=\frac\gamma2<90^\circ$, the ray $DE$ lies inside the right angle $IDC$, so it meets segment $IC$ at a point $X$. In triangle $DIX$ the angles at $D$ and $I$ are $\frac\gamma2$ and $90^\circ-\frac\gamma2$, so the angle at $X$ is $90^\circ$. Hence $CI\perp DE$. $\blacksquare$

---

## o16 · difficulty 3 · Functional equations
*original*

**Statement**

Does there exist a function $f:\mathbb R\to\mathbb R$ such that $f(x)+f(1-x)=x$ for every real $x$?

**Hint 1: What is being asked**

You must decide whether any function at all can satisfy this equation for all real $x$.

**Hint 2: The technique**

Try substituting a related value of $x$.

**Hint 3: The key idea**

The equation holds for every $x$, so it also holds when $x$ is replaced by $1-x$. Write that version down.

**Hint 4: The next step**

Compare the two equations. What happens to the left sides?

**Solution**

**No.** Suppose such an $f$ exists. Replacing $x$ by $1-x$ gives $f(1-x)+f(x)=1-x$. The left side is the same as in the original equation, so $x=1-x$ for every real $x$. But this fails for $x=0$. So no such function exists.

---

## o36 · difficulty 3 · Modular arithmetic, Casework
*original*

**Statement**

Find all primes $p$ such that $8p^2+1$ is also prime.

**Hint 1: What is being asked**

Find every prime $p$ for which $8p^2+1$ is prime too.

**Hint 2: The technique**

Use [[modular-arithmetic]] with [[casework]]: look at $p$ modulo $3$.

**Hint 3: The key idea**

Check $p=2$ and $p=3$ directly. What is $8p^2+1$ mod $3$ for a prime $p\neq3$?

**Hint 4: The next step**

If $3\nmid p$ then $p^2\equiv1\pmod3$. Deduce that $3\mid8p^2+1$.

**Solution**

If $p=3$: $8\cdot9+1=73$, which is prime. ✓

If $p\ne3$: then $p^2\equiv1\pmod3$ (as $p\equiv\pm1$), so $8p^2+1\equiv8+1=9\equiv0\pmod3$. And $8p^2+1>3$, so it is composite. (This includes $p=2$: $33=3\cdot11$.)

So the only such prime is $\boxed{p=3}$.

---

## o18 · difficulty 4 · Double counting
*original*

**Statement**

Prove that $\displaystyle\sum_{k=1}^{n}k\binom nk=n\,2^{n-1}$.

**Hint 1: What is being asked**

Prove the identity for every positive integer $n$.

**Hint 2: The technique**

Find a set that the left side counts in one way and the right side counts in another.

**Hint 3: The key idea**

Interpret $\binom nk$ as choosing a committee of $k$ people from $n$. What does multiplying by $k$ add?

**Hint 4: The next step**

Count pairs (committee, chair), where the chair is a member of the committee. Count by choosing the chair first.

**Solution**

Count the pairs $(C,p)$ where $C$ is a nonempty committee chosen from $n$ people and $p$ is a member of $C$ (the chair).

**By committee size.** For committees of size $k$ there are $\binom nk$ committees and $k$ choices of chair, giving $\sum_{k=1}^nk\binom nk$ pairs.

**By chair.** Choose the chair first: $n$ ways. The remaining $n-1$ people each join the committee or not: $2^{n-1}$ ways. This gives $n\,2^{n-1}$ pairs.

Both counts give the same number of pairs. $\blacksquare$

---

## m12 · difficulty 8 · Graph theory basics, Extremal principle
*Romanian Master of Mathematics (Romania), MathNet 0c8t*

**Statement**

In a country there are $n$ airports and $n$ air companies operating return flights. Each company operates an odd number of flights forming a closed route. Prove that a traveller can complete a closed route consisting of an odd number of flights operated by pairwise distinct companies.

**Hint 1: What is being asked**

Each company's flights form an odd closed route (parallel flights of different companies count as different edges). Show that there is an odd closed route in which no two flights belong to the same company.

**Hint 2: The technique**

Translate to [[graph-theory]]: you have $n$ odd cycles on the same $n$ vertices and want an odd cycle with edges taken from different cycles. Use an [[extremal]] choice: a largest "rainbow" forest.

**Hint 3: The key idea**

Call a set of edges rainbow if no two come from the same company. Take a largest rainbow set of edges containing no cycle.

**Hint 4: The next step**

A forest on $n$ vertices has fewer than $n$ edges, so some company contributes no edge to it. Look at that company's odd cycle.

**Hint 5: The next step**

Show every edge of that cycle joins two vertices in the same tree of the forest, and use that trees are bipartite.

**Solution**

Each company's closed route is an odd cycle on the vertex set of $n$ airports. Call a set of edges *rainbow* if its edges come from different companies. Let $F$ be a rainbow set of edges with no cycle (a rainbow forest) of maximum size.

$F$ has at most $n-1$ edges (it is a forest on $n$ vertices), and its edges come from distinct companies, so some company $C$ has no edge in $F$. Consider the odd cycle of $C$.

No edge $e$ of this cycle joins two different components of $F$ (components include isolated vertices): otherwise $F\cup\{e\}$ would be a larger rainbow forest. So all vertices of the cycle lie in the same component of $F$, a tree $T$. A tree is bipartite: its vertices split into two parts with all tree edges between them. The cycle of $C$ has odd length, so it cannot be properly 2-colored by these parts; hence it has an edge $e$ whose endpoints are in the same part.

The path in $T$ between the endpoints of $e$ has even length (same part), so together with $e$ it forms a cycle of odd length. Its edges are tree edges (from distinct companies) plus $e$ (from $C$, which has no edge in $F$). So it is an odd closed route with pairwise distinct companies. $\blacksquare$

---

## m21 · difficulty 7 · Polynomials and Vieta, Parity
*Baltic Way 2019 (Baltic Way), MathNet 01ey*

**Statement**

Does there exist a polynomial $f(x)$ with integer coefficients of degree four such that for any integer $k$, the polynomial $f(x)+k$ is either irreducible or has a rational root?

**Hint 1: What is being asked**

Decide whether such a degree-four integer polynomial exists, and prove your answer.

**Hint 2: The technique**

Look for a quartic of the form $x^4+\alpha x$ and use [[polynomials]]: if $f+k$ is reducible without a rational root, it factors into two monic quadratics. A [[parity]] argument on the coefficients finishes.

**Hint 3: The key idea**

If a quartic has no rational root but is reducible over $\mathbb Q$, what degrees can its factors have? What does Gauss's lemma say about integer coefficients?

**Hint 4: The next step**

Compare coefficients of $x^4+2x+k=(x^2+ax+b)(x^2+cx+d)$. Eliminate $c$ and look at the equations for $b+d$ and $a(d-b)$.

**Hint 5: The next step**

Consider the parities of $a$, $b+d$ and $d-b$. The choice $\alpha=2$ (that is, $f(x)=x^4+2x$) makes the equation $a(d-b)=2$ impossible.

**Solution**

**Yes**: $f(x)=x^4+2x$ works.

Suppose $f(x)+k=x^4+2x+k$ is reducible over $\mathbb Q$ and has no rational root. Then it has no linear factor, so it is a product of two quadratics, and by Gauss's lemma we may take both monic with integer coefficients: $(x^2+ax+b)(x^2+cx+d)$. Comparing coefficients,
$$a+c=0,\quad b+d+ac=0,\quad ad+bc=2.$$
So $c=-a$, $b+d=a^2$, and $a(d-b)=2$.

Note that $d-b$ and $b+d$ have the same parity.
- If $a$ is odd, then $b+d=a^2$ is odd, so $d-b$ is odd and $a(d-b)$ is odd, not $2$.
- If $a$ is even, then $b+d=a^2$ is even, so $d-b$ is even and $a(d-b)$ is divisible by $4$, not $2$.

Both cases contradict $a(d-b)=2$.

Hence for every integer $k$, $x^4+2x+k$ is irreducible or has a rational root.

---

## m08 · difficulty 7 · Polynomials and Vieta
*Saudi Arabian Mathematical Competitions (Saudi Arabia), MathNet 0dce*

**Statement**

Let $n>1$ be a positive integer. Find all non-constant polynomials $P(x)$ with real coefficients such that
$$P(x)P(x^2)\cdots P(x^n)=P\!\left(x^{\frac{n(n+1)}2}\right)$$
for all real $x$.

**Hint 1: What is being asked**

Determine all non-constant real polynomials satisfying the identity, for a fixed $n\ge2$.

**Hint 2: The technique**

Compare degrees and leading coefficients of both sides ([[polynomials]]); then show any lower-order term would break the degree match.

**Hint 3: The key idea**

Let $P$ have degree $m$ and leading coefficient $a$. Compare leading coefficients on both sides.

**Hint 4: The next step**

Write $P(x)=a(x^m+Q(x))$ with $\deg Q<m$ (and $a=\pm1$). If $Q\neq0$, compare the degree of the largest term that differs from the leading one on each side.

**Solution**

Let $N=\frac{n(n+1)}2$, and let $P$ have degree $m\ge1$ and leading coefficient $a$. Comparing leading coefficients gives $a^n=a$, so $a^{n-1}=1$. If $n$ is even, $a=1$; if $n$ is odd, $a=\pm1$.

Write $P(x)=a\,(x^m+Q(x))$ with $\deg Q<m$ ($Q$ possibly $0$). Suppose for contradiction $Q\ne0$, and let $k=\deg Q<m$. Then the identity says
$$a^n\prod_{j=1}^n\big(x^{jm}+Q(x^j)\big)=a\big(x^{mN}+Q(x^N)\big),\quad\text{so}\quad\prod_{j=1}^n\big(x^{jm}+Q(x^j)\big)-x^{mN}=Q(x^N).$$
On the left, replacing only the $j$th factor's leading term $x^{jm}$ by $Q(x^j)$ contributes degree $mN-j(m-k)$, and all other contributions have lower degree. The largest is $j=1$: degree $mN-(m-k)$, and only this choice reaches it, so its coefficient (the leading coefficient of $Q$) is nonzero. On the right the degree is $kN$. Their difference is $(m-k)N-(m-k)=(m-k)(N-1)>0$ since $N\ge3$. So the degrees differ, a contradiction.

Therefore $Q=0$ and $P(x)=a\,x^m$. Check: $\prod_jax^{jm}=a^nx^{mN}=a\,x^{mN}$ because $a^n=a$. So the solutions are $P(x)=x^m$ for any $m\ge1$ (when $n$ is even), and $P(x)=\pm x^m$ for any $m\ge1$ (when $n$ is odd).

---

## m17 · difficulty 6 · Divisibility and gcd, Casework
*XL Russian mathematical olympiad (Russia), MathNet 0csh*

**Statement**

The teacher gave to Pete four distinct positive integers. Pete has calculated the greatest common divisor of every two of these numbers. He obtained six numbers: $1,2,3,4,5$, and $N$, where $N>5$. Find the least possible value of $N$.

**Hint 1: What is being asked**

Four numbers have six pairwise gcds $1,2,3,4,5,N$. Find the smallest possible $N>5$.

**Hint 2: The technique**

For a number $k$, count how many of the four numbers are divisible by $k$, and then how many of the six gcds are.

**Hint 3: The key idea**

If $j$ of the four numbers are divisible by $k$, how many of the pairwise gcds are divisible by $k$?

**Hint 4: The next step**

Show that the answer can never be exactly $2$. Apply this to $k=2,3,4,5$.

**Hint 5: The next step**

That restricts $N$ to a short list. Then find four numbers realizing the smallest candidate.

**Solution**

The gcd of two numbers is divisible by $k$ exactly when both numbers are divisible by $k$. So if $j$ of the four numbers are divisible by $k$, exactly $\binom j2$ of the six gcds are. This count is $0,0,1,3,6$ for $j=0,1,2,3,4$, so it is never $2$.

Apply this to the six gcds $1,2,3,4,5,N$:
- $k=2$: $2$ and $4$ are divisible by $2$, so the count is at least $2$, hence at least $3$; so $N$ is even.
- $k=3$: $3$ is divisible by $3$. If $3\mid N$ the count would be exactly $2$. So $3\nmid N$.
- $k=4$: $4$ is, so $4\nmid N$. $k=5$: $5\nmid N$.

So $N>5$ is even and not divisible by $3,4,5$: $6,8,10,12$ are excluded, so $N\ge14$.

**$N=14$ occurs:** for $(4,15,70,84)$ the gcds are $\gcd(4,15)=1$, $\gcd(4,70)=2$, $\gcd(4,84)=4$, $\gcd(15,70)=5$, $\gcd(15,84)=3$, $\gcd(70,84)=14$. The minimum is $\boxed{14}$.

---

## o12 · difficulty 3 · Recurrences
*original*

**Statement**

A sequence has $a_1=1$ and $a_{n+1}=2a_n+1$ for $n\ge1$. Find $a_{10}$.

**Hint 1: What is being asked**

You are given the first term and a rule for each next term. Find the tenth term.

**Hint 2: The technique**

Compute a few terms and look for a pattern, or shift the sequence to make it geometric.

**Hint 3: The key idea**

Compute $a_2,a_3,a_4,a_5$ and compare each with a power of $2$.

**Hint 4: The next step**

Each term is one less than a power of $2$. Prove this pattern holds, or just continue to $a_{10}$.

**Solution**

The terms are $1,3,7,15,31,\dots$, each one less than a power of $2$: conjecture $a_n=2^n-1$.

Proof by induction: $a_1=2^1-1$. If $a_n=2^n-1$, then $a_{n+1}=2(2^n-1)+1=2^{n+1}-1$.

So $a_{10}=2^{10}-1=\boxed{1023}$.

---

## m10 · difficulty 5 · Parity
*Selected Problems from Open Contests (Estonia), MathNet 0500*

**Statement**

Find all pairs $(m,n)$ of positive integers for which the $m\times n$ grid contains exactly $225$ rectangles whose side lengths are odd and whose edges lie on the lines of the grid.

**Hint 1: What is being asked**

Count rectangles with odd side lengths in an $m\times n$ grid, and find all $(m,n)$ giving exactly $225$.

**Hint 2: The technique**

Describe a rectangle by the pair of horizontal and the pair of vertical grid lines it uses. Odd side lengths are a statement about [[parity]].

**Hint 3: The key idea**

A rectangle is chosen by two horizontal lines and two vertical lines. When is the distance between two numbered lines odd?

**Hint 4: The next step**

Count pairs of horizontal lines with different parity. Does the answer change when $m$ is even?

**Solution**

Number the horizontal lines $1,\dots,m+1$ and the vertical lines $1,\dots,n+1$. A side length is the difference of two line numbers, which is odd exactly when the two numbers have different parity. So a rectangle with odd sides corresponds to a pair of horizontal lines of different parity and a pair of vertical lines of different parity.

If $m$ is even, $m=2k$, there are $k+1$ odd-numbered and $k$ even-numbered horizontal lines, giving $k(k+1)$ pairs, which is even. Then the total number of rectangles is even and cannot be $225$. The same holds for $n$. So $m$ and $n$ are odd: $m=2k-1$, $n=2l-1$.

Then there are $k$ odd-numbered and $k$ even-numbered horizontal lines, so $k^2$ pairs, and $l^2$ vertical pairs. The number of rectangles is $k^2l^2=(kl)^2=225$, so $kl=15$, giving $(k,l)\in\{(1,15),(3,5),(5,3),(15,1)\}$. Hence
$$(m,n)\in\boxed{\{(1,29),(5,9),(9,5),(29,1)\}}.$$

---

## o02 · difficulty 1 · Parity
*original*

**Statement**

Is there a set of eight odd integers whose sum is $2025$?

**Hint 1: What is being asked**

You need eight odd integers that add up to exactly $2025$, or a reason none exist.

**Hint 2: The technique**

Think about whether the sum of eight odd numbers is even or odd.

**Hint 3: The key idea**

Add the odd numbers two at a time. What is the parity of the sum of two odd numbers?

**Hint 4: The next step**

Group the eight numbers into four pairs, and compare the parity of the total with the parity of $2025$.

**Solution**

No. The sum of two odd integers is even. Group the eight integers into four pairs. Each pair sums to an even number, and a sum of even numbers is even. So the sum of eight odd integers is always even.

Since $2025$ is odd, no such set exists.

---

## o20 · difficulty 4 · Extremal principle
*original*

**Statement**

Let $S$ be a finite set of at least two points in the plane. Prove that it is impossible for every point of $S$ to be the midpoint of two other points of $S$.

**Hint 1: What is being asked**

You must show that in any finite set of points, some point is not the midpoint of two other points of the set.

**Hint 2: The technique**

Look at the point that is most extreme in some direction.

**Hint 3: The key idea**

Among the points of $S$, look at those with the largest $x$-coordinate. Pick the one with the largest $y$-coordinate among them.

**Hint 4: The next step**

Suppose this point $P$ is the midpoint of $Q$ and $R$, both in $S$ and different from $P$. Compare the coordinates of $Q$ and $R$ with those of $P$.

**Solution**

Among the points of $S$ take $P=(p,q)$ with the largest $x$-coordinate, and among those the largest $y$-coordinate. Suppose $P$ is the midpoint of two other points $Q=(x_1,y_1)$ and $R=(x_2,y_2)$ of $S$. Then $x_1+x_2=2p$ and $y_1+y_2=2q$.

Since $x_1,x_2\le p$ and $x_1+x_2=2p$, we get $x_1=x_2=p$. Then $Q$ and $R$ have the same $x$-coordinate as $P$, so by the choice of $P$, $y_1,y_2\le q$. With $y_1+y_2=2q$ this gives $y_1=y_2=q$. So $Q=R=P$, contradicting that they are different from $P$. $\blacksquare$

---

## m22 · difficulty 7 · Polynomials and Vieta, Symmetry and WLOG
*Saudi Arabian Mathematical Competitions (Saudi Arabia), MathNet 0dbf*

**Statement**

Let $P(x)$ be a polynomial of degree $n\ge2$ with rational coefficients such that $P(x)$ has $n$ pairwise different real roots forming an arithmetic progression. Prove that among the roots of $P(x)$ there are two that are also the roots of some polynomial of degree $2$ with rational coefficients.

**Hint 1: What is being asked**

Show that two of the roots satisfy a rational quadratic.

**Hint 2: The technique**

Use [[polynomials]] (Vieta): the sum and the sum of squares of the roots are rational; this forces the sum and product of the two extreme roots to be rational.

**Hint 3: The key idea**

Which two roots are the natural candidates? Think of the first and last roots of the progression.

**Hint 4: The next step**

Let $s=x_1+x_n$ and let $d$ be the common difference. The sum of the roots is $\frac{ns}2$. What does Vieta say about the sum of squares?

**Hint 5: The next step**

Write the roots symmetrically about the midpoint $\frac s2$ and compute $\sum x_i^2$ in terms of $s$ and $d$.

**Solution**

Let the roots be $x_i=x_1+(i-1)d$ with $d>0$, and set $s=x_1+x_n$, $c=\frac s2$. Then $x_i=c+\left(i-\frac{n+1}2\right)d$.

By Vieta, $e_1=\sum x_i$ and $e_2=\sum_{i<j}x_ix_j$ are rational. First, $e_1=nc=\frac{ns}2$, so $s$ is rational.

Next, $\sum x_i^2=e_1^2-2e_2$ is rational. Also
$$\sum x_i^2=nc^2+d^2\sum_{i=1}^n\left(i-\tfrac{n+1}2\right)^2=nc^2+\frac{n(n^2-1)}{12}d^2.$$
Since $nc^2$ is rational, $\frac{n(n^2-1)}{12}d^2$ is rational and $n\ge2$ gives $n(n^2-1)\ne0$, so $d^2$ is rational.

Then $x_1x_n=c^2-\left(\frac{(n-1)d}2\right)^2$ is rational. So $x_1,x_n$ are the roots of $t^2-st+x_1x_n$, a quadratic with rational coefficients. $\blacksquare$

---

## o03 · difficulty 2 · Induction
*original*

**Statement**

Prove that $1+3+5+\dots+(2n-1)=n^2$ for every positive integer $n$.

**Hint 1: What is being asked**

The left side is the sum of the first $n$ odd numbers. You must prove it equals $n^2$ for every $n\ge1$.

**Hint 2: The technique**

The statement depends on $n$, and going from $n$ to $n+1$ adds exactly one new term.

**Hint 3: The key idea**

Check the case $n=1$ first. Then assume the formula holds for some $n$ and write down the sum for $n+1$ using the assumed value.

**Hint 4: The next step**

The new last term is $2(n+1)-1=2n+1$. Show that $n^2+(2n+1)$ is a perfect square.

**Solution**

**Base case.** For $n=1$ the sum is $1=1^2$.

**Step.** Assume $1+3+\dots+(2n-1)=n^2$. Then
$$1+3+\dots+(2n-1)+(2n+1)=n^2+2n+1=(n+1)^2.$$
So the formula holds for $n+1$. By induction it holds for all $n\ge1$. $\blacksquare$

---

## o15 · difficulty 3 · Induction
*original*

**Statement**

Prove that $n!>2^n$ for every integer $n\ge4$.

**Hint 1: What is being asked**

Factorials eventually outgrow powers of $2$. You must prove this from $n=4$ on.

**Hint 2: The technique**

Use [[induction]], starting at $n=4$ (not at $1$).

**Hint 3: The key idea**

Check $n=4$ directly: compare $24$ with $16$.

**Hint 4: The next step**

Assume $n!>2^n$. To get $(n+1)!$ multiply by $n+1$. Compare $n+1$ with $2$.

**Solution**

**Base case.** $4!=24>16=2^4$.

**Step.** Assume $n!>2^n$ for some $n\ge4$. Then
$$(n+1)!=(n+1)\,n!>(n+1)\,2^n\ge2\cdot2^n=2^{n+1},$$
because $n+1\ge5>2$. So the claim holds for $n+1$. $\blacksquare$

---

## o35 · difficulty 4 · Constructive arguments, Parity
*original*

**Statement**

Can plus and minus signs be placed in front of each of the numbers $1,2,\dots,2024$ so that the total is $0$?

**Hint 1: What is being asked**

Decide whether a choice of signs exists making $\pm1\pm2\pm\dots\pm2024=0$.

**Hint 2: The technique**

First check [[parity]] to see if it is ruled out. If not, find an explicit [[constructive]] pattern, perhaps on blocks of consecutive numbers.

**Hint 3: The key idea**

The sum $1+2+\dots+2024$ is even. So parity does not forbid it. Try small cases: can you get $0$ from four consecutive numbers?

**Hint 4: The next step**

For four consecutive numbers $k,k+1,k+2,k+3$ choose signs $+,-,-,+$. What is the total?

**Solution**

**Yes.** For any four consecutive integers, $k-(k+1)-(k+2)+(k+3)=0$. Split $1,\dots,2024$ into $506$ blocks of four consecutive numbers, and use the signs $+,-,-,+$ on each block. Each block contributes $0$, so the total is $0$.

---

## o26 · difficulty 3 · Coordinate geometry
*original*

**Statement**

Points $A=(-1,0)$ and $B=(1,0)$ are given. Describe the set of all points $P$ in the plane with $PA^2+PB^2=10$.

**Hint 1: What is being asked**

Find the shape and equation of the set of points whose squared distances to $A$ and $B$ add up to $10$.

**Hint 2: The technique**

Use [[coordinates]]. Write $P=(x,y)$ and translate the condition into an equation.

**Hint 3: The key idea**

Write $PA^2$ and $PB^2$ with the distance formula in terms of $x$ and $y$.

**Hint 4: The next step**

Expand and simplify. Recognize the resulting equation.

**Solution**

Let $P=(x,y)$. Then $PA^2=(x+1)^2+y^2$ and $PB^2=(x-1)^2+y^2$. Adding,
$$2x^2+2y^2+2=10\ \Longrightarrow\ x^2+y^2=4.$$
The set is the circle with center $(0,0)$ and radius $2$.

---

## o21 · difficulty 4 · Generating functions
*original*

**Statement**

How many triples of non-negative integers $(x,y,z)$ satisfy $x+y+z=10$ with each of $x,y,z$ at most $5$?

**Hint 1: What is being asked**

Count the solutions of $x+y+z=10$ in non-negative integers in which no variable exceeds $5$.

**Hint 2: The technique**

Use [[generating-functions]] or complementary counting: first count without the upper bound, then remove the bad cases.

**Hint 3: The key idea**

How many non-negative solutions are there with no upper bound? The standard stars-and-bars count is $\binom{n+2}{2}$ for sum $n$.

**Hint 4: The next step**

A solution is bad if some variable is at least $6$. Count solutions with $x\ge6$ by shifting $x'=x-6$. Can two variables be at least $6$ at once?

**Solution**

Without a bound there are $\binom{12}{2}=66$ solutions of $x+y+z=10$.

Bad solutions have some variable $\ge6$. If $x\ge6$, put $x'=x-6$; then $x'+y+z=4$ has $\binom62=15$ solutions. The same holds for $y$ and $z$, giving $45$ bad solutions counted by variable. Two variables $\ge6$ would need a sum of at least $12>10$, so no solution is counted twice.

The answer is $66-45=\boxed{21}$. (Generating-function view: the coefficient of $t^{10}$ in $\left(\frac{1-t^6}{1-t}\right)^3$.)

---

## m11 · difficulty 7 · Double counting, Pigeonhole principle, Constructive arguments
*Junior Balkan Mathematical Olympiad (Romania), MathNet 0b5r*

**Statement**

Each of $2009$ (distinct) points in the plane is coloured blue or red, so that on every blue-centered unit circle lie exactly two red points. Determine the largest possible number of blue points.

**Hint 1: What is being asked**

Find the maximum number of blue points when every unit circle centered at a blue point passes through exactly two red points.

**Hint 2: The technique**

Assign to each blue point the pair of red points on its circle and count how many blue points can share a pair.

**Hint 3: The key idea**

Two red points lie on at most how many unit circles? Think about where their centers can be.

**Hint 4: The next step**

Let $r$ be the number of red points. Bound the number of blue points in terms of $r$, then use $r+b=2009$.

**Hint 5: The next step**

For the construction, put the red points on a line and the blue centers on perpendicular bisectors of pairs.

**Solution**

Let there be $r$ red and $b$ blue points, $r+b=2009$. To each blue point assign the pair of red points on its unit circle. Two red points $R_1,R_2$ lie on a common unit circle only if its center is on the perpendicular bisector of $R_1R_2$ at distance $1$ from both, which gives at most $2$ centers. So each pair is assigned to at most $2$ blue points, and
$$b\le2\binom r2=r(r-1).$$
Then $2009=r+b\le r^2$, so $r\ge45$ (as $44^2=1936<2009\le45^2$). Hence $b\le2009-45=1964$.

**Construction.** Take $r=45$ red points $R_i=(r_i,0)$ with distinct $0<r_i<2$. For each pair $i<j$ the two points $\left(\frac{r_i+r_j}2,\pm\sqrt{1-\frac{(r_i-r_j)^2}4}\right)$ are at distance exactly $1$ from $R_i$ and $R_j$. Their number is $2\binom{45}2=1980\ge1964$, so choose $1964$ of them as blue points. A unit circle meets the $x$-axis in at most two points, so the unit circle around such a blue point contains exactly the two red points $R_i,R_j$ it was built from. Blue points built from different pairs are different (they would otherwise be at distance $1$ from at least three red points), and none lies on the $x$-axis, so none is red. This gives $45+1964=2009$ distinct points.

The largest number of blue points is $\boxed{1964}$.

---

## o24 · difficulty 3 · Angle chasing and cyclic quadrilaterals
*original*

**Statement**

$ABCD$ is a cyclic quadrilateral (its vertices lie on a circle) with $\angle ABC=100^\circ$ and $\angle CAD=25^\circ$. Find $\angle ACD$.

**Hint 1: What is being asked**

Find the measure of angle $ACD$ in the cyclic quadrilateral.

**Hint 2: The technique**

Use what you know about the opposite angles of a cyclic quadrilateral.

**Hint 3: The key idea**

In a cyclic quadrilateral opposite angles add to $180^\circ$. Find $\angle ADC$.

**Hint 4: The next step**

Now look at triangle $ACD$ and use the angle sum.

**Solution**

Opposite angles of a cyclic quadrilateral sum to $180^\circ$, so $\angle ADC=180^\circ-100^\circ=80^\circ$.

In triangle $ACD$: $\angle ACD=180^\circ-\angle ADC-\angle CAD=180^\circ-80^\circ-25^\circ=\boxed{75^\circ}$.

---

## o11 · difficulty 3 · Pigeonhole principle
*original*

**Statement**

Five points are placed inside or on the boundary of an equilateral triangle with side length $1$. Show that two of them are at distance at most $\tfrac12$.

**Hint 1: What is being asked**

Whatever positions the five points take inside the triangle, you must find two that are close together (at most $\frac12$ apart).

**Hint 2: The technique**

Cut the triangle into regions in which any two points are automatically close.

**Hint 3: The key idea**

You need regions of diameter at most $\frac12$. Join the midpoints of the three sides.

**Hint 4: The next step**

This cuts the triangle into four smaller equilateral triangles. What is the largest distance between two points of one small triangle?

**Solution**

Join the midpoints of the sides. This divides the triangle into four equilateral triangles of side $\frac12$.

Five points lie in four small triangles (a point on a shared edge is assigned to either triangle), so some small triangle contains two points. Two points in an equilateral triangle of side $\frac12$ are at distance at most $\frac12$, because the largest distance between two points of a triangle is attained at two of its vertices, i.e. it equals the longest side. $\blacksquare$

---
