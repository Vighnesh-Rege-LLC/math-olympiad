### o87
source: original
type: answer
difficulty: 1
techniques: coloring
statement:
A bug walks on a $3\times3$ board made of nine unit cells. In each step it moves to a cell that shares a side with its current cell. The bug starts in the middle cell of the top row. Can it visit every cell of the board exactly once?
asked:
Decide whether the bug can make a walk that starts in the middle cell of the top row and visits each of the nine cells exactly once.
technique:
Paint the cells in a pattern and watch how the colours change as the bug moves.
hint:
Colour the board like a chessboard, with the four corner cells black. How many cells of each colour are there? What colour is the starting cell?
hint:
Each step goes to a cell of the opposite colour. Write down the colours the bug sees, in order, for a walk through all nine cells.
hint:
Count how many cells of the starting colour the walk would need, and compare with how many exist.
solution:
The answer is no.

Colour the board like a chessboard with the four corners black. Then the black cells are the four corners and the centre, so there are $5$ black cells, and the other $4$ cells (the middles of the sides) are white. The starting cell, the middle of the top row, is white.

Two cells sharing a side always have different colours, so the colours along the walk alternate. A walk through all nine cells starting at a white cell sees the colours W, B, W, B, W, B, W, B, W. It would use $5$ white cells. But there are only $4$ white cells. Hence no such walk exists: $\boxed{\text{No}}$.

### o88
source: original
type: answer
difficulty: 2
techniques: extremal
statement:
Several distinct positive integers add up to exactly $100$. What is the largest possible number of integers in such a collection?
asked:
Find the greatest $n$ for which there are $n$ distinct positive integers with sum $100$.
technique:
To fit as many numbers as possible into a fixed total, think about the cheapest choice.
hint:
Suppose there are $n$ numbers. Sort them from smallest to largest. How small can the smallest one be? The second smallest? The $k$-th smallest?
hint:
Show the $k$-th smallest is at least $k$, so the total is at least $1+2+\dots+n$. Find the largest $n$ for which this is at most $100$.
hint:
Finally show that this largest $n$ is really achievable: you must hit $100$ exactly, not just stay below it.
solution:
Suppose $n$ distinct positive integers have sum $100$, and sort them as $a_1<a_2<\dots<a_n$. Since they are distinct positive integers, $a_1\ge1$ and each next one is at least one more than the previous, so $a_k\ge k$ for every $k$. Hence
$$100=a_1+\dots+a_n\ge1+2+\dots+n=\frac{n(n+1)}2.$$
For $n=14$ the right side is $105>100$, and it only grows with $n$. So $n\le13$.

For $n=13$ take $1,2,\dots,12$ (sum $78$) and $22$. These are distinct and sum to $100$. So the maximum is $\boxed{13}$.

### o89
source: original
type: answer
difficulty: 2
techniques: graph-theory
statement:
Five people are at a party. Friendship is mutual, and each person is either a friend of another person or not. Is it possible that the numbers of friends the five people have (among the other four) are exactly $4,4,3,2,1$ in some order?
asked:
Decide whether the five people can have $4,4,3,2,1$ friends respectively.
technique:
Draw people as points and friendships as segments between them, and look at the extreme degrees.
hint:
Look at a person who has $4$ friends. Who are those friends?
hint:
There are two people with $4$ friends. What is then the least number of friends that anyone at the party can have?
solution:
The answer is no.

Suppose it were possible. A person with $4$ friends is a friend of all four other people. Call the two people with $4$ friends $A$ and $B$. Every other person is a friend of $A$ and also a friend of $B$, so each of the other three people has at least $2$ friends. (Also $A$ and $B$ themselves have $4$.) Hence every one of the five people has at least $2$ friends. But the person who is supposed to have exactly $1$ friend contradicts this. So $\boxed{\text{No}}$.

(The degree sum $4+4+3+2+1=14$ is even, so a parity count alone does not rule this out.)

