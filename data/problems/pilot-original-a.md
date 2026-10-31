### o01
source: original
type: proof
difficulty: 1
techniques: pigeonhole, modular-arithmetic
statement:
Show that among any six integers there are two whose difference is divisible by $5$.
asked:
You are given any six integers. You must show that some two of them differ by a multiple of $5$.
technique:
Ask what you can sort the integers into so that two in the same class automatically have the required property.
hint:
Divisibility of a difference by $5$ is about remainders. Two integers have a difference divisible by $5$ exactly when they leave the same remainder on division by $5$.
hint:
How many different remainders are there on division by $5$? Compare that to the number of integers.
solution:
Divide each of the six integers by $5$. There are only five possible remainders: $0,1,2,3,4$. These are the boxes.

Six integers go into five boxes, so two of them, say $a$ and $b$, leave the same remainder $r$. Write $a=5s+r$ and $b=5t+r$. Then $a-b=5(s-t)$ is divisible by $5$. $\blacksquare$

### o02
source: original
type: answer
difficulty: 1
techniques: parity
statement:
Is there a set of eight odd integers whose sum is $2025$?
asked:
You need eight odd integers that add up to exactly $2025$, or a reason none exist.
technique:
Think about whether the sum of eight odd numbers is even or odd.
hint:
Add the odd numbers two at a time. What is the parity of the sum of two odd numbers?
hint:
Group the eight numbers into four pairs, and compare the parity of the total with the parity of $2025$.
solution:
No. The sum of two odd integers is even. Group the eight integers into four pairs. Each pair sums to an even number, and a sum of even numbers is even. So the sum of eight odd integers is always even.

Since $2025$ is odd, no such set exists.

### o03
source: original
type: proof
difficulty: 2
techniques: induction
statement:
Prove that $1+3+5+\dots+(2n-1)=n^2$ for every positive integer $n$.
asked:
The left side is the sum of the first $n$ odd numbers. You must prove it equals $n^2$ for every $n\ge1$.
technique:
The statement depends on $n$, and going from $n$ to $n+1$ adds exactly one new term.
hint:
Check the case $n=1$ first. Then assume the formula holds for some $n$ and write down the sum for $n+1$ using the assumed value.
hint:
The new last term is $2(n+1)-1=2n+1$. Show that $n^2+(2n+1)$ is a perfect square.
solution:
**Base case.** For $n=1$ the sum is $1=1^2$.

**Step.** Assume $1+3+\dots+(2n-1)=n^2$. Then
$$1+3+\dots+(2n-1)+(2n+1)=n^2+2n+1=(n+1)^2.$$
So the formula holds for $n+1$. By induction it holds for all $n\ge1$. $\blacksquare$

### o04
source: original
type: answer
difficulty: 2
techniques: modular-arithmetic
statement:
What is the last digit of $7^{2025}$?
asked:
You need the units digit of the very large number $7^{2025}$.
technique:
The last digit is the remainder mod $10$. Look at how the last digit of powers of $7$ behaves.
hint:
Compute the last digits of $7^1,7^2,7^3,7^4,7^5$. A pattern appears quickly.
hint:
The pattern repeats every $4$ powers. Find the remainder of $2025$ when divided by $4$.
solution:
The last digits of $7^1,7^2,7^3,7^4$ are $7,9,3,1$, and then $7^5$ ends in $7$ again. The last digit of $7^{n}$ depends only on the remainder of $n$ mod $4$: remainder $1\to7$, $2\to9$, $3\to3$, $0\to1$.

Since $2025=4\cdot506+1$, the remainder is $1$, so the last digit is $\boxed{7}$.

### o05
source: original
type: answer
difficulty: 2
techniques: casework
statement:
How many integers $n$ satisfy $|n-3|+|n+2|=9$?
asked:
Count the integers $n$ for which the sum of the distances from $n$ to $3$ and to $-2$ equals $9$.
technique:
An absolute value behaves differently on either side of the point where its inside changes sign.
hint:
The expressions $n-3$ and $n+2$ change sign at $n=3$ and $n=-2$. These two points split the number line into three regions.
hint:
In each region, remove the absolute values and solve the resulting linear equation. Then check that the solution lies in that region.
solution:
Split the line at $-2$ and $3$.

- **$n\ge3$:** the equation is $(n-3)+(n+2)=9$, so $2n-1=9$ and $n=5$. This is $\ge3$, so it is valid.
- **$-2\le n\le3$:** the equation is $(3-n)+(n+2)=5\ne9$. No solutions.
- **$n\le-2$:** the equation is $(3-n)+(-n-2)=9$, so $1-2n=9$ and $n=-4$. This is $\le-2$, so it is valid.

There are $\boxed{2}$ integers: $n=5$ and $n=-4$.

### o06
source: original
type: answer
difficulty: 2
techniques: am-gm
statement:
For positive real $x$, what is the minimum value of $x+\dfrac9x$?
asked:
Over all positive $x$, find the smallest value that $x+\frac9x$ can take.
technique:
The two terms multiply to a constant.
hint:
Apply the inequality "arithmetic mean $\ge$ geometric mean" to the two positive numbers $x$ and $\frac9x$.
hint:
Compute their product. Then find the $x$ at which the two terms are equal, and check that the bound is actually reached.
solution:
By AM-GM, $\dfrac{x+\frac9x}{2}\ge\sqrt{x\cdot\frac9x}=3$, so $x+\frac9x\ge6$.

Equality holds when $x=\frac9x$, i.e. $x=3$, which is allowed. So the minimum is $\boxed{6}$.

