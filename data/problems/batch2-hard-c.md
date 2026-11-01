### m75
source: mathnet
mathnet_id: 09jl
country: Mongolia
competition: Mongolian Mathematical Olympiad Round 3
type: answer
difficulty: 7
techniques: extremal, graph-theory, double-counting
statement:
Find the smallest real number $c$ with $0<c<1$ such that the following holds: every simple graph with $n\ge3$ vertices that contains no triangle and in which every vertex has degree strictly greater than $cn$ is bipartite. (A graph is bipartite if its vertices can be coloured with two colours so that no edge joins two vertices of the same colour.)
asked:
Find the least $c$ for which "triangle-free and minimum degree $>cn$" always forces the graph to be bipartite, and prove that this $c$ works while every smaller value fails.
technique:
A graph that is not bipartite contains some odd cycle; choose one that is as special as possible and see how the rest of the graph can attach to it.
hint:
A small odd cycle shows that $c$ cannot be below $\frac25$. For the other direction, suppose a triangle-free graph is not bipartite and take a shortest odd cycle $C$. What is its length at least?
hint:
Show that a vertex of $C$ has no neighbours on $C$ besides its two cycle neighbours, and that a vertex off $C$ has at most two neighbours on $C$ (three neighbours would cut out a shorter odd cycle).
hint:
Add up the degrees of the vertices of $C$ by counting, for every vertex of the graph, its neighbours on $C$.
solution:
**Answer:** $c=\dfrac25$.

**Values below $\frac25$ fail.** The $5$-cycle has $n=5$ vertices, no triangle, and every degree equals $2=\frac25n$. If $c<\frac25$ then $2>cn$, but the $5$-cycle is not bipartite (an odd cycle cannot be $2$-coloured alternately). So no $c<\frac25$ has the property.

**$c=\frac25$ works.** Let $G$ be a triangle-free graph on $n$ vertices which is not bipartite. We show some vertex has degree at most $\frac{2n}5$.

A graph with no odd cycle is bipartite (colour each connected component by the parity of the distance from a fixed vertex), so $G$ has an odd cycle. Let $C=v_1v_2\dots v_m$ be an odd cycle of minimum length $m$. Since there are no triangles, $m\ge5$.

*Claim 1: a vertex $v_i$ of $C$ has exactly two neighbours on $C$, namely $v_{i-1}$ and $v_{i+1}$ (indices mod $m$).* Suppose there is a chord $v_iv_j$ with $v_i,v_j$ not consecutive on $C$. It splits $C$ into two paths of lengths $a,b\ge2$ with $a+b=m$, and each path together with the chord is a cycle, of lengths $a+1$ and $b+1$. Their sum $m+2$ is odd, so one of them is odd, and its length is at most $m-2+1=m-1<m$. This contradicts the minimality of $m$.

*Claim 2: a vertex $u$ not on $C$ has at most two neighbours on $C$.* Suppose $u$ is adjacent to three vertices of $C$. They cut $C$ into three arcs of lengths $p,q,r\ge1$ with $p+q+r=m$. Each arc together with the two edges from $u$ to its endpoints is a cycle, of lengths $p+2$, $q+2$, $r+2$. An arc of length $1$ would give a triangle, so $p,q,r\ge2$ and each of these cycles has length at least $4$. The three lengths add up to $m+6$, which is odd, so one of them, say $p+2$, is odd. Then $p+2=(m+6)-(q+2)-(r+2)\le m+6-8=m-2$, an odd cycle shorter than $C$, a contradiction.

For a vertex $u$ let $d(u,C)$ be its number of neighbours on $C$. By the claims, $d(u,C)\le2$ for every vertex $u$ of $G$. Counting the pairs $(v,u)$ with $v\in C$ and $uv$ an edge in two ways,
$$\sum_{v\in C}\deg v=\sum_{u\in G}d(u,C)\le2n.$$
So some $v\in C$ has $\deg v\le\frac{2n}m\le\frac{2n}5$.

Hence, if every degree is greater than $\frac25n$, a triangle-free graph must be bipartite, and the smallest constant is $\boxed{\tfrac25}$.

### m76
source: mathnet
mathnet_id: 00hd
country: Asia Pacific Mathematics Olympiad (APMO)
competition: APMO 2016
type: answer
difficulty: 7
techniques: graph-theory, induction, double-counting
statement:
The country Dreamland consists of $2016$ cities. The airline Starways wants to establish some one-way flights between pairs of cities in such a way that each city has exactly one flight out of it. Find the smallest positive integer $k$ such that no matter how Starways establishes its flights, the cities can always be partitioned into $k$ groups so that from any city it is not possible to reach another city in the same group by using at most $28$ flights.
asked:
Each city has exactly one outgoing flight (to a different city). Find the least $k$ such that, for every such flight network, the cities can be split into $k$ groups with no city able to reach another city of its own group in $28$ or fewer flights.
technique:
The groups are the colour classes of a colouring of a suitable graph on the cities; bound how many colours that graph can require.
hint:
For the lower bound, find a flight network containing many cities that pairwise conflict.
hint:
For the upper bound: from a fixed city, the route is forced, so how many cities can it reach in at most $28$ flights? Use this to bound the number of conflicting pairs inside any set of cities.
hint:
Some city in any set has few conflicts inside that set. Remove it, colour the rest, and put it back.
solution:
**Answer:** $k=57$.

Call two cities in *conflict* if one of them can reach the other using at most $28$ flights. We need the least $k$ such that the cities can always be split into $k$ groups with no two conflicting cities in the same group.

**At least $57$ groups may be needed.** Let Starways arrange $57$ of the cities in a cycle $c_1\to c_2\to\dots\to c_{57}\to c_1$, and let every other city fly to $c_1$. For two cycle cities $c_i,c_j$ ($i<j$), $c_i$ reaches $c_j$ in $j-i$ flights and $c_j$ reaches $c_i$ in $57-(j-i)$ flights. These two numbers add up to $57$, so one of them is at most $28$. Hence any two of the $57$ cycle cities conflict and must be in different groups, so $k\ge57$.

**$57$ groups always suffice.** Let $f(u)$ be the city reached from $u$ by its unique outgoing flight. Starting from $u$, every route is forced: after $t$ flights we are at $f^t(u)$. So the cities that $u$ can reach with at most $28$ flights are among $f(u),f^2(u),\dots,f^{28}(u)$, which is at most $28$ cities.

*Claim.* In any nonempty set $W$ of cities there is a city that conflicts with at most $56$ other cities of $W$.

Indeed, for each conflicting pair inside $W$ pick one city of the pair that reaches the other within $28$ flights. Each city of $W$ is picked for at most $28$ pairs, so the number of conflicting pairs inside $W$ is at most $28|W|$. Every pair has two cities, so the sum over $x\in W$ of the number of cities of $W$ conflicting with $x$ is at most $2\cdot28|W|=56|W|$, and some $x$ has at most $56$.

Now we show by induction on $|W|$ that every set $W$ of cities can be split into $57$ groups with no conflicts inside a group. For $|W|=1$ this is clear. For larger $W$, take $x$ from the claim, split $W\setminus\{x\}$ into $57$ good groups by the induction hypothesis, and add $x$ to a group containing none of the at most $56$ cities conflicting with $x$. Such a group exists since there are $57$ groups. Applying this to all $2016$ cities finishes the proof.

