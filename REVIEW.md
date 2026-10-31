# Review sample

40 problems drawn at random (seed 40) from 153. Check the statement, the hints, and above all the solution.

## o01 · difficulty 1 · Pigeonhole principle, Modular arithmetic
*original*

**Statement**

Show that among any six integers there are two whose difference is divisible by $5$.

**Hint 1: What is being asked**

You are given any six integers. You must show that some two of them differ by a multiple of $5$.

**Hint 2: The technique**

Ask what you can sort the integers into so that two in the same class automatically have the required property.

**Hint 3: The key idea**

Divisibility of a difference by $5$ is about remainders. Two integers have a difference divisible by $5$ exactly when they leave the same remainder on division by $5$.

**Hint 4: The next step**

How many different remainders are there on division by $5$? Compare that to the number of integers.

**Solution**

Divide each of the six integers by $5$. There are only five possible remainders: $0,1,2,3,4$. These are the boxes.

Six integers go into five boxes, so two of them, say $a$ and $b$, leave the same remainder $r$. Write $a=5s+r$ and $b=5t+r$. Then $a-b=5(s-t)$ is divisible by $5$. $\blacksquare$

---

## o32 · difficulty 4 · Polynomials and Vieta
*original*

**Statement**

A monic cubic polynomial $P$ satisfies $P(1)=1$, $P(2)=2$ and $P(3)=3$. Find $P(4)$.

**Hint 1: What is being asked**

You know the leading coefficient and three values of the cubic. Find its value at $4$.

**Hint 2: The technique**

Use [[polynomials]]: consider the polynomial $P(x)-x$, whose roots you know.

**Hint 3: The key idea**

What are the roots of $Q(x)=P(x)-x$?

**Hint 4: The next step**

$Q$ is a monic cubic with three known roots, so it factors completely. Then evaluate at $4$.

**Solution**

Let $Q(x)=P(x)-x$. It is a monic cubic with $Q(1)=Q(2)=Q(3)=0$, so $Q(x)=(x-1)(x-2)(x-3)$. Therefore
$$P(4)=4+Q(4)=4+3\cdot2\cdot1=\boxed{10}.$$

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

## m33 · difficulty 7 · Recurrences, Casework
*IMO 2020 Shortlisted Problems (IMO), MathNet 06w4*

**Statement**

Let $n$ be a positive integer. Find the number of permutations $a_1,a_2,\dots,a_n$ of the sequence $1,2,\dots,n$ satisfying
$$a_1\le2a_2\le3a_3\le\dots\le na_n.$$

**Hint 1: What is being asked**

Count the permutations of $1,\dots,n$ for which the products $i\,a_i$ never decrease.

**Hint 2: The technique**

Find where the largest number $n$ can stand. That splits the permutations into cases that reduce to the same question for smaller $n$ ([[recursion]]).

**Hint 3: The key idea**

Compute the answer for $n=1,2,3,4$ and guess.

**Hint 4: The next step**

Let $a_k=n$. Show that if $k\le n-2$, then all of $a_k,a_{k+1},\dots,a_n$ exceed $k$, which is impossible.

**Hint 5: The next step**

So either $a_n=n$, or $a_{n-1}=n$ and then $a_n=n-1$. Check that the remaining conditions are exactly the problem for $n-1$ or $n-2$.

**Solution**

Let $P_n$ be the number of such permutations. Clearly $P_1=1$ and $P_2=2$ (both $1,2$ and $2,1$ work).

**Lemma.** For $n\ge3$, either $a_n=n$, or $a_{n-1}=n$ and $a_n=n-1$.

*Proof.* Let $a_k=n$.
- If $k=n-1$: $(n-1)n=(n-1)a_{n-1}\le na_n$ gives $a_n\ge n-1$, and $a_n\ne n$, so $a_n=n-1$.
- If $k\le n-2$: for $k<i<n$ we have $ia_i\ge ka_k=kn$, so $a_i\ge kn/i>k$. Also $na_n\ge(n-1)a_{n-1}\ge(n-1)(k+1)=nk+(n-1-k)>nk$, so $a_n>k$. Thus the $n-k+1$ distinct numbers $a_k,a_{k+1},\dots,a_n$ all lie in $\{k+1,\dots,n\}$, which has only $n-k$ elements. Contradiction. $\square$

**Counting.** Let $n\ge3$.
- If $a_n=n$, then $a_1,\dots,a_{n-1}$ is a permutation of $1,\dots,n-1$ satisfying the chain up to $(n-1)a_{n-1}$, and the last inequality $(n-1)a_{n-1}\le(n-1)^2<n^2=na_n$ holds automatically. This gives $P_{n-1}$ permutations.
- If $(a_{n-1},a_n)=(n,n-1)$, then $a_1,\dots,a_{n-2}$ is a permutation of $1,\dots,n-2$ satisfying the chain up to $(n-2)a_{n-2}$, and the last two inequalities $(n-2)a_{n-2}\le(n-2)^2<n(n-1)=(n-1)a_{n-1}=na_n$ hold automatically. This gives $P_{n-2}$ permutations.

So $P_n=P_{n-1}+P_{n-2}$ for $n\ge3$, with $P_1=1=F_2$ and $P_2=2=F_3$, where $F_1=F_2=1$, $F_{k+1}=F_k+F_{k-1}$ are the Fibonacci numbers. By induction the answer is $\boxed{P_n=F_{n+1}}$.

---

## o53 · difficulty 3 · Symmetry and WLOG
*original*

**Statement**

Let $f(x)=\dfrac{4^x}{4^x+2}$. Evaluate
$$f\!\left(\tfrac1{100}\right)+f\!\left(\tfrac2{100}\right)+\dots+f\!\left(\tfrac{99}{100}\right).$$

**Hint 1: What is being asked**

Find the exact value of the sum of these $99$ function values.

**Hint 2: The technique**

Pair the terms that are mirror images around the middle of the range and see what each pair adds to.

**Hint 3: The key idea**

The arguments $\frac k{100}$ and $\frac{100-k}{100}$ add up to $1$. Compute $f(x)+f(1-x)$.

**Hint 4: The next step**

Use $4^{1-x}=\dfrac4{4^x}$ to simplify $f(1-x)$. Then count the pairs and don't forget the middle term $k=50$.

**Solution**

First, for any real $x$, using $4^{1-x}=\frac{4}{4^x}$,
$$f(1-x)=\frac{4/4^x}{4/4^x+2}=\frac{4}{4+2\cdot4^x}=\frac2{2+4^x}.$$
Therefore
$$f(x)+f(1-x)=\frac{4^x}{4^x+2}+\frac2{4^x+2}=1.$$

The $99$ terms $k=1,\dots,99$ split into the $49$ pairs $\{k,100-k\}$ for $k=1,\dots,49$, plus the middle term $k=50$. Each pair adds up to $1$, and $f(\tfrac12)=\dfrac{2}{2+2}=\dfrac12$. The sum is
$$49\cdot1+\frac12=\boxed{\dfrac{99}{2}}.$$

---

## o66 · difficulty 3 · AM-GM and mean inequalities
*original*

**Statement**

Positive real numbers $x$ and $y$ satisfy $x+y=12$. Find the maximum possible value of $x^2y$.

**Hint 1: What is being asked**

Find the largest value that $x^2y$ can take, and where it is attained.

**Hint 2: The technique**

Apply the inequality between arithmetic and geometric means to three numbers whose sum is the fixed total $12$ and whose product is a constant multiple of $x^2y$.

**Hint 3: The key idea**

You need three positive terms whose sum is $x+y$ and whose product is proportional to $x^2y$. Two of them should be equal.

**Hint 4: The next step**

Use the three numbers $\frac x2,\frac x2,y$. Their sum is $12$, and equality in AM-GM needs them to be equal.

**Solution**

By AM-GM on the three positive numbers $\frac x2,\frac x2,y$:
$$\frac{\frac x2+\frac x2+y}{3}\ge\sqrt[3]{\frac x2\cdot\frac x2\cdot y}.$$
The left side is $\frac{12}{3}=4$, so $\frac{x^2y}{4}\le4^3=64$ and $x^2y\le256$.

Equality holds when $\frac x2=y$, i.e. $x=2y$; with $x+y=12$ this gives $y=4$, $x=8$, and indeed $8^2\cdot4=256$. The maximum is $\boxed{256}$.

---

## o39 · difficulty 3 · Invariants and monovariants
*original*

**Statement**

The numbers $1,2,\dots,10$ are written on a board. A move consists of erasing two numbers $a$ and $b$ and writing the number $ab+a+b$ in their place. After nine moves, a single number remains. Find this number.

**Hint 1: What is being asked**

Show that the final number does not depend on the order of the moves, and compute it.

**Hint 2: The technique**

Look for a quantity built from the numbers on the board that no move can change.

**Hint 3: The key idea**

Compute $ab+a+b$ for a few small pairs and compare with $a+b$ and $ab$. Try adding $1$ to the result.

**Hint 4: The next step**

Since $ab+a+b+1=(a+1)(b+1)$, consider the product of $(x+1)$ over all numbers $x$ on the board.

**Solution**

Note that $ab+a+b+1=(a+1)(b+1)$. Consider the quantity
$$P=\prod_{x\text{ on the board}}(x+1).$$
A move replaces the factors $(a+1)(b+1)$ by the single factor $(ab+a+b)+1=(a+1)(b+1)$, so $P$ does not change. $P$ is an invariant.

At the start, $P=2\cdot3\cdots11=11!=39916800$. At the end the board holds one number $N$, and $P=N+1$. Therefore $N=11!-1=\boxed{39916799}$, whatever order of moves is used.

---

