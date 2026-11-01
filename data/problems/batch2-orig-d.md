### o102
source: original
type: answer
difficulty: 2
techniques: angle-chasing
statement:
Triangle $ABC$ has $AB=AC$ and $\angle BAC=40^\circ$. The point $D$ lies on the segment $AC$, with $D\ne C$, and satisfies $BD=BC$. Find $\angle ABD$.
asked:
Find the measure, in degrees, of the angle between $BA$ and $BD$.
technique:
Isosceles triangles hand equal angles from one place to another. Write down every angle you can determine, one triangle at a time.
hint:
Start with the angles of triangle $ABC$. Since $AB=AC$, the two base angles are equal.
hint:
Triangle $BCD$ is also isosceles. Which two of its angles are equal, and what is the third one?
hint:
Having found $\angle DBC$, compare it with $\angle ABC$. Why does the ray $BD$ lie inside the angle $ABC$?
solution:
Since $AB=AC$, the base angles are equal: $\angle ABC=\angle ACB=\tfrac12(180^\circ-40^\circ)=70^\circ$.

The point $D$ lies on segment $AC$ and $D\ne C$, so $\angle BCD=\angle BCA=70^\circ$. In triangle $BCD$ we have $BD=BC$, so the angles opposite these sides are equal: $\angle BDC=\angle BCD=70^\circ$. Hence $\angle DBC=180^\circ-70^\circ-70^\circ=40^\circ$.

Because $D$ lies on segment $AC$, the ray $BD$ lies inside angle $ABC$, so $\angle ABD=\angle ABC-\angle DBC=70^\circ-40^\circ=\boxed{30^\circ}$.

### o103
source: original
type: answer
difficulty: 2
techniques: similar-triangles
statement:
In triangle $ABC$ the angle at $C$ is a right angle, $CA=6$ and $CB=8$. A square has one vertex at $C$, one vertex on the segment $CA$, one vertex on the segment $CB$, and its fourth vertex on the hypotenuse $AB$. Find the side length of the square.
asked:
Find the side length of the square described.
technique:
When a line cuts off a corner of a triangle parallel to the opposite side, the small triangle is a scaled copy of the big one.
hint:
Name the square $CDEF$ with $D$ on $CA$, $F$ on $CB$ and $E$ on $AB$, and let its side be $s$. Which side of the square is parallel to $CB$?
hint:
Compare triangle $ADE$ with triangle $ACB$. Express $AD$ in terms of $s$ and set up a proportion.
solution:
Let the square be $CDEF$ with $D$ on $CA$, $F$ on $CB$, $E$ on $AB$, and side $s$. Then $DE\parallel CF$, that is $DE\parallel CB$, and $DE\perp CA$.

Triangles $ADE$ and $ACB$ both have a right angle (at $D$ and at $C$) and share the angle at $A$, so they are similar. Matching sides, $\dfrac{AD}{AC}=\dfrac{DE}{CB}$. Here $AD=6-s$ and $DE=s$, so
$$\frac{6-s}{6}=\frac{s}{8}\ \Longrightarrow\ 48-8s=6s\ \Longrightarrow\ s=\frac{48}{14}=\boxed{\dfrac{24}{7}}.$$

### o104
source: original
type: answer
difficulty: 2
techniques: complex-numbers
statement:
A complex number $z$ satisfies $z+\dfrac1z=1$. Find the value of $z^{2025}+\dfrac1{z^{2025}}$.
asked:
Compute $z^{2025}+z^{-2025}$ for a complex number $z$ with $z+1/z=1$.
technique:
Work out what kind of complex number $z$ must be, then look for a power of $z$ that is simple.
hint:
Multiply the equation by $z$ and solve the quadratic. Where do the solutions sit on the unit circle, and at what angle?
hint:
Write each solution as $e^{i\theta}$, and use that $2025$ is a multiple of $3$.
solution:
Multiplying $z+\frac1z=1$ by $z$ gives $z^2-z+1=0$ (note $z\ne0$), so $z=\frac{1\pm i\sqrt3}2=e^{\pm i\pi/3}$. Then
$$z^{2025}=e^{\pm 2025\,i\pi/3}=e^{\pm 675\,i\pi}=(-1)^{675}=-1,$$
and $\dfrac1{z^{2025}}=-1$ as well. The sum is $\boxed{-2}$.

