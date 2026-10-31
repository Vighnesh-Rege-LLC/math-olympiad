### o62
source: original
type: answer
difficulty: 3
techniques: telescoping
statement:
Evaluate $1\cdot1!+2\cdot2!+3\cdot3!+\dots+9\cdot9!$.
asked:
Find the exact value of the sum of $k\cdot k!$ for $k=1,2,\dots,9$.
technique:
Try to write each term $k\cdot k!$ as a difference of two consecutive-looking quantities, so that most terms cancel when you add.
hint:
Look for something of the form $g(k+1)-g(k)$ that equals $k\cdot k!$. Start from $(k+1)!=(k+1)\cdot k!$.
hint:
Since $(k+1)!-k!=k\cdot k!$, write out the first few and last few terms of the sum and see what survives.
solution:
Since $(k+1)!=(k+1)\,k!=k\cdot k!+k!$, we have
$$k\cdot k!=(k+1)!-k!.$$
Therefore
$$\sum_{k=1}^{9}k\cdot k!=\sum_{k=1}^{9}\big((k+1)!-k!\big)=(2!-1!)+(3!-2!)+\dots+(10!-9!)=10!-1!.$$
All intermediate factorials cancel in pairs. Since $10!=3628800$, the sum is $\boxed{3628799}$.

### o63
source: original
type: answer
difficulty: 5
techniques: telescoping, polynomials
statement:
Evaluate
$$\sum_{k=1}^{10}\frac{k}{k^4+k^2+1}.$$
asked:
Find the exact value of the sum as a fraction.
technique:
The denominator factors, and the two factors are related to each other as $k$ changes. Split each term using partial fractions and watch what cancels.
hint:
Write $k^4+k^2+1=(k^2+1)^2-k^2$ and factor it as a difference of squares.
hint:
The two factors are $k^2-k+1$ and $k^2+k+1$. Compute $\frac1{k^2-k+1}-\frac1{k^2+k+1}$ and compare it with the original term.
hint:
Check that $(k+1)^2-(k+1)+1=k^2+k+1$. This is exactly what makes consecutive terms cancel.
solution:
First, $k^4+k^2+1=(k^2+1)^2-k^2=(k^2-k+1)(k^2+k+1)$. Now
$$\frac1{k^2-k+1}-\frac1{k^2+k+1}=\frac{(k^2+k+1)-(k^2-k+1)}{(k^2-k+1)(k^2+k+1)}=\frac{2k}{k^4+k^2+1}.$$
So
$$\frac{k}{k^4+k^2+1}=\frac12\left(\frac1{k^2-k+1}-\frac1{k^2+k+1}\right).$$
Let $u_k=\dfrac1{k^2-k+1}$. Because $(k+1)^2-(k+1)+1=k^2+k+1$, we have $\dfrac1{k^2+k+1}=u_{k+1}$, and the term equals $\tfrac12(u_k-u_{k+1})$. The sum telescopes:
$$\sum_{k=1}^{10}\frac12(u_k-u_{k+1})=\frac12(u_1-u_{11})=\frac12\left(1-\frac1{111}\right)=\frac12\cdot\frac{110}{111}=\boxed{\dfrac{55}{111}}.$$
Here $u_{11}=\frac1{11^2-11+1}=\frac1{111}$.

### o64
source: original
type: answer
difficulty: 3
techniques: generating-functions
statement:
Four fair six-sided dice, one red, one blue, one green and one yellow, are rolled. In how many of the $6^4$ equally likely outcomes (the colors keep the dice distinguishable) is the sum of the four numbers equal to $14$?
asked:
Count the outcomes (ordered quadruples of numbers from $1$ to $6$) whose sum is $14$.
technique:
Encode the possible values of one die as a polynomial, so that multiplying polynomials adds the values. Then the answer is a single coefficient.
hint:
One die has generating polynomial $x+x^2+\dots+x^6=x\cdot\frac{1-x^6}{1-x}$. The sum of four dice corresponds to the fourth power. You want the coefficient of $x^{14}$.
hint:
Pull out $x^4$, so you need the coefficient of $x^{10}$ in $\left(\frac{1-x^6}{1-x}\right)^4=(1-x^6)^4\cdot(1-x)^{-4}$. Expand each factor.
solution:
The number of outcomes with sum $14$ is the coefficient of $x^{14}$ in
$$(x+x^2+\dots+x^6)^4=x^4\frac{(1-x^6)^4}{(1-x)^4}.$$
So we need the coefficient of $x^{10}$ in $(1-x^6)^4(1-x)^{-4}$.

We have $(1-x^6)^4=1-4x^6+6x^{12}-\dots$, and $(1-x)^{-4}=\sum_{m\ge0}\binom{m+3}{3}x^m$. The coefficient of $x^{10}$ is
$$\binom{13}{3}-4\binom{7}{3}+6\cdot 0=286-4\cdot35=146,$$
where the $x^{12}$ term cannot contribute to $x^{10}$. The answer is $\boxed{146}$.

