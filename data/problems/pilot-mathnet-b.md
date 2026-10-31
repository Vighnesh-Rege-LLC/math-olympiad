### m13
source: mathnet
mathnet_id: 05cw
country: Estonia
competition: Estonian Mathematical Olympiad
type: proof
difficulty: 6
techniques: angle-chasing
statement:
In an isosceles triangle $ABC$ with $AB=AC$, the bisector of the angle $BAC$ intersects $BC$ at $D$. The bisector of the angle $ABC$ intersects the perpendicular bisector of $AD$ at $E$. Prove that the bisector of the angle $ACB$ is perpendicular to $DE$.
asked:
Show that the line $DE$ meets the bisector from $C$ at a right angle.
technique:
First prove $A,B,D,E$ are concyclic, then chase angles at $D$ and at the incenter.
hint:
In an isosceles triangle the bisector $AD$ is also an altitude, so $\angle ADB=90^\circ$. Which circle passes through $A,B,D$?
hint:
Let the bisector of $\angle ABC$ meet that circle again at $E'$. Show $E'A=E'D$, so $E'=E$.
hint:
Let $I$ be the incenter, on $AD$. Compute $\angle EDI$ using the circle and $\angle CID$ in the right triangle $CDI$, and add them.
solution:
Let $\gamma=\angle ABC=\angle ACB$. Since $AB=AC$, the bisector $AD$ is also the altitude, so $\angle ADB=90^\circ$ and $A,B,D$ lie on the circle $\omega$ with diameter $AB$. The incenter $I$ lies on $AD$.

Let the bisector of $\angle ABC$ meet $\omega$ again at $E'$. Since $BE'$ bisects $\angle ABD$, the arcs $AE'$ and $E'D$ are equal, so $E'A=E'D$ and $E'$ is on the perpendicular bisector of $AD$. This line meets $BI$ in one point, so $E'=E$. Thus $ABDE$ is cyclic, with $E$ the midpoint of arc $AD$ not containing $B$, so $E$ and $C$ lie on the same side of $AD$.

Now $\angle EDI=\angle EDA=\angle EBA=\frac\gamma2$ (inscribed angles on arc $EA$). In the right triangle $CDI$, $\angle DCI=\frac\gamma2$ because $CI$ bisects $\angle ACB$, so $\angle CID=90^\circ-\frac\gamma2$.

Since $\angle IDC=90^\circ$ and $E$ is on the same side of $AD$ as $C$ with $\angle EDI=\frac\gamma2<90^\circ$, the ray $DE$ lies inside the right angle $IDC$, so it meets segment $IC$ at a point $X$. In triangle $DIX$ the angles at $D$ and $I$ are $\frac\gamma2$ and $90^\circ-\frac\gamma2$, so the angle at $X$ is $90^\circ$. Hence $CI\perp DE$. $\blacksquare$

### m14
source: mathnet
mathnet_id: 03gy
country: Canada
competition: Canadian Mathematical Olympiad
type: answer
difficulty: 5
techniques: coordinates
statement:
Consider all line segments of length $4$ with one end-point on the line $y=x$ and the other end-point on the line $y=2x$. Find the equation of the locus of the midpoints of these line segments.
asked:
Describe, by an equation in $x$ and $y$, the path traced by the midpoints.
technique:
Use [[coordinates]]: parametrize the two endpoints, express the midpoint, and eliminate the parameters.
hint:
Let the endpoints be $(a,a)$ and $(b,2b)$. Write the midpoint $(x,y)$ in terms of $a$ and $b$.
hint:
Solve for $a$ and $b$ in terms of $x$ and $y$, then substitute into the length condition.
solution:
Let the endpoints be $A=(a,a)$ and $B=(b,2b)$. The midpoint is $(x,y)=\left(\frac{a+b}2,\frac{a+2b}2\right)$. Solving $a+b=2x$, $a+2b=2y$ gives $b=2y-2x$ and $a=4x-2y$.

The length condition is $(b-a)^2+(2b-a)^2=16$. Now $b-a=4y-6x$ and $2b-a=6y-8x$, so
$$(4y-6x)^2+(6y-8x)^2=16\ \Longrightarrow\ 100x^2-144xy+52y^2=16\ \Longrightarrow\ \boxed{25x^2-36xy+13y^2=4}.$$

