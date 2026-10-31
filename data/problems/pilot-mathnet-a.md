### m01
source: mathnet
mathnet_id: 017c
country: Baltic Way
competition: Baltic Way
type: proof
difficulty: 6
techniques: modular-arithmetic, constructive
statement:
Prove that there exists an integer which is divisible by $2010$ and whose decimal notation contains exactly two different digits.
asked:
You must produce (and justify) a multiple of $2010$ written with only two distinct digits.
technique:
A number made only of the digit $9$ is $10^k-1$, so look for a power of $10$ that is $1$ modulo something.
hint:
Factor $2010=10\cdot201$. A multiple of $10$ ends in $0$. You want the rest to be built from a single repeated digit.
hint:
$201$ is coprime to $10$. Euler's theorem gives $k$ with $10^k\equiv1\pmod{201}$. What does that say about $10^k-1$?
hint:
Multiply $10^k-1$ by $10$ and read off its decimal digits.
solution:
Since $201=3\cdot67$ is coprime to $10$, Euler's theorem gives $10^{\varphi(201)}\equiv1\pmod{201}$, where $\varphi(201)=2\cdot66=132$. So $201\mid10^{132}-1$.

Let $N=10\,(10^{132}-1)$. Then $2010=10\cdot201$ divides $N$. The number $10^{132}-1$ is $132$ nines, so $N$ is $132$ nines followed by a $0$. Its digits are exactly $9$ and $0$. $\blacksquare$

### m02
source: mathnet
mathnet_id: 0dsa
country: Singapore
competition: Singapore Mathematical Olympiad (SMO)
type: answer
difficulty: 5
techniques: double-counting, invariants
statement:
Consider a polygon with $m+n$ sides where $m,n$ are positive integers. Colour $m$ of its vertices red and the remaining $n$ vertices blue. A side is given the number $2$ if both its end vertices are red, the number $\frac12$ if both its end vertices are blue and the number $1$ otherwise. Let the product of these numbers be $P$. Find the largest possible value of $P$.
asked:
Over all ways of coloring the vertices, find the largest value of the product of the edge numbers.
technique:
The answer turns out not to depend on the coloring. This is a [[double-counting]] problem: count red endpoints of edges in two ways.
hint:
Write $P=2^{R-B}$, where $R$ is the number of red-red sides and $B$ the number of blue-blue sides. You need $R-B$.
hint:
Count pairs (vertex, side at that vertex) where the vertex is red. Each red vertex lies on exactly two sides.
hint:
Do the same for blue vertices, and subtract the two counts.
solution:
Let $R,B,M$ be the numbers of red-red, blue-blue and mixed sides. Then $P=2^{R}\cdot2^{-B}=2^{R-B}$.

Count pairs (red vertex, side through it). Each of the $m$ red vertices lies on $2$ sides, so there are $2m$ such pairs. A red-red side contributes $2$ pairs and a mixed side $1$, so $2m=2R+M$. Similarly for blue vertices, $2n=2B+M$.

Subtracting: $2(m-n)=2(R-B)$, so $R-B=m-n$ for every coloring. Hence $P=2^{m-n}$ always, and the largest value is $\boxed{2^{m-n}}$.

### m03
source: mathnet
mathnet_id: 032t
country: Bulgaria
competition: 53. Bulgarian Mathematical Olympiad
type: proof
difficulty: 7
techniques: extremal, graph-theory, pigeonhole
statement:
Let $m\ge3$ and $n\ge2$ be integers. Prove that in a group of $N=mn-n+1$ people such that there are two familiar people among any $m$, there is a person who is familiar with $n$ people. Does the statement remain true if $N<mn-n+1$?
asked:
Among $N$ people, any $m$ contain an acquainted pair. Show someone knows at least $n$ people, and decide whether that still holds for smaller groups.
technique:
Model the group as a graph ([[graph-theory]]) and use an [[extremal]] choice: take the largest set of people who all pairwise do not know each other.
hint:
The condition says there are never $m$ mutual strangers. Take a largest group of mutual strangers, of size $l\le m-1$.
hint:
By maximality, every outside person knows someone in the group. Count how many outside people the members of the group know in total, and use pigeonhole.
hint:
For the second question, try $m-1$ cliques of people who know exactly their own clique.
solution:
Take a largest set $S$ of people who pairwise do not know each other, with $|S|=l$. Among any $m$ people two know each other, so $l\le m-1$.