### o65
source: original
type: proof
difficulty: 5
techniques: generating-functions
statement:
For a positive integer $n$, let $D(n)$ be the number of ways to write $n$ as a sum of distinct positive integers, and let $O(n)$ be the number of ways to write $n$ as a sum of odd positive integers, repetition allowed. In both cases the order of the summands does not matter. (For example $D(5)=3$ via $5$, $4+1$, $3+2$, and $O(5)=3$ via $5$, $3+1+1$, $1+1+1+1+1$.) Prove that $D(n)=O(n)$ for every positive integer $n$.
asked:
You must prove that the two counts $D(n)$ and $O(n)$ agree for every $n\ge1$.
technique:
Each count is the coefficient of $x^n$ in an infinite product, one factor per allowed part size. Show the two products are equal.
hint:
For distinct parts, each size $k$ is used $0$ or $1$ times, which contributes a factor $1+x^k$. For odd parts, each odd $k$ may be used any number of times, which contributes $1+x^k+x^{2k}+\dots=\frac1{1-x^k}$.
hint:
Write $1+x^k=\dfrac{1-x^{2k}}{1-x^k}$ and compare the numerator and denominator of the full product over $k\ge1$.
solution:
Consider formal power series in $x$. Choosing a partition of $n$ into distinct parts means choosing, for each $k\ge1$, whether $k$ is used ($0$ or $1$ times). Expanding the product, the coefficient of $x^n$ in
$$\prod_{k\ge1}(1+x^k)$$
counts exactly the ways to pick a set of distinct parts summing to $n$, so it is $D(n)$. (The infinite product makes sense because the factor $1+x^k$ only differs from $1$ in degrees $\ge k$, so each coefficient depends on finitely many factors.)

Similarly, choosing a partition of $n$ into odd parts means choosing for each odd $k$ a multiplicity $m_k\ge0$ with $\sum k\,m_k=n$. The coefficient of $x^n$ in
$$\prod_{k\ge1}\frac1{1-x^{2k-1}}=\prod_{k\ge1}\left(1+x^{2k-1}+x^{2(2k-1)}+\dots\right)$$
is $O(n)$.

Now use $1+x^k=\dfrac{1-x^{2k}}{1-x^k}$:
$$\prod_{k\ge1}(1+x^k)=\prod_{k\ge1}\frac{1-x^{2k}}{1-x^k}=\frac{(1-x^2)(1-x^4)(1-x^6)\cdots}{(1-x)(1-x^2)(1-x^3)(1-x^4)\cdots}.$$
The denominator contains every factor $1-x^m$, $m\ge1$. The numerator contains exactly the factors with $m$ even. Each factor $1-x^m$ is invertible in the ring of formal power series, so cancelling is legitimate (equivalently, truncate everything at degree $n$, where only finitely many factors matter). Cancel those, leaving the factors with $m$ odd in the denominator:
$$\prod_{k\ge1}(1+x^k)=\prod_{k\ge1}\frac1{1-x^{2k-1}}.$$
The two series are equal, so their coefficients of $x^n$ agree: $D(n)=O(n)$. $\blacksquare$

### o66
source: original
type: answer
difficulty: 3
techniques: am-gm
statement:
Positive real numbers $x$ and $y$ satisfy $x+y=12$. Find the maximum possible value of $x^2y$.
asked:
Find the largest value that $x^2y$ can take, and where it is attained.
technique:
Apply the inequality between arithmetic and geometric means to three numbers whose sum is the fixed total $12$ and whose product is a constant multiple of $x^2y$.
hint:
You need three positive terms whose sum is $x+y$ and whose product is proportional to $x^2y$. Two of them should be equal.
hint:
Use the three numbers $\frac x2,\frac x2,y$. Their sum is $12$, and equality in AM-GM needs them to be equal.
solution:
By AM-GM on the three positive numbers $\frac x2,\frac x2,y$:
$$\frac{\frac x2+\frac x2+y}{3}\ge\sqrt[3]{\frac x2\cdot\frac x2\cdot y}.$$
The left side is $\frac{12}{3}=4$, so $\frac{x^2y}{4}\le4^3=64$ and $x^2y\le256$.

Equality holds when $\frac x2=y$, i.e. $x=2y$; with $x+y=12$ this gives $y=4$, $x=8$, and indeed $8^2\cdot4=256$. The maximum is $\boxed{256}$.

### o67
source: original
type: answer
difficulty: 4
techniques: am-gm
statement:
Find the minimum value of $x^2+\dfrac{16}{x}$ over all positive real numbers $x$.
asked:
Find the smallest value of the expression for $x>0$, and the $x$ at which it is attained.
technique:
Split the expression into several terms so that, when you multiply them together, the variable disappears. Then the inequality between arithmetic and geometric means gives a constant lower bound.
hint:
Try to choose terms whose product does not depend on $x$. One copy of $\frac cx$ times $x^2$ leaves a factor of $x$, so you need two copies of a $\frac cx$ term to cancel the $x^2$.
hint:
Write $\frac{16}{x}=\frac8x+\frac8x$ and apply AM-GM to $x^2,\ \frac8x,\ \frac8x$. Check when equality can hold.
solution:
Write $x^2+\dfrac{16}{x}=x^2+\dfrac8x+\dfrac8x$. By AM-GM for three positive numbers,
$$x^2+\frac8x+\frac8x\ge3\sqrt[3]{x^2\cdot\frac8x\cdot\frac8x}=3\sqrt[3]{64}=12.$$
Equality needs $x^2=\frac8x$, i.e. $x^3=8$, $x=2$. At $x=2$ the value is $4+8=12$, so the bound is attained. The minimum is $\boxed{12}$ (at $x=2$).