### m15
source: mathnet
mathnet_id: 0h7f
country: Ukraine
competition: 56th Ukrainian National Mathematical Olympiad, Third Round
type: answer
difficulty: 4
techniques: casework, extremal
statement:
$30$ children, boys and girls, formed a circle. It occurred that there is no child such that both its neighbors are boys. What is the least possible number of girls?
asked:
Find the smallest number of girls, given that no child has two boys as neighbors.
technique:
Use [[casework]] on the structure of the circle: look at the maximal blocks of consecutive boys and the blocks of girls between them.
hint:
How long can a block of consecutive boys be? What if there are three boys in a row?
hint:
Between two blocks of boys, how many girls are needed so that no child sits between two boys?
hint:
If there are $k$ blocks of boys, how many boys and girls are there at most / at least? Then optimize.
solution:
Three boys in a row would make the middle boy have two boy neighbors, so every block of consecutive boys has size at most $2$. Two blocks of boys separated by exactly one girl would give that girl two boy neighbors, so any two consecutive blocks of boys are separated by at least $2$ girls.

Suppose there are $k\ge1$ blocks of boys around the circle. Then there are also $k$ blocks of girls, each of size at least $2$, so $g\ge2k$ girls; and $b\le2k$ boys.

If $g\le15$ then $b\ge15$, so $2k\ge b\ge15$ and $k\ge8$. But then $g\ge2k\ge16$, a contradiction. So $g\ge16$. (With no boys at all, $g=30$.)

**Example with $16$ girls:** around the circle put seven blocks "boy, boy" alternating with girl blocks of sizes $2,2,2,2,2,2,4$. That is $14$ boys and $6\cdot2+4=16$ girls, and no child has two boy neighbors.

The minimum is $\boxed{16}$.

### m16
source: mathnet
mathnet_id: 0ew4
country: Soviet Union
competition: 2nd ASU
type: proof
difficulty: 5
techniques: trigonometry
statement:
$ABCD$ is any convex quadrilateral. Construct a new quadrilateral as follows. Take $A'$ so that $A$ is the midpoint of $DA'$; similarly, $B'$ so that $B$ is the midpoint of $AB'$; $C'$ so that $C$ is the midpoint of $BC'$; and $D'$ so that $D$ is the midpoint of $CD'$. Show that the area of $A'B'C'D'$ is five times the area of $ABCD$.
asked:
Show that the new quadrilateral built by doubling each side outward has exactly five times the area of the original.
technique:
Break $A'B'C'D'$ into $ABCD$ plus four triangles at the corners, and compute each triangle's area with $\frac12ab\sin C$ ([[trigonometry]]).
hint:
Look at triangle $A'B'A$. How do its two sides at $A$ compare with $AD$ and $AB$?
hint:
What is the angle between them, compared with $\angle DAB$?
hint:
Express the area of each of the four corner triangles through triangles such as $ABD$, and add.
solution:
Since $ABCD$ is convex, each corner triangle such as $A'B'A$ lies on the far side of line $AB$ from $ABCD$, so the pieces do not overlap. The quadrilateral $A'B'C'D'$ consists of $ABCD$ together with the four triangles $A'B'A$, $B'C'B$, $C'D'C$, $D'A'D$.

In triangle $A'B'A$: $AA'=AD$ (as $A$ is the midpoint of $DA'$) and $AB'=2AB$ (as $B$ is the midpoint of $AB'$). The ray $AA'$ is opposite to ray $AD$ and the ray $AB'$ is ray $AB$, so $\angle A'AB'=180^\circ-\angle DAB$, which has the same sine as $\angle DAB$. Hence
$$[A'B'A]=\tfrac12\cdot AD\cdot2AB\cdot\sin\angle DAB=2\cdot\tfrac12AD\cdot AB\sin\angle DAB=2[ABD].$$
In the same way, $[B'C'B]=2[BCA]$, $[C'D'C]=2[CDB]$, $[D'A'D]=2[DAC]$.

Since the diagonals split $ABCD$ in two ways, $[ABD]+[CDB]=[ABCD]$ and $[BCA]+[DAC]=[ABCD]$. So the four triangles have total area $2\cdot2[ABCD]=4[ABCD]$, and $[A'B'C'D']=[ABCD]+4[ABCD]=5[ABCD]$. $\blacksquare$