### o90
source: original
type: answer
difficulty: 2
techniques: casework
statement:
In how many ways can exactly $50$ cents be paid using pennies ($1$ cent), nickels ($5$ cents), dimes ($10$ cents) and quarters ($25$ cents)? Two ways are the same if they use the same number of coins of each kind (the order does not matter, and a kind of coin may be used zero times).
asked:
Count the quadruples (pennies, nickels, dimes, quarters) of non-negative integers with total value $50$ cents.
technique:
Split the count by how many of the largest coins are used, so that each piece is a smaller, easier count.
hint:
Split into cases by the number of quarters: $0$, $1$ or $2$. In each case the remaining amount must be paid with pennies, nickels and dimes.
hint:
Once the numbers of dimes and nickels are chosen, the pennies are forced. So for each amount to pay, count the choices of (dimes, nickels) whose value does not exceed that amount.
hint:
For an amount $A$ divisible by $5$, with $d$ dimes the remaining $A-10d$ allows nickels from $0$ up to $(A-10d)/5$.
solution:
The pennies are determined by the other three numbers (they make up the remainder), so we count choices of quarters $q$, dimes $d$ and nickels $n$ with $25q+10d+5n\le50$.

**$q=0$.** Need $10d+5n\le50$. For each $d=0,1,\dots,5$, the number of nickels can be $0,1,\dots,\frac{50-10d}5$, which is $11-2d$ choices. Total: $11+9+7+5+3+1=36$.

**$q=1$.** Need $10d+5n\le25$. Then $d\in\{0,1,2\}$, and nickels range over $0,\dots,\lfloor\frac{25-10d}5\rfloor=5-2d$, giving $6-2d$ choices: $6+4+2=12$.

**$q=2$.** Then $10d+5n\le0$ forces $d=n=0$: $1$ way.

Total: $36+12+1=\boxed{49}$.

### o91
source: original
type: answer
difficulty: 2
techniques: symmetry
statement:
Find the sum of all positive integers less than $100$ that have no common prime factor with $100$ (that is, $\gcd(n,100)=1$).
asked:
Compute $\sum n$ over all $n$ with $1\le n<100$ and $\gcd(n,100)=1$.
technique:
Look for a transformation of the set of terms that sends it to itself, and use it to group the terms.
hint:
If $n$ has no common factor with $100$, what about $100-n$? Compare $\gcd(n,100)$ and $\gcd(100-n,100)$.
hint:
So the allowed numbers split into pairs $\{n,100-n\}$ with a fixed sum. Check that no number is paired with itself, then count the numbers.
hint:
The allowed numbers are the odd numbers not divisible by $5$. Count them.
solution:
Let $S$ be the set of integers $n$ with $1\le n\le 99$ and $\gcd(n,100)=1$. Any common divisor of $n$ and $100$ also divides $100-n$, and conversely any common divisor of $100-n$ and $100$ divides $n$. So $\gcd(100-n,100)=\gcd(n,100)$, and $n\mapsto100-n$ maps $S$ to itself.

Moreover $n=100-n$ would give $n=50$, which is not in $S$. So $S$ splits into pairs $\{n,100-n\}$, each with sum $100$.

Now count $S$. Since $100=2^2\cdot5^2$, $n\in S$ exactly when $n$ is odd and not a multiple of $5$. Among $1,\dots,99$ there are $50$ odd numbers, of which $10$ are multiples of $5$ ($5,15,\dots,95$). So $|S|=40$, forming $20$ pairs.

The sum is $20\cdot100=\boxed{2000}$.

### o92
source: original
type: answer
difficulty: 1
techniques: double-counting
statement:
A school has $30$ students and some number of clubs. Every student belongs to exactly $3$ clubs, and every club has exactly $10$ members. How many clubs does the school have?
asked:
Find the number of clubs.
technique:
Count one and the same collection of facts in two different ways.
hint:
Count the memberships, that is, the pairs (student, club) with the student in the club.
hint:
Count these pairs once by going through the students, and once by going through the clubs. Both counts give the same total.
solution:
Let $c$ be the number of clubs and count the pairs (student, club) in which the student belongs to the club.

Going through the students: each of the $30$ students is in $3$ clubs, giving $30\cdot3=90$ pairs.

Going through the clubs: each of the $c$ clubs has $10$ members, giving $10c$ pairs.

So $10c=90$ and $c=\boxed{9}$.

Such a school exists: split the students into three groups of $10$ and the clubs into three groups of $3$, and let every student of the $i$-th group belong to the three clubs of the $i$-th group of clubs.