### o68
source: original
type: answer
difficulty: 4
techniques: cauchy-schwarz
statement:
Real numbers $x,y,z$ satisfy $x^2+2y^2+3z^2=6$. Find the maximum possible value of $x+2y+3z$.
asked:
Find the largest value of $x+2y+3z$ under the constraint, and a triple that attains it.
technique:
Write the linear expression as a dot product of two vectors, chosen so that one of them has a length you know from the constraint.
hint:
You want $x+2y+3z=(\text{vector }u)\cdot(\text{vector }v)$ where $|u|^2=x^2+2y^2+3z^2$. Think of $u=(x,\sqrt2y,\sqrt3z)$.
hint:
Then $v=(1,\sqrt2,\sqrt3)$. Apply $(u\cdot v)^2\le|u|^2|v|^2$, and find when equality holds (when $u$ and $v$ are parallel).
solution:
Let $u=(x,\sqrt2\,y,\sqrt3\,z)$ and $v=(1,\sqrt2,\sqrt3)$. Then $u\cdot v=x+2y+3z$, $|u|^2=x^2+2y^2+3z^2=6$ and $|v|^2=1+2+3=6$. By the Cauchy-Schwarz inequality,
$$(x+2y+3z)^2\le|u|^2|v|^2=36,$$
so $x+2y+3z\le6$.

Equality holds when $u$ is a positive multiple of $v$. Take $x=y=z=1$: then $x^2+2y^2+3z^2=6$ and $x+2y+3z=6$. The maximum is $\boxed{6}$.

### o69
source: original
type: proof
difficulty: 4
techniques: cauchy-schwarz
statement:
Let $a,b,c$ be positive real numbers. Prove that
$$\frac{a^2}{a+b}+\frac{b^2}{b+c}+\frac{c^2}{c+a}\ge\frac{a+b+c}{2}.$$
asked:
Prove the inequality for all positive reals $a,b,c$.
technique:
The left side is a sum of fractions with squared numerators. Multiply it by a second sum so that Cauchy-Schwarz produces a perfect square.
hint:
Cauchy-Schwarz in the form $\left(\sum p_i^2\right)\left(\sum q_i^2\right)\ge\left(\sum p_iq_i\right)^2$. Take $p_1=\frac{a}{\sqrt{a+b}}$ and find $q_1$ so that $p_1q_1$ is simple.
hint:
Take $q_1=\sqrt{a+b}$, and similarly for the other terms. Then compute $\sum q_i^2=(a+b)+(b+c)+(c+a)$.
solution:
Apply the Cauchy-Schwarz inequality to the vectors
$$\left(\frac{a}{\sqrt{a+b}},\frac{b}{\sqrt{b+c}},\frac{c}{\sqrt{c+a}}\right)\quad\text{and}\quad\left(\sqrt{a+b},\sqrt{b+c},\sqrt{c+a}\right).$$
All entries are real since $a,b,c>0$. We get
$$\left(\frac{a^2}{a+b}+\frac{b^2}{b+c}+\frac{c^2}{c+a}\right)\big((a+b)+(b+c)+(c+a)\big)\ge(a+b+c)^2,$$
because the products of corresponding entries are $a$, $b$, $c$. The second factor on the left equals $2(a+b+c)>0$. Dividing by it,
$$\frac{a^2}{a+b}+\frac{b^2}{b+c}+\frac{c^2}{c+a}\ge\frac{(a+b+c)^2}{2(a+b+c)}=\frac{a+b+c}{2}.\qquad\blacksquare$$

### o70
source: original
type: answer
difficulty: 3
techniques: functional-equations
statement:
Find all functions $f:\mathbb R\setminus\{0\}\to\mathbb R$ such that $f(x)+2f\!\left(\dfrac1x\right)=3x$ for every nonzero real $x$.
asked:
Determine every function satisfying the equation, and check that it works.
technique:
The equation links two values of $f$. Look for another relation between those same two values.
hint:
Replace $x$ by $\frac1x$ in the equation. You now have two equations in the two unknowns $f(x)$ and $f(1/x)$.
hint:
Eliminate $f(1/x)$ to solve for $f(x)$, then substitute back into the original equation to verify.
solution:
Suppose $f$ satisfies the equation. Replacing $x$ by $\frac1x$ (allowed, as $\frac1x\ne0$) gives
$$f\!\left(\tfrac1x\right)+2f(x)=\frac3x.$$
So with $A=f(x)$ and $B=f(1/x)$ we have $A+2B=3x$ and $2A+B=\frac3x$. Doubling the second and subtracting the first: $3A=\frac6x-3x$, so
$$f(x)=\frac2x-x.$$
Check: $f(x)+2f(1/x)=\frac2x-x+2\left(2x-\frac1x\right)=\frac2x-x+4x-\frac2x=3x$. Hence the unique solution is $\boxed{f(x)=\dfrac2x-x}$.

### o71
source: original
type: answer
difficulty: 4
techniques: functional-equations
statement:
Find all functions $f:\mathbb R\to\mathbb R$ such that $f\big(x+f(y)\big)=4y-2x-1$ for all real $x,y$.
asked:
Determine every function satisfying the equation for all real $x$ and $y$, and verify it.
technique:
The equation holds for all $x$, so choose $x$ cleverly in terms of $y$.
hint:
Substitute $x=-f(y)$. The left side becomes $f(0)$, a constant.
hint:
The substitution gives $f(y)$ as an explicit linear function of $y$ involving the unknown constant $f(0)$. Determine that constant by plugging $y=0$ in your formula, then check the result in the original equation.
solution:
Put $x=-f(y)$. Then $f(0)=4y+2f(y)-1$, so
$$f(y)=\frac{f(0)+1}{2}-2y.$$
Let $c=\frac{f(0)+1}{2}$, so $f(y)=c-2y$. Setting $y=0$ gives $f(0)=c$, hence $c=\frac{c+1}{2}$, so $c=1$ and $f(y)=1-2y$.