### o105
source: original
type: answer
difficulty: 2
techniques: generating-functions
statement:
In how many ways can exactly $20$ cents be paid using $1$-cent, $2$-cent and $5$-cent coins? Coins of the same value are identical, and the order of the coins does not matter. (Two ways differ if the numbers of coins of some value differ.)
asked:
Count the triples $(a,b,c)$ of non-negative integers with $a+2b+5c=20$.
technique:
Encode each kind of coin by a power series in which the exponent records the amount of money, and see what multiplying the series does.
hint:
Using only $1$-cent coins, the amounts that can be paid are $0,1,2,\dots$, each in one way. Write this as the series $1+x+x^2+\cdots$. What is the series for the $2$-cent coins alone? For the $5$-cent coins alone?
hint:
The answer is the coefficient of $x^{20}$ in the product of the three series. To extract it, first find the coefficient of $x^m$ in the product of the first two, then sum over the possible numbers of $5$-cent coins.
solution:
A way to pay $m$ cents corresponds to a triple $(a,b,c)$ of non-negative integers with $a+2b+5c=m$. Multiplying out
$$\frac1{1-x}\cdot\frac1{1-x^2}\cdot\frac1{1-x^5}=\left(\sum_{a\ge0}x^a\right)\left(\sum_{b\ge0}x^{2b}\right)\left(\sum_{c\ge0}x^{5c}\right),$$
the coefficient of $x^m$ counts exactly these triples. So the answer is the coefficient of $x^{20}$.

Group the last factor: if the number of $5$-cent coins is $c$, the remaining amount $r=20-5c$ must be paid with $1$- and $2$-cent coins. The coefficient of $x^r$ in $\frac1{(1-x)(1-x^2)}$ is the number of $b\ge0$ with $2b\le r$ (then $a=r-2b$ is determined), namely $\lfloor r/2\rfloor+1$. For $c=0,1,2,3,4$ we have $r=20,15,10,5,0$, giving $11,8,6,3,1$. Hence the number of ways is
$$11+8+6+3+1=\boxed{29}.$$

### o106
source: original
type: answer
difficulty: 1
techniques: expectation
statement:
The numbers $1,2,\dots,10$ are written in a row in a uniformly random order. Call a position $i$ with $1\le i\le 9$ an ascent if the number in position $i$ is smaller than the number in position $i+1$. What is the expected number of ascents?
asked:
Find the average number of ascents over all $10!$ equally likely arrangements.
technique:
Count the ascents one position at a time, and add up the expectations. You do not need to know how the ascents depend on each other.
hint:
For each $i$ from $1$ to $9$ let $X_i=1$ if position $i$ is an ascent and $X_i=0$ otherwise. The number of ascents is $X_1+\dots+X_9$.
hint:
What is the probability that position $i$ holds a smaller number than position $i+1$? Swapping the two entries turns an arrangement with an ascent at $i$ into one without.
solution:
Let $X_i=1$ if there is an ascent at position $i$ and $X_i=0$ otherwise, for $i=1,\dots,9$. The number of ascents is $X=X_1+\dots+X_9$, and by linearity of expectation $E[X]=\sum_i E[X_i]=\sum_i P(\text{ascent at }i)$.

Fix $i$. Swapping the entries in positions $i$ and $i+1$ is a bijection on the set of arrangements, and it exchanges the arrangements where position $i$ holds the smaller number with those where it holds the larger number (the two entries are distinct). So exactly half of the arrangements have an ascent at $i$, i.e. $P(\text{ascent at }i)=\tfrac12$.

Therefore $E[X]=9\cdot\tfrac12=\boxed{\dfrac92}$.

### o108
source: original
type: answer
difficulty: 2
techniques: coordinates
statement:
$ABCD$ is a square with side length $4$ (the vertices are in order around the square). $M$ is the midpoint of side $BC$ and $N$ is the midpoint of side $CD$. Find $\cos\angle MAN$.
asked:
Find the exact value of the cosine of the angle at $A$ in triangle $MAN$.
technique:
Place the square on a coordinate grid so that every point involved gets simple coordinates.
hint:
Put $A$ at the origin, $B=(4,0)$ and $D=(0,4)$. Find the coordinates of $C$, $M$ and $N$.
hint:
The cosine of the angle between two vectors is their dot product divided by the product of their lengths.
solution:
Place $A=(0,0)$, $B=(4,0)$, $C=(4,4)$, $D=(0,4)$. Then $M$, the midpoint of $BC$, is $(4,2)$ and $N$, the midpoint of $CD$, is $(2,4)$.

