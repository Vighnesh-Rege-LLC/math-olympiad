### m25
source: mathnet
mathnet_id: 0gs6
country: Turkey
competition: Team Selection Test for IMO 2019
type: answer
difficulty: 7
techniques: pigeonhole, divisibility
statement:
Let $n$ be a positive integer with $b$ digits and let $l,r$ be non-negative integers with $l+r<b$. A positive integer is called a sub-divisor of $n$ if it divides the number obtained by erasing the first $l$ and the last $r$ digits of $n$ (for some such $l,r$). For example, the sub-divisors of $143$ are $1,2,3,4,7,11,13,14,43$ and $143$. For a positive integer $d$, let $A_d$ be the set of positive integers for which $d$ is not a sub-divisor. Find all positive integers $d$ for which the set $A_d$ is finite.
asked:
Erasing digits from both ends of $n$ leaves a block of consecutive digits. Find every $d$ such that only finitely many positive integers have no block of consecutive digits divisible by $d$.
technique:
Look at the numbers formed by the last few digits of $n$, and use [[pigeonhole]] on something finite.
hint:
First rule out $d$ divisible by $2$ or $5$: find infinitely many numbers all of whose digit blocks avoid such $d$.
hint:
For $\gcd(d,10)=1$, let $T_i$ be the number formed by the last $i$ digits of $n$. If $n$ has at least $d$ digits, look at $T_1,\dots,T_d$ modulo $d$.
hint:
If $T_i\equiv T_j\pmod d$ with $i>j$, then $T_i-T_j$ is a block of digits followed by $j$ zeros. Why can the zeros be dropped?
solution:
**Answer:** exactly the $d$ with $\gcd(d,10)=1$.

**If $2\mid d$ or $5\mid d$, then $A_d$ is infinite.** Take a repunit $11\ldots1$. Every block of its consecutive digits is again a repunit, which is odd and ends in $1$, so it is divisible by neither $2$ nor $5$, hence not by $d$. So every repunit lies in $A_d$.

**If $\gcd(d,10)=1$, then $A_d$ is finite.** We show that every $n$ with at least $d$ digits has $d$ as a sub-divisor. Write $n$ with $b\ge d$ digits and let $T_i$ ($1\le i\le d$) be the number formed by the last $i$ digits of $n$ (leading zeros allowed). $T_i$ is obtained by erasing the first $b-i$ digits, and $(b-i)+0<b$, so if some $T_i$ is divisible by $d$ we are done.

Otherwise the $d$ numbers $T_1,\dots,T_d$ have nonzero remainders mod $d$, and there are only $d-1$ of those, so by pigeonhole $T_i\equiv T_j\pmod d$ for some $i>j$. Now $T_i-T_j=10^j\cdot B$, where $B$ is the number formed by the digits in positions $j+1,\dots,i$ counted from the right. $B$ is obtained by erasing the first $b-i$ and the last $j$ digits, and $(b-i)+j<b$ because $j<i$. Since $d\mid 10^jB$ and $\gcd(d,10)=1$, we get $d\mid B$, so $d$ is a sub-divisor of $n$.

Hence every element of $A_d$ has fewer than $d$ digits, and $A_d$ is finite. (For $d=1$ the set is even empty.) So $A_d$ is finite exactly when $\boxed{\gcd(d,10)=1}$.

### m26
source: mathnet
mathnet_id: 017v
country: Baltic Way
competition: BALTIC WAY
type: proof
difficulty: 7
techniques: double-counting, modular-arithmetic
statement:
The $n\times n$ board is coloured in $n$ colours such that the main diagonal (from top-left to bottom-right) is coloured in the first colour; the two adjacent diagonals are coloured in the second colour; the two next diagonals (one from above and one from below) are coloured in the third colour, etc.; the two corners (top-right and bottom-left) are coloured in the $n$-th colour. It happens that it is possible to place on the board $n$ non-attacking rooks such that no two rooks stand on cells of the same colour. Prove that $n\equiv0$ or $1\pmod4$.
asked:
The cell in row $i$ and column $j$ has colour $|i-j|+1$. If $n$ non-attacking rooks can be placed on cells of $n$ different colours, show that $n$ leaves remainder $0$ or $1$ when divided by $4$.
technique:
Describe the rooks by a permutation and evaluate one sum over the rooks in two different ways ([[double-counting]]); an integrality condition then appears.
hint:
Put the rook of row $k$ in column $f(k)$. Then $f$ is a permutation, and the colours used say exactly which values $|f(k)-k|$ take.
hint:
Compute $\sum_k (f(k)-k)^2$ once from the colours and once by expanding the square.
hint:
You get a formula for $\sum_k k\,f(k)$. This sum is an integer; check for which $n$ the formula is.
solution:
Number rows and columns $1,\dots,n$. The cell $(i,j)$ lies on the diagonal $j-i=\text{const}$, and by the description its colour is $|i-j|+1$.

Non-attacking rooks lie in different rows and columns, so $n$ of them occupy one cell in every row and every column: the rook in row $k$ stands in column $f(k)$, where $f$ is a permutation of $\{1,\dots,n\}$. The $n$ rooks have $n$ different colours among $n$ colours, so the numbers $|f(k)-k|$ ($k=1,\dots,n$) are exactly $0,1,\dots,n-1$ in some order. Therefore
$$\sum_{k=1}^n (f(k)-k)^2=\sum_{i=0}^{n-1}i^2=\frac{(n-1)n(2n-1)}6.$$
On the other hand, since $f$ is a permutation, $\sum f(k)^2=\sum k^2=\frac{n(n+1)(2n+1)}6$, so
$$\sum_{k=1}^n (f(k)-k)^2=\sum f(k)^2+\sum k^2-2\sum k f(k)=\frac{n(n+1)(2n+1)}3-2\sum k f(k).$$
Comparing,
$$\sum_{k=1}^n k f(k)=\frac12\left(\frac{2n(n+1)(2n+1)-(n-1)n(2n-1)}{6}\right)=\frac{n(2n^2+9n+1)}{12}.$$
The left side is an integer, so $4\mid n(2n^2+9n+1)$. Check $n$ modulo $4$:
- $n\equiv2$: $n(2n^2+9n+1)\equiv2\,(8+18+1)=54\equiv2\pmod4$;
- $n\equiv3$: $n(2n^2+9n+1)\equiv3\,(18+27+1)=138\equiv2\pmod4$.

Both are impossible, so $n\equiv0$ or $1\pmod4$. $\blacksquare$

### m27
source: mathnet
mathnet_id: 013f
country: Baltic Way
competition: Baltic Way
type: answer
difficulty: 6
techniques: invariants
statement:
A circle is divided into $13$ segments, numbered consecutively from $1$ to $13$. Five fleas called $A,B,C,D$ and $E$ are sitting in the segments $1,2,3,4$ and $5$. A flea is allowed to jump to an empty segment five positions away in either direction around the circle. Only one flea jumps at the same time, and two fleas cannot be in the same segment. After some jumps, the fleas are back in the segments $1,2,3,4,5$, but possibly in some other order than they started. Which orders are possible?
asked:
Determine which fleas can end up in segments $1,2,3,4,5$ (read in this order) after a sequence of legal jumps of length $5$.
technique:
Renumber the segments so that a jump of $5$ becomes a step to a neighbouring segment. Then look for something the jumps cannot change ([[invariants]]).
hint:
Since $5$ is invertible modulo $13$, list the segments in the order $1,6,11,3,8,13,\dots$ (adding $5$ each time). On this new circle, where does a jump take a flea?
hint:
On the new circle a flea can only step to an adjacent empty place, so it can never pass another flea. What is preserved?
hint:
Find where segments $1,\dots,5$ sit on the new circle and read off which arrangements keep the cyclic order. Then check that every such arrangement really occurs.
solution:
**Answer:** exactly the five cyclic shifts $\boxed{ABCDE,\ BCDEA,\ CDEAB,\ DEABC,\ EABCD}$ (listing the fleas in segments $1,2,3,4,5$).