## m57 · difficulty 7 · Functional equations
*Baltic Way 2011 Problem Shortlist (Baltic Way), MathNet 0182*

**Statement**

Find all functions $f:\mathbb R\to\mathbb R$ such that
$$f(x+f(y))-f(x)=(x+f(y))^3-x^3$$
for all $x,y\in\mathbb R$.

**Hint 1: What is being asked**

Determine every real function for which shifting the argument by any value $f(y)$ changes $f$ by exactly as much as it changes $x\mapsto x^3$.

**Hint 2: The technique**

Subtract the cube: $g(x)=f(x)-x^3$ turns the equation into "every value of $f$ is a period of $g$". Then study the set of periods, which is closed under addition and subtraction.

**Hint 3: The key idea**

Show $g(x+f(y))=g(x)$ for all $x,y$, where $g(x)=f(x)-x^3$.

**Hint 4: The next step**

The periods of $g$ form a group under addition. If $a=f(y_0)\ne0$, then both $f(y)$ and $f(y+a)$ are periods for every $y$. What is their difference?

**Hint 5: The next step**

$(y+a)^3-y^3$ takes every value on a half-line. A group of reals containing a half-line is all of $\mathbb R$.

**Solution**

**Answer:** $f\equiv0$, and $f(x)=x^3+c$ for any real constant $c$.

Let $g(x)=f(x)-x^3$. The equation reads $f(x+f(y))-(x+f(y))^3=f(x)-x^3$, i.e.
$$g(x+f(y))=g(x)\quad\text{for all }x,y.$$
Let $G$ be the set of periods of $g$, i.e. the $p$ with $g(x+p)=g(x)$ for all $x$. If $p,q\in G$ then $g(x+p-q)=g(x-q)=g(x)$, so $p-q\in G$: $G$ is an additive subgroup of $\mathbb R$, and it contains every value of $f$.

If $f\equiv0$, the equation holds ($0=x^3-x^3$). Otherwise pick $y_0$ with $a=f(y_0)\ne0$. For any $y$, both $f(y)$ and $f(y+a)$ lie in $G$, and since $a\in G$ we have $g(y+a)=g(y)$, so
$$f(y+a)-f(y)=(y+a)^3-y^3=3a\left(y+\tfrac a2\right)^2+\tfrac{a^3}4\in G.$$
As $y$ runs over $\mathbb R$ this takes every value in $[\frac{a^3}4,\infty)$ if $a>0$, or in $(-\infty,\frac{a^3}4]$ if $a<0$. So $G$ contains a half-line $H$. For any real $r$, choose $u\in H$ with $u+r\in H$ (take $u$ far enough into the half-line); then $r=(u+r)-u\in G$. Hence $G=\mathbb R$, every real number is a period of $g$, and $g$ is constant, say $g\equiv c$. Thus $f(x)=x^3+c$.

Check: if $f(x)=x^3+c$, then $f(x+f(y))-f(x)=(x+f(y))^3+c-x^3-c=(x+f(y))^3-x^3$. So the solutions are $\boxed{f\equiv0\ \text{ and }\ f(x)=x^3+c\ (c\in\mathbb R)}$.

---

## o83 · difficulty 6 · Complex numbers in geometry
*original*

**Statement**

Let $ABCD$ be a convex quadrilateral. On each of its four sides construct a square lying outside the quadrilateral, and let $P,Q,R,S$ be the centers of the squares on $AB,BC,CD,DA$ respectively. Prove that $PR=QS$ and that the lines $PR$ and $QS$ are perpendicular.

**Hint 1: What is being asked**

Show that the segments joining the centers of opposite squares have equal length and are perpendicular.

**Hint 2: The technique**

Treat the plane as the complex numbers, where rotating a vector by $90^\circ$ is multiplication by $i$. Then each center is an explicit expression in the vertices.

**Hint 3: The key idea**

Orient $ABCD$ counterclockwise. The outside of the quadrilateral is then to the right of each directed side $A\to B$, $B\to C$, and so on. Express the center of the square on $AB$ as the midpoint plus half of the vector $\overrightarrow{AB}$ rotated by $-90^\circ$.

**Hint 4: The next step**

With $a,b,c,d$ the complex numbers of the vertices, the center is $p=\frac{(1+i)a+(1-i)b}{2}$, and similarly for $q,r,s$. Compare $s-q$ with $r-p$.

**Solution**

Reflecting the figure if necessary (which preserves lengths and perpendicularity), assume $A,B,C,D$ are in counterclockwise order. Because $ABCD$ is convex, its interior lies to the left of each directed side, and the exterior to the right.

Let $a,b,c,d$ be the complex numbers of the vertices. The square on $AB$ lying to the right of $A\to B$ has its center at distance $\frac{|AB|}{2}$ from the midpoint of $AB$, perpendicular to $AB$ and on the right. Rotating a vector by $-90^\circ$ means multiplying by $-i$, which sends the direction of $\overrightarrow{AB}$ to the right, so
$$p=\frac{a+b}{2}-i\,\frac{b-a}{2}=ua+vb,\qquad u=\frac{1+i}2,\ v=\frac{1-i}2.$$
In the same way $q=ub+vc$, $r=uc+vd$, $s=ud+va$.

Note $iu=\frac{i-1}{2}=-v$ and $iv=\frac{i+1}{2}=u$. Then
$$i(r-p)=i\big(uc+vd-ua-vb\big)=-vc+ud+va-ub=(ud+va)-(ub+vc)=s-q.$$
So $s-q=i(r-p)$: the vector $\overrightarrow{QS}$ is the vector $\overrightarrow{PR}$ rotated by $90^\circ$, so $QS=PR$ and $QS\perp PR$. (We need $P\ne R$ for the lines to be defined. If $p=r$, then $b-d=-i(a-c)$, so $\operatorname{Im}\big((b-d)\overline{(a-c)}\big)=-|a-c|^2<0$; but for a convex counterclockwise quadrilateral this imaginary part is positive, because the diagonals cross.) $\blacksquare$

---

## o64 · difficulty 3 · Generating functions
*original*

**Statement**

Four fair six-sided dice, one red, one blue, one green and one yellow, are rolled. In how many of the $6^4$ equally likely outcomes (the colors keep the dice distinguishable) is the sum of the four numbers equal to $14$?

**Hint 1: What is being asked**

Count the outcomes (ordered quadruples of numbers from $1$ to $6$) whose sum is $14$.

**Hint 2: The technique**

Encode the possible values of one die as a polynomial, so that multiplying polynomials adds the values. Then the answer is a single coefficient.

**Hint 3: The key idea**

One die has generating polynomial $x+x^2+\dots+x^6=x\cdot\frac{1-x^6}{1-x}$. The sum of four dice corresponds to the fourth power. You want the coefficient of $x^{14}$.

**Hint 4: The next step**

Pull out $x^4$, so you need the coefficient of $x^{10}$ in $\left(\frac{1-x^6}{1-x}\right)^4=(1-x^6)^4\cdot(1-x)^{-4}$. Expand each factor.

**Solution**

The number of outcomes with sum $14$ is the coefficient of $x^{14}$ in
$$(x+x^2+\dots+x^6)^4=x^4\frac{(1-x^6)^4}{(1-x)^4}.$$
So we need the coefficient of $x^{10}$ in $(1-x^6)^4(1-x)^{-4}$.

We have $(1-x^6)^4=1-4x^6+6x^{12}-\dots$, and $(1-x)^{-4}=\sum_{m\ge0}\binom{m+3}{3}x^m$. The coefficient of $x^{10}$ is
$$\binom{13}{3}-4\binom{7}{3}+6\cdot 0=286-4\cdot35=146,$$
where the $x^{12}$ term cannot contribute to $x^{10}$. The answer is $\boxed{146}$.

---

## m20 · difficulty 7 · Divisibility and gcd, Diophantine equations, Modular arithmetic
*Saudi Arabian IMO Booklet (Saudi Arabia), MathNet 0dfz*

**Statement**

Determine the smallest positive integer $a$ for which there exist a prime number $p$ and a positive integer $b\ge2$ such that
$$\frac{a^p-a}p=b^2.$$

**Hint 1: What is being asked**

Find the smallest positive $a$ for which $\frac{a^p-a}{p}$ is a square of an integer $b\ge2$ for some prime $p$.

**Hint 2: The technique**

Use [[divisibility]]: $a$ and $a^{p-1}-1$ are coprime and their product is $pb^2$. Treat $p=2$ and $p\ge3$ separately.

**Hint 3: The key idea**

For $p=2$ the equation is $a(a-1)=2b^2$. Search for the smallest solution with $b\ge2$.

**Hint 4: The next step**

For $p\ge3$ write $a(a^{p-1}-1)=pb^2$ with coprime factors on the left. Each factor is a square or $p$ times a square. Which factors can be squares?

**Hint 5: The next step**

Show that no $a\le8$ works for $p\ge3$: the only square candidates are $a=1$ (which gives $0$) and $a=4$.

**Solution**

**$p=2$.** The equation is $a(a-1)=2b^2$ with $b\ge2$, so $a(a-1)\ge8$. Checking $a=2,\dots,8$ gives $a(a-1)/2=1,3,6,10,15,21,28$, none a square; and $a=9$ gives $36=6^2$, so $a=9$ works with $b=6$.

**$p\ge3$.** Suppose $a\le8$ works. Since $\gcd(a,a^{p-1}-1)=1$ and $a(a^{p-1}-1)=pb^2$, each of the two factors is a perfect square or $p$ times a perfect square, and $p$ divides exactly one of them.