The vectors are $\vec{AM}=(4,2)$ and $\vec{AN}=(2,4)$, with $\vec{AM}\cdot\vec{AN}=8+8=16$ and $|\vec{AM}|=|\vec{AN}|=\sqrt{20}$. Therefore
$$\cos\angle MAN=\frac{16}{\sqrt{20}\sqrt{20}}=\frac{16}{20}=\boxed{\dfrac45}.$$

### o109
source: original
type: answer
difficulty: 5
techniques: expectation
statement:
A permutation $\sigma$ of $\{1,2,\dots,10\}$ is chosen uniformly at random from all $10!$ permutations. Write $\sigma$ as a product of disjoint cycles in the usual way, counting each fixed point as a cycle of length $1$. (For example, the permutation of $\{1,\dots,5\}$ with $1\to2\to3\to1$, $4\to5\to4$ has $2$ cycles.) What is the expected number of cycles of $\sigma$? Give the exact value as a fraction.
asked:
Find the average number of cycles of a random permutation of $\{1,\dots,10\}$.
technique:
The quantity being averaged can be written as a sum of many simple 0-1 quantities, and averages of sums are easy even when the pieces are dependent.
hint:
Fix $k$ and a $k$-element subset $S$ of $\{1,\dots,10\}$. How many different cyclic arrangements of $S$ are there, that is, how many permutations of $S$ consist of a single $k$-cycle?
hint:
For a given cyclic arrangement $c$ of $S$, how many permutations of the whole set contain $c$ as one of their cycles? Divide by $10!$.
hint:
Use linearity of expectation over all candidate cycles of length $k$, and simplify. Then sum over $k$.
solution:
Let $n=10$. For a subset $S\subseteq\{1,\dots,n\}$ with $|S|=k$ and a permutation $c$ of $S$ that is a single $k$-cycle, let $I_{c}(\sigma)=1$ if $c$ is one of the cycles of $\sigma$ (that is, $\sigma$ agrees with $c$ on $S$) and $0$ otherwise. Every cycle of every permutation $\sigma$ is counted by exactly one such pair, so the number of cycles of $\sigma$ equals $\sum I_c(\sigma)$ over all such $c$, and
$$E[\text{cycles}]=\sum_{c}P(\sigma\text{ agrees with }c\text{ on }S).$$

Count the candidates. There are $\binom nk$ subsets $S$ of size $k$. On a given $S$ the number of $k$-cycles is $(k-1)!$: start the cycle at the smallest element of $S$ and list the other $k-1$ elements in the order they are visited, in any of $(k-1)!$ orders.

Now fix such a $c$. The permutations $\sigma$ that agree with $c$ on $S$ are determined by their action on the remaining $n-k$ elements, which can be any permutation of those elements (it maps the complement of $S$ to itself, since $\sigma(S)=S$). There are $(n-k)!$ of them, so $P(\sigma\text{ agrees with }c)=\frac{(n-k)!}{n!}$.

Thus the expected number of cycles of length $k$ is
$$\binom nk\,(k-1)!\,\frac{(n-k)!}{n!}=\frac{n!}{k!\,(n-k)!}\cdot(k-1)!\cdot\frac{(n-k)!}{n!}=\frac1k.$$
Summing over $k=1,\dots,10$ gives
$$E[\text{cycles}]=1+\frac12+\frac13+\dots+\frac1{10}=\boxed{\dfrac{7381}{2520}}.$$
(Indeed, $2520\cdot H_{10}=2520+1260+840+630+504+420+360+315+280+252=7381$.)

