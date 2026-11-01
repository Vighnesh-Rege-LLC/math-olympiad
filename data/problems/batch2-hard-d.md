### m100
source: mathnet
mathnet_id: 0cgm
country: Romania
competition: 74th Romanian Mathematical Olympiad
type: proof
difficulty: 7
techniques: complex-numbers, trigonometry
statement:
Let $ABCDE$ be a convex pentagon whose vertices lie on a circle with centre $O$, with $AB=BC=CD$. Suppose that the centroid of its five vertices (the point $G$ with $\vec{OG}=\frac15(\vec{OA}+\vec{OB}+\vec{OC}+\vec{OD}+\vec{OE})$) coincides with $O$. Prove that $ABCDE$ is a regular pentagon.
asked:
A convex cyclic pentagon has three consecutive equal sides, and the average of its vertices is the centre of the circle. Show that the pentagon is regular.
technique:
Put the circle as the unit circle in the complex plane, so that equal chords become multiplication by a fixed unit complex number.
hint:
Equal chords cut off equal arcs here, so $b=aw$, $c=aw^2$, $d=aw^3$ for some $w=e^{i\theta}$ with $0<\theta<\frac{2\pi}3$. The centroid condition then expresses $e$ in terms of $a$ and $w$.
hint:
Factor $1+w+w^2+w^3=(1+w)(1+w^2)$ and write each factor as a real number times a unit complex number. The condition $|e|=1$ becomes a trigonometric equation in $\theta$.
hint:
Split according to the sign of $\cos\theta$. In one case $E$ lands in the wrong place on the circle; in the other, the equation has exactly one solution.
solution:
Place the circle as the unit circle with $O=0$, and (reflecting if necessary) assume $A,B,C,D,E$ appear counterclockwise in this order, as they do for a convex inscribed pentagon. Let the counterclockwise arcs $AB,BC,CD,DE,EA$ (each containing no other vertex) have measures $\alpha_1,\dots,\alpha_5>0$ with sum $2\pi$.

**Equal arcs.** A chord subtending an arc of measure $\varphi\in(0,2\pi)$ has length $2\sin(\varphi/2)$, and $2\sin(\varphi/2)=2\sin(\psi/2)$ with $\varphi,\psi\in(0,2\pi)$ forces $\psi=\varphi$ or $\psi=2\pi-\varphi$. If $\alpha_2=2\pi-\alpha_1$, then $\alpha_1+\alpha_2=2\pi$ and the other arcs would be $0$, impossible. So $AB=BC$ gives $\alpha_1=\alpha_2$, and likewise $\alpha_2=\alpha_3$. Call this common value $\theta$; since $3\theta<2\pi$, we have $0<\theta<\frac{2\pi}3$.

With $w=e^{i\theta}$ and $a$ the coordinate of $A$, we get $b=aw$, $c=aw^2$, $d=aw^3$, and $e$ lies on the counterclockwise arc from $d$ to $a$, i.e. $e=ae^{i\varphi}$ with $3\theta<\varphi<2\pi$.

**The centroid condition.** $a+b+c+d+e=0$ gives
$$e=-a(1+w+w^2+w^3)=-a(1+w)(1+w^2).$$
Now $1+w=e^{i\theta/2}(e^{-i\theta/2}+e^{i\theta/2})=2\cos\frac\theta2\,e^{i\theta/2}$ and similarly $1+w^2=2\cos\theta\,e^{i\theta}$. Hence
$$e=-a\,e^{3i\theta/2}\cdot4\cos\frac\theta2\cos\theta .$$
Since $0<\frac\theta2<\frac\pi3$, $\cos\frac\theta2>0$. Taking absolute values, $|e|=|a|=1$ gives $4\cos\frac\theta2\,|\cos\theta|=1$; in particular $\cos\theta\neq0$.

**Case $\cos\theta<0$.** Then $4\cos\frac\theta2\cos\theta=-1$ and $e=ae^{3i\theta/2}$. But $\theta<\frac{3\theta}2<2\theta$, so $E$ lies strictly inside the arc from $B$ to $C$, contradicting $3\theta<\varphi<2\pi$ (note $\frac{3\theta}{2}<2\pi$, so this is the actual position of $E$). This case is impossible.

**Case $\cos\theta>0$,** i.e. $0<\theta<\frac\pi2$. The function $g(\theta)=4\cos\frac\theta2\cos\theta$ is a product of two positive strictly decreasing functions on $(0,\frac\pi2)$, so it is strictly decreasing and the equation $g(\theta)=1$ has at most one solution there. And $\theta=\frac{2\pi}5$ is a solution: multiplying $\cos36^\circ\cos72^\circ$ by $\sin36^\circ$,
$$\sin36^\circ\cos36^\circ\cos72^\circ=\tfrac12\sin72^\circ\cos72^\circ=\tfrac14\sin144^\circ=\tfrac14\sin36^\circ,$$
so $\cos36^\circ\cos72^\circ=\frac14$ and $g(\frac{2\pi}5)=1$. Hence $\theta=\frac{2\pi}5$.

Then $e=-a\,e^{3\pi i/5}=a\,e^{i(3\pi/5+\pi)}=a\,e^{8\pi i/5}=aw^4$ (this is consistent with $3\theta<\frac{8\pi}5<2\pi$). So the vertices are $a,aw,aw^2,aw^3,aw^4$ with $w=e^{2\pi i/5}$: all five arcs equal $\frac{2\pi}5$, and $ABCDE$ is a regular pentagon. $\blacksquare$

### m101
source: mathnet
mathnet_id: 099r
country: Mongolia
competition: 45th Mongolian Mathematical Olympiad
type: answer
difficulty: 7
techniques: generating-functions, complex-numbers
statement:
How many subsets $A$ of $\{1,2,\dots,2009\}$ (the empty set included, with sum $0$) have the property that the sum of the elements of $A$ is divisible by $2009$? Note that $2009=7^2\cdot41$.
asked:
Count the subsets of $\{1,\dots,2009\}$ whose element sum is a multiple of $2009$.
technique:
Encode every subset by a monomial in a product of binomials, then extract the exponents divisible by $2009$ by averaging over roots of unity.
hint:
In $f(x)=\prod_{j=1}^{2009}(1+x^j)$ the coefficient of $x^s$ counts subsets with sum $s$. With $\varepsilon=e^{2\pi i/2009}$, the answer is $\frac1{2009}\sum_{k=0}^{2008}f(\varepsilon^k)$.
hint:
If $\eta=\varepsilon^k$ is a primitive $m$-th root of unity, then $\eta^1,\dots,\eta^{2009}$ run through all $m$-th roots of unity, each $2009/m$ times. Evaluate $\prod_{\zeta^m=1}(1+\zeta)$ using $x^m-1=\prod(x-\zeta)$.
hint:
Count how many $k$ give a primitive $m$-th root for each divisor $m$ of $2009$.
solution:
Let $n=2009$, $\varepsilon=e^{2\pi i/n}$ and $f(x)=\prod_{j=1}^{n}(1+x^j)=\sum_s c_sx^s$. Expanding the product, each subset $A$ contributes the monomial $x^{\sum A}$, so $c_s$ is the number of subsets with sum $s$, and we want $N=\sum_{n\mid s}c_s$.

**Filter.** For an integer $s$, $\sum_{k=0}^{n-1}\varepsilon^{ks}$ equals $n$ if $n\mid s$ and $\frac{\varepsilon^{ns}-1}{\varepsilon^s-1}=0$ otherwise. Hence
$$\sum_{k=0}^{n-1}f(\varepsilon^k)=\sum_s c_s\sum_{k=0}^{n-1}\varepsilon^{ks}=nN .$$

**Evaluating $f(\varepsilon^k)$.** Let $g=\gcd(k,n)$ and $m=n/g$. Then $\eta=\varepsilon^k$ is a primitive $m$-th root of unity, so $\eta^j$ depends only on $j\bmod m$, and as $j$ runs over $1,\dots,n$ the residue $j\bmod m$ takes each value exactly $g$ times. The powers $\eta^0,\dots,\eta^{m-1}$ are exactly the $m$ distinct $m$-th roots of unity, so
$$f(\eta)=\Big(\prod_{\zeta^m=1}(1+\zeta)\Big)^g .$$
From $x^m-1=\prod_{\zeta^m=1}(x-\zeta)$ at $x=-1$: $(-1)^m-1=(-1)^m\prod(1+\zeta)$. Since $n$ is odd, so is $m$, and this reads $-2=-\prod(1+\zeta)$, i.e. $\prod(1+\zeta)=2$. Hence $f(\varepsilon^k)=2^{g}=2^{n/m}$.