- If $p\mid a$ then $a=ps^2$ and $a^{p-1}-1=t^2$, i.e. $(a^{(p-1)/2}-t)(a^{(p-1)/2}+t)=1$, forcing $a^{(p-1)/2}=1$, so $a=1$, but $a=ps^2\ge3$. Impossible.
- If $p\nmid a$ then $a=s^2$ and $a^{p-1}-1=pt^2$. The square candidates $a\le8$ are $1$ and $4$; $a=1$ gives $0$, which is not $b^2$ with $b\ge2$. For $a=4$: $(2^{p-1}-1)(2^{p-1}+1)=pt^2$ with coprime factors; by Fermat $p\mid2^{p-1}-1$, so $2^{p-1}+1=c^2$ is a square. Then $(c-1)(c+1)=2^{p-1}$ forces $c-1=2$, $c+1=4$, $2^{p-1}=8$, $p=4$, not prime. Impossible.

So no $a\le8$ works, and the smallest is $\boxed{9}$.

---

## m32 · difficulty 8 · Induction, Extremal principle
*IMO 2019 Shortlisted Problems (IMO), MathNet 06va*

**Statement**

You are given a set of $n$ blocks, each weighing at least $1$; their total weight is $2n$. Prove that for every real number $r$ with $0\le r\le2n-2$ you can choose a subset of the blocks whose total weight is at least $r$ but at most $r+2$.

**Hint 1: What is being asked**

With $n$ blocks of weight at least $1$ and total $2n$, show that every interval $[r,r+2]$ with $0\le r\le 2n-2$ contains the weight of some sub-collection.

**Hint 2: The technique**

The statement is awkward to induct on directly. Prove a stronger version by [[induction]] on $n$, removing the heaviest block ([[extremal]]).

**Hint 3: The key idea**

Strengthen: if $n$ blocks of weight at least $1$ have total $s\le2n$, then for every $r\in[-2,s]$ some subset has weight in $[r,r+2]$.

**Hint 4: The next step**

Remove the heaviest block $x$. The rest satisfy the hypothesis with $n-1$ blocks. Which values of $r$ does the induction hypothesis handle, with and without $x$?

**Hint 5: The next step**

You cover $[-2,s-x]$ and $[x-2,s]$. Show $x-2\le s-x$ using $x\le s-(n-1)$ and $s\le2n$.

**Solution**

We prove the stronger **Claim:** if $n\ge1$ blocks each weigh at least $1$ and their total is $s\le2n$, then for every real $r$ with $-2\le r\le s$ some subset (possibly empty) has total weight in $[r,r+2]$.

The problem follows by taking $s=2n$, since $[0,2n-2]\subset[-2,2n]$.

**Base $n=1$.** One block of weight $s$ with $1\le s\le2$. If $-2\le r\le0$, the empty set (weight $0$) works since $r\le0\le r+2$. If $0<r\le s$, the block works since $r\le s\le2<r+2$.

**Step.** Let $n\ge2$ and let $x$ be the largest weight. Then $x\ge s/n$, so the other $n-1$ blocks have total $s-x\le s\frac{n-1}n\le2(n-1)$, and each weighs at least $1$. By the induction hypothesis:
- for every $r\in[-2,s-x]$ some subset of the other blocks has weight in $[r,r+2]$;
- for every $r\in[x-2,s]$ we have $r-x\in[-2,s-x]$, so some subset $T$ of the other blocks has weight in $[r-x,r-x+2]$, and $T$ together with the heavy block has weight in $[r,r+2]$.

These two intervals cover $[-2,s]$ provided $x-2\le s-x$, i.e. $2x\le s+2$. The other $n-1$ blocks weigh at least $n-1$, so $x\le s-(n-1)$. Also $x\le s-(n-1)\le2n-(n-1)=n+1$. Adding, $2x\le s-(n-1)+n+1=s+2$. This completes the induction. $\blacksquare$

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

## m58 · difficulty 8 · Functional equations
*48th International Mathematical Olympiad Vietnam 2007 Shortlisted Problems with Solutions (IMO), MathNet 06p9*

**Statement**

Find all functions $f:\mathbb R^+\to\mathbb R^+$ such that
$$f(x+f(y))=f(x+y)+f(y)$$
for all $x,y\in\mathbb R^+$. ($\mathbb R^+$ denotes the set of positive real numbers.)

**Hint 1: What is being asked**

Determine every function from the positive reals to the positive reals satisfying the equation.

**Hint 2: The technique**

First show $f(y)>y$, then study $g(y)=f(y)-y>0$.

**Hint 3: The key idea**

If $f(y)<y$, put $x=y-f(y)$. If $f(y)=y$, compare both sides directly.

**Hint 4: The next step**

With $g(y)=f(y)-y$ and $t=x+y$, show $g(t+g(y))=g(t)+y$ for all $t>y>0$. Deduce that $g$ is injective.

**Hint 5: The next step**

For $t>u+v$ compute $g(t+g(u)+g(v))$ in two steps and compare with $g(t+g(u+v))$. This gives additivity; then show $g(g(y))=y$.

**Solution**

**Answer:** $f(x)=2x$.

**Step 1: $f(y)>y$.** Since $f(y)>0$, the equation gives $f(x+f(y))>f(x+y)$ for all $x$. If $f(y)=y$ this reads $f(x+y)>f(x+y)$, impossible. If $f(y)<y$, put $x=y-f(y)>0$: then $f(y)=f(x+f(y))=f(2y-f(y))+f(y)>f(y)$, impossible. So $f(y)>y$.

**Step 2.** Let $g(y)=f(y)-y>0$. For $t>y>0$ put $x=t-y>0$ in the equation: $f(t-y+f(y))=f(t)+f(y)$, i.e. $f(t+g(y))=f(t)+f(y)$. Writing $f=g+\mathrm{id}$:
$$g(t+g(y))+t+g(y)=g(t)+t+g(y)+y,\quad\text{so}\quad g(t+g(y))=g(t)+y\quad(t>y>0).\tag{1}$$
**Injective.** If $g(y_1)=g(y_2)$, take $t>\max(y_1,y_2)$; (1) gives $g(t)+y_1=g(t)+y_2$, so $y_1=y_2$.

**Additive.** Let $u,v>0$ and $t>u+v$. Applying (1) with $(t+g(u),v)$ (valid as $t+g(u)>v$) and then with $(t,u)$:
$$g(t+g(u)+g(v))=g(t+g(u))+v=g(t)+u+v.$$
Also (1) with $(t,u+v)$ gives $g(t+g(u+v))=g(t)+u+v$. By injectivity $t+g(u)+g(v)=t+g(u+v)$, so $g(u+v)=g(u)+g(v)$. Since $g>0$, this implies $g$ is strictly increasing: $g(u+v)>g(u)$.

**Involution.** By (1) and additivity, $g(t)+y=g(t+g(y))=g(t)+g(g(y))$ for $t>y$, so $g(g(y))=y$ for all $y$.

**Conclusion.** If $g(x)>x$ for some $x$, then since $g$ is increasing, $x=g(g(x))>g(x)$, a contradiction. If $g(x)<x$, then $x=g(g(x))<g(x)$, again a contradiction. So $g(x)=x$ and $f(x)=2x$.

Check: $f(x+f(y))=2x+4y$ and $f(x+y)+f(y)=2x+2y+2y=2x+4y$. The only solution is $\boxed{f(x)=2x}$.

---

## m40 · difficulty 6 · Symmetry and WLOG
*Baltic Way (Baltic Way), MathNet 01bf*

**Statement**

Two players play a game on an $N\times N$ board. The players alternately mark a cell in such a way that there is never a diagonal on the board containing two marked cells. A player who cannot move loses. For which $N>0$ does the starting player have a winning strategy?

**Hint 1: What is being asked**

A diagonal means any line of cells parallel to one of the two main diagonals. Players alternately mark cells so that no diagonal (of either direction) ever holds two marks; whoever cannot move loses. For which $N$ does the first player win?

**Hint 2: The technique**

Use a mirror strategy ([[symmetry]]): one player answers each move by its image under a suitable symmetry of the board. Choose the symmetry depending on the parity of $N$.

**Hint 3: The key idea**

The game is finite, so a player who can always answer wins.

**Hint 4: The next step**

For even $N$, let the second player copy each move in the vertical mid-line of the board. Why is the copy always legal?

**Hint 5: The next step**

For odd $N$, the first player takes the centre and then answers with the point reflection in the centre.

**Solution**

**Answer:** exactly for odd $N$.

Use coordinates $(x,y)$, $1\le x,y\le N$. Diagonals are the sets $x-y=\text{const}$ and $x+y=\text{const}$. The game ends after at most $N^2$ moves, so a player who can always make a move after the opponent's move wins.

**$N$ even: the second player wins.** Let $\sigma(x,y)=(N+1-x,y)$, the reflection in the vertical mid-line. It maps diagonals to diagonals (it swaps the two directions). The second player keeps the set $M$ of marked cells symmetric under $\sigma$ after each of her moves; this holds at the start ($M=\varnothing$). Suppose the first player marks $P=(x,y)$ legally. The answer is $\sigma(P)$:
- $\sigma(P)\ne P$ because $N+1-x\ne x$ for even $N$;
- $\sigma(P)$ is not in $M$, since otherwise $P=\sigma(\sigma(P))\in M$;
- $P$ and $\sigma(P)$ are in the same row, at different positions, so they share no diagonal;
- if some $Q\in M$ shared a diagonal with $\sigma(P)$, then $\sigma(Q)\in M$ would share a diagonal with $P$, contradicting that $P$ was legal.

So $\sigma(P)$ is a legal move, after which $M$ is again symmetric. The second player can always move, so she wins.