### o93
source: original
type: answer
difficulty: 2
techniques: recursion
statement:
A staircase has $10$ steps. In one move you climb $1$, $2$ or $3$ steps. In how many different ways can you go from the ground to the top of the staircase? Two ways are different if the sequences of move sizes are different (for example $1,2$ and $2,1$ are different ways to climb $3$ steps).
asked:
Count the sequences of moves of sizes $1$, $2$, $3$ whose sizes add up to $10$.
technique:
Relate the answer for a staircase of $n$ steps to the answers for shorter staircases, then build up from the small cases.
hint:
Let $a_n$ be the number of ways to climb $n$ steps. Look at the last move of a climb. What can it be, and what is left to climb before it?
hint:
This gives $a_n$ in terms of $a_{n-1}$, $a_{n-2}$ and $a_{n-3}$. Work out $a_1,a_2,a_3$ directly and then continue up to $a_{10}$.
solution:
Let $a_n$ be the number of ways to climb $n$ steps, and set $a_0=1$ (one way to climb nothing). Consider the last move of a climb of $n\ge3$ steps. It climbs $1$, $2$ or $3$ steps, and before it the climber has climbed $n-1$, $n-2$ or $n-3$ steps in an arbitrary valid way. These three cases are disjoint and cover everything, so
$$a_n=a_{n-1}+a_{n-2}+a_{n-3}\qquad(n\ge3).$$
Directly: $a_1=1$ (just $1$), $a_2=2$ ($1,1$ and $2$), and $a_3=4$ ($1,1,1$; $1,2$; $2,1$; $3$), which agrees with $a_2+a_1+a_0=4$.

Continuing: $a_4=4+2+1=7$, $a_5=7+4+2=13$, $a_6=13+7+4=24$, $a_7=24+13+7=44$, $a_8=44+24+13=81$, $a_9=81+44+24=149$, $a_{10}=149+81+44=\boxed{274}$.

### o94
source: original
type: proof
difficulty: 2
techniques: constructive, induction
statement:
Prove that for every integer $n\ge3$ there are $n$ pairwise distinct positive integers $d_1,\dots,d_n$ with
$$\frac1{d_1}+\frac1{d_2}+\dots+\frac1{d_n}=1.$$
asked:
For each $n\ge3$, exhibit (describe how to build) $n$ distinct positive integers whose reciprocals add up to $1$.
technique:
Find one small example, then look for a move that turns an example with $n$ terms into one with $n+1$ terms.
hint:
Start with $n=3$ and find three distinct unit fractions summing to $1$. Then try to split one fraction $\frac1m$ into two smaller unit fractions.
hint:
Check the identity $\frac1m=\frac1{m+1}+\frac1{m(m+1)}$.
hint:
Which fraction should be split, so that the new denominators do not clash with the old ones?
solution:
We build the examples one after another.

**$n=3$.** $\frac12+\frac13+\frac16=1$, with denominators $2,3,6$.

**From $n$ to $n+1$.** Suppose $d_1<d_2<\dots<d_n$ are distinct positive integers with $\sum\frac1{d_i}=1$, and let $m=d_n$ be the largest one; $m\ge3$ since $n\ge3$. For every positive integer $m$,
$$\frac1{m+1}+\frac1{m(m+1)}=\frac{m+1}{m(m+1)}=\frac1m.$$
Replace $\frac1{d_n}=\frac1m$ by $\frac1{m+1}+\frac1{m(m+1)}$. The sum is still $1$ and now there are $n+1$ terms, with denominators $d_1,\dots,d_{n-1},\,m+1,\,m(m+1)$. They are distinct: $d_1,\dots,d_{n-1}$ are all smaller than $m$, while $m+1>m$ and $m(m+1)>m+1$ (because $m>1$).

By induction, examples exist for every $n\ge3$. $\blacksquare$

(For instance $n=4$: $2,3,7,42$; $n=5$: $2,3,7,43,1806$.)