**New circle.** Give segment $s$ the label $t\in\{0,1,\dots,12\}$ with $s\equiv1+5t\pmod{13}$. Since $5$ is invertible mod $13$, this is a bijection. In order $t=0,1,\dots,12$ the segments are
$$1,6,11,3,8,13,5,10,2,7,12,4,9.$$
A jump of $5$ segments changes $t$ by $\pm1$ modulo $13$. So, placing the segments on a circle in this order, every jump moves a flea to an adjacent empty place.

**Invariant.** A flea moving to an adjacent empty place does not pass any other flea, so the cyclic order of the five fleas on the new circle never changes. Initially the fleas are at $A:t=0$, $B:t=8$, $C:t=3$, $D:t=11$, $E:t=6$; in increasing $t$ the cyclic order is $A,C,E,B,D$. At the end the fleas again occupy the places $t=0,3,6,8,11$, which are segments $1,3,5,2,4$. Reading these places in increasing $t$ we must see a rotation of $(A,C,E,B,D)$. The five rotations give (segments $1,3,5,2,4$ get the five letters):
- $(A,C,E,B,D)$: segments $1..5$ hold $ABCDE$;
- $(C,E,B,D,A)$: $CDEAB$;
- $(E,B,D,A,C)$: $EABCD$;
- $(B,D,A,C,E)$: $BCDEA$;
- $(D,A,C,E,B)$: $DEABC$.

So only the five cyclic shifts of $ABCDE$ are possible.

**All five occur.** In the $t$-labels, the following steps each go to an adjacent empty place: $A:0\to1\to2$; $D:11\to12\to0$; $B:8\to9\to10$; $E:6\to7\to8$; $B:10\to11$; $C:3\to4\to5\to6$; $A:2\to3$. Afterwards $D,A,C,E,B$ sit at $t=0,3,6,8,11$, i.e. the order is $DEABC$. The occupied places are the same as at the start, so the same sequence of moves (applied to whichever fleas stand on those places) is legal again, and each time it shifts the order by the same rotation. Repeating it gives $ABCDE\to DEABC\to BCDEA\to EABCD\to CDEAB$, so all five cyclic shifts are reachable.

### m28
source: mathnet
mathnet_id: 0113
country: Baltic Way
competition: Baltic Way
type: answer
difficulty: 5
techniques: invariants, parity
statement:
Two squares on an $8\times8$ chessboard are called adjacent if they have a common edge or common corner. Is it possible for a king to begin in some square and visit all squares exactly once in such a way that all moves except the first are made into squares adjacent to an even number of squares already visited?
asked:
A king tours all $64$ squares once. After the first move, each move must enter a square that touches an even number of squares visited earlier. Decide whether such a tour exists.
technique:
Track a count that changes in a controlled way with every move, and compare its parity at the end with a fixed number ([[invariants]], [[parity]]).
hint:
Count unordered pairs of adjacent squares whose two squares have both been visited.
hint:
How much does this count grow on the first move, and how much on each later move?
hint:
At the end of a full tour, the count equals the total number of adjacent pairs on the board. Compute that number.
solution:
**Answer: No.**

Call an unordered pair of adjacent squares *done* if both squares have been visited. At the start only one square is visited, so there are $0$ done pairs.

When the king enters a new square $X$, the new done pairs are exactly the pairs $\{X,Y\}$ with $Y$ adjacent to $X$ and already visited. On the first move the only visited square is the starting one, which is adjacent to $X$, so the count becomes $1$. On every later move, by the rule, $X$ is adjacent to an even number of visited squares, so the count grows by an even number. Hence after every move the number of done pairs is odd.

If a full tour existed, at the end all squares would be visited and every adjacent pair would be done. The number of adjacent pairs on an $8\times8$ board is
$$\underbrace{8\cdot7}_{\text{horizontal}}+\underbrace{8\cdot7}_{\text{vertical}}+\underbrace{2\cdot7\cdot7}_{\text{diagonal}}=56+56+98=210,$$
which is even. This contradicts the oddness, so no such tour exists: the answer is $\boxed{\text{No}}$.

### m29
source: mathnet
mathnet_id: 07du
country: Iran
competition: Iranian Mathematical Olympiad
type: proof
difficulty: 7
techniques: parity, invariants
statement:
$100$ points lie on a circle and they are labeled by $1,2,\dots,100$ in an arbitrary order. A triangle with vertices among these points is called clockwise if, when its vertices are visited in increasing order of their labels, the motion is clockwise. Prove that it is not possible to have exactly $2017$ clockwise triangles.
asked:
For any labeling of $100$ points on a circle by $1,\dots,100$, show that the number of clockwise triangles cannot be $2017$.
technique:
Change the labeling by small steps that are easy to analyse, follow the [[parity]] of the count through each step, and end at a labeling where the count is obvious.
hint:
Swap the labels of two points that are neighbours on the circle. Which triangles can change orientation?
hint:
Only triangles containing both swapped points change, and each of them reverses. How many such triangles are there?
hint:
Any labeling can be turned into any other by swapping the labels of two neighbouring points, repeatedly. Choose a target labeling with no clockwise triangles.
solution:
**Effect of one swap.** Let $P,Q$ be two points that are neighbours on the circle (no other point between them on one of the arcs), and swap their labels. Consider a set of three labels.
- If it contains neither swapped label, nothing changes.
- If it contains exactly one of them, that label moves from one of $P,Q$ to the other. No point lies between $P$ and $Q$, so the cyclic order of the three positions is unchanged and so is the orientation.
- If it contains both swapped labels and a third label at a point $R$, then the two swapped labels exchange positions while $R$ stays. Exchanging two of three points in a cyclic order reverses the orientation, so a clockwise triangle becomes counterclockwise and vice versa.

There are $98$ triangles of the last type. If $a$ of them were clockwise before the swap, then $98-a$ are clockwise after it. So the number of clockwise triangles changes by $(98-a)-a=98-2a$, an even number. **The parity of the number of clockwise triangles is invariant under swapping the labels of two neighbouring points.**

**Reaching a reference labeling.** Number the positions $1,\dots,100$ counterclockwise around the circle. Swapping labels at positions $i$ and $i+1$ is a swap of neighbours, and such adjacent transpositions can turn any arrangement of labels into any other (as in bubble sort). Move to the labeling where label $j$ sits at position $j$. In it, for any labels $i<j<k$ the positions $i,j,k$ are visited counterclockwise, so there are $0$ clockwise triangles.

Hence for every labeling the number of clockwise triangles is even, and in particular it is never $2017$. $\blacksquare$

### m30
source: mathnet
mathnet_id: 0761
country: India
competition: INMO
type: proof
difficulty: 6
techniques: parity
statement:
Let $n$ be a positive integer. Call a nonempty subset $S$ of $\{1,2,\dots,n\}$ good if the arithmetic mean of the elements of $S$ is also an integer. Further let $t_n$ denote the number of good subsets of $\{1,2,\dots,n\}$. Prove that $t_n$ and $n$ are both odd or both even.
asked:
Show that the number of nonempty subsets of $\{1,\dots,n\}$ with integer mean has the same parity as $n$.
technique:
To show that a count is even, split the objects into pairs. Here look for a natural way to pair up good subsets so that only a few are left unpaired ([[parity]]).
hint:
The $n$ one-element subsets are all good. Show that the remaining good subsets come in pairs.
hint:
For a good set $S$ with mean $m$, what happens to the mean if you add $m$ to $S$, or remove it?
hint:
Check that toggling the mean is an involution on good sets with at least two elements, with no fixed points.
solution:
The $n$ singletons $\{1\},\dots,\{n\}$ are good. Let $\mathcal G$ be the family of good subsets with at least two elements; we show $|\mathcal G|$ is even, which gives $t_n=n+|\mathcal G|\equiv n\pmod2$.

For $S\in\mathcal G$ with mean $m$ (an integer between $\min S$ and $\max S$, so $m\in\{1,\dots,n\}$), define $\phi(S)=S\triangle\{m\}$: remove $m$ if $m\in S$, add it otherwise.