### m17
source: mathnet
mathnet_id: 0csh
country: Russia
competition: XL Russian mathematical olympiad
type: answer
difficulty: 6
techniques: divisibility, casework
statement:
The teacher gave to Pete four distinct positive integers. Pete has calculated the greatest common divisor of every two of these numbers. He obtained six numbers: $1,2,3,4,5$, and $N$, where $N>5$. Find the least possible value of $N$.
asked:
Four numbers have six pairwise gcds $1,2,3,4,5,N$. Find the smallest possible $N>5$.
technique:
For a number $k$, count how many of the four numbers are divisible by $k$, and then how many of the six gcds are.
hint:
If $j$ of the four numbers are divisible by $k$, how many of the pairwise gcds are divisible by $k$?
hint:
Show that the answer can never be exactly $2$. Apply this to $k=2,3,4,5$.
hint:
That restricts $N$ to a short list. Then find four numbers realizing the smallest candidate.
solution:
The gcd of two numbers is divisible by $k$ exactly when both numbers are divisible by $k$. So if $j$ of the four numbers are divisible by $k$, exactly $\binom j2$ of the six gcds are. This count is $0,0,1,3,6$ for $j=0,1,2,3,4$, so it is never $2$.

Apply this to the six gcds $1,2,3,4,5,N$:
- $k=2$: $2$ and $4$ are divisible by $2$, so the count is at least $2$, hence at least $3$; so $N$ is even.
- $k=3$: $3$ is divisible by $3$. If $3\mid N$ the count would be exactly $2$. So $3\nmid N$.
- $k=4$: $4$ is, so $4\nmid N$. $k=5$: $5\nmid N$.

So $N>5$ is even and not divisible by $3,4,5$: $6,8,10,12$ are excluded, so $N\ge14$.

**$N=14$ occurs:** for $(4,15,70,84)$ the gcds are $\gcd(4,15)=1$, $\gcd(4,70)=2$, $\gcd(4,84)=4$, $\gcd(15,70)=5$, $\gcd(15,84)=3$, $\gcd(70,84)=14$. The minimum is $\boxed{14}$.

### m18
source: mathnet
mathnet_id: 0f80
country: Soviet Union
competition: 22nd ASU
type: answer
difficulty: 4
techniques: parity, invariants
statement:
A book contains $30$ stories. Each story has a different number of pages under $31$. The first story starts on page $1$ and each story starts on a new page. What is the largest possible number of stories that can begin on odd page numbers?
asked:
The stories have $1,2,\dots,30$ pages in some order. Maximize how many start on an odd page.
technique:
Track how the parity of the starting page changes from one story to the next.
hint:
When does the starting page of the next story have the same parity as the current one, and when does it flip?
hint:
Compare stories with an even number of pages to those with an odd number. How must the odd-length stories alternate?
hint:
How many of each kind are there, and can all even-length stories start on odd pages?
solution:
A story with an even number of pages leaves the parity of the next starting page unchanged, and a story with an odd number of pages flips it. The page counts $1,\dots,30$ contain $15$ odd and $15$ even numbers.

Before the first odd-length story only even-length stories occur, so it starts on page $1+(\text{even})$, an odd page. Between two consecutive odd-length stories only even-length ones occur, so the parity of their starting pages alternates: odd, even, odd, ... Hence among the $15$ odd-length stories exactly $8$ start on odd pages (the 1st, 3rd, ..., 15th), whatever the order.

The even-length stories can all start on odd pages: place all of them first, since $1+(\text{sum of even numbers})$ is odd. So the maximum is $15+8=\boxed{23}$.

### m19
source: mathnet
mathnet_id: 08l7
country: JBMO
competition: 2008 Shortlist JBMO
type: proof
difficulty: 6
techniques: cauchy-schwarz, am-gm
statement:
Show that
$$(x+y+z)\left(\frac1x+\frac1y+\frac1z\right)\ge4\left(\frac x{xy+1}+\frac y{yz+1}+\frac z{zx+1}\right)^2$$
for all positive real numbers $x,y,z$.
asked:
Prove the inequality for all positive reals.
technique:
Use [[cauchy-schwarz]] to bound the left side from below by a perfect square, and [[am-gm]] to bound each fraction on the right.
hint:
Find an expression whose square sits between the two sides. Try $\sqrt{x/y}+\sqrt{y/z}+\sqrt{z/x}$.
hint:
For the left side, apply Cauchy–Schwarz to $(\sqrt x,\sqrt y,\sqrt z)$ and $(1/\sqrt y,1/\sqrt z,1/\sqrt x)$.
hint:
For the right side show $\sqrt{x/y}\ge\frac{2x}{xy+1}$ by AM-GM.
solution:
Let $S=\sqrt{\frac xy}+\sqrt{\frac yz}+\sqrt{\frac zx}$.