### o110
source: original
type: answer
difficulty: 5
techniques: expectation
statement:
A fair coin is flipped repeatedly until the three most recent flips, in order, read heads, tails, heads (H, T, H) for the first time. For example, the flips H, H, T, T, H, T, H stop after $7$ flips. What is the expected number of flips?
asked:
Find the expected total number of flips until the pattern HTH first appears.
technique:
Describe the situation by how much of the target pattern you currently have, and relate the average remaining wait from each situation to the others.
hint:
Let $a$ be the expected number of further flips needed when the last flips give no progress toward HTH (for example at the start), $b$ when the last flip was H, and $c$ when the last two flips were H, T. Think about what the next flip does in each case.
hint:
In state $c$ (last two flips H, T): a head ends the game, a tail leads back to a state with no progress. In state $b$: a head leaves you in state $b$ again, a tail moves you to state $c$. Write three linear equations.
hint:
Solve the system. Also explain why the expectations $a,b,c$ are finite, so that the equations make sense.
solution:
Say we are in state $B$ if the last flip is H, in state $C$ if the last two flips are H, T, and in state $A$ otherwise (this includes the start, and the situation where the last flip is T and the one before it is not H). Let $a,b,c$ be the expected numbers of further flips until HTH appears, starting from each state. The transitions on the next flip are:

- From $A$: H leads to $B$; T leads to $A$ (a T after no progress is still no progress).
- From $B$ (last flip H): H leads to $B$ (the last flip is still H); T leads to $C$.
- From $C$ (last flips H, T): H completes HTH and the game ends; T gives last flips T, T, which is state $A$.

**Finiteness.** From any state, the next three flips are H, T, H with probability $\tfrac18$, which ends the game by then (it may end sooner). So the game is not over after $3m$ further flips with probability at most $(7/8)^m$, and hence the expected number of further flips is at most $3\sum_{m\ge0}(7/8)^m<\infty$.

**Equations.** Conditioning on the next flip (each outcome has probability $\tfrac12$), and counting that flip:
$$a=1+\tfrac12 b+\tfrac12 a,\qquad b=1+\tfrac12 b+\tfrac12 c,\qquad c=1+\tfrac12\cdot0+\tfrac12 a.$$
From the second equation $b=2+c$. From the third $c=1+\tfrac a2$, so $b=3+\tfrac a2$. The first equation gives $\tfrac a2=1+\tfrac b2$, i.e. $a=2+b=5+\tfrac a2$, so $a=10$.

The game starts in state $A$, so the expected number of flips is $\boxed{10}$.

### o111
source: original
type: proof
difficulty: 5
techniques: angle-chasing
statement:
Let $ABC$ be a triangle with $\angle BAC=60^\circ$. The bisector of angle $ABC$ meets side $AC$ at $D$, and the bisector of angle $ACB$ meets side $AB$ at $E$. The segments $BD$ and $CE$ meet at $I$. Prove that
(a) $BE+CD=BC$, and
(b) $ID=IE$.
asked:
Prove both statements: the segments $BE$ and $CD$ together have the length of $BC$, and $I$ is equally far from $D$ and from $E$.
technique:
Find the angles at $I$ first; they turn out to be special, and they will let you transport lengths from one side of the figure to another.
hint:
Compute $\angle BIC$ from the angles of triangle $BIC$, using that $BI$ and $CI$ bisect the angles at $B$ and $C$. What are $\angle BIE$ and $\angle CID$?
hint:
Mark the point $F$ on segment $BC$ with $BF=BE$. Compare triangles $BEI$ and $BFI$.
hint:
Now compare triangles $CFI$ and $CDI$. What do you learn about $CF$ and $CD$?
solution:
Write $\beta=\angle ABC$ and $\gamma=\angle ACB$, so $\beta+\gamma=120^\circ$. Since $BI$ and $CI$ are the bisectors of these angles, in triangle $BIC$
$$\angle BIC=180^\circ-\tfrac\beta2-\tfrac\gamma2=180^\circ-60^\circ=120^\circ.$$
The point $I$ lies on the segments $BD$ and $CE$, between $B$ and $D$ and between $C$ and $E$ (the cevians $BD$ and $CE$ cross inside the triangle). Therefore $\angle BIE=180^\circ-\angle BIC=60^\circ$ and $\angle CID=180^\circ-\angle BIC=60^\circ$.

**A point $F$ on $BC$.** In triangle $BEC$ we have $\angle BCE=\gamma/2$ and $\angle BEC=180^\circ-\beta-\gamma/2=60^\circ+\gamma/2$ (using $\beta+\gamma=120^\circ$), which is larger than $\gamma/2$. The larger side lies opposite the larger angle, so $BC>BE$. Hence there is a point $F$ on the segment $BC$, strictly between $B$ and $C$, with $BF=BE$.