- If $m\notin S$: $S\cup\{m\}$ has sum $m|S|+m=m(|S|+1)$, so its mean is $m$; it has at least $3$ elements.
- If $m\in S$: $S\setminus\{m\}$ has sum $m|S|-m=m(|S|-1)$ and $|S|-1\ge1$ elements, so its mean is $m$. It cannot be a singleton $\{x\}$, since then its mean would be $x\ne m$. So it has at least two elements.

In both cases $\phi(S)\in\mathcal G$ with the same mean $m$, hence $\phi(\phi(S))=S$. Also $\phi(S)\ne S$. So $\phi$ splits $\mathcal G$ into pairs $\{S,\phi(S)\}$, and $|\mathcal G|$ is even. Therefore $t_n\equiv n\pmod 2$. $\blacksquare$

### m31
source: mathnet
mathnet_id: 0382
country: Bulgaria
competition: Team selection test for 23. BMO
type: proof
difficulty: 8
techniques: induction, graph-theory
statement:
After a volleyball tournament (every two teams played exactly once) with $n$ teams it turned out that for any two teams $A$ and $B$ such that $B$ wins over $A$, there exist a positive integer $t$ and teams $C_1,C_2,\dots,C_t$ such that $A$ wins over $C_1$, $C_1$ wins over $C_2$, $\dots$, $C_t$ wins over $B$. Prove that for any $k=3,4,\dots,n$ there exist $k$ teams $A_1,A_2,\dots,A_k$ such that $A_1$ wins over $A_2$, $A_2$ wins over $A_3$, $\dots$, $A_{k-1}$ wins over $A_k$ and $A_k$ wins over $A_1$.
asked:
In a tournament where every team can reach every other team along a chain of wins, show that there are cycles of wins of every length from $3$ up to $n$.
technique:
Use [[induction]] on the cycle length: from a cycle of length $k<n$, build one of length $k+1$ by looking at how an outside team plays against the cycle. Phrase everything as a directed graph ([[graph-theory]]).
hint:
For $k=3$: take a shortest cycle of wins and show it cannot have length $4$ or more by looking at a chord.
hint:
Given a $k$-cycle and an outside team $U$ that beats some cycle team and loses to another, insert $U$ into the cycle.
hint:
Otherwise every outside team beats the whole cycle or loses to the whole cycle. Use the chain condition to find a team $V$ of the second kind that beats a team $U$ of the first kind.
solution:
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

### m32
source: mathnet
mathnet_id: 06va
country: IMO
competition: IMO 2019 Shortlisted Problems
type: proof
difficulty: 8
techniques: induction, extremal
statement:
You are given a set of $n$ blocks, each weighing at least $1$; their total weight is $2n$. Prove that for every real number $r$ with $0\le r\le2n-2$ you can choose a subset of the blocks whose total weight is at least $r$ but at most $r+2$.
asked:
With $n$ blocks of weight at least $1$ and total $2n$, show that every interval $[r,r+2]$ with $0\le r\le 2n-2$ contains the weight of some sub-collection.
technique:
The statement is awkward to induct on directly. Prove a stronger version by [[induction]] on $n$, removing the heaviest block ([[extremal]]).
hint:
Strengthen: if $n$ blocks of weight at least $1$ have total $s\le2n$, then for every $r\in[-2,s]$ some subset has weight in $[r,r+2]$.
hint:
Remove the heaviest block $x$. The rest satisfy the hypothesis with $n-1$ blocks. Which values of $r$ does the induction hypothesis handle, with and without $x$?
hint:
You cover $[-2,s-x]$ and $[x-2,s]$. Show $x-2\le s-x$ using $x\le s-(n-1)$ and $s\le2n$.
solution:
We prove the stronger **Claim:** if $n\ge1$ blocks each weigh at least $1$ and their total is $s\le2n$, then for every real $r$ with $-2\le r\le s$ some subset (possibly empty) has total weight in $[r,r+2]$.

The problem follows by taking $s=2n$, since $[0,2n-2]\subset[-2,2n]$.

**Base $n=1$.** One block of weight $s$ with $1\le s\le2$. If $-2\le r\le0$, the empty set (weight $0$) works since $r\le0\le r+2$. If $0<r\le s$, the block works since $r\le s\le2<r+2$.

**Step.** Let $n\ge2$ and let $x$ be the largest weight. Then $x\ge s/n$, so the other $n-1$ blocks have total $s-x\le s\frac{n-1}n\le2(n-1)$, and each weighs at least $1$. By the induction hypothesis:
- for every $r\in[-2,s-x]$ some subset of the other blocks has weight in $[r,r+2]$;
- for every $r\in[x-2,s]$ we have $r-x\in[-2,s-x]$, so some subset $T$ of the other blocks has weight in $[r-x,r-x+2]$, and $T$ together with the heavy block has weight in $[r,r+2]$.

These two intervals cover $[-2,s]$ provided $x-2\le s-x$, i.e. $2x\le s+2$. The other $n-1$ blocks weigh at least $n-1$, so $x\le s-(n-1)$. Also $x\le s-(n-1)\le2n-(n-1)=n+1$. Adding, $2x\le s-(n-1)+n+1=s+2$. This completes the induction. $\blacksquare$

### m33
source: mathnet
mathnet_id: 06w4
country: IMO
competition: IMO 2020 Shortlisted Problems
type: answer
difficulty: 7
techniques: recursion, casework
statement:
Let $n$ be a positive integer. Find the number of permutations $a_1,a_2,\dots,a_n$ of the sequence $1,2,\dots,n$ satisfying
$$a_1\le2a_2\le3a_3\le\dots\le na_n.$$
asked:
Count the permutations of $1,\dots,n$ for which the products $i\,a_i$ never decrease.
technique:
Find where the largest number $n$ can stand. That splits the permutations into cases that reduce to the same question for smaller $n$ ([[recursion]]).
hint:
Compute the answer for $n=1,2,3,4$ and guess.
hint:
Let $a_k=n$. Show that if $k\le n-2$, then all of $a_k,a_{k+1},\dots,a_n$ exceed $k$, which is impossible.
hint:
So either $a_n=n$, or $a_{n-1}=n$ and then $a_n=n-1$. Check that the remaining conditions are exactly the problem for $n-1$ or $n-2$.
solution:
Let $P_n$ be the number of such permutations. Clearly $P_1=1$ and $P_2=2$ (both $1,2$ and $2,1$ work).

**Lemma.** For $n\ge3$, either $a_n=n$, or $a_{n-1}=n$ and $a_n=n-1$.

*Proof.* Let $a_k=n$.
- If $k=n-1$: $(n-1)n=(n-1)a_{n-1}\le na_n$ gives $a_n\ge n-1$, and $a_n\ne n$, so $a_n=n-1$.
- If $k\le n-2$: for $k<i<n$ we have $ia_i\ge ka_k=kn$, so $a_i\ge kn/i>k$. Also $na_n\ge(n-1)a_{n-1}\ge(n-1)(k+1)=nk+(n-1-k)>nk$, so $a_n>k$. Thus the $n-k+1$ distinct numbers $a_k,a_{k+1},\dots,a_n$ all lie in $\{k+1,\dots,n\}$, which has only $n-k$ elements. Contradiction. $\square$

**Counting.** Let $n\ge3$.
- If $a_n=n$, then $a_1,\dots,a_{n-1}$ is a permutation of $1,\dots,n-1$ satisfying the chain up to $(n-1)a_{n-1}$, and the last inequality $(n-1)a_{n-1}\le(n-1)^2<n^2=na_n$ holds automatically. This gives $P_{n-1}$ permutations.
- If $(a_{n-1},a_n)=(n,n-1)$, then $a_1,\dots,a_{n-2}$ is a permutation of $1,\dots,n-2$ satisfying the chain up to $(n-2)a_{n-2}$, and the last two inequalities $(n-2)a_{n-2}\le(n-2)^2<n(n-1)=(n-1)a_{n-1}=na_n$ hold automatically. This gives $P_{n-2}$ permutations.