Check: $f(x+f(y))=f(x+1-2y)=1-2(x+1-2y)=4y-2x-1$. ✓.

The unique solution is $\boxed{f(x)=1-2x}$.

### o72
source: original
type: answer
difficulty: 4
techniques: polynomials
statement:
Let $a,b,c$ be the three roots of $x^3-x-1=0$. Find $a^5+b^5+c^5$.
asked:
Compute the sum of the fifth powers of the roots, without finding the roots.
technique:
Each root satisfies the cubic, so a high power of a root can be rewritten using lower powers. Add over the three roots and use the relations between the roots and coefficients.
hint:
From $a^3=a+1$ you can multiply by $a^{k}$ to get $a^{k+3}=a^{k+1}+a^{k}$. The same holds for $b$ and $c$.
hint:
Let $p_k=a^k+b^k+c^k$. Then $p_{k+3}=p_{k+1}+p_k$. Find $p_0,p_1,p_2$ using Vieta's formulas, then compute up to $p_5$.
solution:
By Vieta's formulas for $x^3+0x^2-x-1$: $a+b+c=0$, $ab+bc+ca=-1$, $abc=1$. Let $p_k=a^k+b^k+c^k$. Then
$$p_0=3,\qquad p_1=0,\qquad p_2=(a+b+c)^2-2(ab+bc+ca)=0+2=2.$$
Each root $r$ satisfies $r^3=r+1$, so $r^{k+3}=r^{k+1}+r^k$ for $k\ge0$. Summing over $r\in\{a,b,c\}$ gives $p_{k+3}=p_{k+1}+p_k$. Hence
$$p_3=p_1+p_0=3,\quad p_4=p_2+p_1=2,\quad p_5=p_3+p_2=5.$$
So $a^5+b^5+c^5=\boxed{5}$.

### o73
source: original
type: proof
difficulty: 3
techniques: polynomials, divisibility
statement:
Prove that there is no polynomial $P$ with integer coefficients such that $P(2)=5$ and $P(9)=8$.
asked:
Show that no integer-coefficient polynomial can take the value $5$ at $2$ and the value $8$ at $9$.
technique:
Think about differences of values of an integer polynomial at integers.
hint:
For each $n\ge1$, the integer $a-b$ divides $a^n-b^n$. Use this to say something about $P(a)-P(b)$.
hint:
Show that $a-b$ always divides $P(a)-P(b)$, then apply it with $a=9$, $b=2$.
solution:
Let $P(x)=\sum_{n=0}^{d}c_nx^n$ with all $c_n\in\mathbb Z$. For integers $a,b$ and $n\ge1$,
$$a^n-b^n=(a-b)\left(a^{n-1}+a^{n-2}b+\dots+b^{n-1}\right),$$
so $(a-b)\mid(a^n-b^n)$. Therefore
$$P(a)-P(b)=\sum_{n\ge1}c_n(a^n-b^n)$$
is divisible by $a-b$.

If $P(2)=5$ and $P(9)=8$, then $9-2=7$ would divide $P(9)-P(2)=3$, which is false. So no such polynomial exists. $\blacksquare$

### o74
source: original
type: answer
difficulty: 3
techniques: divisibility
statement:
Find all positive integers $n$ such that $n+3$ divides $n^2+3$.
asked:
List every positive integer $n$ for which $n^2+3$ is a multiple of $n+3$.
technique:
Reduce the numerator modulo the divisor, so that the question becomes whether $n+3$ divides a fixed number.
hint:
Write $n^2+3=(n+3)(n-3)+r$ for a constant $r$. What is $r$?
hint:
Then $n+3$ divides $n^2+3$ exactly when it divides $r$. List the divisors of $r$ that are at least $4$.
solution:
Since $n^2-9=(n+3)(n-3)$, we have $n^2+3=(n+3)(n-3)+12$. Thus $n+3\mid n^2+3$ if and only if $n+3\mid12$.

For positive $n$, $n+3\ge4$. The divisors of $12$ that are at least $4$ are $4,6,12$, giving $n=1,3,9$.

Check: $n=1$: $4\mid4$. $n=3$: $6\mid12$. $n=9$: $12\mid84$. The answer is $\boxed{n=1,\,3,\,9}$.

### o75
source: original
type: proof
difficulty: 5
techniques: divisibility, induction
statement:
For positive integers $a$ and $b$, prove that
$$\gcd(2^a-1,\,2^b-1)=2^{\gcd(a,b)}-1.$$
asked:
Show that the greatest common divisor of $2^a-1$ and $2^b-1$ is $2^d-1$, where $d=\gcd(a,b)$.
technique:
Look for a way to reduce the pair of exponents, in the spirit of how $\gcd(a,b)$ is usually computed.
hint:
Suppose $a>b$. Find an integer multiple of $2^b-1$ that you can subtract from $2^a-1$ to get $2^{a-b}-1$.
hint:
$2^a-1-2^{a-b}(2^b-1)=2^{a-b}-1$. So $\gcd(2^a-1,2^b-1)=\gcd(2^{a-b}-1,2^b-1)$. Now induct on $a+b$, or run Euclid's algorithm on the exponents.
solution:
Write $g(a,b)=\gcd(2^a-1,2^b-1)$. We prove $g(a,b)=2^{\gcd(a,b)}-1$ by strong induction on $a+b$.