So the smallest $k$ is $\boxed{57}$.

### m77
source: mathnet
mathnet_id: 0gtu
country: Turkey
competition: Team Selection Test for IMO 2023
type: answer
difficulty: 8
techniques: graph-theory
statement:
In a school having $n$ students any student has exactly $2023$ friends and if two students are not friends then they have exactly $2022$ common friends. Find all possible values of $n$.
asked:
Friendship is mutual. Every student has exactly $2023$ friends, and any two students who are not friends have exactly $2022$ common friends. Determine every $n$ for which such a school exists.
technique:
Reformulate the condition as a local property of a graph, and work out what that property forces around a single vertex.
hint:
Let $H$ be the graph of non-friendships and $m=n-1-2023$ its common degree. Count the common friends of two non-friends $u,v$ in terms of their common neighbours in $H$, and show that adjacent vertices of $H$ have exactly $m-2$ common neighbours in $H$.
hint:
Fix $u$ and look at its $m$ neighbours in $H$. Inside this set, each vertex is adjacent to all but exactly one of the others. What does this force about $m$? Treat $m=0$, $m=1$ and $m=2$ separately.
hint:
For $m\ge4$, take two adjacent neighbours $v,w$ of $u$ and count their common neighbours in $H$: one is missing, and it must lie outside. Conclude that each component of $H$ is $K_{m+2}$ with a perfect matching removed.
solution:
**Answer:** $n\in\{2024,\ 2026,\ 2028,\ 2696,\ 4044\}$.

Let $G$ be the friendship graph and $H$ its complement (students joined in $H$ when they are not friends). Every vertex has degree $2023$ in $G$, so it has degree $m:=n-1-2023$ in $H$.

**Translating the condition.** Let $u,v$ be adjacent in $H$, and let $\lambda$ be their number of common neighbours in $H$. A vertex $x\ne u,v$ is a common friend of $u$ and $v$ exactly when $x$ is in neither $N_H(u)$ nor $N_H(v)$. The sets $N_H(u)\setminus\{v\}$ and $N_H(v)\setminus\{u\}$ have $m-1$ elements each and $\lambda$ in common, so their union has $2(m-1)-\lambda$ elements, and $u,v$ have $(n-2)-2(m-1)+\lambda=n-2m+\lambda$ common friends. The condition says this equals $2022=n-m-2$, that is,
$$\lambda=m-2.$$
So the problem is equivalent to: **$H$ is $m$-regular on $n=m+2024$ vertices, and any two adjacent vertices of $H$ have exactly $m-2$ common neighbours.** (The steps above are reversible, so any such $H$ gives a valid school.)

**$m=0$.** Then $G$ is the complete graph on $2024$ vertices and the condition is vacuous. So $n=2024$ works.

**$m=1$.** Two adjacent vertices of $H$ would need $-1$ common neighbours. Impossible.

**The neighbourhood of a vertex.** Let $m\ge2$, fix $u$ and let $N=N_H(u)$, $|N|=m$. For $v\in N$, the common neighbours of $u$ and $v$ lie in $N$, and there are $m-2$ of them. So inside $N$, every $v$ is adjacent to all but exactly one of the other $m-1$ vertices; call that vertex $v'$. Then $v''=v$, so $v\mapsto v'$ pairs up the vertices of $N$. Hence $m$ is even, and $N$ induces $K_m$ minus a perfect matching. Besides $u$ and its $m-2$ neighbours in $N$, each $v\in N$ has exactly one more neighbour, which lies outside $N\cup\{u\}$; call it $x_v$.

**$m=2$.** Then the condition only says that $H$ is $2$-regular with no triangle, i.e. a disjoint union of cycles of length at least $4$. For example, a single cycle of length $2026$ works, so $n=2026$ is possible.

