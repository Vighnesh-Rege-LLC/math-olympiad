### o37
source: original
type: proof
difficulty: 4
techniques: pigeonhole
statement:
Ten distinct integers are chosen from the set $\{1,2,\dots,99\}$. Prove that among the chosen numbers there are two disjoint nonempty subsets with the same sum.
asked:
For any choice of ten different numbers from $1$ to $99$, you must exhibit two nonempty subsets of the chosen numbers that share no element and have equal sums.
technique:
Count how many subsets there are and how many different sums they can possibly have. Then fix the overlap.
hint:
Count the nonempty subsets of a ten-element set. Then find an upper bound for the sum of any subset of the chosen numbers.
hint:
There are $2^{10}-1=1023$ nonempty subsets, and every subset sum lies between $1$ and the sum of the ten largest possible numbers. Compare these two counts to get two different subsets with equal sums, then deal with elements they have in common.
solution:
Let $A$ be the set of ten chosen numbers. It has $2^{10}-1=1023$ nonempty subsets.

The sum of any subset of $A$ is a positive integer, and it is at most the sum of all elements of $A$. Since the elements are distinct and at most $99$, this is at most $99+98+\dots+90=945$. So every subset sum lies in $\{1,2,\dots,945\}$.

There are $1023>945$ subsets but at most $945$ possible sums, so by the pigeonhole principle two different subsets $B\ne C$ have the same sum.

They may overlap. Remove the common elements: let $B'=B\setminus C$ and $C'=C\setminus B$. Then $B'$ and $C'$ are disjoint, and
$$\sum B'=\sum B-\sum(B\cap C)=\sum C-\sum(B\cap C)=\sum C'.$$
Since $B\ne C$, at least one of $B',C'$ is nonempty. If one of them were empty, the other would have sum $0$; but all elements are positive, so a nonempty set has positive sum. Hence both are nonempty. $\blacksquare$

### o38
source: original
type: answer
difficulty: 4
techniques: pigeonhole, constructive
statement:
Find the smallest positive integer $n$ with the following property: every $n$-element subset of $\{1,2,\dots,20\}$ contains two numbers whose difference is exactly $3$.
asked:
Find the least $n$ such that any $n$ numbers chosen from $1$ to $20$ must include a pair differing by $3$.
technique:
Organise the numbers into groups in which the forbidden pairs have a simple structure, and see how many you can take from each group.
hint:
Write $1,\dots,20$ in three lists according to the remainder mod $3$, each in increasing order. A pair differing by $3$ is a pair of neighbours in one list.
hint:
A list of length $7$ can be cut into three pairs of neighbours and one leftover element. How many elements of the list can you keep without two neighbours? Then build an example that shows the bound is sharp.
solution:
Split $\{1,\dots,20\}$ by remainder mod $3$ into three chains:
$$A:\ 1,4,7,10,13,16,19\ (7),\quad B:\ 2,5,8,11,14,17,20\ (7),\quad C:\ 3,6,9,12,15,18\ (6).$$
Two numbers differ by exactly $3$ if and only if they are neighbours in the same chain.

**A subset with no such pair has at most $11$ elements.** Cut chain $A$ into the boxes $\{1,4\},\{7,10\},\{13,16\},\{19\}$. A box of two neighbours holds at most one element of the subset, so at most $3+1=4$ elements of $A$ are chosen. The same boxes work for $B$: at most $4$. Chain $C$ splits into three pairs, so at most $3$. In total at most $4+4+3=11$.

Hence any $12$ numbers contain two differing by $3$.

**$11$ is attained.** Take $1,7,13,19$ from $A$, $2,8,14,20$ from $B$, and $3,9,15$ from $C$. Within a chain these are non-neighbours, and numbers in different chains have different remainders mod $3$, so no difference equals $3$. So an $11$-element subset without the property exists, and $n\ge12$.

Therefore the answer is $\boxed{12}$.