**$N$ odd: the first player wins.** Let $c$ be the centre cell and $\rho(x,y)=(N+1-x,N+1-y)$ the point reflection in $c$; it maps each diagonal to a diagonal of the same direction, and its only fixed cell is $c$. The first player marks $c$ first and then keeps $M$ symmetric under $\rho$ after each of his moves. When the second player marks a legal cell $P$ (so $P\ne c$ and $P$ shares no diagonal with $c$), he answers $\rho(P)$:
- $\rho(P)\ne P$ and $\rho(P)\notin M$ as before;
- if $P$ and $\rho(P)$ were on a common diagonal, this diagonal would pass through their midpoint, the centre $c$, so $P$ would share a diagonal with $c$; impossible;
- if $Q\in M$ shared a diagonal with $\rho(P)$, then $\rho(Q)\in M$ would share one with $P$; impossible.

So the first player can always move and wins. Hence the starting player wins exactly when $\boxed{N\text{ is odd}}$.

---

## o38 · difficulty 4 · Pigeonhole principle, Constructive arguments
*original*

**Statement**

Find the smallest positive integer $n$ with the following property: every $n$-element subset of $\{1,2,\dots,20\}$ contains two numbers whose difference is exactly $3$.

**Hint 1: What is being asked**

Find the least $n$ such that any $n$ numbers chosen from $1$ to $20$ must include a pair differing by $3$.

**Hint 2: The technique**

Organise the numbers into groups in which the forbidden pairs have a simple structure, and see how many you can take from each group.

**Hint 3: The key idea**

Write $1,\dots,20$ in three lists according to the remainder mod $3$, each in increasing order. A pair differing by $3$ is a pair of neighbours in one list.

**Hint 4: The next step**

A list of length $7$ can be cut into three pairs of neighbours and one leftover element. How many elements of the list can you keep without two neighbours? Then build an example that shows the bound is sharp.

**Solution**

Split $\{1,\dots,20\}$ by remainder mod $3$ into three chains:
$$A:\ 1,4,7,10,13,16,19\ (7),\quad B:\ 2,5,8,11,14,17,20\ (7),\quad C:\ 3,6,9,12,15,18\ (6).$$
Two numbers differ by exactly $3$ if and only if they are neighbours in the same chain.

**A subset with no such pair has at most $11$ elements.** Cut chain $A$ into the boxes $\{1,4\},\{7,10\},\{13,16\},\{19\}$. A box of two neighbours holds at most one element of the subset, so at most $3+1=4$ elements of $A$ are chosen. The same boxes work for $B$: at most $4$. Chain $C$ splits into three pairs, so at most $3$. In total at most $4+4+3=11$.

Hence any $12$ numbers contain two differing by $3$.

**$11$ is attained.** Take $1,7,13,19$ from $A$, $2,8,14,20$ from $B$, and $3,9,15$ from $C$. Within a chain these are non-neighbours, and numbers in different chains have different remainders mod $3$, so no difference equals $3$. So an $11$-element subset without the property exists, and $n\ge12$.

Therefore the answer is $\boxed{12}$.

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

## m38 · difficulty 7 · Casework, Divisibility and gcd
*Benelux Mathematical Olympiad (Benelux Mathematical Olympiad), MathNet 020b*

**Statement**

Find all positive integers $n>1$ with the following property: for each two positive divisors $k,\ell<n$ of $n$, at least one of the numbers $2k-\ell$ and $2\ell-k$ is a (not necessarily positive) divisor of $n$ as well.

**Hint 1: What is being asked**

Find all $n>1$ such that for any proper positive divisors $k,\ell$ of $n$, one of $2k-\ell$, $2\ell-k$ divides $n$ (negative divisors allowed; $0$ never divides $n$).

**Hint 2: The technique**

Apply the condition to cleverly chosen pairs, starting with $1$ and the largest proper divisor, and split into cases ([[casework]]) using [[divisibility]].

**Hint 3: The key idea**

Primes work. For composite $n$ let $p$ be its smallest prime factor and $m=n/p$, the largest proper divisor. Apply the condition to $(1,m)$.

**Hint 4: The next step**

$2m-1$ lies strictly between $m$ and $n$, so it is not a divisor. Deduce $m-2\mid 2p$.

**Hint 5: The next step**

Go through $m-2\in\{1,2,p,2p\}$; in the case $m=p+2$ use the pair $(1,p)$. Finally test the few candidates.

**Solution**

**Answer:** all primes, and $n=6,9,15$.

A number $x$ "divides $n$" here means $x\ne0$ and $|x|$ is a positive divisor of $n$.

**Primes work:** the only divisor below $n$ is $1$, and $2\cdot1-1=1\mid n$.

**Composite $n$.** Let $p$ be the smallest prime factor of $n$ and $m=n/p$. Every prime factor of $m$ is at least $p$, so $m\ge p\ge2$. Also, any divisor $d$ of $n$ with $d>m$ has $n/d<p$, so $n/d=1$: the divisors of $n$ greater than $m$ are only $n$ itself.

Apply the condition to $(k,\ell)=(1,m)$. Since $m<2m-1<2m\le pm=n$, the number $2m-1$ is not a divisor. So $2-m$ divides $n$; in particular $m\ne2$, so $m\ge3$ and $m-2\mid n=pm$. Then $m-2\mid pm-p(m-2)=2p$, so $m-2\in\{1,2,p,2p\}$.

- $m-2=1$: $m=3$, and $p\le m$ gives $p\in\{2,3\}$: $n=6$ or $n=9$.
- $m-2=2$: $m=4$, so $n=4p$ is even, $p=2$ and $n=8$.
- $m-2=p$ with $p$ odd ($p=2$ is the previous case): $n=p(p+2)$. Apply the condition to $(1,p)$: $p-2$ or $2p-1$ divides $n$. If $p-2\mid n$ and $p-2>1$, then $p-2$ has a prime factor smaller than $p$ dividing $n$, impossible; so $p-2=1$, $p=3$. If $2p-1\mid n$: $2p-1<n$, so $2p-1\le m=p+2$, giving $p\le3$, so $p=3$. In both cases $n=15$.
- $m-2=2p$: $m=2p+2$ is even, so $p=2$, $m=6$, $n=12$.

**Testing the candidates $6,8,9,12,15$.**
- $n=8$, pair $(1,2)$: $0$ and $3$, neither divides $8$. Fails.
- $n=12$, pair $(3,6)$: $0$ and $9$, neither divides $12$. Fails.
- $n=6$ (divisors $1,2,3$): $(1,2)\to3$; $(1,3)\to-1$; $(2,3)\to1$. Works.
- $n=9$ (divisors $1,3$): $(1,3)\to-1$. Works.
- $n=15$ (divisors $1,3,5$): $(1,3)\to-1$; $(1,5)\to-3$; $(3,5)\to1$. Works.

(Pairs with $k=\ell$ always work since $2k-k=k$.) So the answer is $\boxed{n\text{ prime, or }n\in\{6,9,15\}}$.

---

## m70 · difficulty 7 · Coordinate geometry, Symmetry and WLOG
*The 16th Japanese Mathematical Olympiad - The First Round (Japan), MathNet 08rn*

**Statement**

The triangle $ABC$ satisfies $BC=5$, $CA=7$ and $AB=8$. Let $O$ be a point inside the triangle $ABC$ such that the triangles $OBC$, $OCA$ and $OAB$ have the same circumradius. Find this common circumradius.

**Hint 1: What is being asked**

A point inside the $5$-$7$-$8$ triangle makes the three triangles it forms with the sides have equal circumradii. Find that radius.

**Hint 2: The technique**

Use vectors (or complex coordinates). Two circles of equal radius through the same two points have centres symmetric about the midpoint of those points; this lets you write $A,B,C$ in terms of $O$ and the three centres.

**Hint 3: The key idea**

Let $O_1,O_2,O_3$ be the circumcentres of $OBC,OCA,OAB$ and $\rho$ the common radius. $O_1$ and $O_2$ are both at distance $\rho$ from $O$ and from $C$. Show $O_1+O_2=O+C$ as vectors.

**Hint 4: The next step**

So $C=O_1+O_2-O$, and similarly for $A$ and $B$. Find a point at distance $\rho$ from all of $A,B,C$.

**Hint 5: The next step**

Conclude $\rho$ is the circumradius of $ABC$; compute it, and check that a valid $O$ exists.

**Solution**

**Answer:** $\dfrac{7\sqrt3}3$.

Let $\rho$ be the common circumradius and $O_1,O_2,O_3$ the circumcentres of $OBC,OCA,OAB$. Treat points as vectors.

**$O_1\ne O_2$.** Otherwise the circles $OBC$ and $OCA$ coincide (same centre and radius), so $A,B,C,O$ lie on one circle, the circumcircle of $ABC$. But a point strictly inside the triangle is strictly inside its circumcircle. So $O_1\ne O_2$, and likewise the three centres are distinct.

**Expressing the vertices.** $O_1$ and $O_2$ are two different points at distance $\rho$ from both $O$ and $C$, so they are the two intersection points of the circles of radius $\rho$ about $O$ and about $C$. These two intersection points are symmetric about the midpoint of $OC$ (the configuration is symmetric in the line $OC$ and in the perpendicular bisector of $OC$). Hence $O_1+O_2=O+C$, i.e. $C=O_1+O_2-O$. Similarly $A=O_2+O_3-O$ and $B=O_3+O_1-O$.

**The circumradius.** Let $K=O_1+O_2+O_3-2O$. Then $K-A=O_1-O$, $K-B=O_2-O$, $K-C=O_3-O$, all of length $\rho$. So $K$ is the circumcentre of $ABC$ and $\rho$ equals its circumradius $R$.