So $P_n=P_{n-1}+P_{n-2}$ for $n\ge3$, with $P_1=1=F_2$ and $P_2=2=F_3$, where $F_1=F_2=1$, $F_{k+1}=F_k+F_{k-1}$ are the Fibonacci numbers. By induction the answer is $\boxed{P_n=F_{n+1}}$.

### m34
source: mathnet
mathnet_id: 056u
country: Estonia
competition: Final Round of National Olympiad
type: answer
difficulty: 6
techniques: pigeonhole, constructive
statement:
Some knights are on a playground. Each knight has three properties: speed, smartness and sightliness. For every knight, each property takes a certain integral value $x$ such that $1\le x\le n$. A knight $A$ can win a knight $B$ if the speed, smartness and sightliness of $A$ are all greater than those of $B$. It is known that none among the knights on the playground can win any of the other knights and every two knights differ by at least one property. Find the largest possible number of knights on the playground.
asked:
Find the largest set of distinct triples in $\{1,\dots,n\}^3$ in which no triple is larger than another in all three coordinates.
technique:
Assign to each knight a "type" so that two knights of the same type would contradict the conditions; then count the types ([[pigeonhole]]). A matching example shows the bound is sharp.
hint:
Two knights whose triples differ by $(c,c,c)$ with $c\ne0$ cannot both be present. Why?
hint:
Slide each triple down along the direction $(1,1,1)$ until its smallest entry is $1$. How many possible end results are there?
hint:
For the example, take all triples whose smallest entry equals $1$.
solution:
**Answer:** $\boxed{3n^2-3n+1}$.

**Upper bound.** For a knight with properties $(a,b,c)$ let $x=\min(a,b,c)-1\ge0$ and define its *base* $(a-x,b-x,c-x)$. The base is a triple in $\{1,\dots,n\}^3$ with smallest entry $1$. If two knights had the same base, their triples would be $(p+x,q+x,r+x)$ and $(p+y,q+y,r+y)$. If $x=y$ the knights coincide in all properties; if, say, $x>y$, the first knight wins the second. Both are excluded, so different knights have different bases. The number of possible bases is the number of triples in $\{1,\dots,n\}^3$ containing at least one $1$, namely $n^3-(n-1)^3=3n^2-3n+1$.

**Example.** Take one knight for every triple in $\{1,\dots,n\}^3$ whose smallest entry is $1$. They are pairwise distinct. If $A$ won $B$, look at a coordinate where $A$ has value $1$: there $B$ would need a value smaller than $1$, impossible. So $3n^2-3n+1$ knights are possible.

### m35
source: mathnet
mathnet_id: 0ai8
country: North Macedonia
competition: Balkan Mathematical Olympiads
type: proof
difficulty: 7
techniques: descent, modular-arithmetic
statement:
A special number is a positive integer $n$ for which there exist positive integers $a,b,c$ and $d$ with
$$n=\frac{a^3+2b^3}{c^3+2d^3}.$$
Prove that
(a) there are infinitely many special numbers;
(b) $2014$ is not a special number.
asked:
Show that infinitely many positive integers are quotients $\frac{a^3+2b^3}{c^3+2d^3}$ with positive integers $a,b,c,d$, and that $2014$ is not such a quotient.
technique:
For (b), find a prime factor of $2014$ modulo which $x^3+2y^3$ behaves rigidly ([[modular-arithmetic]]), then make the solution smaller ([[descent]]).
hint:
For (a), try to make the numerator a multiple of the denominator in an obvious way.
hint:
$2014=2\cdot19\cdot53$. Show that $-2$ is not a cube modulo $19$ by raising a supposed congruence $z^3\equiv-2$ to the $6$th power.
hint:
If $x^3+2y^3=2014(u^3+2v^3)$, show $19$ divides $x,y$ and then $u,v$, and divide everything by $19$.
solution:
**(a)** For every positive integer $k$, taking $a=b=k$ and $c=d=1$ gives $\frac{k^3+2k^3}{1+2}=k^3$. So every perfect cube is special, and there are infinitely many.

**(b) Lemma.** If $19\mid x^3+2y^3$ for integers $x,y$, then $19\mid x$ and $19\mid y$.

*Proof.* Suppose $19\nmid y$. Then $19\nmid x$ too (otherwise $19\mid2y^3$). Let $z\equiv xy^{-1}\pmod{19}$; then $z^3\equiv-2$, and $z\not\equiv0$. Raising to the $6$th power and using Fermat's little theorem, $1\equiv z^{18}\equiv(-2)^6=64\equiv7\pmod{19}$, a contradiction. So $19\mid y$, and then $19\mid x^3$ gives $19\mid x$. $\square$

Suppose $2014=2\cdot19\cdot53$ is special: $x^3+2y^3=2014(u^3+2v^3)$ for positive integers $x,y,u,v$. Among all such quadruples choose one with $x$ minimal.

The right side is divisible by $19$, so by the lemma $x=19x_1$, $y=19y_1$ with positive integers $x_1,y_1$. Substituting and dividing by $19$:
$$19^2(x_1^3+2y_1^3)=2\cdot53\,(u^3+2v^3).$$
Since $\gcd(19,106)=1$, $19\mid u^3+2v^3$, and by the lemma $u=19u_1$, $v=19v_1$. Substituting and dividing by $19^3$:
$$x_1^3+2y_1^3=2014\,(u_1^3+2v_1^3).$$
This is a new quadruple of positive integers with $x_1=x/19<x$, contradicting minimality. Hence $2014$ is not special. $\blacksquare$

### m36
source: mathnet
mathnet_id: 093f
country: Middle European Mathematical Olympiad (MEMO)
competition: Middle European Mathematical Olympiad
type: proof
difficulty: 6
techniques: modular-arithmetic, pigeonhole
statement:
Let $a_1,a_2,a_3,\dots$ be the sequence of positive integers such that
$$a_1=1\quad\text{and}\quad a_{k+1}=a_k^3+1\ \text{ for all positive integers }k.$$
Prove that for every prime number $p$ of the form $3\ell+2$, where $\ell$ is a non-negative integer, there exists a positive integer $n$ such that $a_n$ is divisible by $p$.
asked:
For each prime $p\equiv2\pmod3$, show that some term of the sequence $1,2,9,730,\dots$ (each term is the cube of the previous one plus $1$) is a multiple of $p$.
technique:
Study the map $x\mapsto x^3+1$ on residues mod $p$ ([[modular-arithmetic]]). If it is a bijection, the sequence of residues must come back to where it started, by a [[pigeonhole]] argument.
hint:
Because $\gcd(3,p-1)=1$, cubing is injective mod $p$: find $e$ with $3e\equiv1\pmod{p-1}$ and use Fermat.
hint:
So $f(x)=x^3+1$ permutes the residues mod $p$. Put $a_0=0$; then $a_1=f(a_0)$.
hint:
Iterating a permutation of a finite set from any start, you return to the start.
solution:
Work modulo $p$ and let $f(x)=x^3+1$.

**$f$ is a bijection mod $p$.** Since $p\equiv2\pmod3$, $p-1\equiv1\pmod 3$, so $\gcd(3,p-1)=1$ and there is a positive integer $e$ with $3e\equiv1\pmod{p-1}$, say $3e=1+q(p-1)$ with $q\ge0$. By Fermat, $x^{3e}=x\cdot(x^{p-1})^q\equiv x$ for every $x\not\equiv0$, and also for $x\equiv0$. So if $x^3\equiv y^3$ then $x\equiv(x^3)^e\equiv(y^3)^e\equiv y$. Thus cubing, and hence $f$, is injective on the $p$ residues, so it is a bijection.