**Triangles $BEI$ and $BFI$.** They have $BE=BF$, a common side $BI$, and $\angle EBI=\angle FBI=\beta/2$ (the ray $BI$ is the bisector of angle $ABC$, and $E$, $F$ lie on the two sides of that angle). So they are congruent (SAS). Consequently $IF=IE$ and $\angle BIF=\angle BIE=60^\circ$.

**Triangles $CFI$ and $CDI$.** Since $F$ lies on segment $BC$, the ray $IF$ lies inside angle $BIC$, so $\angle FIC=\angle BIC-\angle BIF=120^\circ-60^\circ=60^\circ=\angle DIC$. Also $\angle FCI=\angle DCI=\gamma/2$ (ray $CI$ bisects angle $ACB$, and $F$, $D$ lie on its two sides), and $CI$ is common. So the triangles are congruent (ASA), giving $CF=CD$ and $IF=ID$.

(a) $BC=BF+FC=BE+CD$. 

(b) $ID=IF=IE$. $\blacksquare$

### o112
source: original
type: answer
difficulty: 4
techniques: similar-triangles
statement:
Triangle $ABC$ has side lengths $AB=13$, $BC=14$ and $CA=15$. Let $D$, $E$, $F$ be the feet of the perpendiculars from $A$ to $BC$, from $B$ to $CA$, and from $C$ to $AB$, respectively. Find the area of triangle $DEF$.
asked:
Find the exact area of the triangle formed by the three feet of the altitudes.
technique:
Triangles cut off at the corners of the figure may be scaled copies of the whole triangle. Scaled copies relate lengths and areas in a predictable way.
hint:
First check that the triangle is acute, so the three feet lie inside the sides. Compute $\cos A$, $\cos B$, $\cos C$.
hint:
In the right triangles $ABE$ and $ACF$, express $AE$ and $AF$ using $\cos A$. Then compare triangle $AEF$ with triangle $ABC$.
hint:
The triangle $ABC$ is cut into $AEF$, $BDF$, $CDE$ and $DEF$. Compute the first three areas from the similarity ratios and subtract from the area of $ABC$.
solution:
**Setup.** Let $a=BC=14$, $b=CA=15$, $c=AB=13$. By the law of cosines
$$\cos A=\frac{b^2+c^2-a^2}{2bc}=\frac{198}{390}=\frac{33}{65},\quad \cos B=\frac{a^2+c^2-b^2}{2ac}=\frac{140}{364}=\frac5{13},\quad \cos C=\frac{a^2+b^2-c^2}{2ab}=\frac{252}{420}=\frac35.$$
All three are positive, so the triangle is acute and each foot lies strictly inside the corresponding side (the foot of the altitude from $B$ lies strictly inside segment $AC$ exactly when the angles at $A$ and $C$ are both acute, and similarly for the other two feet). The area of $ABC$ is $84$ by Heron's formula ($s=21$, $\sqrt{21\cdot7\cdot8\cdot6}=84$).

**Corner triangles.** In the right triangle $ABE$ (right angle at $E$), $AE=AB\cos A$. In the right triangle $ACF$ (right angle at $F$), $AF=AC\cos A$. Hence
$$\frac{AE}{AB}=\frac{AF}{AC}=\cos A,$$
and triangles $AEF$ and $ABC$ share the angle at $A$ (since $E$ lies on $AC$ and $F$ on $AB$, $\angle EAF=\angle CAB$). Matching $AE\leftrightarrow AB$ and $AF\leftrightarrow AC$, the triangles are similar (SAS) with ratio $\cos A$. Therefore $[AEF]=\cos^2A\,[ABC]$. In the same way $[BDF]=\cos^2B\,[ABC]$ and $[CDE]=\cos^2C\,[ABC]$.

**Subtracting.** Since $D,E,F$ lie on the sides, triangle $ABC$ is the union of the non-overlapping triangles $AEF$, $BDF$, $CDE$ and $DEF$. Thus
$$[DEF]=84\left(1-\cos^2A-\cos^2B-\cos^2C\right)=84\left(1-\frac{1089}{4225}-\frac{625}{4225}-\frac{1521}{4225}\right)=84\cdot\frac{990}{4225}=84\cdot\frac{198}{845}=\boxed{\dfrac{16632}{845}}.$$