**$m\ge4$.** Take $v,w\in N$ adjacent (that is, $w\ne v'$). Their common neighbours inside $N\cup\{u\}$ are $u$ and the vertices of $N\setminus\{v,v',w,w'\}$. These four vertices are distinct, because $w\ne v'$, and $w'\ne v$ since $w$ is adjacent to $v$. That gives $1+(m-4)=m-3$ common neighbours, so exactly one more common neighbour lies outside $N\cup\{u\}$. The only outside neighbour of $v$ is $x_v$ and that of $w$ is $x_w$, so $x_v=x_w$. Since $K_m$ minus a perfect matching is connected for $m\ge4$, all $x_v$ ($v\in N$) are one vertex $x$. Then $x$ is adjacent to all $m$ vertices of $N$, so $N_H(x)=N$, and $x$ is not adjacent to $u$.

Thus the set $C=\{u,x\}\cup N$ of $m+2$ vertices has no edges leaving it: $u$ and $x$ have all neighbours in $N$, and each $v\in N$ has its neighbours $u,x$ and $m-2$ vertices of $N$. Inside $C$ the only missing edges are $ux$ and the pairs $vv'$. So every component of $H$ is $K_{m+2}$ minus a perfect matching. Conversely, such a graph works: it is $m$-regular, and two adjacent vertices $p,q$ are adjacent to everything in the component except $p,q$ and their two (distinct) partners, so they have $m+2-4=m-2$ common neighbours.

So for $m\ge4$ the vertex count is $n=b(m+2)$ for some number $b$ of components, with $m$ even. Combining with $n=m+2024$:
$$b(m+2)=m+2024\iff(b-1)(m+2)=2022=2\cdot3\cdot337.$$
Here $m+2$ is an even divisor of $2022$ with $m+2\ge6$, so $m+2\in\{6,674,2022\}$, giving $b-1=337,3,1$ and $n=6\cdot338=2028$, $n=674\cdot4=2696$, $n=2022\cdot2=4044$.

Altogether the possible values are $\boxed{2024,\ 2026,\ 2028,\ 2696,\ 4044}$.

### m78
source: mathnet
mathnet_id: 06pe
country: IMO
competition: 48th International Mathematical Olympiad Vietnam 2007 Shortlisted Problems with Solutions
type: answer
difficulty: 8
techniques: double-counting, modular-arithmetic
statement:
Find all positive integers $n$ for which the numbers in the set $S=\{1,2,\ldots,n\}$ can be coloured red and blue so that the set $S\times S\times S$ contains exactly $2007$ ordered triples $(x,y,z)$ such that (i) $x,y,z$ have the same colour and (ii) $x+y+z$ is divisible by $n$.
asked:
Each of $1,\dots,n$ is coloured red or blue. Find every $n$ for which some colouring has exactly $2007$ ordered triples $(x,y,z)$ of one colour with $n\mid x+y+z$.
technique:
The one-coloured triples are hard to count directly. Count a related family of triples in two different ways.
hint:
Let $r$ and $b$ be the numbers of red and blue elements. How many ordered triples $(x,y,z)$ with $n\mid x+y+z$ are there in total?
hint:
In a two-coloured triple, look at the three cyclic pairs $(x,y),(y,z),(z,x)$. Exactly one of them is (red, blue). How many triples does a given (red, blue) pair belong to in this way?
hint:
You should get $r^2-rb+b^2=2007=9\cdot223$. Show $3\mid r$ and $3\mid b$, then bound the larger of $r/3$, $b/3$.
solution:
**Answer:** $n=69$ and $n=84$.

Fix a colouring, let $R,B$ be the red and blue sets, $r=|R|$, $b=|B|$, $r+b=n$. Call a triple *divisible* if $n\mid x+y+z$.

**Total.** For each pair $(x,y)\in S\times S$ exactly one $z\in S$ makes $(x,y,z)$ divisible (the residues of $1,\dots,n$ mod $n$ are all different). So there are $n^2$ divisible triples.

**Two-coloured divisible triples.** In a two-coloured triple $(x,y,z)$, one colour appears twice and the other once. Going around the cycle $x\to y\to z\to x$ the colour changes exactly twice, once from red to blue and once from blue to red. So exactly one of the pairs $(x,y),(y,z),(z,x)$ lies in $R\times B$. Assign this pair to the triple.

Conversely, take $(x,y)\in R\times B$ and let $z$ be the element with $(x,y,z)$ divisible. The triples $(x,y,z)$, $(y,z,x)$, $(z,x,y)$ are divisible and two-coloured, and $(x,y)$ is assigned to each of them. They are three different ordered triples: for instance $(x,y,z)=(y,z,x)$ would force $x=y$, but $x$ is red and $y$ blue. Any triple to which $(x,y)$ is assigned has $(x,y)$ in one of its three cyclic positions, and the third entry is then forced to be $z$, so it is one of these three. Hence every pair of $R\times B$ is assigned to exactly $3$ triples, and there are exactly $3rb$ two-coloured divisible triples.

Therefore the number of one-coloured divisible triples is
$$n^2-3rb=(r+b)^2-3rb=r^2-rb+b^2,$$
which depends only on $r$ and $b$.

**Solving $r^2-rb+b^2=2007$.** We have $2007=9\cdot223$ with $223$ prime. From $(r+b)^2=2007+3rb$ we get $3\mid(r+b)^2$, so $3\mid r+b$ and $9\mid(r+b)^2$. Then $9\mid3rb$, so $3\mid rb$; together with $3\mid r+b$ this gives $3\mid r$ and $3\mid b$. Write $r=3s$, $b=3c$; then $s^2-sc+c^2=223$. By symmetry assume $s\ge c\ge0$.

- Since $s^2-sc+c^2=s^2-c(s-c)\le s^2$, we get $s^2\ge223$, so $s\ge15$.
- Since $4(s^2-sc+c^2)=(2c-s)^2+3s^2\ge3s^2$, we get $3s^2\le892$, so $s\le17$.

For $s=15$: $c^2-15c+2=0$ has discriminant $217$, not a square. For $s=16$: $c^2-16c+33=0$ has discriminant $124$, not a square. For $s=17$: $c^2-17c+66=(c-6)(c-11)=0$, so $c=6$ or $c=11$.

So $\{r,b\}=\{51,18\}$ or $\{51,33\}$, and $n=r+b\in\{69,84\}$. Conversely, for $n=69$ colour any $51$ numbers red and the other $18$ blue, and for $n=84$ colour $51$ red and $33$ blue; by the formula each has exactly $51^2-51\cdot18+18^2=2007$, respectively $51^2-51\cdot33+33^2=2007$, one-coloured divisible triples.

The answer is $\boxed{n=69\text{ and }n=84}$.

### m79
source: mathnet
mathnet_id: 0j80
country: United States
competition: USAMO
type: proof
difficulty: 7
techniques: double-counting, cauchy-schwarz
statement:
Let $A$ be a set with $|A|=225$. Suppose further that there are eleven subsets $A_1,\dots,A_{11}$ of $A$ such that $|A_i|=45$ for $1\le i\le11$ and $|A_i\cap A_j|=9$ for $1\le i<j\le11$. Prove that $|A_1\cup A_2\cup\dots\cup A_{11}|\ge165$, and give an example for which equality holds.
asked:
Eleven sets of size $45$ pairwise meet in exactly $9$ elements. Show their union has at least $165$ elements, and construct sets where it has exactly $165$.
technique:
Count incidences between elements and sets in two ways, then compare the resulting sums with an inequality.
hint:
Let $x_a$ be the number of sets $A_i$ containing $a$. Compute $\sum_a x_a$ and $\sum_a\binom{x_a}2$ from the data.
hint:
Only elements of the union have $x_a>0$. Which inequality relates $\left(\sum x_a\right)^2$, $\sum x_a^2$ and the number of nonzero terms?
hint:
For equality every element of the union lies in the same number of sets. Which number? Try indexing the elements by small subsets of $\{1,\dots,11\}$.
solution:
For $a\in A$ let $x_a$ be the number of indices $i$ with $a\in A_i$, and let $U=A_1\cup\dots\cup A_{11}$, $u=|U|$. Then $x_a\ge1$ exactly for $a\in U$.

**Two counts.** Counting pairs $(a,i)$ with $a\in A_i$ in two ways,
$$\sum_{a\in U}x_a=\sum_{i=1}^{11}|A_i|=11\cdot45=495.$$
Counting triples $(a,\{i,j\})$ with $i\ne j$ and $a\in A_i\cap A_j$ in two ways (an element in $x_a$ sets lies in $\binom{x_a}2$ such intersections),
$$\sum_{a\in U}\binom{x_a}2=\sum_{i<j}|A_i\cap A_j|=\binom{11}2\cdot9=495.$$
Hence $\sum_{a\in U}x_a^2=2\cdot495+495=1485$.

**The bound.** By the Cauchy–Schwarz inequality applied to the $u$ numbers $x_a$, $a\in U$,
$$495^2=\Big(\sum_{a\in U}x_a\Big)^2\le u\sum_{a\in U}x_a^2=1485\,u,$$
so $u\ge\dfrac{495^2}{1485}=\dfrac{495}{3}=165$.

**Equality.** Equality in Cauchy–Schwarz needs all $x_a$ equal, to $1485/495=3$. So let every element of the union lie in exactly three sets. Let $U$ be the family of all $3$-element subsets of $\{1,2,\dots,11\}$, so $|U|=\binom{11}3=165$, and let $A=U\cup E$ where $E$ is any set of $60$ further elements, so $|A|=225$. Put
$$A_i=\{T\in U: i\in T\}.$$
Then $|A_i|=\binom{10}2=45$ (choose the other two members of $T$), $|A_i\cap A_j|=\binom91=9$ for $i\ne j$ (choose the third member), and $A_1\cup\dots\cup A_{11}=U$ has exactly $165$ elements. $\blacksquare$

### m80
source: mathnet
mathnet_id: 0j2i
country: United States
competition: Team Selection Test 2010
type: proof
difficulty: 8
techniques: double-counting, parity
statement:
Let $T$ be a finite set of positive integers greater than $1$. A subset $S$ of $T$ is called *good* if for every $t\in T$ there exists some $s\in S$ with $\gcd(s,t)>1$. Prove that the number of good subsets of $T$ is odd.
asked:
Show that the number of subsets $S\subseteq T$ such that every element of $T$ shares a common factor greater than $1$ with some element of $S$ is odd.
technique:
Only the parity of a count matters. Find a larger set whose size has the same parity as the number of good subsets, and whose size is easy to determine modulo $2$ by pairing its elements.
hint:
Consider the ordered pairs $(X,Y)$ of subsets of $T$ such that every element of $X$ is coprime to every element of $Y$.
hint:
Swapping $X$ and $Y$ pairs these up. Which pairs are fixed by the swap? (Recall every element of $T$ exceeds $1$.)
hint:
Now fix $X$ and count the possible $Y$. When is that number odd?
solution:
Let $\mathcal P$ be the set of ordered pairs $(X,Y)$ of subsets of $T$ such that $\gcd(x,y)=1$ for all $x\in X$, $y\in Y$. We find the parity of $|\mathcal P|$ in two ways.

**First way: pairing.** The condition is symmetric in $X$ and $Y$, so $(X,Y)\mapsto(Y,X)$ maps $\mathcal P$ to itself, and doing it twice gives the identity. Its fixed points are the pairs $(X,X)\in\mathcal P$. If $X$ had an element $x$, then $\gcd(x,x)=x>1$ would violate the condition, so the only fixed point is $(\varnothing,\varnothing)$. All other elements of $\mathcal P$ split into pairs $\{(X,Y),(Y,X)\}$ with $X\ne Y$. Hence $|\mathcal P|$ is odd.

**Second way: fix $X$.** For $X\subseteq T$ let
$$Z(X)=\{t\in T:\gcd(t,x)=1\text{ for all }x\in X\}.$$
Then $(X,Y)\in\mathcal P$ exactly when $Y\subseteq Z(X)$, so for fixed $X$ there are $2^{|Z(X)|}$ choices of $Y$. Therefore
$$|\mathcal P|=\sum_{X\subseteq T}2^{|Z(X)|}.$$
A term is odd exactly when $Z(X)=\varnothing$, and it is even otherwise. But $Z(X)=\varnothing$ means that every $t\in T$ has some $x\in X$ with $\gcd(t,x)>1$, i.e. $X$ is good. So
$$|\mathcal P|\equiv\#\{\text{good subsets of }T\}\pmod2.$$

Comparing the two ways, the number of good subsets is odd. $\blacksquare$

### m81
source: mathnet
mathnet_id: 0hxm
country: United States
competition: TST
type: answer
difficulty: 7
techniques: pigeonhole, graph-theory
statement:
A tournament on $n$ vertices is obtained by joining every two of $n$ vertices by exactly one directed edge. The edges of a tournament are coloured so that no two edges of the same colour form a directed path of length $2$ (that is, there are no edges $u\to v$ and $v\to w$ of the same colour). For each $n\ge2$, determine the smallest number of colours $f(n)$ for which some tournament on $n$ vertices admits such a colouring.
asked:
Over all tournaments on $n$ vertices, find the least number of colours needed so that no vertex has an incoming and an outgoing edge of the same colour.
technique:
Attach to each vertex some information read off from the colouring, and compare this information at the two ends of an edge.
hint:
Let $S(v)$ be the set of colours of the edges leaving $v$. If $u\to v$ has colour $c$, what can you say about $c$ and the sets $S(u)$, $S(v)$?
hint:
Conclude that the $n$ sets $S(v)$ are pairwise different. This gives the lower bound $2^{f(n)}\ge n$.
hint:
For the construction, use the tournament in which $i\to j$ whenever $i>j$, on the vertices $0,1,\dots,n-1$, and look at binary expansions.
solution:
**Answer:** $f(n)=\lceil\log_2n\rceil$.

**Lower bound.** Take any tournament on $n$ vertices with a valid colouring using $k$ colours. For a vertex $v$ let $S(v)$ be the set of colours of edges leaving $v$.

Let $u\to v$ be an edge with colour $c$. Then $c\in S(u)$. If also $c\in S(v)$, there would be an edge $v\to w$ of colour $c$, and $u\to v\to w$ would be a path of two edges of colour $c$, which is forbidden. So $c\notin S(v)$, and in particular $S(u)\ne S(v)$.

Every two vertices are joined by an edge in some direction, so the $n$ sets $S(v)$ are pairwise different subsets of the $k$ colours. Hence $n\le2^k$, i.e. $k\ge\lceil\log_2n\rceil$.

**Construction.** Let $k=\lceil\log_2n\rceil$, so $n\le2^k$ and every integer $0\le i\le n-1$ has a binary expansion with digits in positions $0,1,\dots,k-1$. Take the tournament on $\{0,1,\dots,n-1\}$ with $i\to j$ whenever $i>j$. For $i>j$, look at the highest binary position in which $i$ and $j$ differ; since $i>j$, there $i$ has digit $1$ and $j$ has digit $0$. Give the edge $i\to j$ this position as its colour. This uses colours from $\{0,\dots,k-1\}$.

Suppose $i\to j$ and $j\to l$ both had colour $c$. From the first edge, $j$ has digit $0$ in position $c$, and from the second edge, $j$ has digit $1$ in position $c$, a contradiction. So the colouring is valid.

Therefore $f(n)=\boxed{\lceil\log_2n\rceil}$.

### m82
source: mathnet
mathnet_id: 0gqd
country: Turkey
competition: Team Selection Test for JBMO
type: answer
difficulty: 6
techniques: extremal, graph-theory
statement:
Between any two cities of a country consisting of $2013$ cities a one-way flight is organized (in exactly one of the two directions), so that there is at least one departure from each city. Determine the maximal possible value of $k$ such that no matter how these flights are arranged, there are $k$ cities each of which can be reached from every other city by using at most two flights.
asked:
Every pair of the $2013$ cities has a flight in one direction, and every city has an outgoing flight. Find the largest $k$ such that there are always at least $k$ cities, each reachable from every other city in one or two flights.
technique:
To show that some city is reachable from everywhere, pick it to be extreme with respect to a suitable count, and turn a failure into a city that beats it in that count.
hint:
For an upper bound, build a network in which one city can only reach two other cities within two flights.
hint:
This is the textbook maximum-wins argument with the flights reversed; the real work is getting two more such cities.
hint:
To get a second and a third such city, repeat the argument, but maximize the number of incoming flights only among the cities that the previous city flies to.
solution:
**Answer:** $k=3$.

Write $X\to Y$ if the flight between $X$ and $Y$ goes from $X$ to $Y$, and call a city *central* if it can be reached from every other city with at most two flights. Let $\deg^-(X)$ be the number of flights arriving at $X$.

**At most $3$ in general.** Take three cities with $A\to B\to C\to A$, and let every other city fly to each of $A,B,C$ (flights among the other cities are arbitrary). Every city has a departure. The only flight out of $A$ goes to $B$, and the only flight out of $B$ goes to $C$. So with at most two flights $A$ reaches only $B$ and $C$, and no other city can be central. Hence $k\le3$.

**Always at least $3$.** *Lemma.* Let $U$ be either the set of all cities, or the set of cities $X$ with $Z\to X$ for some fixed city $Z$, and assume $U\neq\varnothing$. If $A\in U$ has the largest $\deg^-$ among the cities of $U$, then $A$ is central.

*Proof.* Let $X\ne A$. If $X\to A$ we are done, so let $A\to X$.
- If $X\notin U$, then $U$ is the set of cities $Z$ flies to. Note $X\ne Z$, since $Z\to A$ while $A\to X$. As $X\notin U$, the flight between $X$ and $Z$ goes $X\to Z$, and $X\to Z\to A$ works.
- If $X\in U$ and $X$ cannot reach $A$ in at most two flights, then for every $Y$ with $Y\to A$ we must have $Y\to X$ (otherwise $X\to Y\to A$). Also $A\to X$. So $\deg^-(X)\ge\deg^-(A)+1$, contradicting the choice of $A$ in $U$. $\square$

Now apply the lemma three times.
1. Let $A_1$ have the largest $\deg^-$ among all cities. It is central.
2. Let $U_1$ be the set of cities $A_1$ flies to; it is nonempty because $A_1$ has a departure. Let $A_2\in U_1$ have the largest $\deg^-$ in $U_1$. It is central, and $A_2\ne A_1$.
3. Let $U_2$ be the set of cities $A_2$ flies to (nonempty), and $A_3\in U_2$ with the largest $\deg^-$ in $U_2$. It is central. $A_3\ne A_2$, and $A_3\ne A_1$ because $A_1\to A_2$, so $A_1\notin U_2$.

So there are always at least three central cities, and the answer is $\boxed{3}$.

### m83
source: mathnet
mathnet_id: 0gpe
country: Turkey
competition: Team Selection Test for IMO 2011
type: answer
difficulty: 8
techniques: graph-theory, double-counting
statement:
Graphistan has $2011$ cities and Graph Air (GA) is running one-way flights between all pairs of these cities (for each pair, exactly one direction). Determine the maximum possible value of the integer $k$ such that no matter how these flights are arranged, it is possible to travel between any two cities in Graphistan riding only GA flights, as long as the absolute value of the difference between the number of flights originating and terminating at any city is not more than $k$.
asked:
Find the largest $k$ such that every orientation of the $2011$-city network in which each city has $|\text{out}-\text{in}|\le k$ lets you get from any city to any other city.
technique:
Counting the flights inside a well-chosen set of cities in two ways forces that set to be large.
hint:
Since out-degree plus in-degree is $2010$, their difference is even. Translate $|\text{out}-\text{in}|\le1005$ into a lower bound on both the out-degree and the in-degree.
hint:
Let $V_1$ be the set of cities reachable from $v_1$. Every flight leaving a city of $V_1$ ends in $V_1$. Count these flights. Do the same for the cities from which $v_2$ can be reached.
hint:
For $k=1006$, split the cities into a group of $1005$ and a group of $1006$, with all flights between the groups going one way, and balance the flights inside each group.
solution:
**Answer:** $k=1005$.

Each city is joined to the $2010$ others, so $\text{out}(v)+\text{in}(v)=2010$ and $\text{out}(v)-\text{in}(v)=2010-2\,\text{in}(v)$ is even.

**$k=1005$ works.** Since the difference is even, $|\text{out}(v)-\text{in}(v)|\le1005$ means $|2010-2\,\text{in}(v)|\le1004$, i.e. $503\le\text{in}(v)\le1507$, and then also $\text{out}(v)=2010-\text{in}(v)\ge503$. So every city has at least $503$ departing and at least $503$ arriving flights.

Fix cities $v_1\ne v_2$. Let $V_1$ be the set of cities reachable from $v_1$ (including $v_1$). Every flight leaving a city of $V_1$ ends in $V_1$, otherwise its endpoint would be reachable too. So the flights leaving cities of $V_1$ are exactly the flights between two cities of $V_1$, and counting them in two ways,
$$503\,|V_1|\le\sum_{v\in V_1}\text{out}(v)=\binom{|V_1|}2,$$
hence $|V_1|-1\ge1006$, i.e. $|V_1|\ge1007$.

Similarly let $V_2$ be the set of cities from which $v_2$ can be reached (including $v_2$). Every flight arriving at a city of $V_2$ starts in $V_2$, so $503|V_2|\le\sum_{v\in V_2}\text{in}(v)=\binom{|V_2|}2$, and $|V_2|\ge1007$.

As $1007+1007>2011$, there is a city $w\in V_1\cap V_2$, and we can travel $v_1\to\dots\to w\to\dots\to v_2$.

**$k=1006$ fails.** Split the cities into $X=\{x_0,\dots,x_{1004}\}$ and $Y=\{y_0,\dots,y_{1005}\}$, with indices taken modulo $1005$ and $1006$ respectively.
- Inside $X$: $x_i\to x_{i+d}$ for $d=1,\dots,502$. Since $1005=2\cdot502+1$, every pair is covered exactly once, and each $x_i$ has $502$ departures and $502$ arrivals inside $X$.
- Inside $Y$: $y_i\to y_{i+d}$ for $d=1,\dots,502$, and for the $503$ "opposite" pairs $\{y_i,y_{i+503}\}$ with $0\le i\le502$, fly $y_i\to y_{i+503}$. Every pair is covered exactly once. Inside $Y$, $y_0,\dots,y_{502}$ have $503$ departures and $502$ arrivals, and the others $502$ departures and $503$ arrivals.
- Every flight between $X$ and $Y$ goes from $X$ to $Y$.

Then each $x_i$ has $502+1006=1508$ departures and $502$ arrivals, difference $1006$. Each $y_j$ has $503$ or $502$ departures and $1005+502$ or $1005+503$ arrivals, difference $1004$ or $1006$. So every difference is at most $1006$, but no city of $X$ can be reached from $Y$.

Hence the maximum is $\boxed{1005}$.

### m84
source: mathnet
mathnet_id: 0j02
country: United States
competition: USAMO 2010
type: proof
difficulty: 8
techniques: invariants, induction
statement:
There are $n$ students standing in a circle, one behind the other, all facing the same way around the circle. The students have heights $h_1<h_2<\dots<h_n$. If a student with height $h_k$ is standing directly behind a student with height $h_{k-2}$ or less, the two students are permitted to switch places. Prove that it is not possible to make more than $\binom n3$ such switches before reaching a position in which no further switches are possible.
asked:
A switch lets a student move forward past the student directly ahead, provided that student is at least two places lower in the height order. Show that every sequence of switches has length at most $\binom n3$.
technique:
Find a property of the arrangement of a few students that a single switch can change only in restricted ways.
hint:
Call the students $1,\dots,n$ by height rank. Two students whose ranks differ by $1$ never switch. For $i<j$ let $s(i,j)$ be the number of switches between $i$ and $j$; aim for $s(i,j)\le j-i-1$.
hint:
Look at the cyclic order (clockwise or counterclockwise) of the three students $i$, $j-1$, $j$. Which switches can reverse it?
hint:
Just before every switch of $i$ and $j$, student $j$ is directly behind $i$, so the cyclic order of $i,j-1,j$ is the same each time. Deduce that a switch of $i$ with $j-1$ must happen between two switches of $i$ with $j$.
solution:
Refer to the student of height $h_k$ as student $k$. Say "$a$ is directly behind $b$" when $b$ is the next student in the facing direction. A switch between students $j$ and $i$ (with $j\ge i+2$) happens when $j$ is directly behind $i$, and afterwards $i$ is directly behind $j$.

**Orientation of a triple.** For three students $a,b,c$, walk around the circle in the facing direction starting at $a$. Either $b$ comes before $c$ or after it; call this the orientation of the ordered triple $(a,b,c)$. A switch exchanges two neighbours $p,q$ and changes no other position. If the triple contains at most one of $p,q$, its orientation does not change, because that student only moves past a student outside the triple. If the triple contains both $p$ and $q$, its orientation is reversed: seen from the third member, $p$ and $q$ are met in the opposite order after the switch.

**Claim.** For $1\le i<j\le n$, students $i$ and $j$ switch at most $j-i-1$ times in total.

We use induction on $j-i$. If $j=i+1$ they never switch, since a switch requires height ranks at least $2$ apart. Let $j\ge i+2$ and look at the triple $(j,i,j-1)$. Just before any switch of $i$ and $j$, student $j$ is directly behind $i$, so walking forward from $j$ we meet $i$ immediately and $j-1$ later. Thus at the moment just before every $(i,j)$-switch the triple $(j,i,j-1)$ has the same orientation, and the switch itself reverses it. So between two consecutive $(i,j)$-switches the orientation must be reversed again by another switch involving two members of the triple. Students $j-1$ and $j$ never switch. So that switch is between $i$ and $j-1$.

Hence between any two consecutive switches of $i$ and $j$ there is at least one switch of $i$ and $j-1$, which gives $s(i,j)\le s(i,j-1)+1$. By the induction hypothesis $s(i,j-1)\le j-i-2$, so $s(i,j)\le j-i-1$.

**Total.** Every switch is between two students, so the total number of switches is at most
$$\sum_{1\le i<j\le n}(j-i-1).$$
The term $j-i-1$ is the number of $l$ with $i<l<j$, so the sum counts the triples $i<l<j$, and it equals $\binom n3$. $\blacksquare$

### m85
source: mathnet
mathnet_id: 06se
country: IMO
competition: International Mathematical Olympiad Shortlisted Problems
type: answer
difficulty: 8
techniques: constructive, extremal
statement:
In the plane, $2013$ red points and $2014$ blue points are marked so that no three of the marked points are collinear. One needs to draw $k$ lines not passing through the marked points and dividing the plane into several regions. The goal is to do it in such a way that no region contains points of both colours. Find the minimal value of $k$ such that the goal is attainable for every possible configuration of $4027$ points.
asked:
Find the least $k$ such that, whatever the positions of the points (no three collinear), some $k$ lines avoiding the points leave no region with both a red and a blue point.
technique:
Two parts: a configuration that forces many lines, and an explicit recipe that works for every configuration.
hint:
For the lower bound, put the points on a circle with the colours alternating. How many sides of the resulting polygon join points of different colours, and how many of these sides can one line cross?
hint:
For any two points $A,B$ of the same colour, two lines parallel to $AB$, very close to it on either side, cut out a strip containing no marked point except $A$ and $B$.
hint:
Pairing uses two lines per pair, so one point of an odd colour class is left over. Look at the convex hull of all the points: either it has a red vertex, or two neighbouring blue vertices.
solution:
**Answer:** $k=2013$.

Two points lie in the same region exactly when no line has them on opposite sides, and a line has two points on opposite sides exactly when it crosses the segment joining them. So the goal is that every red point and every blue point are separated by at least one line.

**At least $2013$ lines may be needed.** Place the $4027$ points on a circle so that the colours alternate as much as possible: going around, red and blue alternate except for one place where two blue points are neighbours. The convex $4027$-gon with these vertices has $4026$ sides joining points of different colours. The two ends of such a side must be separated, so each such side must be crossed by some line. A line meets the boundary of a convex polygon in at most two points, so it crosses at most two sides. Hence at least $4026/2=2013$ lines are needed.

**$2013$ lines always suffice.**

*Strip lemma.* For two marked points $A,B$ there are two lines, not through marked points, such that the open strip between them contains $A$ and $B$ and no other marked point. Indeed, no other marked point lies on line $AB$, so the smallest distance $\delta$ from another marked point to line $AB$ is positive. Take the two lines parallel to $AB$ at distance $\delta/2$ on either side.

*Cutting off a hull vertex.* If $P$ is a vertex of the convex hull of all marked points, there is a line through $P$ with all other marked points strictly on one side. Moving it slightly towards them gives a line, through no marked point, with only $P$ on one side.

Now take the convex hull of all $4027$ points. They are not all collinear, so the hull is a polygon with at least three vertices.

*Case 1: some hull vertex $R$ is red.* Draw one line cutting off $R$ alone. Split the other $2012$ red points into $1006$ pairs and draw the two strip lines for each pair. That is $1+2\cdot1006=2013$ lines.

*Case 2: all hull vertices are blue.* Take two adjacent hull vertices $B_1,B_2$. All other points lie strictly on one side of line $B_1B_2$ (no three collinear), so a line parallel to $B_1B_2$ and close enough to it has only $B_1,B_2$ on one side. Split the other $2012$ blue points into $1006$ pairs and draw two strip lines for each pair. Again $2013$ lines.

*Why this works.* In Case 1, take a red point $X$ and a blue point $Y$. If $X=R$, the first line separates them. Otherwise $X$ lies in the strip of its pair, which contains no other marked point, so $Y$ is outside the strip and one of the two strip lines separates $X$ from $Y$. Case 2 is the same with the colours exchanged: the blue points $B_1,B_2$ are cut off from all red points by the first line, and every other blue point sits in a strip with no red point. So no region contains two colours.

Therefore the minimal $k$ is $\boxed{2013}$.

### m86
source: mathnet
mathnet_id: 06x0
country: IMO
competition: International Mathematical Olympiad
type: answer
difficulty: 7
techniques: invariants, constructive
statement:
Let $n$ be a positive integer. We start with $n$ piles of pebbles, each initially containing a single pebble. One can perform moves of the following form: choose two piles, take an equal number of pebbles from each pile and form a new pile out of these pebbles. For each positive integer $n$, find the smallest number of non-empty piles that one can obtain by performing a finite sequence of moves of this form.
asked:
A move takes $c\ge1$ pebbles from each of two piles and puts these $2c$ pebbles into a new pile. Starting from $n$ single pebbles, find the fewest non-empty piles that can be reached.
technique:
Small cases suggest the answer. For impossibility, look for a property of the whole configuration that moves can never create.
hint:
If $n$ is a power of $2$, one pile is reachable by merging equal piles repeatedly.
hint:
Let $m$ be an odd divisor of $n$ greater than $1$. Show that if every pile is divisible by $m$ after a move, then every pile was divisible by $m$ before it. Run this backwards from a single pile.
hint:
For two piles when $2^N<n<2^{N+1}$: make a pile of $2^N$, then use it and pairs of pebbles to bring it down to $n-2^N$ while the removed pebbles regroup into another power of $2$.
solution:
**Answer:** $1$ if $n$ is a power of $2$, and $2$ otherwise.

The total number of pebbles never changes, so at least one non-empty pile always remains.

**Powers of $2$.** From $2^N$ piles of size $2^j$, a move on two of them (with $c=2^j$) empties both and creates a pile of $2^{j+1}$. So $2^N$ single pebbles become $2^{N-1}$ piles of $2$, then $2^{N-2}$ piles of $4$, and so on, down to one pile of $2^N$. Hence for $n=2^N$ the answer is $1$.

**One pile is impossible otherwise.** Suppose $n$ is not a power of $2$, and let $m>1$ be an odd divisor of $n$. A move changes piles of sizes $a,b$ into $a-c,\ b-c$ and adds a pile $2c$ (a pile of size $0$ disappears; we may treat it as size $0$). Suppose every pile after the move is divisible by $m$. Then $m\mid2c$, and since $m$ is odd, $m\mid c$. Hence $m\mid(a-c)+c=a$ and $m\mid b$, and the untouched piles did not change. So every pile before the move was divisible by $m$ as well.

If some sequence of moves ended with a single pile, that pile would have $n$ pebbles, divisible by $m$. Going backwards move by move, every earlier position would have all piles divisible by $m$, including the start, where all piles are $1$. This is false, so one pile cannot be reached.

**Two piles are reachable.** Let $2^N<n<2^{N+1}$ (so $N\ge1$) and $r=n-2^N$, with $1\le r\le2^N-1$.
1. Using $2^N$ of the single pebbles, build one pile $L$ of $2^N$ pebbles as above. There remain $r$ single pebbles.
2. Take $1$ pebble from $L$ and $1$ from a single pebble: now $L=2^N-1$, there is one pile of $2$, and $r-1$ single pebbles.
3. Repeat: take $1$ from $L$ and $1$ from the current pile of $2$, forming a new pile of $2$. Each repetition decreases $L$ by $1$ and turns the old pile of $2$ into a single pebble. Do this $2^N-1-r\ge0$ times. Then $L=r$, there is one pile of $2$, and $(r-1)+(2^N-1-r)=2^N-2$ single pebbles.
4. Pair the $2^N-2$ single pebbles into $2^{N-1}-1$ piles of $2$. Together with the existing pile of $2$, we have $2^{N-1}$ piles of $2$, which merge into one pile of $2^N$.

We end with exactly two piles, of sizes $r$ and $2^N$.

So the minimum is $\boxed{1}$ when $n$ is a power of $2$ and $\boxed{2}$ otherwise.

### m87
source: mathnet
mathnet_id: 03u9
country: China
competition: International Mathematical Olympiad
type: proof
difficulty: 9
techniques: descent, modular-arithmetic
statement:
Let $a$ and $b$ be positive integers. Show that if $4ab-1$ divides $(4a^2-1)^2$, then $a=b$.
asked:
Prove that the divisibility $4ab-1\mid(4a^2-1)^2$ for positive integers $a,b$ forces $a=b$.
technique:
Rewrite the divisibility in a more symmetric form; then a smallest counterexample can be made smaller.
hint:
Work modulo $4ab-1$, where $4ab\equiv1$. Multiply $(4a^2-1)$ by $b$ and simplify. Show the condition is equivalent to $4ab-1\mid(a-b)^2$.
hint:
Write $(a-b)^2=k(4ab-1)$ with $k\ge1$ and view it as a quadratic equation in $a$ with $b,k$ fixed. Among all solutions with $a\ne b$ for this $k$, take one with $a+b$ smallest, $a>b$.
hint:
The other root is $a'=(b^2+k)/a$. Show that it is a positive integer, that $a'\ne b$, and that $a'<a$.
solution:
**Step 1: a symmetric form.** Let $N=4ab-1$. Then $\gcd(b,N)=1$, since a common divisor of $b$ and $4ab-1$ divides $1$. Modulo $N$ we have $4ab\equiv1$, so
$$b(4a^2-1)=a\cdot4ab-b\equiv a-b\pmod N,$$
hence $b^2(4a^2-1)^2\equiv(a-b)^2\pmod N$. As $\gcd(b^2,N)=1$, we get
$$N\mid(4a^2-1)^2\iff N\mid(a-b)^2.$$
The right-hand condition is symmetric in $a$ and $b$.

**Step 2: descent.** Suppose there are positive integers $a\ne b$ with $4ab-1\mid(a-b)^2$. Then $(a-b)^2=k(4ab-1)$ for a positive integer $k$ (positive since $a\ne b$). Fix this $k$ and, among all pairs of distinct positive integers $(a,b)$ satisfying
$$(a-b)^2=k(4ab-1),\qquad(\ast)$$
choose one with $a+b$ as small as possible. By symmetry of $(\ast)$ we may assume $a>b$.

Expanding, $(\ast)$ reads
$$a^2-(2b+4kb)\,a+(b^2+k)=0.$$
So $a$ is a root of $x^2-(2b+4kb)x+(b^2+k)$. The other root is
$$a'=(2b+4kb)-a=\frac{b^2+k}{a}.$$
The first expression shows $a'$ is an integer, and the second shows $a'>0$. The pair $(a',b)$ also satisfies $(\ast)$, since it is the same equation with $a$ replaced by the other root.

- $a'\ne b$: otherwise $(\ast)$ for $(a',b)$ would give $0=k(4b^2-1)>0$.
- $a'<a$: this is equivalent to $b^2+k<a^2$. From $(\ast)$, $k=\dfrac{(a-b)^2}{4ab-1}$. Since $a>b\ge1$, we have $4ab-1\ge4a-1>a-b$, so $k<\dfrac{(a-b)^2}{a-b}=a-b\le a^2-b^2$, i.e. $b^2+k<a^2$.

Thus $(a',b)$ is a pair of distinct positive integers satisfying $(\ast)$ with $a'+b<a+b$, contradicting the minimality. Hence no such pair exists.

So $4ab-1\mid(a-b)^2$ forces $a=b$, and by Step 1 so does $4ab-1\mid(4a^2-1)^2$. $\blacksquare$

### m88
source: mathnet
mathnet_id: 0ix6
country: United States
competition: Team Selection Test 2009
type: answer
difficulty: 9
techniques: descent, modular-arithmetic
statement:
Find all pairs of positive integers $(m,n)$ such that $mn-1$ divides $(n^2-n+1)^2$.
asked:
Determine every pair of positive integers $m,n$ for which $(n^2-n+1)^2$ is a multiple of $mn-1$.
technique:
Rewrite the divisibility in a more symmetric form; then solutions can be shrunk until they reach a few small ones.
hint:
Modulo $mn-1$, multiply $n^2-n+1$ by $m$. Show that the condition is equivalent to $mn-1\mid(m+n-1)^2$.
hint:
Write $(m+n-1)^2=k(mn-1)$. Show $k\ge3$, with $k=3$ only for $m=n=2$. With $n$ and $k$ fixed this is a quadratic in $m$; let $m'$ be its other root.
hint:
If $m\ge n\ge2$ and $m'\ge n$, expand $(m-n)(m'-n)\ge0$ using Vieta's formulas to get $k\le3$. So otherwise $(n,m')$ is a smaller solution. Find where the descent stops, and climb back up.
solution:
**Answer:** $(m,n)=(2,2)$, and the pairs with $\{m,n\}=\{t^2+1,\,(t+1)^2+1\}$ for an integer $t\ge0$ (that is, $(1,2),(2,1),(2,5),(5,2),(5,10),(10,5),\dots$).