By maximality of $S$, each of the other $N-l$ people knows at least one member of $S$ (otherwise we could add them). So the members of $S$ together know at least $N-l$ people outside $S$, and by pigeonhole one member knows at least $\frac{N-l}{l}=\frac Nl-1$ of them. Since $l\le m-1$,
$$\frac Nl-1\ge\frac{mn-n+1}{m-1}-1=n-1+\frac1{m-1}>n-1.$$
The number of people known is an integer greater than $n-1$, so it is at least $n$.

**Smaller $N$: not true.** Let $N\le(m-1)n$. Split the people into $m-1$ groups of at most $n$ people each, where people know exactly those in their own group. Among any $m$ people two lie in the same group (pigeonhole), so they know each other. But everyone knows at most $n-1$ people. So the statement fails for $N\le(m-1)n=mn-n$, i.e. for every $N<mn-n+1$.

### m04
source: mathnet
mathnet_id: 01ai
country: Baltic Way
competition: Baltic Way 2013
type: proof
difficulty: 5
techniques: similar-triangles
statement:
Let $ABC$ be a triangle, and let $X,Y,Z$ be points on $BC,CA,AB$ respectively. Suppose that $AX$, $BY$ and $CZ$ intersect in a point $P$. Prove that
$$\frac{AP}{AX}+\frac{BP}{BY}+\frac{CP}{CZ}=2.$$
asked:
Three lines from the vertices meet at one point $P$ inside the triangle. Each ratio compares $AP$ with the full length $AX$ of the line from the vertex through $P$ to the opposite side. Show that the three ratios add to $2$.
technique:
Convert the segment ratios into ratios of areas: triangles on a common base have areas proportional to their heights, and the heights are in the ratio of segments along a line through the vertex ([[similar-triangles]]).
hint:
Write $\frac{AP}{AX}=1-\frac{PX}{AX}$.
hint:
Triangles $PBC$ and $ABC$ share the base $BC$. Their heights above $BC$ are in the ratio $PX:AX$.
solution:
Write $\frac{AP}{AX}=1-\frac{PX}{AX}$. Triangles $PBC$ and $ABC$ have the same base $BC$, and their heights from $P$ and $A$ to $BC$ are in the ratio $PX:AX$ (because $A$, $P$, $X$ are collinear and $X$ is on $BC$). So
$$\frac{PX}{AX}=\frac{[PBC]}{[ABC]}\quad\text{and}\quad\frac{AP}{AX}=1-\frac{[PBC]}{[ABC]}.$$
Similarly $\frac{BP}{BY}=1-\frac{[PCA]}{[ABC]}$ and $\frac{CP}{CZ}=1-\frac{[PAB]}{[ABC]}$. Adding,
$$\text{sum}=3-\frac{[PBC]+[PCA]+[PAB]}{[ABC]}=3-1=2.\ \blacksquare$$

### m05
source: mathnet
mathnet_id: 0hdk
country: Ukraine
competition: 60th Ukrainian National Mathematical Olympiad
type: proof
difficulty: 8
techniques: descent, divisibility
statement:
Let $a$ and $b$ be two different natural numbers such that $a^2+b^2+1$ is divisible by $2ab+1$. Prove that $2ab+1$ is a perfect square.
asked:
Given two different positive integers with $2ab+1\mid a^2+b^2+1$, show that $2ab+1$ is a perfect square.
technique:
Assume it fails, take a counterexample with the smallest sum $a+b$, and construct a smaller one.
hint:
Show first that $2ab+1\mid a^2+b^2+1$ is equivalent to $2ab+1\mid(2a^2+1)^2$. Multiply by $4a^2$ and use $4a^2b^2\equiv1$.
hint:
Write $(2a^2+1)^2=(2ab+1)(2ac+1)$ and explain why the second factor has the form $2ac+1$ with $c$ an integer.
hint:
Show $0<c<a<b$ when $a<b$, and that $(c,a)$ is again a counterexample with smaller sum.
solution:
**Lemma.** For positive integers $a,b$: $2ab+1\mid a^2+b^2+1$ if and only if $2ab+1\mid(2a^2+1)^2$.