If $a=b$, then $g(a,a)=2^a-1=2^{\gcd(a,a)}-1$.

Otherwise, by symmetry assume $a>b$. We have
$$(2^a-1)-2^{a-b}(2^b-1)=2^a-1-2^a+2^{a-b}=2^{a-b}-1.$$
Since $\gcd(m,n)=\gcd(m-kn,n)$ for any integer $k$,
$$g(a,b)=\gcd\big(2^a-1-2^{a-b}(2^b-1),\,2^b-1\big)=\gcd(2^{a-b}-1,2^b-1)=g(a-b,b).$$
Now $a-b\ge1$ and $(a-b)+b<a+b$, so by the induction hypothesis $g(a-b,b)=2^{\gcd(a-b,b)}-1$. Finally $\gcd(a-b,b)=\gcd(a,b)$, so $g(a,b)=2^{\gcd(a,b)}-1$. $\blacksquare$

### o76
source: original
type: answer
difficulty: 3
techniques: diophantine
statement:
How many ordered pairs $(x,y)$ of positive integers satisfy $x^2-y^2=2024$?
asked:
Count the pairs of positive integers with $x^2-y^2=2024$.
technique:
Factor the left side, then use what you know about the two factors, such as their sizes and parities, to list the possibilities.
hint:
Write $x^2-y^2=(x-y)(x+y)$. The two factors have the same parity (their difference is $2y$).
hint:
Since $2024$ is even, both factors are even. Write them as $2d$ and $2e$ with $d<e$ and $de=506$, and count the divisor pairs of $506=2\cdot11\cdot23$.
solution:
Let $u=x-y$ and $v=x+y$. Then $uv=2024$, and since $y>0$ we have $0<u<v$. Also $v-u=2y$ is even, so $u,v$ have the same parity. Their product $2024$ is even, so both are even: $u=2d$, $v=2e$ with $de=506$ and $d<e$.

Conversely, each pair $d<e$ with $de=506$ gives $x=d+e$, $y=e-d>0$, a valid solution, and different pairs give different $(x,y)$.

Now $506=2\cdot11\cdot23$ has $8$ divisors $1,2,11,22,23,46,253,506$, forming $4$ pairs $(d,e)$ with $d<e$: $(1,506),(2,253),(11,46),(22,23)$ ($506$ is not a square). These give $(x,y)=(507,505),(255,251),(57,35),(45,1)$.

So there are $\boxed{4}$ pairs.

### o77
source: original
type: answer
difficulty: 5
techniques: diophantine, modular-arithmetic
statement:
Find all pairs $(a,b)$ of non-negative integers with $3^a-2^b=1$.
asked:
Determine every pair of non-negative integers $(a,b)$ satisfying the equation.
technique:
Handle small exponents directly. For large $b$, look at the equation modulo $4$ to learn about the parity of $a$, which lets you factor.
hint:
Check $a=0$, $b=0$ and $b=1$ by hand. For $b\ge2$, what is $3^a$ modulo $4$, and what does that force about $a$?
hint:
If $a=2k$, then $2^b=3^{2k}-1=(3^k-1)(3^k+1)$. Both factors are divisors of a power of $2$, so both are powers of $2$. Which two powers of $2$ differ by $2$?
solution:
Rewrite as $3^a=2^b+1$.

*Small cases.* If $a=0$ then $2^b=0$, impossible. If $b=0$ then $3^a=2$, impossible. If $b=1$ then $3^a=3$, so $a=1$: the pair $(1,1)$.

*Case $b\ge2$.* Then $3^a=2^b+1\equiv1\pmod4$. Since $3^a\equiv(-1)^a\pmod 4$, $a$ is even; and $a\ge2$ because $3^a\ge5$. Write $a=2k$ with $k\ge1$. Then
$$2^b=3^{2k}-1=(3^k-1)(3^k+1).$$
Both factors are positive divisors of $2^b$, hence powers of $2$: say $3^k-1=2^s$, $3^k+1=2^t$ with $t>s$. Subtracting, $2^t-2^s=2$, so $2^s(2^{t-s}-1)=2$. As $2^{t-s}-1$ is odd and positive, $2^{t-s}-1=1$ and $2^s=2$: $s=1$, $t=2$. So $3^k=3$, $k=1$, $a=2$, and $2^b=8$, $b=3$.

The solutions are $\boxed{(a,b)=(1,1)\text{ and }(2,3)}$. (Check: $3-2=1$, $9-8=1$.)

### o78
source: original
type: answer
difficulty: 5
techniques: expectation
statement:
The numbers $1,2,\dots,8$ are arranged in a row in a uniformly random order. Call an entry a record if it is larger than every entry to its left; the first entry counts as a record. What is the expected number of records?
asked:
Find the expected number of records, as an exact fraction.
technique:
Write the count as a sum of indicator variables, one per position, and compute each position's probability separately without worrying about dependence.
hint:
Let $I_k=1$ if the entry in position $k$ is a record. The expectation of the sum is the sum of the expectations, whether or not the $I_k$ are independent.
hint:
Position $k$ is a record exactly when the largest of the first $k$ entries sits in position $k$. By symmetry, how likely is that?
solution:
Let $I_k$ be the indicator that position $k$ holds a record, $k=1,\dots,8$. The number of records is $I_1+\dots+I_8$, and by linearity of expectation its expectation is $\sum_k\Pr(I_k=1)$.