### o95
source: original
type: answer
difficulty: 5
techniques: coloring, constructive
statement:
Number the rows and columns of a $7\times7$ board $1,2,\dots,7$. Sixteen non-overlapping $1\times3$ tiles are placed on the board, each covering three cells in a row or three cells in a column, so that exactly one cell is left uncovered. Determine all cells that can be the uncovered cell.
asked:
Find every cell (row, column) of the board that can be the single uncovered cell in such a placement of sixteen tiles.
technique:
Colour the cells so that every tile covers a known pattern of colours, then compare with the colour counts of the board. You also need to show that each cell you allow really occurs.
hint:
Colour the cell in row $i$ and column $j$ by the remainder of $i+j$ modulo $3$. What colours does one tile cover, horizontal or vertical?
hint:
Count how many cells of each colour the board has. Sixteen tiles cover equally many cells of each colour, so the uncovered cell has a colour that is determined by the counts.
hint:
Repeat with the remainder of $i-j$ modulo $3$ and combine the two conditions. Then show, with explicit tilings, that all the cells you found are possible. Symmetry reduces the number of tilings to draw.
solution:
Write $(i,j)$ for the cell in row $i$ and column $j$.

**Necessary conditions.** A tile covers three consecutive cells in a row, whose values of $j$ are $j,j+1,j+2$, or three consecutive cells in a column. In either case the values of $i+j$ modulo $3$ are $0,1,2$ in some order, and so are the values of $i-j$ modulo $3$ (the difference changes by $\pm1$ at each cell along a row or a column). So each tile covers exactly one cell of each residue class of $i+j$ and one of each class of $i-j$. Sixteen tiles therefore cover exactly $16$ cells of each class, so the uncovered cell must lie in a class that contains $16+1=17$ cells of the board (and the other two classes must contain $16$).

Count the board's classes. Among $1,\dots,7$ there are $3$ numbers $\equiv1\pmod 3$ ($1,4,7$), $2$ numbers $\equiv2$ ($2,5$) and $2$ numbers $\equiv0$ ($3,6$). The number of cells with $i+j\equiv0$ is $3\cdot2+2\cdot3+2\cdot2=16$ (residue pairs $(1,2),(2,1),(0,0)$). With $i+j\equiv1$: pairs $(1,0),(0,1),(2,2)$ give $6+6+4=16$. With $i+j\equiv2$: pairs $(1,1),(2,0),(0,2)$ give $9+4+4=17$. Hence the uncovered cell has $i+j\equiv2\pmod3$.

Similarly for $i-j$: $i-j\equiv0$ comes from pairs $(1,1),(2,2),(0,0)$, giving $9+4+4=17$ cells; $i-j\equiv1$ comes from $(1,0),(2,1),(0,2)$, giving $6+6+4=16$; $i-j\equiv2$ comes from $(0,1),(1,2),(2,0)$, giving $6+6+4=16$. So the uncovered cell has $i\equiv j\pmod 3$.

Adding, $2i\equiv i+j\equiv2$, so $i\equiv1$, and then $j\equiv1\pmod3$. Thus $i,j\in\{1,4,7\}$: at most nine cells are possible.

**All nine occur.**
- Uncovered $(1,b)$ with $b\in\{1,4,7\}$: in row $1$ the cells to the left of column $b$ and to the right of it form blocks of lengths $b-1$ and $7-b$, which are $0,6$ or $3,3$ or $6,0$; cover each block with horizontal tiles. Rows $2$ to $7$ form a $6\times7$ rectangle: in each column place two vertical tiles.
- Uncovered $(7,b)$: the same picture reflected top to bottom. Uncovered $(a,1)$ and $(a,7)$: the same pictures with rows and columns exchanged. This gives eight cells $(1,1),(1,4),(1,7),(7,1),(7,4),(7,7),(4,1),(4,7)$.
- Uncovered $(4,4)$: use four rectangles around the centre: rows $1$–$3$ by columns $1$–$4$ (four vertical tiles), rows $1$–$4$ by columns $5$–$7$ (four horizontal tiles), rows $5$–$7$ by columns $4$–$7$ (four vertical tiles), rows $4$–$7$ by columns $1$–$3$ (four horizontal tiles). They are disjoint, cover $48$ cells, and miss only $(4,4)$.

So the possible uncovered cells are exactly the nine cells $(i,j)$ with $i,j\in\{1,4,7\}$.

$\boxed{(i,j)\ \text{with}\ i,j\in\{1,4,7\}}$