### o113
source: original
type: proof
difficulty: 5
techniques: complex-numbers
statement:
Let $A_1A_2\dots A_n$ be a regular $n$-gon inscribed in a circle of radius $1$ with centre $O$, and let $P$ be any point of the plane with $OP=r$. Prove that
(a) if $n\ge3$, then $\displaystyle\sum_{k=1}^{n}PA_k^4=n\,(r^4+4r^2+1)$;
(b) if $n\ge4$, then $\displaystyle\sum_{k=1}^{n}PA_k^6=n\,(r^6+9r^4+9r^2+1)$.
asked:
Prove both formulas. In particular, the sums depend on $P$ only through its distance from the centre.
technique:
Put the figure in the complex plane, where a regular polygon has a very clean description and distances are easy to expand.
hint:
Take $O=0$, so the vertices are $w_k=\varepsilon\omega^k$ for $k=1,\dots,n$, where $\omega=e^{2\pi i/n}$ and $|\varepsilon|=1$, and $P=p$ with $|p|=r$. Show that $PA_k^2=r^2+1-s_k$ where $s_k=p\bar w_k+\bar p w_k$.
hint:
Which sums $\sum_k w_k^m$ vanish, and for which $m$? Compute $\sum_k s_k$, $\sum_k s_k^2$ (and later $\sum_k s_k^3$) by expanding, using $|w_k|=1$.
hint:
Then $\sum PA_k^4=\sum(r^2+1-s_k)^2$ and $\sum PA_k^6=\sum(r^2+1-s_k)^3$; expand and substitute.
solution:
Place the circle as the unit circle in the complex plane with $O=0$. Then $A_k$ corresponds to $w_k=\varepsilon\omega^k$ ($k=1,\dots,n$) with $\omega=e^{2\pi i/n}$ and $|\varepsilon|=1$, and $P$ corresponds to $p$ with $|p|=r$.

**Root-of-unity sums.** If $n\nmid m$ then $\omega^m\ne1$, and $\sum_{k=1}^n\omega^{km}=\omega^m\frac{\omega^{nm}-1}{\omega^m-1}=0$. Hence $\sum_k w_k^m=\varepsilon^m\sum_k\omega^{km}=0$, and taking conjugates $\sum_k\bar w_k^{\,m}=0$ as well. For $n\ge3$ this applies to $m=1,2$; for $n\ge4$ also to $m=3$.

**Squared distances.** Since $|w_k|=1$,
$$PA_k^2=|p-w_k|^2=(p-w_k)(\bar p-\bar w_k)=r^2+1-s_k,\qquad s_k:=p\bar w_k+\bar p w_k.$$
Put $u=r^2+1$. Now compute the power sums of $s_k$.

- $\sum_k s_k=p\sum\bar w_k+\bar p\sum w_k=0$.
- $s_k^2=p^2\bar w_k^2+2p\bar p\,w_k\bar w_k+\bar p^2w_k^2=p^2\bar w_k^2+2r^2+\bar p^2w_k^2$. Summing over $k$ and using $\sum w_k^2=\sum\bar w_k^2=0$ (valid for $n\ge3$) gives $\sum_k s_k^2=2nr^2$.
- $s_k^3=p^3\bar w_k^3+3p^2\bar p\,\bar w_k^2w_k+3p\bar p^2\,\bar w_kw_k^2+\bar p^3w_k^3=p^3\bar w_k^3+\bar p^3w_k^3+3r^2s_k$, using $|w_k|=1$. For $n\ge4$, $\sum w_k^3=\sum\bar w_k^3=0$ and $\sum s_k=0$, so $\sum_k s_k^3=0$.

**(a)** For $n\ge3$,
$$\sum PA_k^4=\sum(u-s_k)^2=nu^2-2u\sum s_k+\sum s_k^2=n(r^2+1)^2+2nr^2=n(r^4+4r^2+1).$$

**(b)** For $n\ge4$,
$$\sum PA_k^6=\sum(u-s_k)^3=nu^3-3u^2\sum s_k+3u\sum s_k^2-\sum s_k^3=nu^3+6nur^2=nu\,(u^2+6r^2).$$
Since $u^2+6r^2=r^4+8r^2+1$, this equals $n(r^2+1)(r^4+8r^2+1)=n(r^6+9r^4+9r^2+1)$. $\blacksquare$