Note $(1,1)$ is not a solution ($0$ divides nothing nonzero), so $mn-1\ge1$ below.

**Step 1: symmetric form.** Since $\gcd(m,mn-1)=1$ and $mn\equiv1\pmod{mn-1}$,
$$m(n^2-n+1)=mn\cdot n-mn+m\equiv n-1+m\pmod{mn-1}.$$
So $m^2(n^2-n+1)^2\equiv(m+n-1)^2$, and as $m^2$ is coprime to $mn-1$,
$$mn-1\mid(n^2-n+1)^2\iff mn-1\mid(m+n-1)^2.$$
So we must find all $(m,n)\ne(1,1)$ with
$$(m+n-1)^2=k(mn-1)\qquad(\ast)$$
for a positive integer $k$. This condition is symmetric in $m,n$.

**Step 2: $k\ge3$, with equality only at $(2,2)$.** With $s=m+n$,
$$(m+n-1)^2-3(mn-1)=m^2-mn+n^2-2s+4\ge\frac{s^2}4-2s+4=\Big(\frac s2-2\Big)^2\ge0,$$
using $m^2-mn+n^2=\frac{(m+n)^2+3(m-n)^2}4\ge\frac{s^2}4$. So $k\ge3$, and $k=3$ forces $m=n$ and $s=4$, i.e. $(m,n)=(2,2)$. Indeed $(2,2)$ works: $3\mid9$.