*Proof.* The number $2ab+1$ is odd and coprime to $a^2$ (a common prime divides $a$ and $2ab+1$, hence divides $1$). So $2ab+1\mid a^2+b^2+1$ iff $2ab+1\mid4a^2(a^2+b^2+1)=4a^4+4a^2b^2+4a^2$. Now
$$4a^4+4a^2b^2+4a^2=(2a^2+1)^2+(4a^2b^2-1)=(2a^2+1)^2+(2ab-1)(2ab+1),$$
so this holds iff $2ab+1\mid(2a^2+1)^2$. $\square$

Suppose the claim fails. Among counterexamples $(a,b)$ with $a<b$ (the roles are symmetric) choose one with $a+b$ minimal. By the lemma, $(2a^2+1)^2=(2ab+1)\,q$ for an integer $q$. Modulo $2a$ both $(2a^2+1)^2$ and $2ab+1$ are $\equiv1$, so $q\equiv1\pmod{2a}$ and $q=2ac+1$ for an integer $c\ge0$.

If $c=0$, then $(2a^2+1)^2=2ab+1$ is a square, contradicting that $(a,b)$ is a counterexample. So $c\ge1$. If $c\ge a$, then since $b>a$, $(2ab+1)(2ac+1)>(2a^2+1)^2$, a contradiction. So $0<c<a<b$.

Applying the lemma to the pair $(a,c)$: $(2a^2+1)^2$ is divisible by $2ac+1$, hence $2ac+1\mid a^2+c^2+1$. Also $2ac+1$ is not a square: otherwise $2ab+1=(2a^2+1)^2/(2ac+1)$ would be a square (a quotient of two squares that is an integer). So $(c,a)$ with $c<a$ is a counterexample with sum $c+a<a+b$, contradicting minimality. $\blacksquare$

### m06
source: mathnet
mathnet_id: 0103
country: Baltic Way
competition: Baltic Way 1997
type: answer
difficulty: 5
techniques: modular-arithmetic, casework
statement:
Find all triples $(a,b,c)$ of non-negative integers satisfying $a\ge b\ge c$ and $1\cdot a^3+9\cdot b^2+9\cdot c+7=1997$.
asked:
Find all ordered triples with $a\ge b\ge c\ge0$ solving $a^3+9b^2+9c+7=1997$.
technique:
Use [[modular-arithmetic]] to restrict $a$, then bound the other variables.
hint:
Subtract $7$: $a^3+9b^2+9c=1990$. Reduce modulo $9$. What are the cubes mod $9$?
hint:
This limits $a$ to a few values. Use $a\ge b\ge c$ to show $a$ must be large.
solution:
The equation is $a^3+9b^2+9c=1990$. Since $1990=9\cdot221+1$, we get $a^3\equiv1\pmod9$. Cubes mod $9$ are $0$ (if $3\mid a$), $1$ (if $a\equiv1\pmod3$) and $8$ (if $a\equiv2\pmod3$). So $a\equiv1\pmod3$.

Also $a^3\le1990<13^3$, so $a\le12$, giving $a\in\{1,4,7,10\}$. If $a\le7$, then $b,c\le7$ and the left side is at most $343+9\cdot49+9\cdot7=847<1990$, impossible. So $a=10$ and $9b^2+9c=990$, i.e. $b^2+c=110$. Since $c\le b\le10$: if $b\le9$ then $b^2+c\le81+9=90<110$; so $b=10$ and $c=10$.

The only solution is $\boxed{(10,10,10)}$.