### o39
source: original
type: answer
difficulty: 3
techniques: invariants
statement:
The numbers $1,2,\dots,10$ are written on a board. A move consists of erasing two numbers $a$ and $b$ and writing the number $ab+a+b$ in their place. After nine moves, a single number remains. Find this number.
asked:
Show that the final number does not depend on the order of the moves, and compute it.
technique:
Look for a quantity built from the numbers on the board that no move can change.
hint:
Compute $ab+a+b$ for a few small pairs and compare with $a+b$ and $ab$. Try adding $1$ to the result.
hint:
Since $ab+a+b+1=(a+1)(b+1)$, consider the product of $(x+1)$ over all numbers $x$ on the board.
solution:
Note that $ab+a+b+1=(a+1)(b+1)$. Consider the quantity
$$P=\prod_{x\text{ on the board}}(x+1).$$
A move replaces the factors $(a+1)(b+1)$ by the single factor $(ab+a+b)+1=(a+1)(b+1)$, so $P$ does not change. $P$ is an invariant.

At the start, $P=2\cdot3\cdots11=11!=39916800$. At the end the board holds one number $N$, and $P=N+1$. Therefore $N=11!-1=\boxed{39916799}$, whatever order of moves is used.

### o40
source: original
type: answer
difficulty: 4
techniques: invariants, constructive
statement:
On an island there are $6$ red, $9$ green and $13$ blue chameleons. Whenever two chameleons of different colours meet, both of them change to the third colour (for example a red and a green chameleon both become blue). Meetings can happen in any order we like. For which colours $X$ is it possible that, after some meetings, all $28$ chameleons have colour $X$?
asked:
Decide, for each of red, green and blue, whether it can happen that all chameleons end up that colour.
technique:
Track how the three counts change in a single meeting. Some combination of the counts stays the same modulo a small number.
hint:
In one meeting two of the counts drop by $1$ and the third rises by $2$. What happens to each count modulo $3$?
hint:
The differences between the counts are therefore unchanged mod $3$. Compare these initial differences with what a monochrome final state needs. For the one colour that is not excluded, find a sequence of meetings that works.
solution:
Let $r,g,b$ be the numbers of red, green and blue chameleons. In a meeting, two of the counts decrease by $1$ and the third increases by $2$. Since $-1\equiv2\pmod3$, all three counts change by the same amount modulo $3$. So the differences $r-g$, $g-b$, $r-b$ are invariant mod $3$.

Initially $(r,g,b)=(6,9,13)$, so
$$r-g\equiv0,\qquad g-b=-4\equiv2,\qquad r-b=-7\equiv2\pmod 3.$$

- **All red** needs $g=b=0$, so $g-b\equiv0$. But $g-b\equiv2$ always. Impossible.
- **All green** needs $r=b=0$, so $r-b\equiv0$. But $r-b\equiv2$ always. Impossible.
- **All blue** is possible. Let a red and a green chameleon meet six times: $(6,9,13)\to(0,3,25)$. Then let a green and a blue meet: $(2,2,24)$. Finally let a red and a green meet twice: $(1,1,26)\to(0,0,28)$.

So the answer is $\boxed{\text{only blue}}$.

### o43
source: original
type: proof
difficulty: 3
techniques: extremal
statement:
One hundred real numbers are written around a circle, and each number is equal to the arithmetic mean of its two neighbours. Prove that all the numbers are equal.
asked:
Starting from the condition "each number is the average of its two neighbours", show that the hundred numbers must all coincide.
technique:
Single out the largest number on the circle and see what the condition forces on its neighbours.
hint:
Let $M$ be the largest of the numbers. A mean of two numbers can equal $M$ only in a very special situation.
hint:
Show that both neighbours of a number equal to $M$ are also equal to $M$. Then repeat around the circle.
solution:
Let $M$ be the largest of the hundred numbers (a maximum exists since there are finitely many). Suppose $a$ is a number equal to $M$, with neighbours $x$ and $y$. By hypothesis $a=\frac{x+y}2$, so $x+y=2M$. But $x\le M$ and $y\le M$, hence $x+y\le 2M$ with equality only if $x=y=M$. So both neighbours of $a$ equal $M$.

Starting from a number equal to $M$ and moving one step along the circle, the next number is a neighbour of a number equal to $M$, so it equals $M$ too; repeating, every number on the circle equals $M$. $\blacksquare$

### o45
source: original
type: answer
difficulty: 5
techniques: descent, modular-arithmetic
statement:
Find all triples of integers $(x,y,z)$ satisfying
$$x^2+y^2+z^2=x^2y^2.$$
asked:
List every integer solution of the equation.
technique:
Look for a small modulus that forces all the variables to share a common factor, then repeat. If a nonzero solution existed, you could produce a smaller one, which cannot go on forever.
hint:
Squares are $0$ or $1$ mod $4$. Check all cases for the parities of $x$ and $y$ to show that $x,y,z$ must all be even.
hint:
After writing $x=2a$, $y=2b$, $z=2c$ you get a similar equation with a larger power of $4$ on the right: $a^2+b^2+c^2=4a^2b^2$. Prove that for $x^2+y^2+z^2=4^kx^2y^2$ (any $k\ge0$) all of $x,y,z$ must be even, and keep dividing by $2$.
solution:
Clearly $(0,0,0)$ is a solution. We show there are no others.