**Return to $0$.** Set $a_0=0$; then $a_1=1=f(a_0)$ and $a_{k+1}=f(a_k)$ for all $k\ge0$. Among the $p+1$ residues $a_0,a_1,\dots,a_p$ two coincide (pigeonhole): $a_i\equiv a_j$ with $0\le i<j$. If $i>0$, then $f(a_{i-1})\equiv f(a_{j-1})$, and injectivity gives $a_{i-1}\equiv a_{j-1}$. Repeating, we get $a_0\equiv a_{j-i}$, i.e. $a_n\equiv0\pmod p$ for $n=j-i\ge1$. This $a_n$ is a term of the original sequence and is divisible by $p$. $\blacksquare$

### m37
source: mathnet
mathnet_id: 00lz
country: Austria
competition: 48th Austrian Mathematical Olympiad
type: answer
difficulty: 6
techniques: modular-arithmetic, diophantine
statement:
Find all pairs $(a,b)$ of non-negative integers such that
$$2017^a=b^6-32b+1.$$
asked:
Determine all non-negative integers $a,b$ with $2017^a=b^6-32b+1$.
technique:
Reduce modulo a suitable power of $2$ ([[modular-arithmetic]]) to learn something about $a$, then compare sizes.
hint:
Parity forces $b$ to be even. Write $b=2c$ and look at the equation modulo $64$.
hint:
$2017\equiv33\pmod{64}$ and $33^2\equiv1\pmod{64}$. What does this say about $a$?
hint:
For larger $b$, compare $b^6-32b+1$ with $(b^3)^2$ and $(b^3-1)^2$.
solution:
**Answer:** $\boxed{(a,b)=(0,0)\text{ and }(0,2)}$.

The left side is odd, so $b^6-32b$ is even, so $b$ is even: $b=2c$. Then $b^6-32b=64c^6-64c$, so $2017^a\equiv1\pmod{64}$. Now $2017=31\cdot64+33\equiv33$ and $33^2=1089=17\cdot64+1\equiv1\pmod{64}$, so $2017^a\equiv33$ for odd $a$ and $\equiv1$ for even $a$. Hence $a$ is even and $2017^a$ is a perfect square.

**$b\ge6$ (even, so $b>4$).** We have $b^6-32b+1<b^6=(b^3)^2$, and
$$b^6-32b+1>(b^3-1)^2=b^6-2b^3+1\iff 2b^3>32b\iff b^2>16,$$
which holds. So the right side lies strictly between consecutive squares and is not a square. No solutions.

**Remaining even $b$:**
- $b=0$: $2017^a=1$, so $a=0$.
- $b=2$: $2017^a=64-64+1=1$, so $a=0$.
- $b=4$: $2017^a=4096-128+1=3969$. But $2017<3969<2017^2$, so $3969$ is not a power of $2017$.

So the solutions are $(0,0)$ and $(0,2)$.

### m38
source: mathnet
mathnet_id: 020b
country: Benelux Mathematical Olympiad
competition: Benelux Mathematical Olympiad
type: answer
difficulty: 7
techniques: casework, divisibility
statement:
Find all positive integers $n>1$ with the following property: for each two positive divisors $k,\ell<n$ of $n$, at least one of the numbers $2k-\ell$ and $2\ell-k$ is a (not necessarily positive) divisor of $n$ as well.
asked:
Find all $n>1$ such that for any proper positive divisors $k,\ell$ of $n$, one of $2k-\ell$, $2\ell-k$ divides $n$ (negative divisors allowed; $0$ never divides $n$).
technique:
Apply the condition to cleverly chosen pairs, starting with $1$ and the largest proper divisor, and split into cases ([[casework]]) using [[divisibility]].
hint:
Primes work. For composite $n$ let $p$ be its smallest prime factor and $m=n/p$, the largest proper divisor. Apply the condition to $(1,m)$.
hint:
$2m-1$ lies strictly between $m$ and $n$, so it is not a divisor. Deduce $m-2\mid 2p$.
hint:
Go through $m-2\in\{1,2,p,2p\}$; in the case $m=p+2$ use the pair $(1,p)$. Finally test the few candidates.
solution:
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

### m39
source: mathnet
mathnet_id: 01hr
country: Baltic Way
competition: Baltic Way 2021 Shortlist
type: proof
difficulty: 6
techniques: coloring, pigeonhole
statement:
Let $t$ be a non-zero real number and $n$ be a positive integer. Let $a_1,a_2,\dots,a_{2n-1}$ be real numbers (not necessarily distinct). Prove that there exist indices $i_1<i_2<\dots<i_n$ such that $a_{i_k}-a_{i_l}\ne t$ for any $1\le k,l\le n$.
asked:
From $2n-1$ real numbers, choose $n$ of them (by index) so that no two chosen numbers differ by exactly $t$ in either order.
technique:
[[coloring]]: colour the indices with two colours so that two numbers differing by $t$ always get different colours, then use [[pigeonhole]].
hint:
Only $|t|$ matters, since the condition is required for both orders $k,l$. Assume $t>0$.
hint:
Colour index $i$ by the parity of $\lfloor a_i/t\rfloor$. What happens to this integer when you add $t$ to $a_i$?
hint:
One colour class has at least $n$ indices.
solution:
The condition "$a_{i_k}-a_{i_l}\ne t$ for all $k,l$" is symmetric under $t\mapsto-t$ (swap $k$ and $l$), so we may assume $t>0$.

Colour each index $i\in\{1,\dots,2n-1\}$ by the parity of the integer $\lfloor a_i/t\rfloor$. If $a_j-a_i=t$, then $a_j/t=a_i/t+1$, so $\lfloor a_j/t\rfloor=\lfloor a_i/t\rfloor+1$, and $i,j$ get different colours. Hence two indices of the same colour never have values differing by $t$ in either order.

There are $2n-1$ indices and $2$ colours, so some colour class has at least $n$ indices. Let $i_1<\dots<i_n$ be $n$ of them. For any $k,l$ (including $k=l$, where the difference is $0\ne t$), $a_{i_k}-a_{i_l}\ne t$. $\blacksquare$

### m40
source: mathnet
mathnet_id: 01bf
country: Baltic Way
competition: Baltic Way
type: answer
difficulty: 6
techniques: symmetry
statement:
Two players play a game on an $N\times N$ board. The players alternately mark a cell in such a way that there is never a diagonal on the board containing two marked cells. A player who cannot move loses. For which $N>0$ does the starting player have a winning strategy?
asked:
A diagonal means any line of cells parallel to one of the two main diagonals. Players alternately mark cells so that no diagonal (of either direction) ever holds two marks; whoever cannot move loses. For which $N$ does the first player win?
technique:
Use a mirror strategy ([[symmetry]]): one player answers each move by its image under a suitable symmetry of the board. Choose the symmetry depending on the parity of $N$.
hint:
The game is finite, so a player who can always answer wins.
hint:
For even $N$, let the second player copy each move in the vertical mid-line of the board. Why is the copy always legal?
hint:
For odd $N$, the first player takes the centre and then answers with the point reflection in the centre.
solution:
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

### m41
source: mathnet
mathnet_id: 0a95
country: Nordic Mathematical Olympiad
competition: Nordic Mathematical Contest, NMC 21
type: answer
difficulty: 6
techniques: symmetry
statement:
The number $10^{2007}$ is written on a blackboard. Anne and Berit play a game where the player in turn makes one of two operations:

(i) replace a number $x$ on the blackboard by two integers $a$ and $b$ greater than $1$ such that $x=ab$;

(ii) erase one or both of two equal numbers on the blackboard.

The player who is not able to make her turn loses the game. Anne starts. Who has a winning strategy?
asked:
Starting from $10^{2007}$, players alternately split a number into two factors greater than $1$, or erase one or both of two equal numbers. The player with no move loses. Decide whether Anne (first) or Berit wins.
technique:
After a good first move the board splits into two "mirror" halves, and the first player can copy every move of the opponent in the other half ([[symmetry]]).
hint:
Anne's first move: split $10^{2007}$ into a power of $2$ and a power of $5$.
hint:
Keep the board of the form $2^{e_1},\dots,2^{e_k},5^{e_1},\dots,5^{e_k}$ after each of Anne's moves. Show Anne can restore this after any move of Berit.
hint:
Also check that the game cannot go on forever.
solution:
**Answer: Anne wins.**