### o96
source: original
type: proof
difficulty: 5
techniques: extremal, graph-theory
statement:
In a group of people, some pairs know each other (knowing is mutual). Prove that the people can be divided into two teams (one of them may be empty) so that every person knows at least as many people in the other team as in their own team.
asked:
Show that a split into two teams exists in which no one has strictly more acquaintances in their own team than in the opposite team.
technique:
There are only finitely many ways to split the group, so some split is best in a measurable sense.
hint:
Among all splits, choose one that maximizes a suitable count of acquaintance pairs. Which pairs should the count be about?
hint:
Count the acquainted pairs whose two members lie in different teams, and take a split with the most such pairs. Suppose some person $v$ has more acquaintances in their own team than in the other team.
hint:
Move $v$ to the other team. Count exactly how many acquainted pairs change from "same team" to "different teams" and vice versa, and compare.
solution:
Model the group as a graph: people are vertices, and two vertices are joined by an edge when the people know each other. A split is a choice of two (possibly empty) teams $A$, $B$ with $A\cup B$ equal to the whole group and $A\cap B=\emptyset$. Call an edge *crossing* if its endpoints are in different teams.

There are finitely many splits, so we may choose a split for which the number of crossing edges is as large as possible. We claim this split has the required property.

Suppose not: some person $v$, say in team $A$, has $s$ acquaintances in $A$ and $t$ acquaintances in $B$ with $s>t$. Move $v$ to team $B$, keeping everybody else where they are. Only edges at $v$ can change their status:
- The $s$ edges from $v$ to acquaintances in $A$ were not crossing and become crossing.
- The $t$ edges from $v$ to acquaintances in $B$ were crossing and become non-crossing.
All other edges are unchanged. So the number of crossing edges increases by $s-t>0$, contradicting the maximality of our split.

Hence in the chosen split nobody has more acquaintances in their own team than in the other team. $\blacksquare$

### o97
source: original
type: proof
difficulty: 5
techniques: graph-theory, extremal
statement:
A country has several cities, and some pairs of cities are joined by a direct two-way road (at most one road between two cities). Every city has direct roads to at least three other cities. Prove that one can start in some city, travel along a closed route that uses at least three different roads, visits an even number of different cities, never visits a city twice (except returning to the start), and comes back to the start.
asked:
Prove that the road network contains a cycle with an even number of cities (equivalently, an even number of roads).
technique:
Look at an extreme object in the network, such as a route that cannot be extended, and use what the degree condition says about its end.
hint:
Take a route (a path without repeated cities) with as many cities as possible. Where can the neighbours of its first city lie?
hint:
The first city $v_0$ has at least three neighbours, all on the path $v_0,v_1,\dots,v_m$. Besides $v_1$ there are two more, $v_i$ and $v_j$ with $2\le i<j$. Each of them closes a cycle with the path.
hint:
There are three natural cycles using $v_0$, $v_i$, $v_j$. Compute their numbers of cities, and see what happens if all of them are odd.
solution:
Because there are finitely many cities, we can choose a longest path $v_0v_1\dots v_m$ (the cities $v_0,\dots,v_m$ are all different, consecutive ones are joined by roads, and $m$ is as large as possible).

Every neighbour of $v_0$ lies on this path. Indeed, if $v_0$ had a neighbour $w$ outside the path, then $w v_0 v_1\dots v_m$ would be a longer path.

The city $v_0$ has at least three neighbours, all among $v_1,\dots,v_m$. One of them is $v_1$ (it is joined to $v_0$ by the path), so at least two others exist; call them $v_i$ and $v_j$ with $2\le i<j\le m$.

Consider these three closed routes:
1. $v_0v_1\dots v_iv_0$, which visits $i+1$ cities ($i+1\ge3$);
2. $v_0v_1\dots v_jv_0$, which visits $j+1$ cities;
3. $v_0v_iv_{i+1}\dots v_jv_0$, which visits $(j-i+1)+1=j-i+2$ cities ($\ge3$ since $j>i$).

Each is a cycle: the cities in each list are distinct and consecutive ones are joined (using the roads $v_0v_i$ and $v_0v_j$ for the closing steps).