**Claim.** For every integer $k\ge0$, if integers $x,y,z$ satisfy $x^2+y^2+z^2=4^kx^2y^2$, then $x,y,z$ are all even.

Recall that a square is $0$ or $1$ mod $4$, being $0$ exactly for even numbers.

- If $k\ge1$, the right side is $\equiv0\pmod4$. A sum of three numbers each equal to $0$ or $1$ mod $4$ is $\equiv0$ only if all three are $0$, so $x,y,z$ are even.
- If $k=0$: if $x,y$ are both odd, then $x^2y^2\equiv1$ while $x^2+y^2+z^2\equiv2$ or $3$. If exactly one of $x,y$ is odd, then $x^2y^2\equiv0$ while $x^2+y^2+z^2\equiv1+z^2\equiv1$ or $2$. So $x,y$ are both even. Then $x^2y^2\equiv0$ and $x^2+y^2+z^2\equiv z^2\pmod 4$, so $z^2\equiv0$ and $z$ is even.

This proves the claim.

Now suppose $(x,y,z)\ne(0,0,0)$ solves the original equation ($k=0$). By the claim $x,y,z$ are even; write $x=2x_1,y=2y_1,z=2z_1$. Then $4(x_1^2+y_1^2+z_1^2)=16x_1^2y_1^2$, i.e. $x_1^2+y_1^2+z_1^2=4x_1^2y_1^2$, an equation of the claim with $k=1$, so $x_1,y_1,z_1$ are even. Dividing by $2$ again gives the equation with $k=2$, and so on: in general $(x/2^j,y/2^j,z/2^j)$ is an integer solution of the equation with $k=j$, for every $j\ge0$. So $2^j$ divides each of $x,y,z$ for all $j$, which forces $x=y=z=0$, a contradiction.

Hence the only solution is $\boxed{(x,y,z)=(0,0,0)}$.

### o46
source: original
type: answer
difficulty: 5
techniques: descent, recursion
statement:
Find all pairs of positive integers $(a,b)$ with
$$a^2+b^2+1=3ab.$$
asked:
Describe every pair of positive integers satisfying the equation.
technique:
Treat the equation as a quadratic in $a$ for fixed $b$. Its two roots are linked, and replacing the larger variable by the other root gives a smaller solution.
hint:
Fix $b$ and think of $a$ as a root of $t^2-3bt+(b^2+1)=0$. What is the other root, and why is it a positive integer?
hint:
Assume $a>b$. Show the other root is smaller than $b$ (the case $b=1$ aside), so you can step down to a solution with smaller entries. Where does the process end, and how do you reverse it?
solution:
Define the sequence $u_0=u_1=1$ and $u_{n+1}=3u_n-u_{n-1}$, so $u_n=1,1,2,5,13,34,89,\dots$.

**Answer.** The solutions are exactly the pairs $(u_n,u_{n+1})$ and $(u_{n+1},u_n)$ for $n\ge0$: that is $(1,1),(1,2),(2,1),(2,5),(5,2),(5,13),(13,5),\dots$.

**These are solutions.** $(u_0,u_1)=(1,1)$ works: $1+1+1=3$. Suppose $(u_{n-1},u_n)$ is a solution. Then $u_{n-1}$ is a root of $t^2-3u_nt+u_n^2+1=0$, and the other root is $3u_n-u_{n-1}=u_{n+1}$ (sum of roots is $3u_n$). Since $u_{n+1}$ is a root, $(u_n,u_{n+1})$ satisfies $u_n^2+u_{n+1}^2+1=3u_nu_{n+1}$. Induction proves all these are solutions, and the equation is symmetric.

**There are no others.** Because the equation is symmetric, consider a solution $(a,b)$ with $a\ge b$ and prove by strong induction on $a$ that $(a,b)=(u_{n+1},u_n)$ for some $n\ge0$.