**Left $\ge S^2$.** By Cauchy–Schwarz with the vectors $(\sqrt x,\sqrt y,\sqrt z)$ and $\left(\frac1{\sqrt y},\frac1{\sqrt z},\frac1{\sqrt x}\right)$,
$$(x+y+z)\left(\frac1y+\frac1z+\frac1x\right)\ge\left(\sqrt{\tfrac xy}+\sqrt{\tfrac yz}+\sqrt{\tfrac zx}\right)^2=S^2.$$
**$S\ge$ the bracket.** AM-GM gives $xy+1\ge2\sqrt{xy}$, so
$$\frac{2x}{xy+1}\le\frac{2x}{2\sqrt{xy}}=\sqrt{\frac xy}.$$
Adding the three cyclic versions, $S\ge2\left(\frac x{xy+1}+\frac y{yz+1}+\frac z{zx+1}\right)$, and squaring (both sides positive) gives $S^2\ge4(\dots)^2$.

Combining, the left side is at least $S^2\ge4\left(\frac x{xy+1}+\dots\right)^2$. $\blacksquare$

### m20
source: mathnet
mathnet_id: 0dfz
country: Saudi Arabia
competition: Saudi Arabian IMO Booklet
type: answer
difficulty: 7
techniques: divisibility, diophantine, modular-arithmetic
statement:
Determine the smallest positive integer $a$ for which there exist a prime number $p$ and a positive integer $b\ge2$ such that
$$\frac{a^p-a}p=b^2.$$
asked:
Find the smallest positive $a$ for which $\frac{a^p-a}{p}$ is a square of an integer $b\ge2$ for some prime $p$.
technique:
Use [[divisibility]]: $a$ and $a^{p-1}-1$ are coprime and their product is $pb^2$. Treat $p=2$ and $p\ge3$ separately.
hint:
For $p=2$ the equation is $a(a-1)=2b^2$. Search for the smallest solution with $b\ge2$.
hint:
For $p\ge3$ write $a(a^{p-1}-1)=pb^2$ with coprime factors on the left. Each factor is a square or $p$ times a square. Which factors can be squares?
hint:
Show that no $a\le8$ works for $p\ge3$: the only square candidates are $a=1$ (which gives $0$) and $a=4$.
solution:
**$p=2$.** The equation is $a(a-1)=2b^2$ with $b\ge2$, so $a(a-1)\ge8$. Checking $a=2,\dots,8$ gives $a(a-1)/2=1,3,6,10,15,21,28$, none a square; and $a=9$ gives $36=6^2$, so $a=9$ works with $b=6$.

**$p\ge3$.** Suppose $a\le8$ works. Since $\gcd(a,a^{p-1}-1)=1$ and $a(a^{p-1}-1)=pb^2$, each of the two factors is a perfect square or $p$ times a perfect square, and $p$ divides exactly one of them.

- If $p\mid a$ then $a=ps^2$ and $a^{p-1}-1=t^2$, i.e. $(a^{(p-1)/2}-t)(a^{(p-1)/2}+t)=1$, forcing $a^{(p-1)/2}=1$, so $a=1$, but $a=ps^2\ge3$. Impossible.
- If $p\nmid a$ then $a=s^2$ and $a^{p-1}-1=pt^2$. The square candidates $a\le8$ are $1$ and $4$; $a=1$ gives $0$, which is not $b^2$ with $b\ge2$. For $a=4$: $(2^{p-1}-1)(2^{p-1}+1)=pt^2$ with coprime factors; by Fermat $p\mid2^{p-1}-1$, so $2^{p-1}+1=c^2$ is a square. Then $(c-1)(c+1)=2^{p-1}$ forces $c-1=2$, $c+1=4$, $2^{p-1}=8$, $p=4$, not prime. Impossible.

So no $a\le8$ works, and the smallest is $\boxed{9}$.