Suppose all three numbers of cities were odd. Then $i+1$ odd gives $i$ even, and $j+1$ odd gives $j$ even. But then $j-i+2$ is even, a contradiction. So at least one of the three cycles has an even number of cities. $\blacksquare$

### o98
source: original
type: answer
difficulty: 4
techniques: casework
statement:
Find the number of quadruples $(a,b,c,d)$ of positive integers with $a\le b\le c\le d$ such that
$$\frac1a+\frac1b+\frac1c+\frac1d=1.$$
asked:
Count the non-decreasing quadruples of positive integers whose reciprocals add up to $1$.
technique:
Bound the smallest variable, then let each of its possible values open a smaller problem with fewer unknowns.
hint:
Since $a$ is the smallest, $1=\frac1a+\dots\le\frac4a$. Find the possible values of $a$, and rule out $a=1$.
hint:
For each value of $a$, bound $b$ in the same way using the remaining sum $1-\frac1a$ shared by three fractions.
hint:
Once $a$ and $b$ are fixed you must solve $\frac1c+\frac1d=\frac pq$. Bound $c$ again and solve for $d$, or use a factoring trick when the right side is a unit fraction $\frac1k$, namely $(c-k)(d-k)=k^2$.
solution:
Since all four fractions are positive, $a\ge2$. Also $1\le\frac4a$ gives $a\le4$. We treat the cases $a=2,3,4$ and use repeatedly that for $x\le y$ with $\frac1x+\frac1y=s$ we have $\frac1x<s\le\frac2x$.

**Case $a=2$.** Then $\frac1b+\frac1c+\frac1d=\frac12$ with $b\ge2$. Since $\frac1b<\frac12$, $b\ge3$; and $\frac12\le\frac3b$ gives $b\le6$.
- $b=3$: $\frac1c+\frac1d=\frac16$, with $c\ge7$ and $\frac16\le\frac2c$ so $c\le12$. Multiplying out, $(c-6)(d-6)=36$ with $1\le c-6\le d-6$. So $c-6\in\{1,2,3,4,6\}$ and $(c,d)=(7,42),(8,24),(9,18),(10,15),(12,12)$: $5$ solutions.
- $b=4$: $\frac1c+\frac1d=\frac14$, $c\ge5$, and $(c-4)(d-4)=16$ with $1\le c-4\le d-4$: $c-4\in\{1,2,4\}$, $(c,d)=(5,20),(6,12),(8,8)$: $3$ solutions.
- $b=5$: $\frac1c+\frac1d=\frac3{10}$ with $c\ge5$ and $\frac3{10}\le\frac2c$, so $c\le6$. $c=5$ gives $\frac1d=\frac1{10}$, $d=10$. $c=6$ gives $\frac1d=\frac3{10}-\frac16=\frac2{15}$, not a unit fraction. $1$ solution: $(2,5,5,10)$.
- $b=6$: $\frac1c+\frac1d=\frac13$ with $c\ge6$ and $\frac13\le\frac2c$, so $c\le6$. $c=6$ gives $d=6$. $1$ solution: $(2,6,6,6)$.

That is $5+3+1+1=10$ solutions.

**Case $a=3$.** Then $\frac1b+\frac1c+\frac1d=\frac23$ with $b\ge3$ and $\frac23\le\frac3b$, so $b\le4$.
- $b=3$: $\frac1c+\frac1d=\frac13$, $c\ge4$ (since $c=3$ would need $\frac1d=0$), and $(c-3)(d-3)=9$ with $1\le c-3\le d-3$: $(c,d)=(4,12),(6,6)$: $2$ solutions.
- $b=4$: $\frac1c+\frac1d=\frac5{12}$ with $c\ge4$ and $\frac5{12}\le\frac2c$, so $c\le4$. $c=4$ gives $\frac1d=\frac5{12}-\frac14=\frac16$, $d=6$. $1$ solution: $(3,4,4,6)$.

That is $3$ solutions.

**Case $a=4$.** Then $b,c,d\ge4$, so $\frac1b+\frac1c+\frac1d\le\frac34$, with equality only for $b=c=d=4$. Since the sum must be $1-\frac14=\frac34$, we get exactly $(4,4,4,4)$: $1$ solution.

Total: $10+3+1=\boxed{14}$.