**Counting.** For a divisor $m$ of $n$, the $k\in\{0,\dots,n-1\}$ with $n/\gcd(k,n)=m$ are $k=(n/m)t$ with $0\le t<m$ and $\gcd(t,m)=1$; there are $\varphi(m)$ of them. Therefore
$$N=\frac1n\sum_{m\mid n}\varphi(m)\,2^{n/m}.$$
For $n=2009$ the divisors are $1,7,49,41,287,2009$ with $\varphi$ equal to $1,6,42,40,240,1680$, so
$$N=\boxed{\dfrac{2^{2009}+6\cdot2^{287}+40\cdot2^{49}+42\cdot2^{41}+240\cdot2^{7}+3360}{2009}}.$$

### m102
source: mathnet
mathnet_id: 0k5h
country: United States
competition: USA TSTST
type: answer
difficulty: 8
techniques: generating-functions, constructive
statement:
Let $S=\{1,\dots,100\}$, and for every positive integer $n$ define
$$T_n=\{(a_1,\dots,a_n)\in S^n\mid a_1+\dots+a_n\equiv0\pmod{100}\}.$$
Determine which $n$ have the following property: if we colour any $75$ elements of $S$ red, then at least half of the $n$-tuples in $T_n$ have an even number of coordinates with red elements.
asked:
For which $n$ is it true that, whichever $75$ of the numbers $1,\dots,100$ are red, the $n$-tuples with sum divisible by $100$ having an even number of red entries are at least as many as those having an odd number?
technique:
Give each element a sign according to its colour and form a polynomial whose $n$-th power records signed tuples by their sum; the tuples with sum divisible by $100$ are then picked out with $100$-th roots of unity.
hint:
Let $R(x)$ and $B(x)$ be the sums of $x^s$ over red and over non-red $s$. In $(B(x)-R(x))^n$ each tuple appears with sign $(-1)^{\#\text{red}}$. So (even) $-$ (odd) in $T_n$ equals $\frac1{100}\sum_{\omega^{100}=1}(B(\omega)-R(\omega))^n$.
hint:
For $\omega\neq1$, $B(\omega)+R(\omega)=\sum_{s=1}^{100}\omega^s=0$. Rewrite the sum using only $B$, and recognise $\frac1{100}\sum_\omega B(\omega)^n$ as a count.
hint:
For odd $n$ you need a colouring where no $n$-tuple of non-red numbers has sum divisible by $100$. Think modulo $4$.
solution:
**Answer:** exactly the $\boxed{\text{even } n}$.

Fix a colouring with $75$ red and $25$ blue (non-red) elements. Let $R(x)=\sum_{s\text{ red}}x^s$, $B(x)=\sum_{s\text{ blue}}x^s$ and $P(x)=B(x)-R(x)$. Expanding,
$$P(x)^n=\sum_{(a_1,\dots,a_n)\in S^n}(-1)^{r(a)}x^{a_1+\dots+a_n},$$
where $r(a)$ is the number of red coordinates. Let $X$ and $Y$ be the numbers of tuples in $T_n$ with an even, respectively odd, number of red coordinates. With $\omega$ running over the $100$-th roots of unity, $\frac1{100}\sum_\omega\omega^m$ is $1$ if $100\mid m$ and $0$ otherwise, so
$$X-Y=\frac1{100}\sum_{\omega^{100}=1}P(\omega)^n .$$
For $\omega=1$: $P(1)=25-75=-50$. For $\omega\neq1$: $B(\omega)+R(\omega)=\sum_{s=1}^{100}\omega^s=0$, so $P(\omega)=2B(\omega)$. Therefore
$$X-Y=\frac1{100}\Big[(-50)^n+\sum_{\omega\ne1}2^nB(\omega)^n\Big]=\frac{(-50)^n-50^n}{100}+2^n Z,\qquad Z=\frac1{100}\sum_{\omega^{100}=1}B(\omega)^n,$$
where we added and subtracted the $\omega=1$ term $2^nB(1)^n=2^n25^n=50^n$. By the same filter, $Z$ is the number of tuples in $T_n$ all of whose coordinates are blue, so $Z\ge0$.

**$n$ even.** Then $(-50)^n-50^n=0$, so $X-Y=2^nZ\ge0$, i.e. $X\ge Y$ for every colouring: at least half of $T_n$ has an even number of red coordinates.

**$n$ odd.** Colour blue the $25$ numbers $1,5,9,\dots,97$ (those $\equiv1\pmod4$) and the other $75$ red. A blue $n$-tuple has sum $\equiv n\not\equiv0\pmod4$, so it is never in $T_n$, and $Z=0$. Then $X-Y=\frac{-2\cdot50^n}{100}=-50^{n-1}<0$, so fewer than half of the tuples in $T_n$ have an even number of red coordinates, and the property fails.

### m103
source: mathnet
mathnet_id: 06ip
country: Hong Kong
competition: 1997-2023 IMO HK TST
type: answer
difficulty: 7
techniques: recursion
statement:
One day, one alien comes to the Earth. Every day, each alien on the Earth does exactly one of four things, each with probability $\frac14$: (1) destroys himself, (2) splits into two aliens, (3) splits into three aliens, (4) does nothing. A newly created alien also acts in this way, starting on the next day, and all aliens act independently of each other and of the past. Find the probability that eventually there is no alien on the Earth.
asked:
Starting from one alien that each day dies, becomes $2$, becomes $3$ or stays, each with probability $\frac14$, independently, find the probability that the aliens eventually die out.
technique:
Condition on what the first alien does on the first day. Independence turns the probability for several aliens into a power of the probability for one.
hint:
Let $p_n$ be the probability that all aliens are gone by the end of day $n$. Conditioning on day $1$ gives $p_{n+1}=\frac14\big(1+p_n+p_n^2+p_n^3\big)$, with $p_0=0$.
hint:
The answer is $\lim p_n$. Any limit must be a fixed point of $f(t)=\frac14(1+t+t^2+t^3)$; factor $f(t)-t$.
hint:
The fixed points are $1$ and $-1\pm\sqrt2$. Show by induction that $p_n$ never exceeds the smallest nonnegative one.
solution:
Let $E_n$ be the event that no alien is left at the end of day $n$, and $p_n=P(E_n)$, so $p_0=0$. Once the population is $0$ it stays $0$, so $E_1\subseteq E_2\subseteq\cdots$, and the event "eventually no alien" is $E=\bigcup_nE_n$. By continuity of probability along an increasing union, $P(E)=\lim_{n\to\infty}p_n$.

**Recursion.** Condition on what the original alien does on day $1$. If he destroys himself, $E_{n+1}$ holds. Otherwise he leaves $k\in\{1,2,3\}$ aliens, each of which starts an independent family behaving exactly like the original one; $E_{n+1}$ holds exactly when each of these $k$ families has died out within the next $n$ days, which has probability $p_n^k$. Hence
$$p_{n+1}=f(p_n),\qquad f(t)=\tfrac14\left(1+t+t^2+t^3\right).$$

**Fixed points.** $4(f(t)-t)=t^3+t^2-3t+1=(t-1)(t^2+2t-1)$, with roots $1$ and $-1\pm\sqrt2$. Let $q=\sqrt2-1\approx0.414$, the only root in $[0,1)$.

**Bounds.** $f$ is increasing on $[0,\infty)$. We show $0\le p_n\le p_{n+1}\le q$ for all $n$ by induction. For $n=0$: $p_0=0\le p_1=\frac14\le q$. If $p_{n-1}\le p_n\le q$, then applying the increasing $f$ gives $p_n\le p_{n+1}\le f(q)=q$.

So $(p_n)$ is increasing and bounded by $q$, hence converges to some $L\in[\frac14,q]$. Since $f$ is continuous, $L=\lim p_{n+1}=f(L)$, so $L$ is a fixed point of $f$ in $[\frac14,q]$. The only one is $q$. Therefore the probability that the aliens eventually die out is
$$P(E)=\boxed{\sqrt2-1}.$$

(Remark: the equation $c=f(c)$ for $c=P(E)$ alone also has the root $c=1$; the bound $p_n\le q$ is what excludes it.)

### m104
source: mathnet
mathnet_id: 0cd9
country: Romania
competition: THE Fifteenth ROMANIAN MASTER OF MATHEMATICS
type: proof
difficulty: 7
techniques: complex-numbers
statement:
Given a triangle $ABC$, let $H$ and $O$ be its orthocentre and circumcentre, respectively. Let $K$ be the midpoint of the segment $AH$. Let $\ell$ be any line through $O$, and let $P$ and $Q$ be the orthogonal projections of $B$ and $C$ onto $\ell$, respectively. Prove that $KP+KQ\ge BC$.
asked:
Show that the sum of the distances from the midpoint of $AH$ to the feet of the perpendiculars from $B$ and $C$ to any line through the circumcentre is at least $BC$.
technique:
Put the circumcircle as the unit circle in the complex plane; the orthocentre, the midpoint $K$ and the projections onto a line through the origin all have short formulas there.
hint:
With $O=0$ and $|a|=|b|=|c|=1$, the orthocentre is $h=a+b+c$, so $k=a+\frac{b+c}2$. If $\ell$ has unit direction $u$, the projection of $z$ onto $\ell$ is $\frac12(z+u^2\bar z)$.
hint:
Compute $k-p$ and multiply by $b$ (which does not change the modulus). Do the same for $k-q$ with $c$.
hint:
You should get $KP=\frac12|2ab+bc-u^2|$ and $KQ=\frac12|2ac+bc-u^2|$. Now one application of the triangle inequality finishes.
solution:
Scale so that the circumradius is $1$ and use complex coordinates with $O=0$; lower-case letters denote coordinates, so $|a|=|b|=|c|=1$ and $\bar z=1/z$ for $z\in\{a,b,c\}$.

**Orthocentre.** Let $h=a+b+c$. Then $h-a=b+c$ and
$$\overline{\left(\frac{b+c}{b-c}\right)}=\frac{1/b+1/c}{1/b-1/c}=\frac{c+b}{c-b}=-\frac{b+c}{b-c},$$
so $\frac{h-a}{b-c}$ is purely imaginary: either $h=a$ or $AH'\perp BC$ where $H'$ is the point $h$. Likewise for $B$ and $C$. If $h\notin\{a,b,c\}$, then $h$ lies on two altitudes, so $h$ is the orthocentre. If, say, $h=a$, then $b=-c$, $BC$ is a diameter, the angle at $A$ is right, and the orthocentre is $A=h$ again. So in all cases $H=h$, and
$$k=\frac{a+h}2=a+\frac{b+c}2 .$$

**Projections.** Let $u$ be a unit complex number in the direction of $\ell$. The projection of $z$ onto the line $\{tu:t\in\mathbb R\}$ is $u\operatorname{Re}(z\bar u)=\frac u2(z\bar u+\bar zu)=\frac12(z+u^2\bar z)$. Hence
$$p=\frac12\Big(b+\frac{u^2}b\Big),\qquad q=\frac12\Big(c+\frac{u^2}c\Big).$$

**Distances.** 
$$k-p=a+\frac c2-\frac{u^2}{2b},\qquad\text{so}\qquad KP=|k-p|=|b|\,|k-p|=\frac12\left|2ab+bc-u^2\right|.$$
Symmetrically $KQ=\frac12\left|2ac+bc-u^2\right|$. Put $w=bc-u^2$. By the triangle inequality,
$$KP+KQ=\frac12\big(|2ab+w|+|2ac+w|\big)\ge\frac12\big|(2ab+w)-(2ac+w)\big|=|a|\,|b-c|=BC .$$
This holds for every line $\ell$ through $O$. $\blacksquare$

### m105
source: mathnet
mathnet_id: 0grr
country: Turkey
competition: Team Selection Test
type: answer
difficulty: 8
techniques: cauchy-schwarz
statement:
Let $a_0,a_1,\dots,a_{100}$ and $b_1,b_2,\dots,b_{100}$ be real numbers such that for every $n=0,1,\dots,99$ one of the following holds:
$$a_{n+1}=\frac{a_n}2,\ \ b_{n+1}=\frac12-a_n\qquad\text{or}\qquad a_{n+1}=2a_n^2,\ \ b_{n+1}=a_n .$$
If $a_{100}\le a_0$, find the maximal value of $b_1+b_2+\dots+b_{100}$.
asked:
At each step the sequence $a$ is either halved or replaced by twice its square, with $b$ recording a matching amount. If $a$ does not end above where it started, how large can the total of the $b$'s be?
technique:
Express each $b_n$ and the step rule through the ratio $a_n/a_{n-1}$, so that the condition $a_{100}\le a_0$ can be fed into a fractional sum estimate.
hint:
Dispose of $a_0\le0$ first. For $a_0>0$ all $a_n>0$; check that in both cases $b_n=\frac{a_n}{a_{n-1}}-a_{n-1}$.
hint:
Both options satisfy $(a_n-\frac{a_{n-1}}2)(a_n-2a_{n-1}^2)=0$. Divide by $a_na_{n-1}$ to get an identity involving $\frac{a_n}{a_{n-1}}$ and $\frac{a_{n-1}^2}{a_n}$, and sum it.
hint:
You then need $\sum_{n=1}^{100}\frac{a_{n-1}^2}{a_n}\ge\sum_{n=1}^{100}a_{n-1}$. Use the Engel form of Cauchy-Schwarz and $a_{100}\le a_0$.
solution:
**Answer:** $\boxed{50}$.

Let $S=b_1+\dots+b_{100}$.

**$a_0<0$ is impossible.** We show $a_n>a_0$ for all $n\ge1$. For $n=1$: $a_0/2>a_0$ as $a_0<0$, and $2a_0^2>0>a_0$. If $a_n>a_0$: when $a_n<0$, either $a_{n+1}=a_n/2>a_n>a_0$ or $a_{n+1}=2a_n^2>0>a_0$; when $a_n\ge0$, both options give $a_{n+1}\ge0>a_0$. So $a_{100}>a_0$, contradicting the hypothesis.

**$a_0=0$.** Then every $a_n=0$, and each $b_n$ is $\frac12$ or $0$, so $S\le50$.

**$a_0>0$.** Both options keep the sequence positive, so all $a_n>0$. If step $n$ uses the first option, $\frac{a_n}{a_{n-1}}=\frac12$ and $b_n=\frac12-a_{n-1}$; if it uses the second, $\frac{a_n}{a_{n-1}}=2a_{n-1}$ and $b_n=a_{n-1}$. In both cases
$$b_n=\frac{a_n}{a_{n-1}}-a_{n-1}.$$
Also in both cases $(a_n-\frac{a_{n-1}}2)(a_n-2a_{n-1}^2)=0$, i.e. $a_n^2-a_n\big(\frac{a_{n-1}}2+2a_{n-1}^2\big)+a_{n-1}^3=0$. Dividing by $a_na_{n-1}>0$:
$$\frac{a_n}{a_{n-1}}=\frac12+2a_{n-1}-\frac{a_{n-1}^2}{a_n}.$$
Therefore
$$S=\sum_{n=1}^{100}\Big(\frac{a_n}{a_{n-1}}-a_{n-1}\Big)=50+\sum_{n=1}^{100}a_{n-1}-\sum_{n=1}^{100}\frac{a_{n-1}^2}{a_n}.$$
Let $X=a_0+\dots+a_{99}>0$ and $Y=a_1+\dots+a_{100}>0$. Since $a_{100}\le a_0$, $Y\le X$. By the Cauchy-Schwarz inequality in Engel form,
$$\sum_{n=1}^{100}\frac{a_{n-1}^2}{a_n}\ge\frac{X^2}{Y}\ge\frac{X^2}{X}=X .$$
Hence $S\le50+X-X=50$.

**The value $50$ is attained:** take $a_n=\frac12$ for all $n$ and always the second option: $2\cdot\left(\frac12\right)^2=\frac12$, so the sequence is constant, $a_{100}=a_0$, and every $b_n=\frac12$, giving $S=50$.

### m106
source: mathnet
mathnet_id: 0kus
country: United States
competition: USA TSTST
type: proof
difficulty: 6
techniques: cauchy-schwarz, telescoping
statement:
Let $n\ge m\ge1$ be integers. Prove that
$$\sum_{k=m}^{n}\left(\frac1{k^2}+\frac1{k^3}\right)\ge m\cdot\left(\sum_{k=m}^{n}\frac1{k^2}\right)^2 .$$
asked:
Show that the sum of $\frac1{k^2}+\frac1{k^3}$ over $m\le k\le n$ is at least $m$ times the square of the sum of $\frac1{k^2}$ over the same range.
technique:
The right side is the square of a sum, so an inequality that bounds such a square by a product of two sums is natural; the work is in choosing the two sums so that the unwanted one collapses.
hint:
Write $\frac1{k^2}+\frac1{k^3}=\frac{k+1}{k^3}$. Try to bound $\big(\sum\frac1{k^2}\big)^2$ by $\Big(\sum\frac{k+1}{k^3}\Big)\cdot\Big(\sum c_k\Big)$ for suitable $c_k$.
hint:
Cauchy-Schwarz forces $c_k=\dfrac{(1/k^2)^2}{(k+1)/k^3}$. Simplify it.
hint:
$c_k=\frac1{k(k+1)}=\frac1k-\frac1{k+1}$, and its sum over $m\le k\le n$ is less than $\frac1m$.
solution:
For $k\ge1$ put $x_k=\frac1{k^2}+\frac1{k^3}=\frac{k+1}{k^3}>0$ and $y_k=\frac1{k^2}$. By the Cauchy-Schwarz inequality,
$$\Big(\sum_{k=m}^ny_k\Big)^2=\Big(\sum_{k=m}^n\sqrt{x_k}\cdot\frac{y_k}{\sqrt{x_k}}\Big)^2\le\Big(\sum_{k=m}^nx_k\Big)\Big(\sum_{k=m}^n\frac{y_k^2}{x_k}\Big).$$
Here
$$\frac{y_k^2}{x_k}=\frac{1/k^4}{(k+1)/k^3}=\frac1{k(k+1)}=\frac1k-\frac1{k+1},$$
so the last sum telescopes:
$$\sum_{k=m}^n\frac{y_k^2}{x_k}=\frac1m-\frac1{n+1}<\frac1m .$$
Since $\sum x_k>0$, we get
$$\Big(\sum_{k=m}^n\frac1{k^2}\Big)^2<\frac1m\sum_{k=m}^n\left(\frac1{k^2}+\frac1{k^3}\right),$$
and multiplying by $m$ gives the claim (even with strict inequality). $\blacksquare$

### m107
source: mathnet
mathnet_id: 03bh
country: Bulgaria
competition: Team selection test for the 54th IMO
type: answer
difficulty: 8
techniques: similar-triangles, angle-chasing
statement:
The incircle of triangle $ABC$ touches the sides $BC$ and $AC$ at points $A_1$ and $B_1$, respectively. The lines $B_1A_1$ and $AB$ meet at a point $X$ such that $A$ lies between $X$ and $B$. If $\angle CXB=90^\circ$ and $BC^2=AB^2+BC\cdot AC$, find the angles of triangle $ABC$.
asked:
Given the length condition $BC^2=AB^2+BC\cdot AC$ and that $X=A_1B_1\cap AB$ sees $BC$ at a right angle, determine the three angles of the triangle.
technique:
Rewrite the length condition as a product of two lengths along $BC$ equal to $AB^2$; that is the signature of a pair of triangles sharing the angle at $B$. A suitable auxiliary point on $BC$ makes it appear.
hint:
Write $a=BC$, $b=CA$, $c=AB$. The condition says $a(a-b)=c^2$, so $a>b$. Let $Y$ be the point of $BC$ with $CY=b$. Show that $AY\parallel A_1B_1$, and that $BY\cdot BC=BA^2$.
hint:
From $BY\cdot BC=BA^2$, triangles $BAC$ and $BYA$ are similar, so $\angle BAY=\angle BCA$. Transfer this angle to $X$ using $XA_1\parallel AY$ and conclude that $X,A,A_1,C$ are concyclic.
hint:
The circle then gives $AA_1\perp BC$. When is the foot of the altitude from $A$ the incircle's touch point?
solution:
**Answer:** $\angle A=108^\circ$, $\angle B=\angle C=36^\circ$.

Write $a=BC$, $b=CA$, $c=AB$, $s=\frac{a+b+c}2$; the tangent lengths are $CA_1=CB_1=s-c$, $BA_1=s-b$, $AB_1=s-a$. We use directed angles $\measuredangle(\ell,m)$ between lines, modulo $180^\circ$.

**Step 1: an auxiliary point.** The condition reads $a^2-ab=c^2$, i.e. $a(a-b)=c^2>0$, so $a>b$. Let $Y$ be the point on segment $BC$ with $CY=b$; then $BY=a-b$. The homothety with centre $C$ and ratio $\frac{b}{s-c}$ maps $B_1$ (on ray $CA$ at distance $s-c$) to $A$ and $A_1$ (on ray $CB$ at distance $s-c$) to $Y$. Hence $AY\parallel B_1A_1$.

**Step 2: similar triangles.** $BY\cdot BC=(a-b)a=c^2=BA^2$, so $\frac{BA}{BY}=\frac{BC}{BA}$, and triangles $BAC$ and $BYA$ share the angle at $B$. By SAS they are similar, with $B\to B$, $A\to Y$, $C\to A$. This similarity maps ray $BA$ to ray $BC$ and ray $BC$ to ray $BA$, so it reverses orientation; therefore directed angles change sign:
$$\measuredangle(AB,AY)=-\measuredangle(CB,CA)=\measuredangle(CA,CB).$$

**Step 3: a circle.** The lines $XA$ and $AB$ coincide, and $XA_1\parallel AY$. Hence
$$\measuredangle(XA,XA_1)=\measuredangle(AB,AY)=\measuredangle(CA,CB)=\measuredangle(CA,CA_1).$$
So $X,A,A_1,C$ lie on one circle. (The four points are distinct: $X$ lies on line $AB$ outside segment $AB$, $A_1$ is interior to $BC$.) In this circle,
$$\measuredangle(A_1A,A_1C)=\measuredangle(XA,XC)=\measuredangle(XB,XC)=90^\circ,$$
using that $A$ lies on line $XB$ and $\angle CXB=90^\circ$. So $AA_1\perp BC$.

**Step 4: the triangle is isosceles.** From the right triangles $ABA_1$ and $ACA_1$: $c^2-(s-b)^2=AA_1^2=b^2-(s-c)^2$. Hence
$$c^2-b^2=(s-b)^2-(s-c)^2=(c-b)(2s-b-c)=(c-b)a .$$
If $c\neq b$, dividing gives $c+b=a$, impossible in a triangle. So $b=c$, and the condition becomes $a^2-ab-b^2=0$, i.e. $\frac ab=\frac{1+\sqrt5}2$. In the isosceles triangle, $\cos C=\frac{a/2}{b}=\frac{1+\sqrt5}4=\cos36^\circ$, so $\angle B=\angle C=36^\circ$ and $\angle A=108^\circ$.

**Step 5: such a triangle works.** Take $b=c$ and $a=\frac{1+\sqrt5}2b$ (angles $108^\circ,36^\circ,36^\circ$). The length condition holds. By Menelaus for the transversal $A_1B_1X$ of triangle $ABC$, $\frac{AX}{XB}=\frac{A_1C}{BA_1}\cdot\frac{AB_1}{B_1C}=\frac{s-c}{s-b}\cdot\frac{s-a}{s-c}=\frac{s-a}{s-b}<1$ (as $a>b$), and since $A_1,B_1$ are interior points of their sides, $X$ lies on line $AB$ outside the segment, on the side of $A$; so $A$ lies between $X$ and $B$. Steps 1 to 3 used only the length condition, so $X,A,A_1,C$ are concyclic; and since $b=c$, $A_1$ is the midpoint of $BC$ and $AA_1\perp BC$. Hence $\measuredangle(XB,XC)=\measuredangle(A_1A,A_1C)=90^\circ$, i.e. $\angle CXB=90^\circ$. So the angles are $\boxed{\angle A=108^\circ,\ \angle B=\angle C=36^\circ}$.

### m108
source: mathnet
mathnet_id: 07fs
country: Iran
competition: 37th Iranian Mathematical Olympiad
type: proof
difficulty: 8
techniques: angle-chasing
statement:
In an acute-angled triangle $ABC$ the altitudes $BE$ and $CF$ meet at $H$. The line through $H$ perpendicular to $EF$ meets the arc $BC$ of the circumcircle of $ABC$ not containing $A$ at $K$. If $AK$ and $BC$ meet at $P$, prove that $PK=PH$.
asked:
Show that $P=AK\cap BC$ is equidistant from $K$ and from the orthocentre $H$.
technique:
Find a circle through $H$ and $K$ whose centre is forced onto $BC$, then show by chasing angles at $K$ that this centre also lies on $AK$. Directed angles keep the argument free of case distinctions.
hint:
Two classical facts: $AO\perp EF$ (with $O$ the circumcentre), and the reflection $H'$ of $H$ in $BC$ lies on the circumcircle and on line $AH$. So $HK\parallel AO$, and any circle through $H$ and $H'$ has its centre on $BC$.
hint:
Let $Q$ be the centre of the circle through $H,H',K$. It suffices to show $Q$ lies on line $AK$. Useful lemma: if $X,Y,Z$ lie on a circle with centre $Q$, then $\measuredangle QXY=\measuredangle XZY-90^\circ$.
hint:
Apply the lemma twice: in the circumcircle to $\measuredangle OAK$ (using $H'$ as the third point), and in the circle $HH'K$ to $\measuredangle QKH$. Then use $KH\parallel AO$.
solution:
Let $\Gamma$ be the circumcircle, $O$ its centre, and $\measuredangle(\ell,m)$, $\measuredangle XYZ=\measuredangle(YX,YZ)$ directed angles modulo $180^\circ$.

**Lemma.** If $X,Y,Z$ lie on a circle with centre $Q$, then $\measuredangle QXY=\measuredangle XZY-90^\circ$.
*Proof.* Let $X^*$ be the antipode of $X$, so $Q$ lies on $XX^*$ and $\measuredangle XYX^*=90^\circ$ (if $Y=X^*$ both sides are $0$). The directed angles of triangle $XYX^*$ sum to $0$: $\measuredangle YXX^*+\measuredangle XX^*Y+\measuredangle X^*YX=0$, so $\measuredangle QXY=\measuredangle X^*XY=-\measuredangle YXX^*=\measuredangle XX^*Y+\measuredangle X^*YX=\measuredangle XX^*Y-90^\circ$, and $\measuredangle XX^*Y=\measuredangle XZY$ (inscribed angles). $\square$

**Fact 1: $AO\perp EF$.** As the triangle is acute, $E,F$ lie on the sides and $O$ is inside. $B,C,E,F$ lie on the circle with diameter $BC$, so $\angle AFE=\angle ACB=C$. In the isosceles triangle $OAB$, $\angle AOB=2C$, so $\angle OAB=90^\circ-C$. The ray $AO$ meets segment $EF$ at some $Z$, and in triangle $AFZ$ the angles at $A$ and $F$ are $90^\circ-C$ and $C$, so $\angle AZF=90^\circ$. Hence the line through $H$ perpendicular to $EF$ is parallel to $AO$: $HK\parallel AO$.

**Fact 2.** Let $H'$ be the reflection of $H$ in $BC$. Then $H'$ lies on line $AH$ (which is perpendicular to $BC$), and $\angle BH'C=\angle BHC=180^\circ-A$ with $H'$ on the other side of $BC$ from $A$, so $ABH'C$ is cyclic: $H'\in\Gamma$.

**The isosceles case.** If $AB=AC$, then $EF\parallel BC$, the line through $H$ perpendicular to $EF$ is the altitude $AH$, so $K=H'$ and $P$ is the foot $D$ of that altitude; then $PK=DH'=DH=PH$.

**The general case.** Let $AB\neq AC$. Then $K\neq H'$: otherwise $HK$ would be the line $AH$, and $AH\perp EF$ together with $AH\perp BC$ would give $EF\parallel BC$, i.e. $\frac{AE}{AC}=\frac{AF}{AB}$; with $AE=AB\cos A$ and $AF=AC\cos A$ this forces $AB=AC$. Also $K\neq A$ because $K$ is on the other arc. So $K$ is not on line $AHH'$, and $H,H',K$ are three non-collinear points; let $\omega$ be their circle and $Q$ its centre. Since $BC$ is the perpendicular bisector of $HH'$, $Q$ lies on $BC$.

*Angle at $K$ in $\omega$:* by the lemma with $(X,Y,Z)=(K,H,H')$,
$$\measuredangle QKH=\measuredangle KH'H-90^\circ=-\measuredangle AH'K-90^\circ,$$
because $H'H$ and $H'A$ are the same line.

*Angle at $K$ from $AK$:* by the lemma in $\Gamma$ with $(X,Y,Z)=(A,K,H')$, $\measuredangle OAK=\measuredangle AH'K-90^\circ$. Since $KH\parallel AO$,
$$\measuredangle(KA,KH)=\measuredangle(AK,AO)=-\measuredangle OAK=90^\circ-\measuredangle AH'K .$$
Modulo $180^\circ$ the two results agree: $\measuredangle(KQ,KH)=\measuredangle(KA,KH)$. Hence the lines $KQ$ and $KA$ coincide, i.e. $Q$ lies on line $AK$.

Since $K$ is on the arc $BC$ not containing $A$, the points $A$ and $K$ are on opposite sides of $BC$, so line $AK$ is not $BC$ and meets it in exactly one point, $P$. As $Q$ lies on both lines, $Q=P$. So $P$ is the centre of $\omega$, and $PK=PH$. $\blacksquare$

### m109
source: mathnet
mathnet_id: 07hp
country: Iran
competition: 40th Iranian Mathematical Olympiad
type: proof
difficulty: 8
techniques: similar-triangles, complex-numbers
statement:
Let $ABC$ be a triangle with $\angle BAC\neq90^\circ$ and $AB\neq BC$. Let $T$ be the second intersection of the $A$-symmedian (the reflection of the median from $A$ in the bisector of angle $A$) with the circumcircle of $ABC$. Let $D\neq A$ be the point on line $AC$ with $BD=BA$. The tangent at $D$ to the circumcircle of $ADT$ meets the circumcircle of $DCT$ a second time at $K$. Prove that $\angle BKC=90^\circ$.
asked:
Show that $K$ lies on the circle with diameter $BC$.
technique:
Chasing angles in the two circles through $D$ and $T$ produces a pair of directly similar triangles with common vertex $T$; that similarity pins down $K$, and coordinates on the circumcircle finish the computation.
hint:
Show that triangles $TKC$ and $TDA$ are directly similar (equal directed angles at $K,D$ and at $C,A$). So the spiral similarity with centre $T$ taking $A\mapsto C$ also takes $D\mapsto K$, and $K-C=\lambda(D-A)$ with $\lambda=\frac{C-T}{A-T}$.
hint:
Use complex numbers with the circumcircle as unit circle. Then $d=b+c-\frac{ac}b$, and you can check that $t=\frac{2bc-ab-ac}{b+c-2a}$ is on the unit circle and on the symmedian.
hint:
Compute $\lambda$ and $k$, and compare $|k-m|$ with $|c-m|$ where $m=\frac{b+c}2$.
solution:
Directed angles $\measuredangle XYZ=\measuredangle(YX,YZ)$ are taken modulo $180^\circ$. Use complex coordinates with the circumcircle $\Gamma$ of $ABC$ the unit circle; lower-case letters are coordinates, $\bar z=1/z$ on $\Gamma$, and $m=\frac{b+c}2$ is the midpoint of $BC$. Since $\angle A\neq90^\circ$, $BC$ is not a diameter, so $b+c\neq0$.

**Non-degeneracy.** $D$ is the reflection of $A$ in the foot of the perpendicular from $B$ to $AC$; $D\neq A$ as $\angle A\ne 90^\circ$, and $D\neq C$ as $BC\ne BA$. Line $AC$ meets $\Gamma$ only in $A,C$, so $D\notin\Gamma$ and $T\ne D$. The tangent at $D$ to circle $ADT$ is not line $AC$ (that line passes through $A$, a second point of the circle), so $K\neq C$; it does not pass through $T$, so $K\ne T$; and the circles $ADT$, $DCT$ are not tangent at $D$, since they share the second point $T$ and are distinct ($A,D,C$ are collinear). So $K$ is well defined and $K\notin\{C,D,T\}$.

**Step 1: a spiral similarity.** In circle $DCTK$: $\measuredangle TKC=\measuredangle TDC=\measuredangle TDA$ (as $D,C,A$ are collinear), and $\measuredangle KCT=\measuredangle KDT$. By the tangent-chord angle in circle $ADT$, $\measuredangle KDT=\measuredangle DAT$. So triangles $KCT$ and $DAT$ have equal directed angles at corresponding vertices $K\leftrightarrow D$ and $C\leftrightarrow A$, hence are directly similar with $T\leftrightarrow T$. Equivalently, with $\lambda=\frac{c-t}{a-t}$ we have $c-t=\lambda(a-t)$ and $k-t=\lambda(d-t)$; subtracting,
$$k=c+\lambda(d-a).$$

**Step 2: coordinates of $D$ and $T$.** The foot of the perpendicular from $b$ to chord $ac$ is $\frac12\big(a+b+c-\frac{ac}b\big)$, so $d=b+c-\frac{ac}b$ and
$$d-a=(b-a)+\frac{c(b-a)}b=\frac{(b-a)(b+c)}b .$$
Let $t=\frac{2bc-ab-ac}{b+c-2a}$; the denominator is nonzero because $|b+c|<2$ for $b\neq c$. Then
$$\bar t=\frac{\frac2{bc}-\frac1{ab}-\frac1{ac}}{\frac1b+\frac1c-\frac2a}=\frac{2a-b-c}{ab+ac-2bc}=\frac1t,$$
so $t\in\Gamma$; and $t-a=\frac{2(a-b)(a-c)}{b+c-2a}\neq0$. Line $AX$ is the reflection of line $AY$ in the bisector of angle $A$ exactly when $\measuredangle(AB,AX)=\measuredangle(AY,AC)$, i.e. when $\frac{(x-a)(y-a)}{(b-a)(c-a)}$ is real. With $x=t$, $y=m$:
$$\frac{(t-a)(m-a)}{(b-a)(c-a)}=\frac{\frac{2(a-b)(a-c)}{b+c-2a}\cdot\frac{b+c-2a}2}{(b-a)(c-a)}=1 .$$
So $t$ lies on the $A$-symmedian and on $\Gamma$, and $t\ne a$: it is the point $T$.

**Step 3: computing $k$.** $c-t=\frac{(c-a)(c-b)}{b+c-2a}$, so $\lambda=\frac{c-t}{a-t}=\frac{(c-a)(c-b)}{-2(a-b)(a-c)}=\frac{c-b}{2(a-b)}$. Hence
$$k=c+\frac{c-b}{2(a-b)}\cdot\frac{(b-a)(b+c)}b=c+\frac{(b-c)(b+c)}{2b}=\frac{2bc+b^2-c^2}{2b}.$$
Then $k-m=\frac{2bc+b^2-c^2-b^2-bc}{2b}=\frac{c(b-c)}{2b}$, so $|k-m|=\frac{|b-c|}2=MB=MC$.

So $K$ lies on the circle with diameter $BC$. Finally $K\neq C$ (shown above) and $K\ne B$ (as $k=b$ would give $(b-c)^2=0$). By Thales' theorem, $\angle BKC=90^\circ$. $\blacksquare$

### m110
source: mathnet
mathnet_id: 0hgg
country: Ukraine
competition: 62nd Ukrainian National Mathematical Olympiad, Third Round, First Tour
type: answer
difficulty: 7
techniques: trigonometry
statement:
In an acute triangle $ABC$ the points $H$ and $O$ are the orthocentre and the circumcentre, respectively. The line $HO$ meets the sides $AB$ and $AC$ at points $X$ and $Y$, respectively, so that $H$ lies on the segment $OX$. It turns out that $XH=HO=OY$. Find the angle $\angle BAC$.
asked:
The Euler line cuts off equal thirds $XH=HO=OY$ between sides $AB$ and $AC$. Determine angle $A$.
technique:
Turn the equal segments into ratios of distances from $H$ and $O$ to the sides, and express those distances through the circumradius and the cosines of the angles.
hint:
Along a line, the distance to a fixed line changes linearly. Since $O$ is the midpoint of $HY$ and $H$ the midpoint of $XO$: $d(H,AC)=2\,d(O,AC)$ and $d(O,AB)=2\,d(H,AB)$.
hint:
With circumradius $R$: $d(O,AC)=R\cos B$ and $d(H,AC)=2R\cos A\cos C$, and similarly for $AB$. You get $\cos A\cos C=\cos B$ and $4\cos A\cos B=\cos C$.
hint:
Expand $\cos B=-\cos(A+C)$ and $\cos C=-\cos(A+B)$ to get $\tan A\tan C$ and $\tan A\tan B$, then use $\tan A+\tan B+\tan C=\tan A\tan B\tan C$.
solution:
**Answer:** $\angle BAC=\boxed{60^\circ}$.

Let $R$ be the circumradius and write $A,B,C$ for the angles, all acute. For a point $Z$ and a side line $\ell$, let $f_\ell(Z)$ be the signed distance from $Z$ to $\ell$, positive on the side of the triangle; along any line, $f_\ell$ is an affine function of the position.

**Distances.** $O$ is inside the triangle and $\angle BOC=2A$, so $f_{BC}(O)=R\cos A$; likewise $f_{CA}(O)=R\cos B$, $f_{AB}(O)=R\cos C$. The altitude from $B$ has length $c\sin A=2R\sin A\sin C$, and $BH=2R\cos B$ (in the acute triangle $H$ lies on this altitude between $B$ and the foot). So
$$f_{CA}(H)=2R(\sin A\sin C-\cos B)=2R(\sin A\sin C+\cos(A+C))=2R\cos A\cos C,$$
and likewise $f_{AB}(H)=2R\cos A\cos B$, $f_{BC}(H)=2R\cos B\cos C$.

**Necessity.** $H$ and $O$ are interior points ($H\ne O$, since otherwise the line $HO$ is undefined), and $X,Y$ are the two points where line $HO$ meets the boundary; as $H$ lies between $X$ and $O$, the order on the line is $X,H,O,Y$. (We need $X\ne Y$: if the line met the boundary in only one point, then $OY=OX=XH+HO=2HO\ne HO$, contradicting $HO=OY$.) From $HO=OY$, $O$ is the midpoint of $HY$, so $0=f_{CA}(Y)=2f_{CA}(O)-f_{CA}(H)$. From $XH=HO$, $H$ is the midpoint of $XO$, so $0=f_{AB}(X)=2f_{AB}(H)-f_{AB}(O)$. Therefore
$$\cos A\cos C=\cos B,\qquad 4\cos A\cos B=\cos C .$$
Since $\cos B=-\cos(A+C)=\sin A\sin C-\cos A\cos C$, the first gives $2\cos A\cos C=\sin A\sin C$, i.e. $\tan A\tan C=2$. Since $\cos C=\sin A\sin B-\cos A\cos B$, the second gives $5\cos A\cos B=\sin A\sin B$, i.e. $\tan A\tan B=5$. Put $t=\tan A>0$; then $\tan B=\frac5t$, $\tan C=\frac2t$. As $A+B+C=180^\circ$, $\tan A+\tan B+\tan C=\tan A\tan B\tan C$, i.e. $t+\frac7t=\frac{10}t$, so $t^2=3$, $t=\sqrt3$ and $A=60^\circ$.

**Such a triangle exists.** Take $A=60^\circ$ and $B,C$ acute with $\tan B=\frac5{\sqrt3}$, $\tan C=\frac2{\sqrt3}$; this is consistent since $\tan(A+B)=\frac{\sqrt3+5/\sqrt3}{1-5}=-\frac2{\sqrt3}=-\tan C$. Then $\cos B=\frac{\sqrt{21}}{14}$, $\cos C=\frac{\sqrt{21}}7$, and one checks $\cos A\cos C=\cos B$ and $4\cos A\cos B=\cos C$. The triangle is not equilateral, so $H\ne O$. Let $Y'=2O-H$ and $X'=2H-O$, so that $X'H=HO=OY'$, with $H$ between $X'$ and $O$ and $O$ between $H$ and $Y'$. By the relations, $f_{CA}(Y')=0$ and $f_{AB}(X')=0$, and
$$f_{AB}(Y')=2R(\cos C-\cos A\cos B)>0,\quad f_{BC}(Y')=2R(\cos A-\cos B\cos C)=2R\left(\tfrac12-\tfrac3{14}\right)>0,$$
$$f_{CA}(X')=R(4\cos A\cos C-\cos B)=R\cdot\tfrac{3\sqrt{21}}{14}>0,\quad f_{BC}(X')=R(4\cos B\cos C-\cos A)=R\left(\tfrac{6}{7}-\tfrac12\right)>0 .$$
So $Y'$ lies on side $AC$ and $X'$ on side $AB$ (strictly inside them); these are the points $Y,X$ where line $HO$ meets the sides, and $XH=HO=OY$ holds. Hence the answer is $60^\circ$.

### m111
source: mathnet
mathnet_id: 06wa
country: IMO
competition: IMO 2021 Shortlisted Problems
type: proof
difficulty: 6
techniques: telescoping
statement:
Let $n\ge2$ be an integer, and let $a_1,a_2,\dots,a_n$ be positive real numbers such that $a_1+a_2+\dots+a_n=1$. Prove that
$$\sum_{k=1}^{n}\frac{a_k}{1-a_k}\left(a_1+a_2+\dots+a_{k-1}\right)^2<\frac13 .$$
asked:
With $s_{k-1}$ the sum of the terms before $a_k$, show that the weighted sum of $\frac{a_k}{1-a_k}s_{k-1}^2$ stays below $\frac13$.
technique:
The constant $\frac13$ and the squares of partial sums suggest comparing each term with the increment of a simple function of the partial sums, so that the bounds add up to something that collapses.
hint:
Let $s_k=a_1+\dots+a_k$, so $s_0=0$, $s_n=1$. Note that $\frac13=\frac13(s_n^3-s_0^3)$.
hint:
Try to prove the termwise bound $\frac{a_k}{1-a_k}s_{k-1}^2<\frac13\left(s_k^3-s_{k-1}^3\right)$.
hint:
With $x=s_{k-1}$ and $a=a_k$, the right side is $a\left(x^2+ax+\frac{a^2}3\right)$. Use $x+a\le1$.
solution:
Let $s_k=a_1+\dots+a_k$ for $0\le k\le n$, so $s_0=0$, $s_n=1$, and $s_k=s_{k-1}+a_k$.

**Termwise bound.** Fix $k$ and write $x=s_{k-1}\ge0$ and $a=a_k>0$. Since $x+a=s_k\le1$ and $n\ge2$, we have $0<a<1$ (all terms are positive), so $1-a>0$. Now
$$\frac13\left(s_k^3-s_{k-1}^3\right)=\frac13\left((x+a)^3-x^3\right)=a\left(x^2+ax+\frac{a^2}3\right),$$
and
$$x^2+ax+\frac{a^2}3-\frac{x^2}{1-a}=ax-\frac{ax^2}{1-a}+\frac{a^2}3=\frac{ax(1-a-x)}{1-a}+\frac{a^2}3 .$$
Here $ax(1-a-x)\ge0$ because $x\ge0$ and $x+a\le1$, and $\frac{a^2}3>0$. Hence $\frac{x^2}{1-a}<x^2+ax+\frac{a^2}3$, and multiplying by $a>0$,
$$\frac{a_k}{1-a_k}s_{k-1}^2<\frac13\left(s_k^3-s_{k-1}^3\right).$$

**Summation.** Adding over $k=1,\dots,n$, the right sides telescope:
$$\sum_{k=1}^{n}\frac{a_k}{1-a_k}s_{k-1}^2<\frac13\left(s_n^3-s_0^3\right)=\frac13 .\qquad\blacksquare$$

### m112
source: mathnet
mathnet_id: 01v6
country: Belarus
competition: Selection and Training Session
type: answer
difficulty: 6
techniques: coordinates, polynomials
statement:
Consider the hyperbola $y=\frac1x$ and four circles $S_1,S_2,S_3,S_4$. The circle $S_1$ meets the hyperbola at exactly the four points $Z_1,Z_2,Z_3,Z_4$; $S_2$ meets it at exactly $Z_3,Z_4,Z_5,Z_6$; $S_3$ at exactly $Z_5,Z_6,Z_7,Z_8$; and $S_4$ at exactly $Z_7,Z_8,Z_1,Z_2$. The points $Z_1,\dots,Z_8$ are distinct. The radii of $S_1,S_2,S_3$ are $R_1,R_2,R_3$. Find the radius of $S_4$.
asked:
Express the radius of the fourth circle through $R_1,R_2,R_3$.
technique:
Substitute $y=\frac1x$ into the equation of a circle: the abscissae of the four intersection points are the roots of a quartic, and its coefficients encode the centre and the radius.
hint:
For the circle $(x-a)^2+(y-b)^2=R^2$, the abscissae $x_1,\dots,x_4$ of the intersection points are the roots of $x^4-2ax^3+(a^2+b^2-R^2)x^2-2bx+1=0$.
hint:
By Vieta, $\sum x_i=2a$, $\prod x_i=1$, $\sum\frac1{x_i}=2b$ and $\sum_{i<j}x_ix_j=a^2+b^2-R^2$. Find a formula for $R^2$ in terms of the points alone.
hint:
Show $4R^2=\sum_i\left(x_i^2+\frac1{x_i^2}\right)=\sum_i OZ_i^2$, where $O$ is the origin.
solution:
**Answer:** $R_4=\boxed{\sqrt{R_1^2-R_2^2+R_3^2}}$.

**Lemma.** If a circle of radius $R$ meets $y=\frac1x$ in exactly four points $Z_1,\dots,Z_4$, then $4R^2=OZ_1^2+OZ_2^2+OZ_3^2+OZ_4^2$, where $O$ is the origin.

*Proof.* Let the circle be $(x-a)^2+(y-b)^2=R^2$. A point $(x,\frac1x)$ ($x\ne0$) lies on it iff $(x-a)^2+(\frac1x-b)^2=R^2$; multiplying by $x^2\neq0$,
$$x^4-2ax^3+(a^2+b^2-R^2)x^2-2bx+1=0 .$$
This quartic has the four distinct abscissae $x_1,\dots,x_4$ of the $Z_i$ as roots (distinct points of the hyperbola have distinct abscissae), so these are all its roots. Let $e_1=\sum x_i$, $e_2=\sum_{i<j}x_ix_j$, $e_3=\sum_{i<j<k}x_ix_jx_k$, $e_4=x_1x_2x_3x_4$. Vieta's formulas give $e_1=2a$, $e_2=a^2+b^2-R^2$, $e_3=2b$, $e_4=1$. Then $\sum\frac1{x_i}=\frac{e_3}{e_4}=2b$ and $\sum_{i<j}\frac1{x_ix_j}=\frac{e_2}{e_4}=e_2$. Hence
$$\sum x_i^2=e_1^2-2e_2=4a^2-2e_2,\qquad \sum\frac1{x_i^2}=\Big(\sum\frac1{x_i}\Big)^2-2\sum_{i<j}\frac1{x_ix_j}=4b^2-2e_2,$$
and
$$\sum_{i=1}^4OZ_i^2=\sum\Big(x_i^2+\frac1{x_i^2}\Big)=4a^2+4b^2-4e_2=4R^2 .\qquad\square$$

**Applying the lemma** to the four circles, with $d_i=OZ_i^2$:
$$4R_1^2=d_1+d_2+d_3+d_4,\quad 4R_2^2=d_3+d_4+d_5+d_6,\quad 4R_3^2=d_5+d_6+d_7+d_8,\quad 4R_4^2=d_7+d_8+d_1+d_2 .$$
Therefore $4R_1^2-4R_2^2+4R_3^2=d_1+d_2+d_7+d_8=4R_4^2$, so $R_4^2=R_1^2-R_2^2+R_3^2$ and $R_4=\sqrt{R_1^2-R_2^2+R_3^2}$. (Configurations exist. If $x_1,\dots,x_4$ are distinct, nonzero, with product $1$, put $a=\frac{e_1}2$, $b=\frac{e_3}2$, $\rho=a^2+b^2-e_2$; then $\prod(x-x_i)=x^4-2ax^3+(a^2+b^2-\rho)x^2-2bx+1$, so the four points $(x_i,\frac1{x_i})$ satisfy $(x-a)^2+(y-b)^2=\rho$, which forces $\rho>0$ (four distinct points), and they are the only common points. So one may take $x_1x_2=x_5x_6=q$ and $x_3x_4=x_7x_8=\frac1q$ with eight distinct abscissae.)

### m113
source: mathnet
mathnet_id: 0gtt
country: Turkey
competition: Team Selection Test for IMO 2023
type: proof
difficulty: 8
techniques: angle-chasing, complex-numbers
statement:
$ABCD$ is a trapezoid with $AB\parallel CD$ (vertices in this order around it). A point $T$ in its interior satisfies $\angle ATD=\angle CTB$. The line $AT$ meets the circumcircle of $ACD$ a second time at $K$, and the line $BT$ meets the circumcircle of $BCD$ a second time at $L$. Assuming $K\neq L$, show that $KL\parallel AB$.
asked:
Show that the two second intersection points $K$ and $L$ lie on a line parallel to the bases.
technique:
Bring in one more circle, through $T,C,D$: the angle condition becomes a statement about two of its chords, and powers of points on line $CD$ transfer it to $K$ and $L$.
hint:
Let $AT,BT$ meet line $CD$ at $A_1,B_1$, and meet the circle $TCD$ again at $A_2,B_2$. Use directed angles at $T$ to show $A_2B_2\parallel CD$ (or $A_2=B_2$).
hint:
Compute the power of $A_1$ with respect to the circles $TCD$ and $ACD$: $A_1T\cdot A_1A_2=A_1C\cdot A_1D=A_1A\cdot A_1K$ (signed). So $K-A_1=\lambda(A_2-A_1)$ for a real $\lambda$; do the same at $B_1$.
hint:
The homothety with centre $T$ taking line $AB$ to line $CD$ shows the two ratios are equal. Then write $K-L$ as a combination of $A_1-B_1$ and $A_2-B_2$.
solution:
Let $\omega$ be the circle through $T,C,D$ (it exists, as $T$ is not on line $CD$). Directed angles $\measuredangle(\ell,m)$ are taken modulo $180^\circ$.

**Setup.** $T$ lies strictly between the parallel lines $AB$ and $CD$, so line $AT$ meets line $CD$ at a point $A_1$ with $T$ strictly between $A$ and $A_1$; similarly $B_1=BT\cap CD$. Let $k>0$ be the ratio of the distances from $T$ to $CD$ and to $AB$. The homothety with centre $T$ and ratio $-k$ maps line $AB$ to line $CD$, hence $A\mapsto A_1$ and $B\mapsto B_1$:
$$A_1-T=-k(A-T),\qquad B_1-T=-k(B-T).$$
Let $A_2$ be the second intersection of line $AT$ with $\omega$ ($A_2=T$ if the line is tangent), and define $B_2$ from line $BT$ likewise.

**Step 1: $A_2B_2\parallel CD$ or $A_2=B_2$.** Since $T$ is inside the convex quadrilateral $ABCD$, the rays $TA,TB,TC,TD$ occur around $T$ in this rotational order, and $\angle DTA$ (resp. $\angle BTC$) is the rotation, in that common sense, from ray $TD$ to ray $TA$ (resp. from $TB$ to $TC$). The hypothesis therefore gives $\measuredangle(TD,TA)=\measuredangle(TB,TC)$, i.e.
$$\measuredangle(TA_2,TD)=\measuredangle(TA,TD)=\measuredangle(TC,TB)=\measuredangle(TC,TB_2).$$
Take $\omega$ as the unit circle in the complex plane. For points $X,Y$ of $\omega$, the inscribed angle theorem (with the tangent at $T$ playing the role of line $TX$ when $X=T$) says $\measuredangle(TX,TY)\equiv\frac12\big(\arg y-\arg x\big)\pmod{180^\circ}$. So the displayed equality gives $\arg\frac d{a_2}\equiv\arg\frac{b_2}c\pmod{360^\circ}$, and as all four numbers have modulus $1$, $\frac d{a_2}=\frac{b_2}c$, i.e. $a_2b_2=cd$. For points on the unit circle, $a_2b_2=cd$ means that the chord $A_2B_2$ is parallel to the chord $CD$ (both are perpendicular to the direction $\sqrt{cd}$), or $A_2=B_2$. In either case $A_2-B_2$ is a real multiple of $C-D$.

**Step 2: power of a point.** The point $A_1$ lies on line $CD$ and on line $AT$. Its power with respect to $\omega$ and with respect to the circle $ACD$ (which meets line $AT$ at $A$ and $K$), computed with signed lengths, gives
$$\overline{A_1T}\cdot\overline{A_1A_2}=\overline{A_1C}\cdot\overline{A_1D}=\overline{A_1A}\cdot\overline{A_1K}.$$
As $A\neq A_1$, this says $K-A_1=\lambda(A_2-A_1)$ with $\lambda=\dfrac{\overline{A_1T}}{\overline{A_1A}}$. From the homothety, $T-A_1=k(A-T)$ and $A-A_1=(1+k)(A-T)$, so $\lambda=\frac k{1+k}$. In the same way $L-B_1=\mu(B_2-B_1)$ with $\mu=\frac k{1+k}=\lambda$.

**Conclusion.** Subtracting,
$$K-L=(1-\lambda)(A_1-B_1)+\lambda(A_2-B_2).$$
$A_1-B_1$ is a real multiple of $C-D$ because $A_1,B_1$ lie on line $CD$, and so is $A_2-B_2$ by Step 1. Hence $K-L$ is a real multiple of $C-D$, nonzero by assumption, so $KL\parallel CD\parallel AB$. $\blacksquare$

### m114
source: mathnet
mathnet_id: 0bmu
country: Romania
competition: 66th NMO SELECTION TESTS FOR THE BALKAN AND INTERNATIONAL MATHEMATICAL OLYMPIADS
type: proof
difficulty: 7
techniques: trigonometry
statement:
Let $ABC$ be a triangle with inradius $r$. Let $R_A$ be the radius of the circle which is internally tangent at $A$ to the circumcircle of $ABC$ and tangent to the line $BC$; define $R_B$ and $R_C$ similarly. Show that
$$\frac1{R_A}+\frac1{R_B}+\frac1{R_C}\le\frac2r .$$
asked:
Prove that the reciprocals of the radii of the three circles tangent to the circumcircle at a vertex and to the opposite side sum to at most $\frac2r$.
technique:
Locate the centre of each circle on the radius $OA$ and compute its radius from a distance condition; afterwards everything is an inequality between trigonometric functions of the angles.
hint:
The centre is $P=A+t(O-A)$ with radius $tR$. Signed distances to $BC$ vary linearly along $AO$; with $h_a$ the altitude and $R\cos A$ the signed distance from $O$ to $BC$, show $\frac1{R_A}=\frac1R+\frac{1-\cos A}{h_a}$.
hint:
Use $\frac1{h_a}=\frac a{2S}$ and $\frac2r=\frac{a+b+c}S$ ($S$ the area). The claim becomes $\frac{6S}R\le\sum a(1+\cos A)$; then pass to $a=2R\sin A$.
hint:
You should reach $4\sin A\sin B\sin C\le\sin A+\sin B+\sin C$. Write both sides through half-angles; it reduces to $8\sin\frac A2\sin\frac B2\sin\frac C2\le1$.
solution:
Let $O,R$ be the circumcentre and circumradius, $S$ the area, $a,b,c$ the sides, $s=\frac{a+b+c}2$, $h_a=\frac{2S}a$, and write $A,B,C$ also for the angles.

**Computing $R_A$.** A circle internally tangent to the circumcircle at $A$ has its centre on segment $AO$: $P=A+t(O-A)$, radius $tR$, with $0<t<1$. Let $f$ be the signed distance to line $BC$, positive on the side of $A$; $f$ is affine, $f(A)=h_a$, and $f(O)=R\cos A$ (as $\angle BOC=2A$ or $360^\circ-2A$; $O$ is on the side of $A$ iff $A$ is acute). Since the circle passes through $A$ with $f(A)>0$, it touches line $BC$ exactly when $f(P)=tR$ (if $f(P)=-tR$, every point of the circle would have $f\le0$). Thus
$$(1-t)h_a+tR\cos A=tR\iff t=\frac{h_a}{h_a+R(1-\cos A)},$$
which indeed lies in $(0,1)$. Hence $R_A=tR$ and
$$\frac1{R_A}=\frac{h_a+R(1-\cos A)}{Rh_a}=\frac1R+\frac{1-\cos A}{h_a}=\frac1R+\frac{a(1-\cos A)}{2S}.$$

**Reduction.** Since $r=\frac Ss$, $\frac2r=\frac{a+b+c}S$. Summing the three formulas, the claim is
$$\frac3R+\sum\frac{a(1-\cos A)}{2S}\le\sum\frac{a}S\iff\frac{6S}R\le\sum a(1+\cos A).$$
With $a=2R\sin A$ etc. and $S=\frac{abc}{4R}=2R^2\sin A\sin B\sin C$, the left side is $12R\sin A\sin B\sin C$ and the right side is $2R\left(\sum\sin A+\frac12\sum\sin2A\right)$.

**Two identities** (with $A+B+C=180^\circ$):
- $\sin2A+\sin2B=2\sin(A+B)\cos(A-B)=2\sin C\cos(A-B)$ and $\sin2C=2\sin C\cos C=-2\sin C\cos(A+B)$, so $\sum\sin2A=2\sin C\big(\cos(A-B)-\cos(A+B)\big)=4\sin A\sin B\sin C$.
- $\sin A+\sin B=2\cos\frac C2\cos\frac{A-B}2$ and $\sin C=2\cos\frac C2\cos\frac{A+B}2$, so $\sum\sin A=4\cos\frac A2\cos\frac B2\cos\frac C2$.

So the claim becomes $12\prod\sin A\le2\sum\sin A+4\prod\sin A$, i.e. $4\prod\sin A\le\sum\sin A$. Writing $\sin A=2\sin\frac A2\cos\frac A2$, this is
$$32\prod\sin\tfrac A2\prod\cos\tfrac A2\le4\prod\cos\tfrac A2\iff8\sin\tfrac A2\sin\tfrac B2\sin\tfrac C2\le1,$$
since all half-angle cosines are positive.

**The last inequality.** Let $x=\sin\frac C2\in(0,1)$. Then
$$\sin\tfrac A2\sin\tfrac B2=\tfrac12\Big(\cos\tfrac{A-B}2-\cos\tfrac{A+B}2\Big)\le\tfrac12\big(1-\sin\tfrac C2\big)=\tfrac{1-x}2,$$
so $8\prod\sin\frac A2\le4x(1-x)\le(x+(1-x))^2=1$. All steps were equivalences or this bound, so $\frac1{R_A}+\frac1{R_B}+\frac1{R_C}\le\frac2r$. $\blacksquare$ (Equality holds for the equilateral triangle.)