**Step 3: the jump.** Fix a solution $(m,n)$ of $(\ast)$ with quotient $k$. As an equation in $m$, $(\ast)$ reads
$$m^2-(kn-2n+2)\,m+(n-1)^2+k=0.$$
Its other root is $m'=kn-2n+2-m=\dfrac{(n-1)^2+k}{m}$, a positive integer, and $(m',n)$ satisfies $(\ast)$ with the same $k$.

*Claim.* If $m\ge n\ge2$ and $(m,n)\ne(2,2)$, then $m'<n$.

Suppose instead $m'\ge n$. Then $(m-n)(m'-n)\ge0$, i.e. $mm'-n(m+m')+n^2\ge0$. By Vieta's formulas this is
$$(n-1)^2+k-n(kn-2n+2)+n^2\ge0\iff(2n-1)^2\ge k(n^2-1).$$
For $n\ge2$ we have $(2n-1)^2<4(n^2-1)$, so $k<4$ and therefore $k=3$. By Step 2, $(m,n)=(2,2)$, a contradiction.

**Step 4: the case $n=1$.** If $n=1$ then $(\ast)$ is $m^2=k(m-1)$ with $m\ge2$, so $m-1\mid m^2\equiv1\pmod{m-1}$, hence $m=2$, giving $(2,1)$ (with $k=4$).