### m21
source: mathnet
mathnet_id: 01ey
country: Baltic Way
competition: Baltic Way 2019
type: answer
difficulty: 7
techniques: polynomials, parity
statement:
Does there exist a polynomial $f(x)$ with integer coefficients of degree four such that for any integer $k$, the polynomial $f(x)+k$ is either irreducible or has a rational root?
asked:
Decide whether such a degree-four integer polynomial exists, and prove your answer.
technique:
Look for a quartic of the form $x^4+\alpha x$ and use [[polynomials]]: if $f+k$ is reducible without a rational root, it factors into two monic quadratics. A [[parity]] argument on the coefficients finishes.
hint:
If a quartic has no rational root but is reducible over $\mathbb Q$, what degrees can its factors have? What does Gauss's lemma say about integer coefficients?
hint:
Compare coefficients of $x^4+2x+k=(x^2+ax+b)(x^2+cx+d)$. Eliminate $c$ and look at the equations for $b+d$ and $a(d-b)$.
hint:
Consider the parities of $a$, $b+d$ and $d-b$. The choice $\alpha=2$ (that is, $f(x)=x^4+2x$) makes the equation $a(d-b)=2$ impossible.
solution:
**Yes**: $f(x)=x^4+2x$ works.

Suppose $f(x)+k=x^4+2x+k$ is reducible over $\mathbb Q$ and has no rational root. Then it has no linear factor, so it is a product of two quadratics, and by Gauss's lemma we may take both monic with integer coefficients: $(x^2+ax+b)(x^2+cx+d)$. Comparing coefficients,
$$a+c=0,\quad b+d+ac=0,\quad ad+bc=2.$$
So $c=-a$, $b+d=a^2$, and $a(d-b)=2$.

Note that $d-b$ and $b+d$ have the same parity.
- If $a$ is odd, then $b+d=a^2$ is odd, so $d-b$ is odd and $a(d-b)$ is odd, not $2$.
- If $a$ is even, then $b+d=a^2$ is even, so $d-b$ is even and $a(d-b)$ is divisible by $4$, not $2$.

Both cases contradict $a(d-b)=2$.

Hence for every integer $k$, $x^4+2x+k$ is irreducible or has a rational root.

### m22
source: mathnet
mathnet_id: 0dbf
country: Saudi Arabia
competition: Saudi Arabian Mathematical Competitions
type: proof
difficulty: 7
techniques: polynomials, symmetry
statement:
Let $P(x)$ be a polynomial of degree $n\ge2$ with rational coefficients such that $P(x)$ has $n$ pairwise different real roots forming an arithmetic progression. Prove that among the roots of $P(x)$ there are two that are also the roots of some polynomial of degree $2$ with rational coefficients.
asked:
Show that two of the roots satisfy a rational quadratic.
technique:
Use [[polynomials]] (Vieta): the sum and the sum of squares of the roots are rational; this forces the sum and product of the two extreme roots to be rational.
hint:
Which two roots are the natural candidates? Think of the first and last roots of the progression.
hint:
Let $s=x_1+x_n$ and let $d$ be the common difference. The sum of the roots is $\frac{ns}2$. What does Vieta say about the sum of squares?
hint:
Write the roots symmetrically about the midpoint $\frac s2$ and compute $\sum x_i^2$ in terms of $s$ and $d$.
solution:
Let the roots be $x_i=x_1+(i-1)d$ with $d>0$, and set $s=x_1+x_n$, $c=\frac s2$. Then $x_i=c+\left(i-\frac{n+1}2\right)d$.

By Vieta, $e_1=\sum x_i$ and $e_2=\sum_{i<j}x_ix_j$ are rational. First, $e_1=nc=\frac{ns}2$, so $s$ is rational.

Next, $\sum x_i^2=e_1^2-2e_2$ is rational. Also
$$\sum x_i^2=nc^2+d^2\sum_{i=1}^n\left(i-\tfrac{n+1}2\right)^2=nc^2+\frac{n(n^2-1)}{12}d^2.$$
Since $nc^2$ is rational, $\frac{n(n^2-1)}{12}d^2$ is rational and $n\ge2$ gives $n(n^2-1)\ne0$, so $d^2$ is rational.

Then $x_1x_n=c^2-\left(\frac{(n-1)d}2\right)^2$ is rational. So $x_1,x_n$ are the roots of $t^2-st+x_1x_n$, a quadratic with rational coefficients. $\blacksquare$