(Remark: the hypotheses are really used. For $n=3$ in (b) one has $\sum w_k^3=3\varepsilon^3\ne0$, and the sum then does depend on the direction of $P$.)

### o114
source: original
type: answer
difficulty: 5
techniques: generating-functions
statement:
How many strings $d_1d_2\dots d_8$ of eight decimal digits (each $d_i\in\{0,1,\dots,9\}$, leading zeros allowed) have digit sum $d_1+d_2+\dots+d_8=36$?
asked:
Count the $8$-tuples of digits from $0$ to $9$ whose sum is exactly $36$.
technique:
Package the choices for each digit into a polynomial whose exponents record the digit's value; the count you want is one coefficient of a product.
hint:
Each digit contributes the factor $1+x+\dots+x^9$. The answer is the coefficient of $x^{36}$ in its eighth power. Write the factor as a quotient using the geometric series formula.
hint:
You then need the coefficient of $x^{36}$ in $(1-x^{10})^8(1-x)^{-8}$. Expand $(1-x^{10})^8$ with the binomial theorem and recall the coefficients of $(1-x)^{-8}$.
hint:
The coefficient of $x^m$ in $(1-x)^{-8}$ is $\binom{m+7}{7}$. Only terms with $10j\le36$ contribute.
solution:
The number of such strings is the coefficient of $x^{36}$ in
$$\left(1+x+\dots+x^9\right)^8=\left(\frac{1-x^{10}}{1-x}\right)^8=(1-x^{10})^8\,(1-x)^{-8},$$
because choosing the term $x^{d_i}$ from the $i$-th factor gives the exponent $d_1+\dots+d_8$.

By the binomial theorem $(1-x^{10})^8=\sum_{j=0}^8(-1)^j\binom8jx^{10j}$, and $(1-x)^{-8}=\sum_{m\ge0}\binom{m+7}{7}x^m$ (this is the number of ways to write $m$ as an ordered sum of $8$ non-negative integers). The coefficient of $x^{36}$ in the product is therefore
$$\sum_{j}(-1)^j\binom8j\binom{36-10j+7}{7},$$
where only $j$ with $10j\le36$, i.e. $j=0,1,2,3$, contribute:
$$\binom{43}{7}-8\binom{33}{7}+28\binom{23}{7}-56\binom{13}{7}.$$
With $\binom{43}{7}=32\,224\,114$, $\binom{33}{7}=4\,272\,048$, $\binom{23}{7}=245\,157$, $\binom{13}{7}=1716$, this is
$$32\,224\,114-34\,176\,384+6\,864\,396-96\,096=\boxed{4\,816\,030}.$$

### o115
source: original
type: answer
difficulty: 6
techniques: generating-functions, complex-numbers
statement:
How many subsets of $\{1,2,\dots,2025\}$ have a sum of elements divisible by $5$? The empty set (sum $0$) counts. Give the answer as a closed-form expression.
asked:
Count the subsets of $\{1,2,\dots,2025\}$ (including the empty set) whose elements add up to a multiple of $5$.
technique:
Encode every subset by a product of simple factors, one per element, and find a way to keep only the exponents that are multiples of $5$.
hint:
The polynomial $f(x)=\prod_{i=1}^{2025}(1+x^i)$ has $x^s$ with coefficient equal to the number of subsets with sum $s$. You want the sum of the coefficients of $x^s$ over $5\mid s$. Which averages of $f$ at the fifth roots of unity isolate those terms?
hint:
If $\omega=e^{2\pi i/5}$, then $\frac15\sum_{j=0}^4f(\omega^j)$ is the required count. For $j\ne0$, split the product over $i$ into $405$ blocks of five consecutive integers.
hint:
Within one block, $ji$ runs over all residues mod $5$. Evaluate $\prod_{r=0}^4(1+\omega^r)$ using the factorisation of $z^5-1$ at $z=-1$.
solution:
Let $f(x)=\prod_{i=1}^{2025}(1+x^i)$. Expanding, $f(x)=\sum_s c_sx^s$ where $c_s$ is the number of subsets with element sum $s$. We want $\sum_{5\mid s}c_s$.