### o99
source: original
type: answer
difficulty: 4
techniques: symmetry
statement:
A round table has $2024$ chairs placed at equal distances around it. Alice and Bob take turns, Alice first. On a turn, a player seats a guest on an empty chair, subject to the rule that the chair must not be next to a chair that already has a guest (the two neighbours of a chair are the chairs immediately to its left and right). A player who cannot make a move loses. Which player has a winning strategy?
asked:
Decide who wins this game with best play from both sides, and describe the winning strategy.
technique:
Think about what structure of the table one of the players could exploit.
hint:
Number the chairs $0,1,\dots,2023$ around the table. Which chair is exactly opposite chair $x$?
hint:
Suppose the player who moves second always answers by taking the chair opposite to the one the opponent just took. Show that this reply is always legal. What do you know about the guests seated before the opponent's move?
hint:
For legality you must check three things about the opposite chair $x'$: it is empty, it is not adjacent to an occupied chair, and it is not adjacent to the chair $x$ just taken.
solution:
Number the chairs $0,1,\dots,2023$ around the table, with arithmetic modulo $2024$. For a chair $x$ let $x'=x+1012$ be the opposite chair. Then $(x')'=x$, and $x'$ is a neighbour of $y$ exactly when $x$ is a neighbour of $y'$ (shifting everything by $1012$ preserves neighbourhood).

**Bob (the second player) wins.** His strategy: whenever Alice seats a guest on chair $x$, Bob seats a guest on $x'$.

We prove by induction that Bob can always do this legally. Before each of Alice's moves, the set $T$ of occupied chairs is *symmetric*: $y\in T\iff y'\in T$ (at the start $T=\emptyset$, and each round adds $x$ and $x'$ together). Suppose Alice legally takes $x$, so $x\notin T$ and neither neighbour of $x$ is in $T$. We check that $x'$ is legal for Bob, in the position $T\cup\{x\}$:
- $x'$ is empty: $x'\ne x$ because $1012\not\equiv0\pmod{2024}$, and $x'\notin T$ since otherwise $x=(x')'\in T$ by symmetry.
- $x'$ is not adjacent to a chair of $T$: if a neighbour $z$ of $x'$ were in $T$, then $z'\in T$ by symmetry, and $z'$ is a neighbour of $x$, contradicting the legality of Alice's move.
- $x'$ is not adjacent to $x$: that would need $1012\equiv\pm1\pmod{2024}$, which is false.

So Bob's reply is legal, and the occupied set is symmetric again. Every move of Alice is thus followed by a legal move of Bob. The game is finite (at most $2024$ guests), so it ends, and the player who cannot move must be Alice (Bob always has a move after Alice's). Hence Bob wins: $\boxed{\text{the second player (Bob)}}$.