**Computing $R$.** By the law of cosines, $\cos B=\frac{8^2+5^2-7^2}{2\cdot8\cdot5}=\frac12$, so $B=60^\circ$ and $R=\frac{CA}{2\sin B}=\frac7{\sqrt3}=\frac{7\sqrt3}3$.

**Existence.** The triangle is acute ($5^2+7^2>8^2$), so its orthocentre $H$ lies inside it. Since $\angle BHC=180^\circ-\angle A$, the circumradius of $HBC$ is $\frac{BC}{2\sin\angle BHC}=\frac{a}{2\sin A}=R$, and likewise for $HCA$ and $HAB$. So $O=H$ is such a point, and the common circumradius is $\boxed{\tfrac{7\sqrt3}{3}}$.

---

## o74 · difficulty 3 · Divisibility and gcd
*original*

**Statement**

Find all positive integers $n$ such that $n+3$ divides $n^2+3$.

**Hint 1: What is being asked**

List every positive integer $n$ for which $n^2+3$ is a multiple of $n+3$.

**Hint 2: The technique**

Reduce the numerator modulo the divisor, so that the question becomes whether $n+3$ divides a fixed number.

**Hint 3: The key idea**

Write $n^2+3=(n+3)(n-3)+r$ for a constant $r$. What is $r$?

**Hint 4: The next step**

Then $n+3$ divides $n^2+3$ exactly when it divides $r$. List the divisors of $r$ that are at least $4$.

**Solution**

Since $n^2-9=(n+3)(n-3)$, we have $n^2+3=(n+3)(n-3)+12$. Thus $n+3\mid n^2+3$ if and only if $n+3\mid12$.

For positive $n$, $n+3\ge4$. The divisors of $12$ that are at least $4$ are $4,6,12$, giving $n=1,3,9$.

Check: $n=1$: $4\mid4$. $n=3$: $6\mid12$. $n=9$: $12\mid84$. The answer is $\boxed{n=1,\,3,\,9}$.

---

## m54 · difficulty 7 · Cauchy–Schwarz and Titu's lemma, Double counting
*North Macedonia (North Macedonia), MathNet 0ag3*

**Statement**

Let $p_1,p_2,\dots,p_{2009}$ be positive real numbers. Prove the inequality
$$\sum_{i=1}^{2009}\frac{p_i}{p_{i+1}+p_{i+2}+\dots+p_{i+1004}}\ge\frac{2009}{1004},$$
where the indices are taken modulo $2009$.

**Hint 1: What is being asked**

Each $p_i$ is divided by the sum of the next $1004$ numbers around the circle. Show the total is at least $\frac{2009}{1004}$.

**Hint 2: The technique**

Turn each fraction into a square over a product and apply Cauchy-Schwarz in Engel form. The denominator that appears can be identified exactly by counting pairs ([[double-counting]]).

**Hint 3: The key idea**

Write $\frac{p_i}{S_i}=\frac{p_i^2}{p_iS_i}$, where $S_i$ is the denominator, and apply Engel form.

**Hint 4: The next step**

In $\sum_ip_iS_i$, each product $p_ip_j$ with $i\ne j$ appears how many times? Think about the two "distances" from $i$ to $j$ and from $j$ to $i$ around the circle.

**Hint 5: The next step**

You need $\big(\sum p_i\big)^2\ge\frac{2009}{1004}\sum_{i<j}p_ip_j$. Compare $\sum_{i<j}p_ip_j$ with $\sum p_i^2$.

**Solution**

Let $S_i=p_{i+1}+\dots+p_{i+1004}$ (indices mod $2009$), $T=\sum p_i$ and $e=\sum_{i<j}p_ip_j$. By Cauchy-Schwarz in Engel form,
$$\sum_i\frac{p_i}{S_i}=\sum_i\frac{p_i^2}{p_iS_i}\ge\frac{T^2}{\sum_ip_iS_i}.$$
**The denominator equals $e$.** $\sum_ip_iS_i$ is the sum of $p_ip_j$ over ordered pairs $(i,j)$ with $j-i\equiv d\pmod{2009}$ for some $d\in\{1,\dots,1004\}$. For an unordered pair $\{i,j\}$ with $i\ne j$, the residues of $j-i$ and $i-j$ lie in $\{1,\dots,2008\}$ and add to $2009$, so exactly one of them lies in $\{1,\dots,1004\}$. Hence each unordered pair is counted exactly once, and $\sum_ip_iS_i=e$.

**Comparison.** From $\sum_{i<j}(p_i-p_j)^2\ge0$ we get $2008\sum p_i^2\ge2e$, i.e. $\sum p_i^2\ge\frac{e}{1004}$. Therefore
$$T^2=\sum p_i^2+2e\ge\frac e{1004}+2e=\frac{2009}{1004}\,e.$$
Combining, $\sum_i\frac{p_i}{S_i}\ge\frac{T^2}{e}\ge\frac{2009}{1004}$. (Equality holds when all $p_i$ are equal: each term is then $\frac1{1004}$.) $\blacksquare$

---

## o56 · difficulty 3 · Double counting
*original*

**Statement**

At a camp there are $15$ students. The staff splits them into teams of three students each (a student may be on several teams) in such a way that every pair of students is together on exactly one team. How many teams are there?

**Hint 1: What is being asked**

Find the total number of teams.

**Hint 2: The technique**

Count, in two different ways, the pairs consisting of a student and a team that student is on. First find how many teams one student is on.

**Hint 3: The key idea**

Fix a student $S$. Each of the other $14$ students shares exactly one team with $S$. How many other students does one team containing $S$ include?

**Hint 4: The next step**

Once you know how many teams each student is on, count all (student, team) memberships in two ways: by students and by teams.

**Solution**

Fix a student $S$. Each of the other $14$ students is on exactly one team with $S$, and each team containing $S$ has exactly $2$ other students. So the teams containing $S$ partition the other $14$ students into pairs: $S$ is on $14/2=7$ teams.

Now count the pairs (student, team on which the student plays) in two ways. Each of the $15$ students is on $7$ teams, giving $15\cdot7=105$ pairs. Each team has $3$ students, so with $T$ teams there are $3T$ pairs. Hence $3T=105$ and $T=\boxed{35}$.

(Such a system of teams exists: take the $15$ nonzero vectors of $\mathbb F_2^4$ as students and the triples $\{a,b,a+b\}$ as teams.)

---

## o77 · difficulty 5 · Diophantine equations, Modular arithmetic
*original*

**Statement**

Find all pairs $(a,b)$ of non-negative integers with $3^a-2^b=1$.

**Hint 1: What is being asked**

Determine every pair of non-negative integers $(a,b)$ satisfying the equation.

**Hint 2: The technique**

Handle small exponents directly. For large $b$, look at the equation modulo $4$ to learn about the parity of $a$, which lets you factor.

**Hint 3: The key idea**

Check $a=0$, $b=0$ and $b=1$ by hand. For $b\ge2$, what is $3^a$ modulo $4$, and what does that force about $a$?

**Hint 4: The next step**

If $a=2k$, then $2^b=3^{2k}-1=(3^k-1)(3^k+1)$. Both factors are divisors of a power of $2$, so both are powers of $2$. Which two powers of $2$ differ by $2$?

**Solution**

Rewrite as $3^a=2^b+1$.

*Small cases.* If $a=0$ then $2^b=0$, impossible. If $b=0$ then $3^a=2$, impossible. If $b=1$ then $3^a=3$, so $a=1$: the pair $(1,1)$.

*Case $b\ge2$.* Then $3^a=2^b+1\equiv1\pmod4$. Since $3^a\equiv(-1)^a\pmod 4$, $a$ is even; and $a\ge2$ because $3^a\ge5$. Write $a=2k$ with $k\ge1$. Then
$$2^b=3^{2k}-1=(3^k-1)(3^k+1).$$
Both factors are positive divisors of $2^b$, hence powers of $2$: say $3^k-1=2^s$, $3^k+1=2^t$ with $t>s$. Subtracting, $2^t-2^s=2$, so $2^s(2^{t-s}-1)=2$. As $2^{t-s}-1$ is odd and positive, $2^{t-s}-1=1$ and $2^s=2$: $s=1$, $t=2$. So $3^k=3$, $k=1$, $a=2$, and $2^b=8$, $b=3$.

The solutions are $\boxed{(a,b)=(1,1)\text{ and }(2,3)}$. (Check: $3-2=1$, $9-8=1$.)

---

## m62 · difficulty 6 · Polynomials and Vieta
*Benelux Mathematical Olympiad (Benelux Mathematical Olympiad), MathNet 01zv*

**Statement**

Find all polynomials $p(x)$ with real coefficients such that
$$p(a+b-2c)+p(b+c-2a)+p(c+a-2b)=3p(a-b)+3p(b-c)+3p(c-a)$$
for all $a,b,c\in\mathbb R$.

**Hint 1: What is being asked**

Determine every real polynomial satisfying the identity for all real $a,b,c$.

**Hint 2: The technique**

Specialize the variables to get a one-variable identity $p(-2x)=p(x)+3p(-x)$, and compare coefficients of each power of $x$.

**Hint 3: The key idea**

Put $a=b=c$, then put $b=c=0$.

**Hint 4: The next step**

In $p(-2x)=p(x)+3p(-x)$, the coefficient of $x^k$ gives $(-2)^k a_k=(1+3(-1)^k)a_k$. For which $k$ can $a_k\ne0$?

**Solution**

**Answer:** $p(x)=\alpha x^2+\beta x$ with $\alpha,\beta\in\mathbb R$.