### o07
source: original
type: answer
difficulty: 2
techniques: telescoping
statement:
Evaluate $\dfrac1{1\cdot2}+\dfrac1{2\cdot3}+\dfrac1{3\cdot4}+\dots+\dfrac1{99\cdot100}$.
asked:
Find the exact value of this sum of $99$ fractions.
technique:
This sum [[telescoping|telescopes]]. Each term can be split into a difference of two simpler fractions.
hint:
Write $\frac1{k(k+1)}$ as a difference $\frac1k-\frac1{k+1}$.
hint:
Write out the first few and last few terms of the new sum and see what cancels.
solution:
Since $\dfrac1{k(k+1)}=\dfrac1k-\dfrac1{k+1}$, the sum is
$$\left(1-\tfrac12\right)+\left(\tfrac12-\tfrac13\right)+\dots+\left(\tfrac1{99}-\tfrac1{100}\right).$$
Every middle term cancels, leaving $1-\dfrac1{100}=\boxed{\dfrac{99}{100}}$.

### o08
source: original
type: proof
difficulty: 2
techniques: divisibility
statement:
Show that for every integer $n$, the numbers $2n+1$ and $3n+2$ have no common divisor greater than $1$.
asked:
Whatever $n$ is, the greatest common divisor of $2n+1$ and $3n+2$ must be $1$.
technique:
A common divisor of two numbers also divides every integer combination of them.
hint:
Suppose $d$ divides both $2n+1$ and $3n+2$. Form a combination of the two numbers in which $n$ disappears.
hint:
Try $2(3n+2)-3(2n+1)$.
solution:
Let $d$ be a positive common divisor of $2n+1$ and $3n+2$. Then $d$ divides
$$2(3n+2)-3(2n+1)=6n+4-6n-3=1.$$
So $d=1$. $\blacksquare$

### o09
source: original
type: answer
difficulty: 3
techniques: coloring, parity
statement:
Two opposite corner squares are removed from a $6\times6$ board. Can the remaining $34$ squares be covered exactly by $17$ dominoes (each domino covers two adjacent squares)?
asked:
You must decide whether the damaged board can be tiled exactly with dominoes, and justify it.
technique:
Color the board so that every domino must cover a fixed combination of colors.
hint:
Color the board like a chessboard. What colors does a single domino cover?
hint:
Count how many squares of each color remain after removing the two corners. What do the colors of two opposite corners have in common?
solution:
**No.** Color the board like a chessboard. Every domino covers one square of each color, so $17$ dominoes cover $17$ black and $17$ white squares.

Opposite corners $(1,1)$ and $(6,6)$ have the same color, since $1+1$ and $6+6$ are both even. A full board has $18$ squares of each color, so removing two squares of the same color leaves $16$ of that color and $18$ of the other. These counts differ from $17$ and $17$, so no tiling exists.

### o10
source: original
type: answer
difficulty: 3
techniques: invariants
statement:
The numbers $1,2,3,\dots,10$ are written on a board. A move erases two numbers $a$ and $b$ and writes $a+b-1$ in their place. After nine moves one number remains. What is it?
asked:
Whatever order of moves is used, find the single number left at the end.
technique:
Look for a quantity that does not change with any move.
hint:
Each move replaces two numbers by one. Look at the sum of the numbers together with how many numbers are on the board.
hint:
Find how the sum changes and how the count changes in one move. Combine them so that the change cancels.
solution:
In one move, the sum $S$ of the numbers decreases by $1$ (since $a+b$ is replaced by $a+b-1$), and the count $k$ of numbers decreases by $1$. So $S-k$ never changes.

At the start, $S=55$ and $k=10$, so $S-k=45$. At the end, $k=1$, so $S=45+1=\boxed{46}$.

### o11
source: original
type: proof
difficulty: 3
techniques: pigeonhole
statement:
Five points are placed inside or on the boundary of an equilateral triangle with side length $1$. Show that two of them are at distance at most $\tfrac12$.
asked:
Whatever positions the five points take inside the triangle, you must find two that are close together (at most $\frac12$ apart).
technique:
Cut the triangle into regions in which any two points are automatically close.
hint:
You need regions of diameter at most $\frac12$. Join the midpoints of the three sides.
hint:
This cuts the triangle into four smaller equilateral triangles. What is the largest distance between two points of one small triangle?
solution:
Join the midpoints of the sides. This divides the triangle into four equilateral triangles of side $\frac12$.

Five points lie in four small triangles (a point on a shared edge is assigned to either triangle), so some small triangle contains two points. Two points in an equilateral triangle of side $\frac12$ are at distance at most $\frac12$, because the largest distance between two points of a triangle is attained at two of its vertices, i.e. it equals the longest side. $\blacksquare$

### o12
source: original
type: answer
difficulty: 3
techniques: recursion
statement:
A sequence has $a_1=1$ and $a_{n+1}=2a_n+1$ for $n\ge1$. Find $a_{10}$.
asked:
You are given the first term and a rule for each next term. Find the tenth term.
technique:
Compute a few terms and look for a pattern, or shift the sequence to make it geometric.
hint:
Compute $a_2,a_3,a_4,a_5$ and compare each with a power of $2$.
hint:
Each term is one less than a power of $2$. Prove this pattern holds, or just continue to $a_{10}$.
solution:
The terms are $1,3,7,15,31,\dots$, each one less than a power of $2$: conjecture $a_n=2^n-1$.

Proof by induction: $a_1=2^1-1$. If $a_n=2^n-1$, then $a_{n+1}=2(2^n-1)+1=2^{n+1}-1$.

So $a_{10}=2^{10}-1=\boxed{1023}$.