### m07
source: mathnet
mathnet_id: 08mq
country: JBMO
competition: Junior Balkan Mathematical Olympiad Shortlist
type: proof
difficulty: 6
techniques: am-gm
statement:
Let $x_i>1$ for all $i\in\{1,2,\dots,2011\}$. Prove the inequality
$$\sum_{i=1}^{2011}\frac{x_i^2}{x_{i+1}-1}\ge8044,$$
where $x_{2012}=x_1$. When does equality hold?
asked:
Prove the cyclic inequality and find the equality case.
technique:
Use [[am-gm]] twice: once to bound each numerator from below by a multiple of $x_i-1$, and once on a cyclic product that telescopes to $1$.
hint:
Compare $x_i^2$ with $4(x_i-1)$. What square is involved?
hint:
After that replacement, the sum has terms $\frac{x_i-1}{x_{i+1}-1}$. What is the product of all of them?
solution:
For every $i$, $(x_i-2)^2\ge0$ gives $x_i^2\ge4(x_i-1)$. All denominators are positive, so
$$\sum\frac{x_i^2}{x_{i+1}-1}\ge4\sum_{i=1}^{2011}\frac{x_i-1}{x_{i+1}-1}.$$
The $2011$ positive numbers $\frac{x_i-1}{x_{i+1}-1}$ have product $1$ (it telescopes around the cycle), so by AM-GM their sum is at least $2011$. Hence the original sum is at least $4\cdot2011=8044$.

Equality needs $x_i=2$ for every $i$ (from the first step), and then every ratio is $1$, so the second step is also tight. Equality holds exactly when all $x_i=2$.

### m08
source: mathnet
mathnet_id: 0dce
country: Saudi Arabia
competition: Saudi Arabian Mathematical Competitions
type: answer
difficulty: 7
techniques: polynomials
statement:
Let $n>1$ be a positive integer. Find all non-constant polynomials $P(x)$ with real coefficients such that
$$P(x)P(x^2)\cdots P(x^n)=P\!\left(x^{\frac{n(n+1)}2}\right)$$
for all real $x$.
asked:
Determine all non-constant real polynomials satisfying the identity, for a fixed $n\ge2$.
technique:
Compare degrees and leading coefficients of both sides ([[polynomials]]); then show any lower-order term would break the degree match.
hint:
Let $P$ have degree $m$ and leading coefficient $a$. Compare leading coefficients on both sides.
hint:
Write $P(x)=a(x^m+Q(x))$ with $\deg Q<m$ (and $a=\pm1$). If $Q\neq0$, compare the degree of the largest term that differs from the leading one on each side.
solution:
Let $N=\frac{n(n+1)}2$, and let $P$ have degree $m\ge1$ and leading coefficient $a$. Comparing leading coefficients gives $a^n=a$, so $a^{n-1}=1$. If $n$ is even, $a=1$; if $n$ is odd, $a=\pm1$.

Write $P(x)=a\,(x^m+Q(x))$ with $\deg Q<m$ ($Q$ possibly $0$). Suppose for contradiction $Q\ne0$, and let $k=\deg Q<m$. Then the identity says
$$a^n\prod_{j=1}^n\big(x^{jm}+Q(x^j)\big)=a\big(x^{mN}+Q(x^N)\big),\quad\text{so}\quad\prod_{j=1}^n\big(x^{jm}+Q(x^j)\big)-x^{mN}=Q(x^N).$$
On the left, replacing only the $j$th factor's leading term $x^{jm}$ by $Q(x^j)$ contributes degree $mN-j(m-k)$, and all other contributions have lower degree. The largest is $j=1$: degree $mN-(m-k)$, and only this choice reaches it, so its coefficient (the leading coefficient of $Q$) is nonzero. On the right the degree is $kN$. Their difference is $(m-k)N-(m-k)=(m-k)(N-1)>0$ since $N\ge3$. So the degrees differ, a contradiction.