**Necessity.** With $a=b=c$ we get $3p(0)=9p(0)$, so $p(0)=0$. With $b=c=0$ the arguments on the left are $a,-2a,a$ and on the right $a,0,-a$, so
$$p(-2a)+2p(a)=3p(a)+3p(0)+3p(-a),\quad\text{i.e.}\quad p(-2x)=p(x)+3p(-x)$$
for all $x$. Let $p(x)=\sum a_kx^k$. Comparing coefficients of $x^k$: $(-2)^ka_k=(1+3(-1)^k)a_k$. For even $k$ this says $2^k=4$ or $a_k=0$, so $a_k=0$ unless $k=2$. For odd $k$ it says $-2^k=-2$ or $a_k=0$, so $a_k=0$ unless $k=1$. Hence $p(x)=\alpha x^2+\beta x$.

**Sufficiency.** The condition is linear in $p$, so check $x$ and $x^2$. For $p(x)=x$ both sides are $0$, since the three arguments on each side add to $0$. For $p(x)=x^2$:
$$(a+b-2c)^2+(b+c-2a)^2+(c+a-2b)^2=6(a^2+b^2+c^2)-6(ab+bc+ca),$$
$$3\big((a-b)^2+(b-c)^2+(c-a)^2\big)=6(a^2+b^2+c^2)-6(ab+bc+ca).$$
So the solutions are $\boxed{p(x)=\alpha x^2+\beta x}$.

---

## m49 · difficulty 7 · Diophantine equations, Divisibility and gcd
*20th Korean Mathematical Olympiad Final Round (South Korea), MathNet 0eu6*

**Statement**

Find all triplets $(x,y,z)$ of positive integers satisfying $1+4^x+4^y=z^2$.

**Hint 1: What is being asked**

Find all positive integers $x,y,z$ with $1+4^x+4^y=z^2$.

**Hint 2: The technique**

Compare $z^2$ with the squares next to $(2^y)^2$, and when that fails, factor $z^2-1$ and count powers of $2$ ([[diophantine]], [[divisibility]]).

**Hint 3: The key idea**

By symmetry let $x\le y$. Compare $1+4^x+4^y$ with $(2^y+1)^2=4^y+2^{y+1}+1$.

**Hint 4: The next step**

This settles $2x\le y+1$. For $2x>y+1$, write $(z-1)(z+1)=4^x(1+4^{y-x})$. What is $\gcd(z-1,z+1)$?

**Hint 5: The next step**

One of $z\pm1$ is divisible by $2^{2x-1}$. Compare the resulting lower bound for $z^2$ with the actual size of $1+4^x+4^y$.

**Solution**

**Answer:** $(x,y,z)=\boxed{(t,\,2t-1,\,2^{2t-1}+1)\ \text{and}\ (2t-1,\,t,\,2^{2t-1}+1)}$ for positive integers $t$.

The equation is symmetric in $x,y$, so let $x\le y$. Note $z^2>4^y=(2^y)^2$, so $z\ge2^y+1$, while $(2^y+1)^2=4^y+2^{y+1}+1$.

**Case $2x<y+1$.** Then $4^x<2^{y+1}$, so $(2^y)^2<z^2<(2^y+1)^2$. Impossible.

**Case $2x=y+1$.** Then $z^2=4^y+2^{y+1}+1=(2^y+1)^2$, so $z=2^y+1$. With $x=t$ we get $y=2t-1\ge t$ and the solution $(t,2t-1,2^{2t-1}+1)$.

**Case $2x>y+1$.** Since $y\ge x$, this gives $x\ge2$, and $y\le2x-2$. Write $(z-1)(z+1)=4^x(1+4^{y-x})$. The number $z$ is odd, so $z-1,z+1$ are even with $\gcd(z-1,z+1)=2$; one of them is $\equiv2\pmod4$, so the other carries all remaining factors of $2$. The right side is divisible by $2^{2x}$, hence the other factor is divisible by $2^{2x-1}$, and $z+1\ge2^{2x-1}$. Since $x\ge2$, $2^{2x-1}-1>0$, so
$$z^2\ge(2^{2x-1}-1)^2=4\cdot4^{2x-2}-4^x+1.$$
But $z^2=1+4^x+4^y\le1+4^x+4^{2x-2}$. Together: $3\cdot4^{2x-2}\le2\cdot4^x$, i.e. $3\cdot4^{x-2}\le2$, so $x<2$. Contradiction.

Swapping $x$ and $y$ gives the second family. (For $t=1$ both give $(1,1,3)$.)

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

## m31 · difficulty 8 · Induction, Graph theory basics
*Team selection test for 23. BMO (Bulgaria), MathNet 0382*

**Statement**

After a volleyball tournament (every two teams played exactly once) with $n$ teams it turned out that for any two teams $A$ and $B$ such that $B$ wins over $A$, there exist a positive integer $t$ and teams $C_1,C_2,\dots,C_t$ such that $A$ wins over $C_1$, $C_1$ wins over $C_2$, $\dots$, $C_t$ wins over $B$. Prove that for any $k=3,4,\dots,n$ there exist $k$ teams $A_1,A_2,\dots,A_k$ such that $A_1$ wins over $A_2$, $A_2$ wins over $A_3$, $\dots$, $A_{k-1}$ wins over $A_k$ and $A_k$ wins over $A_1$.

**Hint 1: What is being asked**

In a tournament where every team can reach every other team along a chain of wins, show that there are cycles of wins of every length from $3$ up to $n$.

**Hint 2: The technique**

Use [[induction]] on the cycle length: from a cycle of length $k<n$, build one of length $k+1$ by looking at how an outside team plays against the cycle. Phrase everything as a directed graph ([[graph-theory]]).

**Hint 3: The key idea**

For $k=3$: take a shortest cycle of wins and show it cannot have length $4$ or more by looking at a chord.

**Hint 4: The next step**

Given a $k$-cycle and an outside team $U$ that beats some cycle team and loses to another, insert $U$ into the cycle.

**Hint 5: The next step**

Otherwise every outside team beats the whole cycle or loses to the whole cycle. Use the chain condition to find a team $V$ of the second kind that beats a team $U$ of the first kind.

**Solution**

Draw an arrow $X\to Y$ when $X$ beats $Y$. Between two distinct teams there is exactly one arrow. The condition implies: for any distinct $X,Y$ there is a directed walk from $X$ to $Y$ (if $X\to Y$ directly; otherwise $Y\to X$ and the condition gives a walk $X\to C_1\to\dots\to C_t\to Y$).

**A $3$-cycle exists.** Take any game, say $B\to A$, and the walk $A\to C_1\to\dots\to C_t\to B$; with $B\to A$ it is a closed walk, which contains a directed cycle. Let $v_1\to v_2\to\dots\to v_L\to v_1$ be a shortest directed cycle; $L\ge3$ because two teams play only once. If $L\ge4$, look at the game between $v_1$ and $v_3$: if $v_3\to v_1$ then $v_1\to v_2\to v_3\to v_1$ is a shorter cycle; if $v_1\to v_3$ then $v_1\to v_3\to\dots\to v_L\to v_1$ is a shorter cycle. Either way we contradict minimality, so $L=3$.

**From $k$ to $k+1$ ($3\le k<n$).** Let $A_1\to A_2\to\dots\to A_k\to A_1$ be a cycle and $\mathcal C$ its set of teams.

*Case 1: some outside team $U$ beats one team of $\mathcal C$ and loses to another.* Going around the cycle, the cycle teams are of two kinds (beating $U$ or losing to $U$) and both kinds occur, so there is an index $i$ with $A_i\to U$ and $U\to A_{i+1}$ (indices mod $k$). Then $A_1\to\dots\to A_i\to U\to A_{i+1}\to\dots\to A_k\to A_1$ is a cycle of length $k+1$.

*Case 2: every outside team beats all of $\mathcal C$ (set $S$) or loses to all of $\mathcal C$ (set $T$).* Since $k<n$, $S\cup T\ne\varnothing$.

First, $S\ne\varnothing$. Otherwise take $V\in T$ and a walk from $V$ to $A_1$. Let $Q$ be the first team of the walk in $\mathcal C$ and $R$ the team just before it. Then $R\notin\mathcal C$, so $R\in T$, but $R\to Q$ contradicts that $T$-teams lose to all of $\mathcal C$.

Now take $U_0\in S$ and a walk from $A_1$ to $U_0$. Let $U$ be the first team of the walk lying in $S$ and $V$ the team just before it, so $V\to U$. $V$ is not in $S$, and $V\notin\mathcal C$ because every team of $\mathcal C$ loses to $U$. Hence $V\in T$. Now
$$U\to A_1\to A_2\to\dots\to A_{k-1}\to V\to U$$
is a cycle: $U\to A_1$ as $U\in S$, $A_{k-1}\to V$ as $V\in T$, and $V\to U$. It has $k+1$ distinct teams.

In both cases we get a cycle of length $k+1$. By induction there are cycles of every length $3,4,\dots,n$. $\blacksquare$

---

## m15 · difficulty 4 · Casework, Extremal principle
*56th Ukrainian National Mathematical Olympiad, Third Round (Ukraine), MathNet 0h7f*

**Statement**

$30$ children, boys and girls, formed a circle. It occurred that there is no child such that both its neighbors are boys. What is the least possible number of girls?

**Hint 1: What is being asked**

Find the smallest number of girls, given that no child has two boys as neighbors.

**Hint 2: The technique**

Use [[casework]] on the structure of the circle: look at the maximal blocks of consecutive boys and the blocks of girls between them.

**Hint 3: The key idea**

How long can a block of consecutive boys be? What if there are three boys in a row?

**Hint 4: The next step**

Between two blocks of boys, how many girls are needed so that no child sits between two boys?

**Hint 5: The next step**