**The game is finite.** All numbers on the board are greater than $1$. Let $\Omega(x)$ be the number of prime factors of $x$ counted with multiplicity, and consider $\Phi=\sum(2\Omega(x)-1)$ over the numbers on the board, a positive integer. Splitting $x=ab$ changes $\Phi$ by $(2\Omega(a)-1)+(2\Omega(b)-1)-(2\Omega(x)-1)=-1$; erasing decreases it by at least $1$. So the game ends.

**Strategy.** Anne first replaces $10^{2007}$ by $2^{2007}$ and $5^{2007}$. She then keeps the following property after each of her moves: the board consists of $2^{e_1},\dots,2^{e_k}$ and $5^{e_1},\dots,5^{e_k}$ for some exponents $e_i\ge1$ (the two lists have the same exponents).

Every number on such a board is a power of $2$ or a power of $5$. Consider Berit's move:
- She splits $2^{e}$ into $a\cdot b$ with $a,b>1$. Then $a=2^f$, $b=2^{e-f}$ with $1\le f\le e-1$. Anne splits a copy of $5^{e}$ (which exists) into $5^f$ and $5^{e-f}$.
- She erases one or two copies of $2^{e}$, which appeared at least twice. Then $5^{e}$ also appears at least twice, and Anne erases the same number of copies of $5^{e}$.
- Moves on powers of $5$ are answered in the same way on powers of $2$.

In each case Anne's answer is legal and restores the property. So Anne always has a move after Berit, and since the game is finite, Berit is eventually the one who cannot move. $\boxed{\text{Anne}}$ wins.

### m42
source: mathnet
mathnet_id: 03mi
country: Canada
competition: Canadian Mathematical Olympiad
type: answer
difficulty: 6
techniques: constructive, modular-arithmetic
statement:
The sequence $a_1,a_2,\dots,a_n$ consists of the numbers $1,2,\dots,n$ in some order. For which positive integers $n$ is it possible that the $n+1$ numbers $0,\ a_1,\ a_1+a_2,\ a_1+a_2+a_3,\ \dots,\ a_1+a_2+\dots+a_n$ all have different remainders when divided by $n+1$?
asked:
Find all $n$ for which some ordering of $1,\dots,n$ has its $n+1$ partial sums (starting with $0$) pairwise different modulo $n+1$.
technique:
One partial sum is fixed whatever the order; check it against $0$ ([[modular-arithmetic]]). For the other $n$, build an explicit ordering ([[constructive]]).
hint:
The last partial sum is always $1+2+\dots+n$. When is it $\equiv0\pmod{n+1}$?
hint:
For odd $n=2k+1$, try alternating small odd numbers with large even numbers: $1,\,n-1,\,3,\,n-3,\,5,\dots$
hint:
In that ordering, consecutive pairs $a_{2j}+a_{2j+1}$ and $a_{2j-1}+a_{2j}$ are constant modulo $n+1$.
solution:
**Answer:** exactly the odd $n$.

**$n$ even is impossible.** The last partial sum is $1+\dots+n=\frac n2(n+1)\equiv0\pmod{n+1}$, the same remainder as the first number $0$.

**$n=2k+1$ odd: a construction.** Put $a_i=i$ for odd $i$ and $a_i=n+1-i$ for even $i$:
$$1,\ n-1,\ 3,\ n-3,\ 5,\ \dots,\ 2,\ n.$$
Odd positions carry the odd numbers $1,3,\dots,n$; even positions $i=2,4,\dots,2k$ carry $n+1-i$, which runs over the even numbers $2k,\dots,2$. So this is a permutation of $1,\dots,n$. Let $b_j=a_1+\dots+a_j$, $b_0=0$.
- For even indices: $a_{2t-1}+a_{2t}=(2t-1)+(n+1-2t)=n\equiv-1$, so $b_{2j}\equiv-j\equiv n+1-j$ for $j=1,\dots,k$: the remainders $n,n-1,\dots,k+2$.
- For odd indices: $a_{2t}+a_{2t+1}=(n+1-2t)+(2t+1)=n+2\equiv1$, so $b_{2j+1}=a_1+\sum_{t=1}^{j}(a_{2t}+a_{2t+1})\equiv1+j$ for $j=0,\dots,k$: the remainders $1,2,\dots,k+1$.

Together with $b_0=0$ these are $0,1,\dots,2k+1$, all different. So the answer is $\boxed{n\text{ odd}}$.

### m43
source: mathnet
mathnet_id: 0da9
country: Saudi Arabia
competition: Team selection tests for IMO 2018
type: answer
difficulty: 7
techniques: constructive, parity
statement:
Find all positive integers $k$ such that there exists a permutation $(a_1,a_2,\dots,a_{1000})$ of $(1,2,\dots,1000)$ satisfying $|a_i-i|=k$ for all $i=1,2,\dots,1000$.
asked:
Find every $k$ for which the numbers $1,\dots,1000$ can be permuted so that each number moves exactly $k$ places.
technique:
Work inside one residue class mod $k$; a [[parity]] condition appears, and a block pattern gives the [[constructive]] part.
hint:
Inside one residue class $x_1<x_2<\dots<x_m$ (step $k$), the permutation sends each $x_j$ to $x_{j-1}$ or $x_{j+1}$. Which element can be sent to $x_1$?
hint:
Show that such a permutation of a class must swap $x_1\leftrightarrow x_2$, $x_3\leftrightarrow x_4$, $\dots$, so $m$ is even.
hint:
The class sizes are $\lfloor 1000/k\rfloor$ or $\lfloor 1000/k\rfloor+1$. When can they all be even?
solution:
**Answer:** exactly the divisors of $500$: $\boxed{k\in\{1,2,4,5,10,20,25,50,100,125,250,500\}}$.

**Construction when $k\mid500$.** Then $2k\mid1000$. Cut $1,\dots,1000$ into blocks of $2k$ consecutive numbers $\{2kq+1,\dots,2kq+2k\}$. Inside each block send $2kq+j\mapsto2kq+j+k$ for $1\le j\le k$ and $2kq+j\mapsto2kq+j-k$ for $k<j\le2k$. This permutes each block and moves every number by exactly $k$.

**Necessity.** Suppose such a permutation exists. Since $a_i=i\pm k$, it maps each residue class mod $k$ in $\{1,\dots,1000\}$ to itself. Fix a class $x_1<x_2<\dots<x_m$ (so $x_{j+1}=x_j+k$) and write $a_{x_j}=x_{\sigma(j)}$; then $\sigma$ is a permutation of $\{1,\dots,m\}$ with $|\sigma(j)-j|=1$ for all $j$.

*Claim: $m$ is even.* Induct on $m$. If $m=1$, $\sigma(1)=1$, impossible. If $m\ge2$: the only $j$ with $\sigma(j)=1$ is $j=2$, and $\sigma(1)$ must be $2$. So $\sigma$ swaps $1,2$ and restricts to $\{3,\dots,m\}$ with the same property, so by induction $m-2$ is even (or $m=2$). $\square$

Now write $1000=qk+s$ with $0\le s<k$. The class sizes are $q+1$ for $s$ classes and $q$ for the other $k-s$ classes. If $s>0$, both sizes occur (since $0<s<k$), and $q,q+1$ cannot both be even. So $s=0$, $k\mid1000$, and $q=1000/k$ is even, i.e. $2k\mid1000$, i.e. $k\mid500$.

### m44
source: mathnet
mathnet_id: 02er
country: Brazil
competition: XIII OBM
type: proof
difficulty: 6
techniques: extremal
statement:
At a party every woman dances with at least one man, and no man dances with every woman. Show that there are men $M$ and $M'$ and women $W$ and $W'$ such that $M$ dances with $W$, $M'$ dances with $W'$, but $M$ does not dance with $W'$, and $M'$ does not dance with $W$.
asked:
Given that each woman has a partner and no man has danced with all women, find two men and two women forming the pattern: $M$–$W$ and $M'$–$W'$ dance, while $M$–$W'$ and $M'$–$W$ do not.
technique:
Choose $M$ by an [[extremal]] property and let the hypotheses produce the other three people.
hint:
Let $M$ be a man who dances with the largest number of women.
hint:
Pick a woman $W'$ that $M$ does not dance with, and a partner $M'$ of $W'$.
hint:
If $M'$ danced with every partner of $M$, compare the numbers of partners.
solution:
There are women at the party (if there were none, any man would vacuously dance with every woman), and each of them dances with some man, so there are men too. Let $M$ be a man who dances with the maximum number of women.