**Step 5: all solutions.** We show by strong induction on $m+n$ that every solution other than $(2,2)$ has $\{m,n\}=\{t^2+1,(t+1)^2+1\}$ for some $t\ge0$. By symmetry let $m\ge n$. If $n=1$, Step 4 gives $(2,1)$, which is the case $t=0$. Let $n\ge2$ and $(m,n)\ne(2,2)$. By the claim, $(n,m')$ is a solution with $m'<n\le m$, so it has a smaller sum.

It is not $(2,2)$: then its quotient would be $3$, so $(m,n)$ would also have $k=3$ and be $(2,2)$ by Step 2. Hence by induction $\{n,m'\}=\{t^2+1,(t+1)^2+1\}$, and these pairs have $k=4$, because
$$(t^2+1)\big((t+1)^2+1\big)-1=(t^2+t+1)^2\quad\text{and}\quad t^2+1+(t+1)^2+1-1=2(t^2+t+1).$$
So $k=4$ for $(m,n)$ too. Since $n>m'$, $n=(t+1)^2+1$, so write $n=v^2+1$ with $v=t+1\ge1$. For $k=4$ the quadratic in Step 3 is
$$x^2-(2v^2+4)x+v^4+4=0,$$
whose roots are $v^2+2\pm2v$, i.e. $(v-1)^2+1$ and $(v+1)^2+1$. The numbers $m$ and $m'$ are the two roots, so $m$ is $(v-1)^2+1$ or $(v+1)^2+1$, and $\{m,n\}$ is again of the form $\{u^2+1,(u+1)^2+1\}$. This completes the induction.

**Check.** The identity above shows $(m+n-1)^2=4(mn-1)$ for $\{m,n\}=\{t^2+1,(t+1)^2+1\}$, so these pairs satisfy $(\ast)$, and $(2,2)$ does as well. By Step 1 they are exactly the solutions:
$$\boxed{(m,n)=(2,2)\ \text{ or }\ \{m,n\}=\{t^2+1,\,(t+1)^2+1\},\ t\ge0.}$$

### m89
source: mathnet
mathnet_id: 0d33
country: Saudi Arabia
competition: Selection tests for the International Mathematical Olympiad 2013
type: answer
difficulty: 7
techniques: constructive
statement:
Determine if there exists an infinite sequence of positive integers $a_1,a_2,a_3,\ldots$ such that
(i) each positive integer occurs exactly once in the sequence, and
(ii) each positive integer occurs exactly once in the sequence $|a_1-a_2|,\ |a_2-a_3|,\ \ldots,\ |a_k-a_{k+1}|,\ \ldots$
asked:
Decide whether the positive integers can be listed, each exactly once, so that the gaps between consecutive terms also list every positive integer exactly once.
technique:
Build the sequence step by step, keeping both lists free of repeats, and make sure every number eventually gets its turn. Very large terms give you room.
hint:
Keep a finite sequence with distinct terms and distinct gaps. Let $M$ be its largest term; every gap so far is at most $M-1$.
hint:
To add the smallest missing term $x$, first append a huge number and then $x$. To add the smallest missing gap $y$, append a huge number $A$ and then $A+y$. Check that no repeats arise.
hint:
Alternate the two kinds of extension. Why does every positive integer eventually appear in both lists?
solution:
**Answer:** yes, such a sequence exists.

We build it in stages. At every stage we have a finite sequence $a_1,\dots,a_N$ of distinct positive integers whose gaps $|a_i-a_{i+1}|$ ($1\le i<N$) are also distinct. Let $M$ be its largest term. All terms lie in $[1,M]$, so every gap is at most $M-1$. Start with the one-term sequence $a_1=1$.

**Extension V (adds a missing term).** Let $x$ be the smallest positive integer that is not a term; then $x\le M+1$. Put $A=2M+2$ and append $A$, then $x$. The two new terms are new: $A>M$, $x$ was missing, and $x\le M+1<A$. The two new gaps are $A-a_N\ge A-M=M+2$ and $A-x\ge2M+2-(M+1)=M+1$. Both exceed every old gap (which are $\le M-1$), and they differ from each other because $a_N\ne x$.

**Extension D (adds a missing gap).** Let $y$ be the smallest positive integer that is not a gap. Since $M$ is not a gap, $y\le M$. Put $A=2M+2$ and append $A$, then $A+y$. The new terms $A<A+y$ both exceed $M$, so they are new. The new gaps are $A-a_N\ge M+2$ and $y$. The first exceeds all old gaps, $y$ is not an old gap by choice, and $y\le M<A-a_N$.

In both cases the extended sequence again has distinct terms and distinct gaps. Now alternate: V, D, V, D, … forever. This defines an infinite sequence in which no term and no gap repeats (any repeat would already show up in some finite stage).

**Every number appears.** Let $x_r$ be the smallest missing term before the $r$-th application of V. That application adds $x_r$, and terms are never removed, so $x_{r+1}>x_r$. A strictly increasing sequence of positive integers is unbounded, so for every positive integer $v$ some $x_r>v$, which means $v$ is a term by then. In the same way the smallest missing gaps $y_r$ before the applications of D strictly increase, so every positive integer becomes a gap.

So both (i) and (ii) hold, and the answer is $\boxed{\text{yes}}$.