If there are $k$ blocks of boys, how many boys and girls are there at most / at least? Then optimize.

**Solution**

Three boys in a row would make the middle boy have two boy neighbors, so every block of consecutive boys has size at most $2$. Two blocks of boys separated by exactly one girl would give that girl two boy neighbors, so any two consecutive blocks of boys are separated by at least $2$ girls.

Suppose there are $k\ge1$ blocks of boys around the circle. Then there are also $k$ blocks of girls, each of size at least $2$, so $g\ge2k$ girls; and $b\le2k$ boys.

If $g\le15$ then $b\ge15$, so $2k\ge b\ge15$ and $k\ge8$. But then $g\ge2k\ge16$, a contradiction. So $g\ge16$. (With no boys at all, $g=30$.)

**Example with $16$ girls:** around the circle put seven blocks "boy, boy" alternating with girl blocks of sizes $2,2,2,2,2,2,4$. That is $14$ boys and $6\cdot2+4=16$ girls, and no child has two boy neighbors.

The minimum is $\boxed{16}$.

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

## m65 · difficulty 6 · Complex numbers in geometry
*37th Iranian Mathematical Olympiad (Iran), MathNet 07fm*

**Statement**

Let $A_1,A_2,\dots,A_k$ be points on the unit circle. Prove that
$$\sum_{1\le i<j\le k}d(A_i,A_j)^2\le k^2,$$
where $d(A_i,A_j)$ denotes the distance between $A_i$ and $A_j$.

**Hint 1: What is being asked**

For $k$ points on a circle of radius $1$, show that the sum of the squared distances over all pairs is at most $k^2$.

**Hint 2: The technique**

Put the points in the complex plane as $z_i$ with $|z_i|=1$ and expand $|z_i-z_j|^2=(z_i-z_j)(\bar z_i-\bar z_j)$. The sum of the cross terms is controlled by $|z_1+\dots+z_k|^2$.

**Hint 3: The key idea**

$|z_i-z_j|^2=2-(\bar z_iz_j+z_i\bar z_j)$ when $|z_i|=|z_j|=1$.

**Hint 4: The next step**

Expand $\left|\sum z_i\right|^2=\left(\sum z_i\right)\left(\sum\bar z_i\right)$ and identify the cross terms.

**Solution**

Place the unit circle in the complex plane and let $A_i$ correspond to $z_i$ with $|z_i|=1$. Then $d(A_i,A_j)^2=|z_i-z_j|^2=(z_i-z_j)(\bar z_i-\bar z_j)=2-(\bar z_iz_j+z_i\bar z_j)$. Summing over $i<j$:
$$\sum_{i<j}|z_i-z_j|^2=2\binom k2-\sum_{i\ne j}\bar z_iz_j,$$
where the last sum is over ordered pairs. On the other hand,
$$\Big|\sum_{i=1}^kz_i\Big|^2=\Big(\sum_iz_i\Big)\Big(\sum_j\bar z_j\Big)=\sum_i|z_i|^2+\sum_{i\ne j}\bar z_iz_j=k+\sum_{i\ne j}\bar z_iz_j.$$
Therefore
$$\sum_{i<j}d(A_i,A_j)^2=k(k-1)-\Big(\Big|\sum z_i\Big|^2-k\Big)=k^2-\Big|\sum_{i=1}^kz_i\Big|^2\le k^2.$$
Equality holds exactly when $z_1+\dots+z_k=0$, i.e. when the centroid of the points is the centre of the circle. $\blacksquare$

---

## m01 · difficulty 6 · Modular arithmetic, Constructive arguments
*Baltic Way (Baltic Way), MathNet 017c*

**Statement**

Prove that there exists an integer which is divisible by $2010$ and whose decimal notation contains exactly two different digits.

**Hint 1: What is being asked**

You must produce (and justify) a multiple of $2010$ written with only two distinct digits.

**Hint 2: The technique**

A number made only of the digit $9$ is $10^k-1$, so look for a power of $10$ that is $1$ modulo something.

**Hint 3: The key idea**

Factor $2010=10\cdot201$. A multiple of $10$ ends in $0$. You want the rest to be built from a single repeated digit.

**Hint 4: The next step**

$201$ is coprime to $10$. Euler's theorem gives $k$ with $10^k\equiv1\pmod{201}$. What does that say about $10^k-1$?

**Hint 5: The next step**

Multiply $10^k-1$ by $10$ and read off its decimal digits.

**Solution**

Since $201=3\cdot67$ is coprime to $10$, Euler's theorem gives $10^{\varphi(201)}\equiv1\pmod{201}$, where $\varphi(201)=2\cdot66=132$. So $201\mid10^{132}-1$.

Let $N=10\,(10^{132}-1)$. Then $2010=10\cdot201$ divides $N$. The number $10^{132}-1$ is $132$ nines, so $N$ is $132$ nines followed by a $0$. Its digits are exactly $9$ and $0$. $\blacksquare$

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

## m67 · difficulty 6 · Trigonometry in geometry
*Nordic Mathematical Contest, NMC 7 (Nordic Mathematical Olympiad), MathNet 0a7l*

**Statement**

A hexagon is inscribed in a circle of radius $r$. Two of the sides of the hexagon have length $1$, two have length $2$ and two have length $3$. Show that $r$ satisfies the equation
$$2r^3-7r-3=0.$$

**Hint 1: What is being asked**

A cyclic hexagon has sides $1,1,2,2,3,3$ in some order. Show that its circumradius $r$ is a root of $2r^3-7r-3$.

**Hint 2: The technique**

A chord of length $\ell$ cuts off an arc whose half-angle $\phi$ satisfies $\ell=2r\sin\phi$. The six arcs fill the circle, which gives one trigonometric relation among three half-angles.

**Hint 3: The key idea**

Let the arcs cut off by the sides have measures $2\phi_1,\dots,2\phi_6$ summing to $360^\circ$. Show that sides of equal length cut off equal arcs, all less than $180^\circ$.

**Hint 4: The next step**

With half-angles $\alpha,\beta,\gamma$ for lengths $1,2,3$ you get $\alpha+\beta+\gamma=90^\circ$. Then $\sin\gamma=\cos(\alpha+\beta)$.

**Hint 5: The next step**

Expand $\cos(\alpha+\beta)$, isolate the product of cosines and square.

**Solution**

The six vertices split the circle into six arcs (each not containing other vertices), with measures adding to $360^\circ$. A side cutting off an arc of measure $\theta\in(0^\circ,360^\circ)$ has length $2r\sin\frac\theta2$.

**Equal sides cut off equal arcs.** Two sides of the same length $\ell$ cut off arcs $\theta,\theta'$ with $\sin\frac\theta2=\sin\frac{\theta'}2$, so $\theta'=\theta$ or $\theta'=360^\circ-\theta$. The second option would make these two arcs fill the whole circle, leaving nothing for the other four arcs; so $\theta'=\theta$. Hence the arcs are $2\alpha,2\alpha,2\beta,2\beta,2\gamma,2\gamma$ for the lengths $1,2,3$, with $4(\alpha+\beta+\gamma)=360^\circ$, i.e. $\alpha+\beta+\gamma=90^\circ$. All of $\alpha,\beta,\gamma$ lie in $(0^\circ,90^\circ)$ and
$$\sin\alpha=\frac1{2r},\qquad\sin\beta=\frac1r,\qquad\sin\gamma=\frac3{2r}.$$
**The equation.** Since $\gamma=90^\circ-(\alpha+\beta)$, $\sin\gamma=\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta$, so
$$\cos\alpha\cos\beta=\frac3{2r}+\frac1{2r^2}=\frac{3r+1}{2r^2}.$$
The cosines are positive, $\cos\alpha=\sqrt{1-\frac1{4r^2}}$ and $\cos\beta=\sqrt{1-\frac1{r^2}}$. Squaring and multiplying by $4r^4$:
$$(4r^2-1)(r^2-1)=(3r+1)^2\iff4r^4-5r^2+1=9r^2+6r+1\iff2r(2r^3-7r-3)=0.$$
As $r>0$, we get $2r^3-7r-3=0$. $\blacksquare$

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

## m44 · difficulty 6 · Extremal principle
*XIII OBM (Brazil), MathNet 02er*

**Statement**

At a party every woman dances with at least one man, and no man dances with every woman. Show that there are men $M$ and $M'$ and women $W$ and $W'$ such that $M$ dances with $W$, $M'$ dances with $W'$, but $M$ does not dance with $W'$, and $M'$ does not dance with $W$.

**Hint 1: What is being asked**

Given that each woman has a partner and no man has danced with all women, find two men and two women forming the pattern: $M$–$W$ and $M'$–$W'$ dance, while $M$–$W'$ and $M'$–$W$ do not.

**Hint 2: The technique**

Choose $M$ by an [[extremal]] property and let the hypotheses produce the other three people.

**Hint 3: The key idea**

Let $M$ be a man who dances with the largest number of women.

**Hint 4: The next step**

Pick a woman $W'$ that $M$ does not dance with, and a partner $M'$ of $W'$.

**Hint 5: The next step**

If $M'$ danced with every partner of $M$, compare the numbers of partners.

**Solution**

There are women at the party (if there were none, any man would vacuously dance with every woman), and each of them dances with some man, so there are men too. Let $M$ be a man who dances with the maximum number of women.

$M$ does not dance with every woman, so there is a woman $W'$ he does not dance with. $W'$ dances with some man $M'$, and $M'\ne M$.

Suppose $M'$ danced with every woman who dances with $M$. Then $M'$ dances with all partners of $M$ and also with $W'$, who is not a partner of $M$, so $M'$ has more partners than $M$. This contradicts the choice of $M$. Hence there is a woman $W$ who dances with $M$ but not with $M'$.