$M$ does not dance with every woman, so there is a woman $W'$ he does not dance with. $W'$ dances with some man $M'$, and $M'\ne M$.

Suppose $M'$ danced with every woman who dances with $M$. Then $M'$ dances with all partners of $M$ and also with $W'$, who is not a partner of $M$, so $M'$ has more partners than $M$. This contradicts the choice of $M$. Hence there is a woman $W$ who dances with $M$ but not with $M'$.

Now $M$ dances with $W$, $M'$ dances with $W'$, $M$ does not dance with $W'$, and $M'$ does not dance with $W$. $\blacksquare$

### m45
source: mathnet
mathnet_id: 0gmz
country: Turkey
competition: 14th Turkish Mathematical Olympiad
type: answer
difficulty: 7
techniques: double-counting, extremal
statement:
Find the largest real number $t$ such that, in any school with $2006$ students and $14$ teachers where every student is acquainted with at least one teacher, a student and a teacher can be found such that they are acquainted with each other, and the ratio of the number of students who are acquainted with the teacher to the number of teachers who are acquainted with the student is at least $t$.
asked:
For each acquainted pair (teacher $i$, student $j$) form $a_i/b_j$, where $a_i$ is the number of students teacher $i$ knows and $b_j$ the number of teachers student $j$ knows. Find the largest $t$ such that some pair always reaches $t$.
technique:
Assume every acquainted pair has a small ratio and add up the resulting inequalities over all acquainted pairs; group the sum by teachers and by students ([[double-counting]]).
hint:
The all-acquainted school shows $t\le2006/14$.
hint:
Suppose $a_i/b_j<2006/14$ for every acquainted pair, i.e. $\frac1{b_j}<\frac{2006}{14}\cdot\frac1{a_i}$.
hint:
Sum over all acquainted pairs: $\sum\frac1{b_j}=2006$, while $\sum\frac1{a_i}$ equals the number of teachers who know somebody.
solution:
**Answer:** $\boxed{t=\dfrac{2006}{14}=\dfrac{1003}7}$.

Let $a_i$ be the number of students acquainted with teacher $i$ and $b_j$ the number of teachers acquainted with student $j$ ($b_j\ge1$). Let $E$ be the set of acquainted pairs $(i,j)$; it is nonempty.

**$t$ cannot be larger.** If everybody knows everybody, every pair has ratio $2006/14$.

**Some pair always reaches $2006/14$.** Suppose not: $a_i/b_j<\frac{2006}{14}$ for all $(i,j)\in E$. For $(i,j)\in E$ we have $a_i\ge1$, so this says $\frac1{b_j}<\frac{2006}{14}\cdot\frac1{a_i}$. Sum over $E$:
- Grouping by students, $\sum_{(i,j)\in E}\frac1{b_j}=\sum_{j}b_j\cdot\frac1{b_j}=2006$.
- Grouping by teachers, $\sum_{(i,j)\in E}\frac1{a_i}=\sum_{i:\,a_i\ge1}a_i\cdot\frac1{a_i}\le14$.

So $2006<\frac{2006}{14}\cdot14=2006$, a contradiction. Hence in every school some acquainted pair has ratio at least $2006/14$, and the largest $t$ is $2006/14$.

### m46
source: mathnet
mathnet_id: 01yy
country: Belarus
competition: SELECTION and TRAINING SESSION
type: answer
difficulty: 7
techniques: graph-theory, constructive
statement:
There are $n\ge2$ cities in a country. Some pairs of cities are connected with an air communication, and for any such pair the connection is mutual. It is possible to travel from any city to any other (possibly with a couple of flights). It is also known that the minimal number of flights needed to travel from any given city to another doesn't exceed the same number $m$, and for any city $A$ there exists another city $B$ which cannot be reached from $A$ by less than $m$ flights. Given $n$, find all possible values of $m$.
asked:
Cities are joined by two-way flights so that every city can reach every other, and from every city the farthest other city needs exactly $m$ flights. For given $n$, find all possible $m$.
technique:
In [[graph-theory]] terms, every vertex has eccentricity $m$. Bound $m$ through a spanning tree and its middle vertex; then give a [[constructive]] example for each allowed value.
hint:
Deleting edges never shortens distances. Pass to a spanning tree.
hint:
In a tree on $n$ vertices take a longest path and its middle vertex $c$. Show every vertex is within $\lceil (n-1)/2\rceil=\lfloor n/2\rfloor$ of $c$.
hint:
For the example use a cycle of length $2m$ and attach the remaining vertices as "copies" of one cycle vertex.
solution:
**Answer:** all $m$ with $\boxed{1\le m\le\lfloor n/2\rfloor}$.

Model the cities as a connected graph $G$. The conditions say that every vertex has eccentricity (largest distance to another vertex) exactly $m$. Since $n\ge2$, $m\ge1$.

**Upper bound.** Take a spanning tree $T$ of $G$. Distances in $T$ are at least those in $G$. Let $v_0v_1\dots v_D$ be a longest path in $T$; $D\le n-1$. Let $c=v_h$ with $h=\lfloor D/2\rfloor$, so $h\le D-h=\lceil D/2\rceil$. Take any vertex $x$, and let $v_j$ be the vertex of the path closest to $x$ in $T$, with $e=\operatorname{dist}_T(x,v_j)$. The tree path from $x$ to $v_j$ followed by the path to $v_0$ (or $v_D$) is a path of length $e+j$ (or $e+D-j$), so by maximality $e\le j$ and $e\le D-j$. Then
$$\operatorname{dist}_T(c,x)=e+|j-h|\le\begin{cases}(D-j)+(j-h)=D-h,& j\ge h,\\ j+(h-j)=h,& j<h,\end{cases}$$
so $\operatorname{dist}_T(c,x)\le\lceil D/2\rceil\le\lceil(n-1)/2\rceil=\lfloor n/2\rfloor$. Hence $m$, the eccentricity of $c$ in $G$, is at most $\lfloor n/2\rfloor$.

**Examples.** For $m=1$ take the complete graph: all eccentricities are $1$.

For $2\le m\le\lfloor n/2\rfloor$, take a cycle $v_0v_1\dots v_{2m-1}v_0$ and $n-2m$ further vertices $u_1,\dots,u_{n-2m}$, each joined to $v_0,v_1,v_{2m-1}$ and to all other $u$'s. Map every $u_i$ to $v_0$ and fix the cycle vertices. Every edge goes to an edge of the cycle or collapses to a point, so distances do not increase under this map.
- For two cycle vertices this shows the distance is the cycle distance (the cycle itself gives the reverse inequality).
- For $u_i$ and a cycle vertex $y\ne v_0$: $u_i$ has the same cycle neighbours $v_1,v_{2m-1}$ as $v_0$, so $\operatorname{dist}(u_i,y)\le\operatorname{dist}_C(v_0,y)$, and the map gives $\ge$. So $\operatorname{dist}(u_i,y)=\operatorname{dist}_C(v_0,y)$; also $\operatorname{dist}(u_i,v_0)=\operatorname{dist}(u_i,u_l)=1$.

On a $2m$-cycle every vertex has eccentricity $m$. Hence every cycle vertex has eccentricity $m$ in $G$ (the extra vertices are at distance $\le m$), and every $u_i$ has eccentricity $\max(1,m)=m$ (it is at distance $m$ from $v_m$). This graph has $n$ vertices and is connected.