Position $k$ is a record exactly when the maximum of the first $k$ entries is in position $k$. The set of values in the first $k$ positions is some $k$-element set, and given that set, every one of its $k$ elements is equally likely to be in position $k$ (the arrangement is uniform, so all orders of those $k$ values among the first $k$ positions are equally likely). So $\Pr(I_k=1)=\frac1k$.

Therefore the expected number of records is
$$1+\frac12+\frac13+\dots+\frac18=\frac{840+420+280+210+168+140+120+105}{840}=\frac{2283}{840}=\boxed{\dfrac{761}{280}}.$$

### o79
source: original
type: answer
difficulty: 4
techniques: expectation
statement:
A fair coin is flipped $10$ times. A run is a maximal block of consecutive flips with the same result (for example HHTHT has runs HH, T, H, T, four in all). What is the expected number of runs?
asked:
Find the expected number of runs in $10$ flips.
technique:
Use linearity of expectation over suitable indicator variables.
hint:
The number of runs is $1$ plus the number of positions $i$ where flip $i$ and flip $i+1$ differ.
hint:
For a fixed $i$, find the probability that flips $i$ and $i+1$ differ, then add over all $i$.
solution:
Every run except the first begins at a flip that differs from the previous flip, and every such flip begins a new run. So
$$\text{number of runs}=1+\sum_{i=1}^{9}J_i,$$
where $J_i=1$ if flips $i$ and $i+1$ differ and $0$ otherwise.

For fixed $i$, given flip $i$, flip $i+1$ is different with probability $\frac12$ (the flips are independent and fair). So $E[J_i]=\frac12$. By linearity of expectation,
$$E[\text{runs}]=1+9\cdot\frac12=\boxed{\dfrac{11}{2}}.$$

### o80
source: original
type: proof
difficulty: 3
techniques: coordinates
statement:
Let $ABCD$ be a rectangle and let $P$ be any point in its plane (inside, outside or on the boundary). Prove that $PA^2+PC^2=PB^2+PD^2$.
asked:
Show that the sum of the squared distances from $P$ to two opposite vertices equals the sum for the other two opposite vertices.
technique:
Place the rectangle in a coordinate system aligned with its sides, so every distance is given by an explicit formula.
hint:
Put $A=(0,0)$, $B=(w,0)$, $C=(w,h)$, $D=(0,h)$ and $P=(x,y)$.
hint:
Write each squared distance as $(\text{difference of }x)^2+(\text{difference of }y)^2$ and expand.
solution:
Choose coordinates with $A=(0,0)$, $B=(w,0)$, $C=(w,h)$, $D=(0,h)$, where $w,h>0$ are the side lengths, and let $P=(x,y)$. Then
$$PA^2=x^2+y^2,\qquad PC^2=(x-w)^2+(y-h)^2,$$
$$PB^2=(x-w)^2+y^2,\qquad PD^2=x^2+(y-h)^2.$$
Hence
$$PA^2+PC^2=x^2+y^2+(x-w)^2+(y-h)^2=PB^2+PD^2,$$
since both sums consist of the same four terms $x^2,\ y^2,\ (x-w)^2,\ (y-h)^2$. $\blacksquare$

### o81
source: original
type: answer
difficulty: 4
techniques: coordinates
statement:
A triangle has side lengths $13$, $14$ and $15$. Let $O$ be its circumcenter and $H$ its orthocenter. Find the distance $OH$.
asked:
Find the length of the segment joining the circumcenter and the orthocenter of the $13$-$14$-$15$ triangle.
technique:
Put one side along an axis and give each vertex coordinates. Both centers are then found by writing down simple linear conditions.
hint:
Put $B=(0,0)$ and $C=(14,0)$ with the side of length $14$ on the $x$-axis. The vertex $A$ is at distance $13$ from $B$ and $15$ from $C$; find it (it has integer coordinates).
hint:
$A=(5,12)$. The circumcenter lies on the perpendicular bisector $x=7$ of $BC$ and is equidistant from $B$ and $A$. The orthocenter lies on the altitude $x=5$ and on the altitude from $B$, which is perpendicular to $AC$.
solution:
Let $B=(0,0)$, $C=(14,0)$ and $A=(x,y)$ with $y>0$, $x^2+y^2=169$ and $(x-14)^2+y^2=225$. Subtracting gives $-28x+196=56$, so $x=5$ and $y=12$. So $A=(5,12)$.

*Circumcenter.* $O$ lies on the perpendicular bisector of $BC$, so $O=(7,k)$. From $OB^2=OA^2$: $49+k^2=4+(12-k)^2=148-24k+k^2$, so $24k=99$ and $k=\frac{33}{8}$. Thus $O=\left(7,\frac{33}{8}\right)$.

*Orthocenter.* $H$ lies on the altitude from $A$, the vertical line $x=5$, so $H=(5,m)$. It also lies on the altitude from $B$, which is perpendicular to $AC$. Since $\overrightarrow{AC}=(9,-12)$, we need $(5,m)\cdot(9,-12)=0$: $45-12m=0$, $m=\frac{15}{4}$. Thus $H=\left(5,\frac{15}{4}\right)$.