Now $M$ dances with $W$, $M'$ dances with $W'$, $M$ does not dance with $W'$, and $M'$ does not dance with $W$. $\blacksquare$

---

## m64 · difficulty 8 · Generating functions, Polynomials and Vieta
*Mongolian Mathematical Olympiad (Mongolia), MathNet 09eu*

**Statement**

For a finite set $A=\{a_1,a_2,\dots,a_n\}$ of positive integers let $A^*$ be the multiset $\{a_i+a_j\mid1\le i<j\le n\}$. For instance, if $A=\{1,2,3,4\}$ then $A^*=\{3,4,5,5,6,7\}$. Let $A$ and $B$ be two different sets of positive integers, each with at least two elements, such that $A^*=B^*$. Prove that $|A|=|B|$ and that this common size is a power of $2$.

**Hint 1: What is being asked**

Two different sets with at least two elements have the same multiset of pairwise sums. Show they have the same size, and that the size is a power of $2$.

**Hint 2: The technique**

Encode each set by $f(x)=\sum_{a\in A}x^a$. The pairwise sums are encoded by $\frac{f(x)^2-f(x^2)}2$, so the hypothesis becomes a polynomial identity. Then look at the order of vanishing at $x=1$.

**Hint 3: The key idea**

Show $\sum_{s\in A^*}x^s=\frac{f(x)^2-f(x^2)}2$, so $f(x)^2-g(x)^2=f(x^2)-g(x^2)$ where $g$ encodes $B$.

**Hint 4: The next step**

$f-g$ is a nonzero polynomial with $f(1)-g(1)=0$. Write $f(x)-g(x)=(x-1)^kh(x)$ with $h(1)\ne0$.

**Hint 5: The next step**

Factor $f(x^2)-g(x^2)$ the same way, cancel $(x-1)^k$, and set $x=1$.

**Solution**

Let $n=|A|$ and $m=|B|$. The multiset $A^*$ has $\binom n2$ elements and $B^*$ has $\binom m2$. Since $x\mapsto\binom x2$ is strictly increasing for integers $x\ge1$ and $n,m\ge2$, $A^*=B^*$ gives $n=m$.

Let $f(x)=\sum_{a\in A}x^a$ and $g(x)=\sum_{b\in B}x^b$. Expanding the square,
$$f(x)^2=\sum_{a\in A}x^{2a}+2\sum_{i<j}x^{a_i+a_j}=f(x^2)+2\sum_{s\in A^*}x^s,$$
where the last sum counts multiplicities. The same holds for $B$, so $A^*=B^*$ gives $f(x)^2-f(x^2)=g(x)^2-g(x^2)$, i.e.
$$\big(f(x)-g(x)\big)\big(f(x)+g(x)\big)=f(x^2)-g(x^2).\tag{1}$$
Since $A\ne B$, the polynomial $f-g$ is not zero. Also $f(1)-g(1)=n-n=0$, so $x-1$ divides it. Write $f(x)-g(x)=(x-1)^kh(x)$ with $k\ge1$, $h$ a polynomial and $h(1)\ne0$. Replacing $x$ by $x^2$, $f(x^2)-g(x^2)=(x^2-1)^kh(x^2)=(x-1)^k(x+1)^kh(x^2)$. Substituting in (1) and cancelling the nonzero factor $(x-1)^k$ (polynomials over $\mathbb R$ have no zero divisors):
$$h(x)\big(f(x)+g(x)\big)=(x+1)^kh(x^2).$$
At $x=1$: $h(1)\cdot2n=2^kh(1)$, and since $h(1)\ne0$, $n=2^{k-1}$. So $|A|=|B|=2^{k-1}$ is a power of $2$ (and $k\ge2$ because $n\ge2$). $\blacksquare$

---

## m45 · difficulty 7 · Double counting, Extremal principle
*14th Turkish Mathematical Olympiad (Turkey), MathNet 0gmz*

**Statement**

Find the largest real number $t$ such that, in any school with $2006$ students and $14$ teachers where every student is acquainted with at least one teacher, a student and a teacher can be found such that they are acquainted with each other, and the ratio of the number of students who are acquainted with the teacher to the number of teachers who are acquainted with the student is at least $t$.

**Hint 1: What is being asked**

For each acquainted pair (teacher $i$, student $j$) form $a_i/b_j$, where $a_i$ is the number of students teacher $i$ knows and $b_j$ the number of teachers student $j$ knows. Find the largest $t$ such that some pair always reaches $t$.

**Hint 2: The technique**

Assume every acquainted pair has a small ratio and add up the resulting inequalities over all acquainted pairs; group the sum by teachers and by students ([[double-counting]]).

**Hint 3: The key idea**

The all-acquainted school shows $t\le2006/14$.

**Hint 4: The next step**

Suppose $a_i/b_j<2006/14$ for every acquainted pair, i.e. $\frac1{b_j}<\frac{2006}{14}\cdot\frac1{a_i}$.

**Hint 5: The next step**

Sum over all acquainted pairs: $\sum\frac1{b_j}=2006$, while $\sum\frac1{a_i}$ equals the number of teachers who know somebody.

**Solution**

**Answer:** $\boxed{t=\dfrac{2006}{14}=\dfrac{1003}7}$.

Let $a_i$ be the number of students acquainted with teacher $i$ and $b_j$ the number of teachers acquainted with student $j$ ($b_j\ge1$). Let $E$ be the set of acquainted pairs $(i,j)$; it is nonempty.

**$t$ cannot be larger.** If everybody knows everybody, every pair has ratio $2006/14$.

**Some pair always reaches $2006/14$.** Suppose not: $a_i/b_j<\frac{2006}{14}$ for all $(i,j)\in E$. For $(i,j)\in E$ we have $a_i\ge1$, so this says $\frac1{b_j}<\frac{2006}{14}\cdot\frac1{a_i}$. Sum over $E$:
- Grouping by students, $\sum_{(i,j)\in E}\frac1{b_j}=\sum_{j}b_j\cdot\frac1{b_j}=2006$.
- Grouping by teachers, $\sum_{(i,j)\in E}\frac1{a_i}=\sum_{i:\,a_i\ge1}a_i\cdot\frac1{a_i}\le14$.

So $2006<\frac{2006}{14}\cdot14=2006$, a contradiction. Hence in every school some acquainted pair has ratio at least $2006/14$, and the largest $t$ is $2006/14$.

---

## o59 · difficulty 4 · Recurrences
*original*

**Statement**

How many permutations $\sigma$ of $\{1,2,\dots,7\}$ have no fixed point, that is, $\sigma(i)\ne i$ for every $i$?

**Hint 1: What is being asked**

Count the arrangements of $1,\dots,7$ in which no number stays in its own position.

**Hint 2: The technique**

Let $D_n$ be the count for $n$ numbers. Decide where the last number goes and relate what remains to the smaller counts $D_{n-1}$ and $D_{n-2}$.

**Hint 3: The key idea**

Let $\sigma(n)=k$ with $k\ne n$ ($n-1$ choices). Split into two cases: $\sigma(k)=n$ or $\sigma(k)\ne n$.

**Hint 4: The next step**

In the first case, the other $n-2$ numbers form a smaller derangement. In the second, if $\sigma(j)=n$, redefine the value at $j$ to be $k$ and delete $n$. Show this gives a derangement of $n-1$ elements and that it is reversible.

**Solution**

Call such a permutation a derangement and let $D_n$ be the number of derangements of $\{1,\dots,n\}$. Clearly $D_1=0$ and $D_2=1$.

**Claim:** $D_n=(n-1)(D_{n-1}+D_{n-2})$ for $n\ge3$.

Let $\sigma$ be a derangement of $\{1,\dots,n\}$ and $k=\sigma(n)$; then $k\ne n$, giving $n-1$ choices of $k$. Fix $k$ and count the derangements with $\sigma(n)=k$.

- *Case $\sigma(k)=n$.* Then $\sigma$ swaps $n$ and $k$, and on the remaining $n-2$ numbers it is a derangement of that set. Conversely any derangement of those $n-2$ numbers extends. So there are $D_{n-2}$ such $\sigma$.
- *Case $\sigma(k)\ne n$.* Let $j$ be the element with $\sigma(j)=n$; then $j\ne n$ (as $\sigma(n)=k\ne n$) and $j\ne k$. Define $\sigma'$ on $\{1,\dots,n-1\}$ by $\sigma'(j)=k$ and $\sigma'(i)=\sigma(i)$ for $i\notin\{j,n\}$. The values of $\sigma$ on $\{1,\dots,n-1\}\setminus\{j\}$ are all numbers except $n$ and $k$ (the values $\sigma(j)=n$ and $\sigma(n)=k$ are the other two), so $\sigma'$ is a permutation of $\{1,\dots,n-1\}$, and it has no fixed point ($\sigma'(j)=k\ne j$). Conversely, given a derangement $\sigma'$ of $\{1,\dots,n-1\}$, put $j=\sigma'^{-1}(k)$ (note $j\ne k$), and define $\sigma(n)=k$, $\sigma(j)=n$, $\sigma(i)=\sigma'(i)$ otherwise: this is a derangement of $\{1,\dots,n\}$ with $\sigma(k)\ne n$, and the two constructions are inverse. So there are $D_{n-1}$ such $\sigma$.

Adding the cases and multiplying by the $n-1$ choices of $k$ proves the claim.

Now compute:
$$D_3=2(1+0)=2,\quad D_4=3(2+1)=9,\quad D_5=4(9+2)=44,\quad D_6=5(44+9)=265,\quad D_7=6(265+44)=1854.$$
The answer is $\boxed{1854}$.

---