Therefore $Q=0$ and $P(x)=a\,x^m$. Check: $\prod_jax^{jm}=a^nx^{mN}=a\,x^{mN}$ because $a^n=a$. So the solutions are $P(x)=x^m$ for any $m\ge1$ (when $n$ is even), and $P(x)=\pm x^m$ for any $m\ge1$ (when $n$ is odd).

### m09
source: mathnet
mathnet_id: 0hgo
country: Ukraine
competition: 62nd Ukrainian National Mathematical Olympiad, Third Round, First Tour
type: answer
difficulty: 4
techniques: constructive, modular-arithmetic
statement:
Does there exist a trinomial $f(x)=ax^2+bx+c$ with integer coefficients such that $a$ isn't divisible by $2022$ and all numbers $f(1),f(2),\dots,f(2022)$ give different remainders under division by $2022$?
asked:
Decide whether a quadratic with integer coefficients, whose leading coefficient is not a multiple of $2022$, can take $2022$ distinct values modulo $2022$ at $x=1,\dots,2022$.
technique:
This asks for a [[constructive]] example; use [[modular-arithmetic]] and the idea that $x(x+1)$ is always even.
hint:
The simplest map that hits every remainder is $x\mapsto x$. Try to add a term that is always a multiple of $2022$.
hint:
Since $x(x+1)$ is even, which multiple of $x(x+1)$ is divisible by $2022=2\cdot1011$?
solution:
**Yes.** Take $f(x)=1011x^2+1012x=1011\,x(x+1)+x$. The product $x(x+1)$ is even, so $1011\,x(x+1)$ is divisible by $2\cdot1011=2022$. Hence $f(x)\equiv x\pmod{2022}$, so $f(1),\dots,f(2022)$ have the remainders $1,2,\dots,2021,0$, all different. And $a=1011$ is not divisible by $2022$.

### m10
source: mathnet
mathnet_id: 0500
country: Estonia
competition: Selected Problems from Open Contests
type: answer
difficulty: 5
techniques: parity
statement:
Find all pairs $(m,n)$ of positive integers for which the $m\times n$ grid contains exactly $225$ rectangles whose side lengths are odd and whose edges lie on the lines of the grid.
asked:
Count rectangles with odd side lengths in an $m\times n$ grid, and find all $(m,n)$ giving exactly $225$.
technique:
Describe a rectangle by the pair of horizontal and the pair of vertical grid lines it uses. Odd side lengths are a statement about [[parity]].
hint:
A rectangle is chosen by two horizontal lines and two vertical lines. When is the distance between two numbered lines odd?
hint:
Count pairs of horizontal lines with different parity. Does the answer change when $m$ is even?
solution:
Number the horizontal lines $1,\dots,m+1$ and the vertical lines $1,\dots,n+1$. A side length is the difference of two line numbers, which is odd exactly when the two numbers have different parity. So a rectangle with odd sides corresponds to a pair of horizontal lines of different parity and a pair of vertical lines of different parity.

If $m$ is even, $m=2k$, there are $k+1$ odd-numbered and $k$ even-numbered horizontal lines, giving $k(k+1)$ pairs, which is even. Then the total number of rectangles is even and cannot be $225$. The same holds for $n$. So $m$ and $n$ are odd: $m=2k-1$, $n=2l-1$.

Then there are $k$ odd-numbered and $k$ even-numbered horizontal lines, so $k^2$ pairs, and $l^2$ vertical pairs. The number of rectangles is $k^2l^2=(kl)^2=225$, so $kl=15$, giving $(k,l)\in\{(1,15),(3,5),(5,3),(15,1)\}$. Hence
$$(m,n)\in\boxed{\{(1,29),(5,9),(9,5),(29,1)\}}.$$