*Distance.*
$$OH^2=(7-5)^2+\left(\frac{33}{8}-\frac{30}{8}\right)^2=4+\frac9{64}=\frac{265}{64},$$
so $OH=\boxed{\dfrac{\sqrt{265}}{8}}$.

### o82
source: original
type: answer
difficulty: 5
techniques: complex-numbers, trigonometry
statement:
Find the exact value of
$$\sin\frac{\pi}{7}\sin\frac{2\pi}{7}\sin\frac{3\pi}{7}\sin\frac{4\pi}{7}\sin\frac{5\pi}{7}\sin\frac{6\pi}{7}.$$
asked:
Compute the product of $\sin\frac{k\pi}{7}$ for $k=1,\dots,6$ as an exact number.
technique:
Realize the sines as lengths of segments between points on the unit circle in the complex plane, and use the polynomial whose roots are the seventh roots of unity.
hint:
Let $\zeta=e^{2\pi i/7}$. Factor $x^6+x^5+\dots+1$ using its roots $\zeta,\zeta^2,\dots,\zeta^6$, then plug in $x=1$.
hint:
That gives $\prod_{k=1}^6(1-\zeta^k)=7$. Now find $|1-\zeta^k|$ in terms of $\sin\frac{k\pi}{7}$ by factoring out $e^{i\pi k/7}$.
solution:
Let $\zeta=e^{2\pi i/7}$. The numbers $1,\zeta,\dots,\zeta^6$ are the seven roots of $x^7-1$, so $x^7-1=(x-1)\prod_{k=1}^{6}(x-\zeta^k)$. Dividing by $x-1$,
$$1+x+x^2+\dots+x^6=\prod_{k=1}^{6}(x-\zeta^k).$$
Setting $x=1$: $\prod_{k=1}^{6}(1-\zeta^k)=7$. Taking absolute values, $\prod_{k=1}^6|1-\zeta^k|=7$.

For $1\le k\le6$,
$$1-\zeta^k=e^{i\pi k/7}\left(e^{-i\pi k/7}-e^{i\pi k/7}\right)=-2i\sin\frac{k\pi}{7}\,e^{i\pi k/7},$$
so $|1-\zeta^k|=2\sin\frac{k\pi}7$ (the sine is positive since $0<\frac{k\pi}7<\pi$). Therefore
$$2^6\prod_{k=1}^{6}\sin\frac{k\pi}{7}=7,\qquad\text{so the product is }\boxed{\dfrac{7}{64}}.$$

### o83
source: original
type: proof
difficulty: 6
techniques: complex-numbers
statement:
Let $ABCD$ be a convex quadrilateral. On each of its four sides construct a square lying outside the quadrilateral, and let $P,Q,R,S$ be the centers of the squares on $AB,BC,CD,DA$ respectively. Prove that $PR=QS$ and that the lines $PR$ and $QS$ are perpendicular.
asked:
Show that the segments joining the centers of opposite squares have equal length and are perpendicular.
technique:
Treat the plane as the complex numbers, where rotating a vector by $90^\circ$ is multiplication by $i$. Then each center is an explicit expression in the vertices.
hint:
Orient $ABCD$ counterclockwise. The outside of the quadrilateral is then to the right of each directed side $A\to B$, $B\to C$, and so on. Express the center of the square on $AB$ as the midpoint plus half of the vector $\overrightarrow{AB}$ rotated by $-90^\circ$.
hint:
With $a,b,c,d$ the complex numbers of the vertices, the center is $p=\frac{(1+i)a+(1-i)b}{2}$, and similarly for $q,r,s$. Compare $s-q$ with $r-p$.
solution:
Reflecting the figure if necessary (which preserves lengths and perpendicularity), assume $A,B,C,D$ are in counterclockwise order. Because $ABCD$ is convex, its interior lies to the left of each directed side, and the exterior to the right.

Let $a,b,c,d$ be the complex numbers of the vertices. The square on $AB$ lying to the right of $A\to B$ has its center at distance $\frac{|AB|}{2}$ from the midpoint of $AB$, perpendicular to $AB$ and on the right. Rotating a vector by $-90^\circ$ means multiplying by $-i$, which sends the direction of $\overrightarrow{AB}$ to the right, so
$$p=\frac{a+b}{2}-i\,\frac{b-a}{2}=ua+vb,\qquad u=\frac{1+i}2,\ v=\frac{1-i}2.$$
In the same way $q=ub+vc$, $r=uc+vd$, $s=ud+va$.

Note $iu=\frac{i-1}{2}=-v$ and $iv=\frac{i+1}{2}=u$. Then
$$i(r-p)=i\big(uc+vd-ua-vb\big)=-vc+ud+va-ub=(ud+va)-(ub+vc)=s-q.$$
So $s-q=i(r-p)$: the vector $\overrightarrow{QS}$ is the vector $\overrightarrow{PR}$ rotated by $90^\circ$, so $QS=PR$ and $QS\perp PR$. (We need $P\ne R$ for the lines to be defined. If $p=r$, then $b-d=-i(a-c)$, so $\operatorname{Im}\big((b-d)\overline{(a-c)}\big)=-|a-c|^2<0$; but for a convex counterclockwise quadrilateral this imaginary part is positive, because the diagonals cross.) $\blacksquare$