### m23
source: mathnet
mathnet_id: 05bw
country: Estonia
competition: Estonian Mathematical Olympiad
type: proof
difficulty: 4
techniques: cauchy-schwarz
statement:
Anna, Berta and Carol make fruit drinks from syrup. Anna makes $a$ litres of drink by mixing water and syrup in the proportion of $a:1$. Berta makes $b$ litres of drink by mixing water and syrup in the proportion of $b:1$. Carol makes $c$ litres of drink by mixing water and syrup in the proportion of $c:1$. (It is not known if $a$, $b$ and $c$ are integers.) They make $6$ litres of drink in total. Prove that they use at most $2$ litres of syrup.
asked:
Translate to an inequality in $a,b,c$ with $a+b+c=6$ and prove it.
technique:
After translating, apply [[cauchy-schwarz]] (Titu's form) to the sum of reciprocals.
hint:
In $a$ litres of drink with water : syrup $=a:1$, what fraction is syrup? So how much syrup is in Anna's drink?
hint:
You want $\sum\frac a{a+1}\le2$. Rewrite it using $\frac a{a+1}=1-\frac1{a+1}$.
hint:
Apply Titu's lemma to $\sum\frac1{a+1}$ with $\sum(a+1)=9$.
solution:
In Anna's drink the syrup is $\frac1{a+1}$ of the volume, so she uses $\frac a{a+1}$ litres of syrup; similarly for the others. We must show that $a+b+c=6$ with $a,b,c>0$ implies
$$\frac a{a+1}+\frac b{b+1}+\frac c{c+1}\le2.$$
Since $\frac a{a+1}=1-\frac1{a+1}$, this is equivalent to $\frac1{a+1}+\frac1{b+1}+\frac1{c+1}\ge1$. By Cauchy–Schwarz (Titu's lemma),
$$\frac1{a+1}+\frac1{b+1}+\frac1{c+1}\ge\frac{(1+1+1)^2}{(a+1)+(b+1)+(c+1)}=\frac9{6+3}=1.\ \blacksquare$$

### m24
source: mathnet
mathnet_id: 01ph
country: Belarus
competition: Belarusian Mathematical Olympiad
type: proof
difficulty: 8
techniques: pigeonhole, cauchy-schwarz
statement:
$N\ge2$ segments are arranged inside a unit circle $\Gamma$. The sum of the lengths of all these segments is equal to $2\sqrt N$. Prove that there exists a concentric with $\Gamma$ circumference intersecting at least two of these segments.
asked:
Show that some circle centered at the center of $\Gamma$ meets at least two of the segments.
technique:
Think of the set of distances from the center $O$ to points of a segment as an interval, and use an averaging argument ([[pigeonhole]] for areas) together with [[cauchy-schwarz]] on the lengths.
hint:
A circle of radius $r$ about $O$ meets a segment exactly when $r$ lies in the segment's range of distances $[r_{\min},r_{\max}]$. What would it mean if no circle met two segments?
hint:
If those intervals were disjoint, compare $\sum(r_{\max}^2-r_{\min}^2)$ with $1$.
hint:
Show that $r_{\max}^2-r_{\min}^2\ge\frac{d^2}4$ for a segment of length $d$, then use $\sum d_i^2\ge\frac{(\sum d_i)^2}N$.
solution:
For a segment $s$ let $I_s=[r_{\min},r_{\max}]\subseteq[0,1]$ be the set of distances from the center $O$ to its points. A circle of radius $r$ about $O$ meets $s$ iff $r\in I_s$. Suppose, for contradiction, that no circle meets two segments, i.e. the intervals $I_s$ are pairwise disjoint.

Disjoint intervals in $[0,1]$ satisfy $\sum(r_{\max}^2-r_{\min}^2)\le\int_0^12r\,dr=1$, and the inequality is strict because $N\ge2$ disjoint closed intervals cannot cover the connected interval $[0,1]$. So $\sum(r_{\max}^2-r_{\min}^2)<1$.

**Claim.** If a segment $AB$ has length $d$, then $r_{\max}^2-r_{\min}^2\ge\frac{d^2}4$. Let $C$ be the foot of the perpendicular from $O$ to line $AB$.
- If $C$ is on segment $AB$: $r_{\min}=OC$ and $r_{\max}=\max(OA,OB)$, so $r_{\max}^2-r_{\min}^2=\max(AC^2,BC^2)\ge\frac{d^2}4$.
- If $C$ is outside, say beyond $B$: $r_{\min}=OB$, $r_{\max}=OA$, and $OA^2-OB^2=AC^2-BC^2=(AC-BC)(AC+BC)=d\,(AC+BC)\ge d^2$.

Summing with the lengths $d_1,\dots,d_N$ and Cauchy–Schwarz,
$$\sum(r_{\max}^2-r_{\min}^2)\ge\frac14\sum d_i^2\ge\frac1{4N}\Big(\sum d_i\Big)^2=\frac{4N}{4N}=1,$$
contradicting the strict inequality above. $\blacksquare$