### m11
source: mathnet
mathnet_id: 0b5r
country: Romania
competition: Junior Balkan Mathematical Olympiad
type: answer
difficulty: 7
techniques: double-counting, pigeonhole, constructive
statement:
Each of $2009$ (distinct) points in the plane is coloured blue or red, so that on every blue-centered unit circle lie exactly two red points. Determine the largest possible number of blue points.
asked:
Find the maximum number of blue points when every unit circle centered at a blue point passes through exactly two red points.
technique:
Assign to each blue point the pair of red points on its circle and count how many blue points can share a pair.
hint:
Two red points lie on at most how many unit circles? Think about where their centers can be.
hint:
Let $r$ be the number of red points. Bound the number of blue points in terms of $r$, then use $r+b=2009$.
hint:
For the construction, put the red points on a line and the blue centers on perpendicular bisectors of pairs.
solution:
Let there be $r$ red and $b$ blue points, $r+b=2009$. To each blue point assign the pair of red points on its unit circle. Two red points $R_1,R_2$ lie on a common unit circle only if its center is on the perpendicular bisector of $R_1R_2$ at distance $1$ from both, which gives at most $2$ centers. So each pair is assigned to at most $2$ blue points, and
$$b\le2\binom r2=r(r-1).$$
Then $2009=r+b\le r^2$, so $r\ge45$ (as $44^2=1936<2009\le45^2$). Hence $b\le2009-45=1964$.

**Construction.** Take $r=45$ red points $R_i=(r_i,0)$ with distinct $0<r_i<2$. For each pair $i<j$ the two points $\left(\frac{r_i+r_j}2,\pm\sqrt{1-\frac{(r_i-r_j)^2}4}\right)$ are at distance exactly $1$ from $R_i$ and $R_j$. Their number is $2\binom{45}2=1980\ge1964$, so choose $1964$ of them as blue points. A unit circle meets the $x$-axis in at most two points, so the unit circle around such a blue point contains exactly the two red points $R_i,R_j$ it was built from. Blue points built from different pairs are different (they would otherwise be at distance $1$ from at least three red points), and none lies on the $x$-axis, so none is red. This gives $45+1964=2009$ distinct points.

The largest number of blue points is $\boxed{1964}$.

### m12
source: mathnet
mathnet_id: 0c8t
country: Romania
competition: Romanian Master of Mathematics
type: proof
difficulty: 8
techniques: graph-theory, extremal
statement:
In a country there are $n$ airports and $n$ air companies operating return flights. Each company operates an odd number of flights forming a closed route. Prove that a traveller can complete a closed route consisting of an odd number of flights operated by pairwise distinct companies.
asked:
Each company's flights form an odd closed route (parallel flights of different companies count as different edges). Show that there is an odd closed route in which no two flights belong to the same company.
technique:
Translate to [[graph-theory]]: you have $n$ odd cycles on the same $n$ vertices and want an odd cycle with edges taken from different cycles. Use an [[extremal]] choice: a largest "rainbow" forest.
hint:
Call a set of edges rainbow if no two come from the same company. Take a largest rainbow set of edges containing no cycle.
hint:
A forest on $n$ vertices has fewer than $n$ edges, so some company contributes no edge to it. Look at that company's odd cycle.
hint:
Show every edge of that cycle joins two vertices in the same tree of the forest, and use that trees are bipartite.
solution:
Each company's closed route is an odd cycle on the vertex set of $n$ airports. Call a set of edges *rainbow* if its edges come from different companies. Let $F$ be a rainbow set of edges with no cycle (a rainbow forest) of maximum size.

$F$ has at most $n-1$ edges (it is a forest on $n$ vertices), and its edges come from distinct companies, so some company $C$ has no edge in $F$. Consider the odd cycle of $C$.

No edge $e$ of this cycle joins two different components of $F$ (components include isolated vertices): otherwise $F\cup\{e\}$ would be a larger rainbow forest. So all vertices of the cycle lie in the same component of $F$, a tree $T$. A tree is bipartite: its vertices split into two parts with all tree edges between them. The cycle of $C$ has odd length, so it cannot be properly 2-colored by these parts; hence it has an edge $e$ whose endpoints are in the same part.

The path in $T$ between the endpoints of $e$ has even length (same part), so together with $e$ it forms a cycle of odd length. Its edges are tree edges (from distinct companies) plus $e$ (from $C$, which has no edge in $F$). So it is an odd closed route with pairwise distinct companies. $\blacksquare$