### o100
source: original
type: answer
difficulty: 6
techniques: double-counting, constructive
statement:
Each cell of a $7\times7$ table contains either $0$ or $1$. There are no two rows and two columns such that all four cells where these rows and columns cross contain $1$ (the two rows need not be adjacent, nor the two columns). What is the largest possible number of $1$s in the table?
asked:
Find the maximum number of $1$s in a $7\times7$ table of $0$s and $1$s that contains no "rectangle of four $1$s" at the crossings of two rows and two columns, and show that this maximum is attained.
technique:
Count a suitable family of objects, such as pairs of positions inside the rows, in two ways, and then use an inequality. A matching construction must also be exhibited.
hint:
For each row, look at the pairs of columns in which that row has a $1$. What does the rectangle condition say about a given pair of columns across different rows?
hint:
A given pair of columns can occur in at most one row. Count (row, pair of columns) in two ways to bound $\sum_i\binom{r_i}2$, where $r_i$ is the number of $1$s in row $i$.
hint:
Show that $22$ ones would force $\sum\binom{r_i}2\ge24$; to do this write $\sum r_i^2=\sum(r_i-3)^2+6\sum r_i-63$. For the construction think of seven "lines" of three columns each, any two of which share exactly one column, for instance $\{i,i+1,i+3\}$ modulo $7$.
solution:
**Upper bound.** Let $r_i$ be the number of $1$s in row $i$ and $S=\sum r_i$ the total. Count the triples (row $i$, two columns $c<c'$) such that row $i$ has $1$s in both columns $c$ and $c'$.

By rows: row $i$ contributes $\binom{r_i}2$, so the total is $\sum_i\binom{r_i}2$.

By column pairs: a given pair of columns can occur in at most one row, because two rows both having $1$s in these two columns would form a forbidden rectangle. There are $\binom72=21$ pairs of columns. So the total is at most $21$.

Hence $\sum_i\binom{r_i}2\le21$.

Suppose $S\ge22$. Turning some $1$s into $0$s keeps the table free of rectangles, so we may assume $S=22$. Then
$$\sum r_i^2=\sum(r_i-3)^2+6\sum r_i-63=\sum(r_i-3)^2+69.$$
Since $\sum(r_i-3)=22-21=1\ne0$, not all $r_i$ equal $3$, so some integer $r_i-3$ is nonzero and $\sum(r_i-3)^2\ge1$. Thus $\sum r_i^2\ge70$ and
$$\sum_i\binom{r_i}2=\frac{\sum r_i^2-\sum r_i}2\ge\frac{70-22}2=24>21,$$
a contradiction. So $S\le21$.

**Construction with $21$.** Number rows and columns $0,\dots,6$. In row $i$ put $1$s exactly in columns $i,\ i+1,\ i+3$ (modulo $7$). Each row has three $1$s, so there are $21$ in total. Two different rows $i\ne i'$ share at most one column with a $1$: a common column would give a solution of $i+a\equiv i'+b\pmod 7$ with $a,b\in\{0,1,3\}$, i.e. $i-i'\equiv b-a$. The differences $b-a$ with $a\ne b$ are $\pm1,\pm2,\pm3$, that is $1,6,2,5,3,4$ modulo $7$, each exactly once, and $a=b$ gives $i=i'$. So $i-i'$ determines $(a,b)$ uniquely and two rows share exactly one column. No rectangle can occur.

The maximum is $\boxed{21}$.

### o101
source: original
type: proof
difficulty: 5
techniques: pigeonhole
statement:
The integers $1,2,\dots,10$ are written in a row in some order. Prove that one can find four of them that appear in increasing order from left to right, or four that appear in decreasing order from left to right (the four need not be next to each other).
asked:
Show that every arrangement of $1,\dots,10$ in a row contains an increasing or a decreasing subsequence of length $4$.
technique:
Attach to each number some data that is forced to be different for different numbers, and count the possible values of this data.
hint:
For each position $k$, let $a_k$ be the length of the longest increasing subsequence that ends at position $k$ and $b_k$ the length of the longest decreasing subsequence that ends there. Suppose all $a_k,b_k\le3$.
hint:
Show that the pairs $(a_k,b_k)$ are pairwise different for different positions $k$: compare two positions $i<j$ and look at whether the number at $i$ is smaller or larger than the one at $j$.
hint:
Count the possible pairs $(a,b)$ with $1\le a,b\le3$ and compare with $10$.
solution:
Let the row be $x_1,x_2,\dots,x_{10}$ (a permutation of $1,\dots,10$). For each position $k$ let $a_k$ be the length of the longest increasing subsequence that ends at $x_k$ and $b_k$ the length of the longest decreasing subsequence that ends at $x_k$. Both are at least $1$ (the single number $x_k$).

Claim: if $i<j$ then $(a_i,b_i)\ne(a_j,b_j)$. The numbers are distinct, so either $x_i<x_j$ or $x_i>x_j$.
- If $x_i<x_j$, then appending $x_j$ to a longest increasing subsequence ending at $x_i$ gives an increasing subsequence ending at $x_j$ of length $a_i+1$. So $a_j\ge a_i+1>a_i$.
- If $x_i>x_j$, then similarly $b_j\ge b_i+1>b_i$.
In both cases the pairs differ.

Now suppose, for contradiction, that there is no increasing and no decreasing subsequence of length $4$. Then every $a_k$ and every $b_k$ is at most $3$, so each pair $(a_k,b_k)$ lies in $\{1,2,3\}\times\{1,2,3\}$, which has only $9$ elements. There are $10$ positions with pairwise different pairs, which is impossible (pigeonhole). Hence some $a_k\ge4$ or some $b_k\ge4$, which gives the required four numbers. $\blacksquare$