### o84
source: original
type: answer
difficulty: 4
techniques: trigonometry
statement:
Find the exact value of $\sin10^\circ\,\sin50^\circ\,\sin70^\circ$.
asked:
Compute the product exactly.
technique:
Rewrite the factors so that a product-collapsing identity applies.
hint:
Use $\sin\theta=\cos(90^\circ-\theta)$ to rewrite the product as $\cos80^\circ\cos40^\circ\cos20^\circ$.
hint:
Multiply and divide by $\sin20^\circ$. Each time, $\sin\theta\cos\theta=\frac12\sin2\theta$ combines two factors.
solution:
Since $\sin10^\circ=\cos80^\circ$, $\sin50^\circ=\cos40^\circ$, $\sin70^\circ=\cos20^\circ$, the product is $P=\cos20^\circ\cos40^\circ\cos80^\circ$. Multiply by $\sin20^\circ\ne0$ and use $\sin\theta\cos\theta=\frac12\sin2\theta$ three times:
$$\sin20^\circ\cos20^\circ=\tfrac12\sin40^\circ,$$
$$\tfrac12\sin40^\circ\cos40^\circ=\tfrac14\sin80^\circ,$$
$$\tfrac14\sin80^\circ\cos80^\circ=\tfrac18\sin160^\circ=\tfrac18\sin20^\circ.$$
So $P\sin20^\circ=\frac18\sin20^\circ$, giving $P=\boxed{\dfrac18}$.

### o85
source: original
type: answer
difficulty: 4
techniques: angle-chasing
statement:
In an acute triangle $ABC$ we have $\angle A=70^\circ$, $\angle B=75^\circ$ and $\angle C=35^\circ$. Let $O$ be the circumcenter and $H$ the orthocenter. Find $\angle OAH$.
asked:
Find the angle between the segments $AO$ and $AH$, in degrees.
technique:
Compute the angle each of the two lines makes with side $AB$, using a right triangle for the altitude and an isosceles triangle for the radius.
hint:
Let $D$ be the foot of the altitude from $A$. In right triangle $ABD$, find $\angle BAD$. The orthocenter lies on $AD$.
hint:
For $\angle BAO$, use the central angle $\angle AOB$ and the fact that $OA=OB$. Then subtract.
solution:
Let $D$ be the foot of the altitude from $A$. The triangle is acute, so $D$ lies on segment $BC$ and $H$ lies on segment $AD$ inside the triangle. In right triangle $ABD$, $\angle BAD=90^\circ-\angle B=15^\circ$, so $\angle BAH=15^\circ$.

The central angle on chord $AB$ is $\angle AOB=2\angle C=70^\circ$ (the triangle is acute, so $O$ is inside and on the same side of $AB$ as $C$). Triangle $OAB$ is isosceles with $OA=OB$, so $\angle OAB=\frac{180^\circ-70^\circ}{2}=55^\circ$.

Both $O$ and $H$ lie inside the triangle, so rays $AO$ and $AH$ both lie inside $\angle BAC$ and are measured from ray $AB$. Therefore
$$\angle OAH=\angle OAB-\angle HAB=55^\circ-15^\circ=\boxed{40^\circ}.$$
(In general $\angle OAB-\angle HAB=(90^\circ-C)-(90^\circ-B)=B-C$.)

### o86
source: original
type: proof
difficulty: 5
techniques: similar-triangles
statement:
In a trapezoid $ABCD$ with $AB\parallel CD$, let $AB=a$ and $CD=b$. The diagonals $AC$ and $BD$ meet at $P$. The line through $P$ parallel to $AB$ meets $AD$ at $M$ and $BC$ at $N$. Prove that $MN=\dfrac{2ab}{a+b}$.
asked:
Show that the segment through the diagonal intersection, parallel to the bases and cut off by the legs, has length $\frac{2ab}{a+b}$.
technique:
Parallel lines create pairs of similar triangles. Use one pair to find where $P$ divides the diagonals, and other pairs to measure the two halves of $MN$.
hint:
Triangles $PAB$ and $PCD$ are similar. What does this say about the ratio $AP:PC$?
hint:
Once you know $AP:AC$, use that $MP\parallel DC$ to get a triangle containing $M,P$ similar to triangle $ADC$. Do the same on the other side with triangle $CAB$.
solution:
Since $AB\parallel CD$, the angles $\angle PAB=\angle PCD$ and $\angle PBA=\angle PDC$ (alternate angles), so triangles $PAB$ and $PCD$ are similar with ratio $a:b$. Hence $AP:PC=a:b$, so
$$\frac{AP}{AC}=\frac{a}{a+b},\qquad\frac{CP}{CA}=\frac{b}{a+b}.$$
Since $M$ lies on $AD$ and $MP\parallel DC$, triangles $AMP$ and $ADC$ are similar (they share the angle at $A$, and $\angle AMP=\angle ADC$ as corresponding angles). Thus
$$MP=DC\cdot\frac{AP}{AC}=\frac{ab}{a+b}.$$
Similarly $N$ lies on $BC$ and $PN\parallel AB$, so triangles $CPN$ and $CAB$ are similar, and
$$PN=AB\cdot\frac{CP}{CA}=a\cdot\frac{b}{a+b}=\frac{ab}{a+b}.$$
From the similar triangles, $AM/AD=AP/AC<1$, so $M$ lies on segment $AD$, and likewise $N$ lies on segment $BC$. The point $P$ is inside the convex trapezoid, so on the line $MN$ it lies between the boundary points $M$ and $N$. Therefore
$$MN=MP+PN=\frac{2ab}{a+b}.\qquad\blacksquare$$