### m47
source: mathnet
mathnet_id: 01h8
country: Baltic Way
competition: Baltic Way 2020
type: answer
difficulty: 7
techniques: divisibility, double-counting
statement:
Let $N$ be a positive integer. Determine the number of pairs $(a,b)$ of positive integers $a$ and $b$ such that the number
$$\frac{ab}{a+b}$$
is a divisor of $N$.
asked:
Count ordered pairs of positive integers $(a,b)$ for which $\frac{ab}{a+b}$ is a positive integer dividing $N$, and express the answer through the number of divisors of $N$.
technique:
Fix the value $m=\frac{ab}{a+b}$ and factor the resulting equation ([[divisibility]]). Then sum over all $m\mid N$ and evaluate the sum prime by prime.
hint:
$\frac{ab}{a+b}=m$ is equivalent to $(a-m)(b-m)=m^2$.
hint:
Show $a,b>m$, so the pairs for a fixed $m$ correspond to the positive divisors of $m^2$.
hint:
Compute $\sum_{m\mid N}d(m^2)$ using multiplicativity: for $N=\prod p_i^{s_i}$ it factors over the primes.
solution:
**Answer:** $\boxed{d(N)^2}$, where $d(N)$ is the number of positive divisors of $N$.

Fix a positive divisor $m$ of $N$. For positive $a,b$, $\frac{ab}{a+b}=m$ is equivalent to $ab=ma+mb$, i.e. $(a-m)(b-m)=m^2$. Moreover $\frac{ab}{a+b}<\frac{ab}{a}=b$ and similarly $<a$, so $a-m$ and $b-m$ are positive. Hence the pairs with value $m$ correspond bijectively to ordered factorizations $m^2=uv$ with $u,v$ positive ($a=m+u$, $b=m+v$), and their number is $d(m^2)$. Pairs with different values are different, so the total is
$$\sum_{m\mid N}d(m^2).$$
Let $N=\prod_{i=1}^tp_i^{s_i}$. A divisor is $m=\prod p_i^{e_i}$ with $0\le e_i\le s_i$, and $d(m^2)=\prod(2e_i+1)$. Expanding the product,
$$\sum_{m\mid N}d(m^2)=\prod_{i=1}^t\sum_{e=0}^{s_i}(2e+1)=\prod_{i=1}^t(s_i+1)^2=d(N)^2.$$
(For $N=1$ both sides equal $1$: the only pair is $(2,2)$.)

### m48
source: mathnet
mathnet_id: 0dr9
country: Singapore
competition: Singapore Mathematical Olympiad (SMO)
type: answer
difficulty: 7
techniques: divisibility, extremal
statement:
Determine the largest odd positive integer $N$ such that every odd integer $k$ with $1<k<N$ and $\gcd(k,N)=1$ is a prime.
asked:
Find the largest odd $N$ such that every odd number between $1$ and $N$ coprime to $N$ is prime.
technique:
Find small composite odd numbers that must share a factor with $N$ ([[divisibility]]), then compare sizes ([[extremal]]).
hint:
If $p$ is an odd prime with $p^2<N$, then $p\mid N$.
hint:
Let $3=q_1<q_2<\dots$ be the odd primes. Using Bertrand's postulate ($q_{j+1}<2q_j$), prove $q_{j+1}^2<q_1q_2\cdots q_j$ for $j\ge4$.
hint:
Conclude $N\le121$, and then check the range $49<N\le121$.
solution:
**Answer:** $\boxed{105}$.

Call an odd $N$ *admissible* if it has the property.

**Key fact.** If $N$ is admissible and $p$ is an odd prime with $p^2<N$, then $p\mid N$: indeed $p^2$ is odd, composite and $1<p^2<N$, so it is not coprime to $N$.

**An inequality.** Let $q_1=3,q_2=5,q_3=7,q_4=11,\dots$ be the odd primes. We claim $q_{j+1}^2<q_1q_2\cdots q_j$ for all $j\ge4$. For $j=4$: $13^2=169<3\cdot5\cdot7\cdot11=1155$. If it holds for $j$, then Bertrand's postulate (there is a prime strictly between $q_{j+1}$ and $2q_{j+1}$) gives $q_{j+2}<2q_{j+1}$, so
$$q_{j+2}^2<4q_{j+1}^2<4\,q_1\cdots q_j<q_1\cdots q_jq_{j+1},$$
since $q_{j+1}>4$.

**$N\le121$.** Suppose an admissible $N>121=q_4^2$. Let $j$ be the largest index with $q_j^2<N$; then $j\ge4$. By the key fact $q_1q_2\cdots q_j\mid N$, so $N\ge q_1\cdots q_j>q_{j+1}^2$, contradicting the maximality of $j$. So $N\le121$.

**$49<N\le121$.** Then $9,25,49<N$, so $3,5,7\mid N$ and $105\mid N$. The only such $N$ in this range is $105$.

**$105$ is admissible.** An odd $k$ with $1<k<105$ coprime to $105$ has no prime factor $2,3,5,7$. If it were composite it would be at least $11^2=121>105$. So it is prime.

Any other admissible $N$ is at most $49$, so the largest is $105$.

### m49
source: mathnet
mathnet_id: 0eu6
country: South Korea
competition: 20th Korean Mathematical Olympiad Final Round
type: answer
difficulty: 7
techniques: diophantine, divisibility
statement:
Find all triplets $(x,y,z)$ of positive integers satisfying $1+4^x+4^y=z^2$.
asked:
Find all positive integers $x,y,z$ with $1+4^x+4^y=z^2$.
technique:
Compare $z^2$ with the squares next to $(2^y)^2$, and when that fails, factor $z^2-1$ and count powers of $2$ ([[diophantine]], [[divisibility]]).
hint:
By symmetry let $x\le y$. Compare $1+4^x+4^y$ with $(2^y+1)^2=4^y+2^{y+1}+1$.
hint:
This settles $2x\le y+1$. For $2x>y+1$, write $(z-1)(z+1)=4^x(1+4^{y-x})$. What is $\gcd(z-1,z+1)$?
hint:
One of $z\pm1$ is divisible by $2^{2x-1}$. Compare the resulting lower bound for $z^2$ with the actual size of $1+4^x+4^y$.
solution:
**Answer:** $(x,y,z)=\boxed{(t,\,2t-1,\,2^{2t-1}+1)\ \text{and}\ (2t-1,\,t,\,2^{2t-1}+1)}$ for positive integers $t$.

The equation is symmetric in $x,y$, so let $x\le y$. Note $z^2>4^y=(2^y)^2$, so $z\ge2^y+1$, while $(2^y+1)^2=4^y+2^{y+1}+1$.

**Case $2x<y+1$.** Then $4^x<2^{y+1}$, so $(2^y)^2<z^2<(2^y+1)^2$. Impossible.

**Case $2x=y+1$.** Then $z^2=4^y+2^{y+1}+1=(2^y+1)^2$, so $z=2^y+1$. With $x=t$ we get $y=2t-1\ge t$ and the solution $(t,2t-1,2^{2t-1}+1)$.

**Case $2x>y+1$.** Since $y\ge x$, this gives $x\ge2$, and $y\le2x-2$. Write $(z-1)(z+1)=4^x(1+4^{y-x})$. The number $z$ is odd, so $z-1,z+1$ are even with $\gcd(z-1,z+1)=2$; one of them is $\equiv2\pmod4$, so the other carries all remaining factors of $2$. The right side is divisible by $2^{2x}$, hence the other factor is divisible by $2^{2x-1}$, and $z+1\ge2^{2x-1}$. Since $x\ge2$, $2^{2x-1}-1>0$, so
$$z^2\ge(2^{2x-1}-1)^2=4\cdot4^{2x-2}-4^x+1.$$
But $z^2=1+4^x+4^y\le1+4^x+4^{2x-2}$. Together: $3\cdot4^{2x-2}\le2\cdot4^x$, i.e. $3\cdot4^{x-2}\le2$, so $x<2$. Contradiction.

Swapping $x$ and $y$ gives the second family. (For $t=1$ both give $(1,1,3)$.)