- If $a=b$, then $2a^2+1=3a^2$, so $a=1$: the pair $(u_1,u_0)$.
- If $b=1$ and $a>1$: $a^2+2=3a$ gives $a=2$ (as $a>1$), which is $(u_2,u_1)$.
- If $a>b\ge2$: $a$ is a root of $t^2-3bt+b^2+1=0$, so the other root is $a'=3b-a$, an integer, and $aa'=b^2+1>0$ shows $a'>0$. Since $a\ge b+1$, $a'=\dfrac{b^2+1}{a}\le\dfrac{b^2+1}{b+1}=b-1+\dfrac2{b+1}<b$ because $b\ge2$. So $(b,a')$ is a solution in positive integers with $a'<b<a$. Its larger entry $b$ is smaller than $a$, so by the induction hypothesis $(b,a')=(u_{n+1},u_n)$ for some $n$. Then $a=3b-a'=3u_{n+1}-u_n=u_{n+2}$, so $(a,b)=(u_{n+2},u_{n+1})$.

This completes the proof. (For $n\ge1$, $u_n=F_{2n-1}$, the Fibonacci numbers of odd index $1,3,5,7,\dots$ with $u_0=1$, so apart from $(1,1)$ the solutions are the pairs $(F_{2k-1},F_{2k+1})$ and their reversals.) The answer is the family $\boxed{(u_n,u_{n+1})\text{ and }(u_{n+1},u_n),\ n\ge0}$.

### o47
source: original
type: answer
difficulty: 2
techniques: parity
statement:
There are $2025$ lamps in a row, all initially off. A move consists of choosing any two lamps and switching both (an off lamp turns on, an on lamp turns off). What is the largest number of lamps that can be on at the same time?
asked:
Over all sequences of moves, find the maximum possible number of lit lamps and show it is attained.
technique:
Watch how the number of lit lamps can change in one move, and what that says about its parity.
hint:
A move toggles two lamps. List the possible changes in the number of lit lamps (both off, one of each, both on).
hint:
Show that the number of lit lamps is always even. Then find a sequence of moves reaching the largest even number allowed.
solution:
In one move two lamps are switched. If both were off, the number of lit lamps goes up by $2$; if one was on and one off, it is unchanged; if both were on, it goes down by $2$. So the number of lit lamps always changes by an even amount. It starts at $0$, so it is always even.

Since $2025$ is odd, all $2025$ lamps can never be on at once, so at most $2024$ are on.

This is attained: switch the pairs $(1,2),(3,4),\dots,(2023,2024)$, one move each. Then lamps $1,\dots,2024$ are on.

The answer is $\boxed{2024}$.

### o48
source: original
type: answer
difficulty: 2
techniques: modular-arithmetic, divisibility
statement:
What is the remainder when $1!+2!+3!+\dots+100!$ is divided by $60$?
asked:
Find the remainder of this huge sum upon division by $60$.
technique:
Work modulo $60$ and see which terms vanish.
hint:
Find the smallest $k$ for which $60$ divides $k!$.
hint:
Once $60\mid k!$, every larger factorial is also divisible by $60$. Compute the remaining terms directly.
solution:
Since $5!=120=2\cdot60$, for every $k\ge5$ the number $k!=5!\cdot6\cdots k$ is a multiple of $60$. Hence only the first four terms matter mod $60$:
$$1!+2!+3!+4!=1+2+6+24=33.$$
So the remainder is $\boxed{33}$.

### o49
source: original
type: proof
difficulty: 3
techniques: modular-arithmetic
statement:
Prove that the equation $x^3+y^3+z^3=2021$ has no solutions in integers $x,y,z$.
asked:
Show that no three integers have cubes summing to $2021$.
technique:
Look at cubes modulo a small number so that very few residues occur.
hint:
Compute the cubes of $0,1,\dots,8$ modulo $9$.
hint:
The cube of an integer mod $9$ takes only three values. List all the sums of three such values and compare with $2021\bmod 9$.
solution:
The cube of an integer depends only on the integer mod $9$:
$$0^3\equiv0,\ 1^3\equiv1,\ 2^3\equiv8,\ 3^3\equiv0,\ 4^3=64\equiv1,\ 5^3=125\equiv8,\ 6^3\equiv0,\ 7^3=343\equiv1,\ 8^3=512\equiv8.$$
So every cube is $\equiv0,1$ or $8\equiv-1\pmod9$.

A sum of three such numbers is of the form $\epsilon_1+\epsilon_2+\epsilon_3$ with each $\epsilon_i\in\{-1,0,1\}$, so it lies between $-3$ and $3$. Hence $x^3+y^3+z^3\bmod 9$ is one of $-3,-2,-1,0,1,2,3$, that is one of $6,7,8,0,1,2,3$. In particular it is never $4$ or $5$.

Now $2021=9\cdot224+5\equiv5\pmod9$. So $x^3+y^3+z^3\equiv5\pmod 9$ is impossible. $\blacksquare$

### o50
source: original
type: answer
difficulty: 4
techniques: casework
statement:
Find all real numbers $x$ such that
$$x^2-8\lfloor x\rfloor+5=0,$$
where $\lfloor x\rfloor$ denotes the greatest integer not exceeding $x$.
asked:
Determine every real solution of the equation.
technique:
Fix the integer part of $x$ and treat each possibility as its own case.
hint:
Let $n=\lfloor x\rfloor$. The equation says $x^2=8n-5$. What does this force for the sign of $x$ and for $n$?
hint:
The condition $n\le x<n+1$ turns into $n^2\le 8n-5<(n+1)^2$. Solve these two inequalities for the integer $n$.
solution:
Let $n=\lfloor x\rfloor$, so $n\le x<n+1$, and the equation reads $x^2=8n-5$.

Since $x^2\ge0$ we need $8n-5\ge0$, so $n\ge1$. Then $x\ge n\ge1>0$, so $x=\sqrt{8n-5}$, and the condition $n\le x<n+1$ is equivalent to
$$n^2\le 8n-5<(n+1)^2.$$

- $n^2\le8n-5\iff n^2-8n+5\le0\iff 4-\sqrt{11}\le n\le4+\sqrt{11}$, i.e. (for integers) $1\le n\le7$, since $4-\sqrt{11}\approx0.68$ and $4+\sqrt{11}\approx7.32$.
- $8n-5<(n+1)^2\iff n^2-6n+6>0\iff n<3-\sqrt3\approx1.27$ or $n>3+\sqrt3\approx4.73$. For integers $n\ge1$: $n=1$ or $n\ge5$.

Combining: $n\in\{1,5,6,7\}$. The corresponding values $8n-5$ are $3,35,43,51$.

So the solutions are $x=\boxed{\sqrt3,\ \sqrt{35},\ \sqrt{43},\ \sqrt{51}}$. (Check: $\lfloor\sqrt3\rfloor=1,\ \lfloor\sqrt{35}\rfloor=5,\ \lfloor\sqrt{43}\rfloor=6,\ \lfloor\sqrt{51}\rfloor=7$.)

### o51
source: original
type: answer
difficulty: 3
techniques: coloring
statement:
A $5\times5$ board has one bug in each of its $25$ cells. At noon every bug crawls to a cell sharing a side with its own cell. Can it happen that afterwards every cell again contains exactly one bug?
asked:
Decide whether all bugs can each move to a side-adjacent cell so that every cell still has exactly one bug.
technique:
Colour the cells in a pattern so that every move changes the colour, then count cells of each colour.
hint:
Colour the board like a chessboard. What colour is the destination of a bug that starts on a dark cell?
hint:
Count the dark and light cells of a $5\times5$ board, and count how many bugs must land on each colour.
solution:
**No.** Colour the board like a chessboard with the corners dark. A $5\times5$ board has $13$ dark and $12$ light cells.

A bug moving to a cell sharing a side changes colour. The $13$ bugs starting on dark cells therefore end on light cells. But there are only $12$ light cells, so some light cell would contain at least two bugs. Hence it is impossible. The answer is $\boxed{\text{No}}$.

### o53
source: original
type: answer
difficulty: 3
techniques: symmetry
statement:
Let $f(x)=\dfrac{4^x}{4^x+2}$. Evaluate
$$f\!\left(\tfrac1{100}\right)+f\!\left(\tfrac2{100}\right)+\dots+f\!\left(\tfrac{99}{100}\right).$$
asked:
Find the exact value of the sum of these $99$ function values.
technique:
Pair the terms that are mirror images around the middle of the range and see what each pair adds to.
hint:
The arguments $\frac k{100}$ and $\frac{100-k}{100}$ add up to $1$. Compute $f(x)+f(1-x)$.
hint:
Use $4^{1-x}=\dfrac4{4^x}$ to simplify $f(1-x)$. Then count the pairs and don't forget the middle term $k=50$.
solution:
First, for any real $x$, using $4^{1-x}=\frac{4}{4^x}$,
$$f(1-x)=\frac{4/4^x}{4/4^x+2}=\frac{4}{4+2\cdot4^x}=\frac2{2+4^x}.$$
Therefore
$$f(x)+f(1-x)=\frac{4^x}{4^x+2}+\frac2{4^x+2}=1.$$

The $99$ terms $k=1,\dots,99$ split into the $49$ pairs $\{k,100-k\}$ for $k=1,\dots,49$, plus the middle term $k=50$. Each pair adds up to $1$, and $f(\tfrac12)=\dfrac{2}{2+2}=\dfrac12$. The sum is
$$49\cdot1+\frac12=\boxed{\dfrac{99}{2}}.$$

### o54
source: original
type: answer
difficulty: 4
techniques: constructive, pigeonhole
statement:
What is the largest number of elements a subset of $\{1,2,\dots,100\}$ can have if it contains no two numbers one of which is exactly twice the other?
asked:
Find the maximum size of a subset of $\{1,\dots,100\}$ with no pair $(m,2m)$ both in it, and show it can be achieved.
technique:
Partition the numbers into chains in which the forbidden pairs are neighbours, bound each chain, then build an example matching the bound.
hint:
Every number can be written as $m\cdot2^j$ with $m$ odd. Group numbers by their odd part $m$; a forbidden pair is two consecutive members of such a chain.
hint:
In a chain of length $L$, at most $\lceil L/2\rceil$ elements can be chosen with no two consecutive. Find how many chains have each length, add up the bounds, and check that choosing alternate elements attains them.
solution:
Write each $k\in\{1,\dots,100\}$ uniquely as $k=m\cdot2^j$ with $m$ odd. For a fixed odd $m$, the numbers with this odd part form the chain $m,2m,4m,\dots$ (up to $100$). Two numbers where one is twice the other are exactly two consecutive members of one chain.

If a chain has $L$ members, a subset with no two consecutive members has at most $\lceil L/2\rceil$ of them: group the chain into $\lfloor L/2\rfloor$ pairs of consecutive members, plus a singleton if $L$ is odd; each pair contributes at most one element and the singleton at most one. Taking the 1st, 3rd, 5th, ... members attains exactly $\lceil L/2\rceil$.

The chains by odd part $m$:

| $L$ | odd $m$ | number of chains | max chosen each |
|---|---|---|---|
| 7 | 1 | 1 | 4 |
| 6 | 3 | 1 | 3 |
| 5 | 5 | 1 | 3 |
| 4 | 7, 9, 11 | 3 | 2 |
| 3 | 13, 15, ..., 25 | 7 | 2 |
| 2 | 27, 29, ..., 49 | 12 | 1 |
| 1 | 51, 53, ..., 99 | 25 | 1 |

(Check: chain length is the number of $j$ with $m2^j\le100$; the chains contain $7+6+5+12+21+24+25=100$ numbers.)

The maximum is
$$4+3+3+3\cdot2+7\cdot2+12\cdot1+25\cdot1=4+3+3+6+14+12+25=\boxed{67}.$$
It is attained by choosing from each chain the 1st, 3rd, 5th, ... member, and different chains do not interact, since a pair $(k,2k)$ always lies in one chain.

### o56
source: original
type: answer
difficulty: 3
techniques: double-counting
statement:
At a camp there are $15$ students. The staff splits them into teams of three students each (a student may be on several teams) in such a way that every pair of students is together on exactly one team. How many teams are there?
asked:
Find the total number of teams.
technique:
Count, in two different ways, the pairs consisting of a student and a team that student is on. First find how many teams one student is on.
hint:
Fix a student $S$. Each of the other $14$ students shares exactly one team with $S$. How many other students does one team containing $S$ include?
hint:
Once you know how many teams each student is on, count all (student, team) memberships in two ways: by students and by teams.
solution:
Fix a student $S$. Each of the other $14$ students is on exactly one team with $S$, and each team containing $S$ has exactly $2$ other students. So the teams containing $S$ partition the other $14$ students into pairs: $S$ is on $14/2=7$ teams.

Now count the pairs (student, team on which the student plays) in two ways. Each of the $15$ students is on $7$ teams, giving $15\cdot7=105$ pairs. Each team has $3$ students, so with $T$ teams there are $3T$ pairs. Hence $3T=105$ and $T=\boxed{35}$.

(Such a system of teams exists: take the $15$ nonzero vectors of $\mathbb F_2^4$ as students and the triples $\{a,b,a+b\}$ as teams.)

### o58
source: original
type: answer
difficulty: 5
techniques: recursion
statement:
In how many ways can a $3\times12$ rectangle be tiled by $1\times2$ dominoes (placed horizontally or vertically, without overlap, covering everything)?
asked:
Count the domino tilings of a $3\times 12$ board.
technique:
Look at the leftmost column and ask what covers it. You will need a second family of shapes, such as the board with one corner cell removed, to close the system of recurrences.
hint:
Let $a_n$ be the number of tilings of a $3\times n$ board, and $b_n$ the number for a $3\times n$ board with its top-left cell removed. Look at the cell in the top-left corner (for $a_n$) and the cell below it (for $b_n$) and see how each can be covered.
hint:
You should find $a_n=a_{n-2}+2b_{n-1}$ and $b_n=b_{n-2}+a_{n-1}$. Start from $a_0=1,\ b_0=0,\ b_1=1$ and compute up to $a_{12}$.
solution:
Let $a_n$ be the number of tilings of the $3\times n$ board (with $a_0=1$), and $b_n$ the number of tilings of the $3\times n$ board with the top cell of the first column removed (so $b_0=0$, $b_1=1$, and $b_n=0$ for even $n$, a count of cells being odd). By symmetry, removing the bottom cell gives the same number $b_n$.

**Recurrence for $a_n$ ($n\ge2$).** Look at the top cell of the first column.
- It is covered by a vertical domino with the cell below it. Then the bottom cell of column 1 must be covered by a horizontal domino reaching into column 2. What is left is the board with columns $2,\dots,n$ and the bottom cell of column 2 removed: $b_{n-1}$ ways (by the symmetry).
- It is covered by a horizontal domino with the top cell of column 2. Then the middle cell of column 1 is covered either vertically with the bottom cell, leaving the board of columns $2,\dots,n$ with the top cell of column 2 removed: $b_{n-1}$ ways; or horizontally into column 2, and then the bottom cell of column 1 is forced to be horizontal too, filling both columns: $a_{n-2}$ ways.

So $a_n=a_{n-2}+2b_{n-1}$.

**Recurrence for $b_n$ ($n\ge2$).** The first column has only its middle and bottom cells. The middle cell is covered:
- vertically with the bottom cell: the rest is a full $3\times(n-1)$ board, $a_{n-1}$ ways;
- horizontally into column 2: then the bottom cell of column 1 must be horizontal too. In column 2 only the top cell is left, which must be covered horizontally with the top cell of column 3; what remains is columns $3,\dots,n$ with the top cell of column 3 removed, $b_{n-2}$ ways.

So $b_n=a_{n-1}+b_{n-2}$.

**Computation.** Using $a_0=1,\ b_0=0,\ b_1=1$ (and $a_1=0$), and only the odd-$n$ values of $b$ and even-$n$ values of $a$ matter:
$$\begin{aligned}
a_2&=a_0+2b_1=3, & b_3&=a_2+b_1=4,\\
a_4&=a_2+2b_3=11, & b_5&=a_4+b_3=15,\\
a_6&=a_4+2b_5=41, & b_7&=a_6+b_5=56,\\
a_8&=a_6+2b_7=153, & b_9&=a_8+b_7=209,\\
a_{10}&=a_8+2b_9=571, & b_{11}&=a_{10}+b_9=780,\\
a_{12}&=a_{10}+2b_{11}=2131.
\end{aligned}$$

The number of tilings is $\boxed{2131}$.

### o59
source: original
type: answer
difficulty: 4
techniques: recursion
statement:
How many permutations $\sigma$ of $\{1,2,\dots,7\}$ have no fixed point, that is, $\sigma(i)\ne i$ for every $i$?
asked:
Count the arrangements of $1,\dots,7$ in which no number stays in its own position.
technique:
Let $D_n$ be the count for $n$ numbers. Decide where the last number goes and relate what remains to the smaller counts $D_{n-1}$ and $D_{n-2}$.
hint:
Let $\sigma(n)=k$ with $k\ne n$ ($n-1$ choices). Split into two cases: $\sigma(k)=n$ or $\sigma(k)\ne n$.
hint:
In the first case, the other $n-2$ numbers form a smaller derangement. In the second, if $\sigma(j)=n$, redefine the value at $j$ to be $k$ and delete $n$. Show this gives a derangement of $n-1$ elements and that it is reversible.
solution:
Call such a permutation a derangement and let $D_n$ be the number of derangements of $\{1,\dots,n\}$. Clearly $D_1=0$ and $D_2=1$.

**Claim:** $D_n=(n-1)(D_{n-1}+D_{n-2})$ for $n\ge3$.

Let $\sigma$ be a derangement of $\{1,\dots,n\}$ and $k=\sigma(n)$; then $k\ne n$, giving $n-1$ choices of $k$. Fix $k$ and count the derangements with $\sigma(n)=k$.

- *Case $\sigma(k)=n$.* Then $\sigma$ swaps $n$ and $k$, and on the remaining $n-2$ numbers it is a derangement of that set. Conversely any derangement of those $n-2$ numbers extends. So there are $D_{n-2}$ such $\sigma$.
- *Case $\sigma(k)\ne n$.* Let $j$ be the element with $\sigma(j)=n$; then $j\ne n$ (as $\sigma(n)=k\ne n$) and $j\ne k$. Define $\sigma'$ on $\{1,\dots,n-1\}$ by $\sigma'(j)=k$ and $\sigma'(i)=\sigma(i)$ for $i\notin\{j,n\}$. The values of $\sigma$ on $\{1,\dots,n-1\}\setminus\{j\}$ are all numbers except $n$ and $k$ (the values $\sigma(j)=n$ and $\sigma(n)=k$ are the other two), so $\sigma'$ is a permutation of $\{1,\dots,n-1\}$, and it has no fixed point ($\sigma'(j)=k\ne j$). Conversely, given a derangement $\sigma'$ of $\{1,\dots,n-1\}$, put $j=\sigma'^{-1}(k)$ (note $j\ne k$), and define $\sigma(n)=k$, $\sigma(j)=n$, $\sigma(i)=\sigma'(i)$ otherwise: this is a derangement of $\{1,\dots,n\}$ with $\sigma(k)\ne n$, and the two constructions are inverse. So there are $D_{n-1}$ such $\sigma$.

Adding the cases and multiplying by the $n-1$ choices of $k$ proves the claim.

Now compute:
$$D_3=2(1+0)=2,\quad D_4=3(2+1)=9,\quad D_5=4(9+2)=44,\quad D_6=5(44+9)=265,\quad D_7=6(265+44)=1854.$$
The answer is $\boxed{1854}$.

### o61
source: original
type: answer
difficulty: 4
techniques: graph-theory, extremal
statement:
A graph on $10$ vertices has $m$ edges (no loops, no multiple edges). Find the smallest $m$ such that every such graph with $m$ edges is connected.
asked:
Find the least number of edges that forces a $10$-vertex graph to be connected, and justify that fewer edges do not force it.
technique:
Think of the largest number of edges a disconnected graph can have.
hint:
Find a disconnected graph on $10$ vertices with as many edges as possible. A natural candidate is a complete graph plus something small.
hint:
If a graph is disconnected, split the vertices into two nonempty parts with no edges between them, of sizes $k$ and $10-k$. Bound the number of edges by $\binom k2+\binom{10-k}2$ and show this is at most $\binom92$. The identity $k(10-k)-9=(k-1)(9-k)$ helps.
solution:
**A disconnected graph with $36$ edges exists.** Take a complete graph on $9$ vertices ($\binom92=36$ edges) and an isolated tenth vertex. It is disconnected. Removing edges from it gives disconnected graphs with every number of edges $m\le36$. So no $m\le36$ forces connectivity.

**Every graph with $37$ edges is connected.** Let $G$ be disconnected on $10$ vertices. Choose a connected component with vertex set of size $k$, $1\le k\le9$; there are no edges between it and the other $10-k$ vertices, so the number of edges is at most
$$\binom k2+\binom{10-k}2=\frac{k^2+(10-k)^2-10}2=\frac{100-2k(10-k)-10}2=45-k(10-k).$$
Now $k(10-k)-9=(k-1)(9-k)\ge0$ for $1\le k\le9$, so $k(10-k)\ge9$ and the number of edges is at most $45-9=36$.

Hence a graph with at least $37$ edges is connected, and the smallest such $m$ is $\boxed{37}$.