**Roots of unity filter.** Let $\omega=e^{2\pi i/5}$. For an integer $s$, $\sum_{j=0}^4\omega^{js}$ equals $5$ if $5\mid s$ and $0$ otherwise (a geometric sum with ratio $\omega^s\ne1$ in the second case). Therefore
$$\sum_{5\mid s}c_s=\frac15\sum_{j=0}^{4}f(\omega^j).$$

**The terms.** For $j=0$: $f(1)=2^{2025}$.

For $j\in\{1,2,3,4\}$: since $\gcd(j,5)=1$, as $i$ runs over any five consecutive integers, $\omega^{ji}$ runs over all five fifth roots of unity exactly once. The integers $1,\dots,2025$ split into $405$ blocks of five consecutive integers, so
$$f(\omega^j)=\left(\prod_{r=0}^{4}(1+\omega^r)\right)^{405}.$$
Since $z^5-1=\prod_{r=0}^4(z-\omega^r)$, putting $z=-1$ gives $-2=\prod_{r}(-1-\omega^r)=(-1)^5\prod_r(1+\omega^r)$, hence $\prod_{r}(1+\omega^r)=2$. So $f(\omega^j)=2^{405}$.

**Result.**
$$\sum_{5\mid s}c_s=\frac{2^{2025}+4\cdot2^{405}}{5}=\boxed{\dfrac{2^{2025}+2^{407}}{5}}.$$

### o116
source: original
type: answer
difficulty: 4
techniques: diophantine
statement:
Find all pairs of integers $(x,y)$ such that
$$x^3-y^3=3xy+37.$$
asked:
Determine every pair of integers $(x,y)$ satisfying the equation.
technique:
Rewrite the equation in terms of quantities that make it nearly one-variable, then show that only a few cases are possible.
hint:
Write $d=x-y$ and use $x^3-y^3=d^3+3xyd$. Rewrite the equation to isolate $xy$ in terms of $d$.
hint:
Given $d$ and the product $P=xy$, the number $y$ satisfies $y^2+dy-P=0$. This forces the discriminant $d^2+4P$ to be non-negative, which bounds $d$.
hint:
After clearing denominators, treat the cases $d>1$ and $d<1$ separately (the sign of $d-1$ matters when multiplying an inequality). Then check the few remaining values of $d$.
solution:
Let $d=x-y$. Since $x^3-y^3=(x-y)^3+3xy(x-y)=d^3+3dxy$, the equation reads
$$d^3+3dxy=3xy+37,\qquad\text{i.e.}\qquad 3xy\,(d-1)=37-d^3.$$

If $d=1$ the left side is $0$ while the right side is $36$, impossible. So $d\ne1$ and
$$xy=P:=\frac{37-d^3}{3(d-1)}.$$
Since $x=y+d$, we have $y^2+dy-P=0$, which has a real solution $y$ only if its discriminant is non-negative: $d^2+4P\ge0$, that is
$$d^2+\frac{4(37-d^3)}{3(d-1)}\ge0.$$
Multiply by $3(d-1)$ and note $3d^2(d-1)+4(37-d^3)=-d^3-3d^2+148$.

* If $d>1$ we multiply by a positive number, getting $148-d^3-3d^2\ge0$, i.e. $d^3+3d^2\le148$. Since $5^3+3\cdot5^2=200>148$ and the left side increases for $d>1$, this gives $d\in\{2,3,4\}$.
* If $d<1$, i.e. $d\le0$, we multiply by a negative number and the inequality reverses: $148-d^3-3d^2\le0$, i.e. $d^2(d+3)\ge148$. But for $d\le-3$ we have $d^2(d+3)\le0$, and for $-3\le d\le0$ we have $d^2\le9$ and $d+3\le3$, so $d^2(d+3)\le27<148$. So there is no solution.

Now check $d=2,3,4$:
- $d=2$: $P=\frac{29}{3}$, not an integer.
- $d=3$: $P=\frac{10}{6}$, not an integer.
- $d=4$: $P=\frac{-27}{9}=-3$. Then $y^2+4y+3=0$, so $y=-1$ or $y=-3$, with $x=y+4=3$ or $1$.

Verification: $(3,-1)$: $27+1=28=3\cdot3\cdot(-1)+37=28$. $(1,-3)$: $1+27=28=3\cdot1\cdot(-3)+37=28$.

The solutions are $\boxed{(x,y)=(3,-1)\ \text{and}\ (1,-3)}$.

