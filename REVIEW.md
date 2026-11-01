# Review sample

40 problems drawn at random (seed 40) from 212. Check the statement, the hints, and above all the solution.

## m109 · difficulty 8 · Similar triangles and power of a point, Complex numbers in geometry
*40th Iranian Mathematical Olympiad (Iran), MathNet 07hp*

**Statement**

Let $ABC$ be a triangle with $\angle BAC\neq90^\circ$ and $AB\neq BC$. Let $T$ be the second intersection of the $A$-symmedian (the reflection of the median from $A$ in the bisector of angle $A$) with the circumcircle of $ABC$. Let $D\neq A$ be the point on line $AC$ with $BD=BA$. The tangent at $D$ to the circumcircle of $ADT$ meets the circumcircle of $DCT$ a second time at $K$. Prove that $\angle BKC=90^\circ$.

**Hint 1: What is being asked**

Show that $K$ lies on the circle with diameter $BC$.

**Hint 2: The technique**

Chasing angles in the two circles through $D$ and $T$ produces a pair of directly similar triangles with common vertex $T$; that similarity pins down $K$, and coordinates on the circumcircle finish the computation.

**Hint 3: The key idea**

Show that triangles $TKC$ and $TDA$ are directly similar (equal directed angles at $K,D$ and at $C,A$). So the spiral similarity with centre $T$ taking $A\mapsto C$ also takes $D\mapsto K$, and $K-C=\lambda(D-A)$ with $\lambda=\frac{C-T}{A-T}$.

**Hint 4: The next step**

Use complex numbers with the circumcircle as unit circle. Then $d=b+c-\frac{ac}b$, and you can check that $t=\frac{2bc-ab-ac}{b+c-2a}$ is on the unit circle and on the symmedian.

**Hint 5: The next step**

Compute $\lambda$ and $k$, and compare $|k-m|$ with $|c-m|$ where $m=\frac{b+c}2$.

**Solution**

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

---

## o113 · difficulty 5 · Complex numbers in geometry
*original*

**Statement**

Let $A_1A_2\dots A_n$ be a regular $n$-gon inscribed in a circle of radius $1$ with centre $O$, and let $P$ be any point of the plane with $OP=r$. Prove that
(a) if $n\ge3$, then $\displaystyle\sum_{k=1}^{n}PA_k^4=n\,(r^4+4r^2+1)$;
(b) if $n\ge4$, then $\displaystyle\sum_{k=1}^{n}PA_k^6=n\,(r^6+9r^4+9r^2+1)$.

**Hint 1: What is being asked**

Prove both formulas. In particular, the sums depend on $P$ only through its distance from the centre.

**Hint 2: The technique**

Put the figure in the complex plane, where a regular polygon has a very clean description and distances are easy to expand.

**Hint 3: The key idea**

Take $O=0$, so the vertices are $w_k=\varepsilon\omega^k$ for $k=1,\dots,n$, where $\omega=e^{2\pi i/n}$ and $|\varepsilon|=1$, and $P=p$ with $|p|=r$. Show that $PA_k^2=r^2+1-s_k$ where $s_k=p\bar w_k+\bar p w_k$.

**Hint 4: The next step**

Which sums $\sum_k w_k^m$ vanish, and for which $m$? Compute $\sum_k s_k$, $\sum_k s_k^2$ (and later $\sum_k s_k^3$) by expanding, using $|w_k|=1$.

**Hint 5: The next step**

Then $\sum PA_k^4=\sum(r^2+1-s_k)^2$ and $\sum PA_k^6=\sum(r^2+1-s_k)^3$; expand and substitute.

**Solution**

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

---

## o98 · difficulty 4 · Casework
*original*

**Statement**

Find the number of quadruples $(a,b,c,d)$ of positive integers with $a\le b\le c\le d$ such that
$$\frac1a+\frac1b+\frac1c+\frac1d=1.$$

**Hint 1: What is being asked**

Count the non-decreasing quadruples of positive integers whose reciprocals add up to $1$.

**Hint 2: The technique**

Bound the smallest variable, then let each of its possible values open a smaller problem with fewer unknowns.

**Hint 3: The key idea**

Since $a$ is the smallest, $1=\frac1a+\dots\le\frac4a$. Find the possible values of $a$, and rule out $a=1$.

**Hint 4: The next step**

For each value of $a$, bound $b$ in the same way using the remaining sum $1-\frac1a$ shared by three fractions.

**Hint 5: The next step**

Once $a$ and $b$ are fixed you must solve $\frac1c+\frac1d=\frac pq$. Bound $c$ again and solve for $d$, or use a factoring trick when the right side is a unit fraction $\frac1k$, namely $(c-k)(d-k)=k^2$.

**Solution**

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

---

## m33 · difficulty 7 · Recurrences, Casework
*IMO 2020 Shortlisted Problems (IMO), MathNet 06w4*

**Statement**

Let $n$ be a positive integer. Find the number of permutations $a_1,a_2,\dots,a_n$ of the sequence $1,2,\dots,n$ satisfying
$$a_1\le2a_2\le3a_3\le\dots\le na_n.$$

**Hint 1: What is being asked**

Count the permutations of $1,\dots,n$ for which the products $i\,a_i$ never decrease.

**Hint 2: The technique**

Find where the largest number $n$ can stand. That splits the permutations into cases that reduce to the same question for smaller $n$ ([[recursion]]).

**Hint 3: The key idea**

Compute the answer for $n=1,2,3,4$ and guess.

**Hint 4: The next step**

Let $a_k=n$. Show that if $k\le n-2$, then all of $a_k,a_{k+1},\dots,a_n$ exceed $k$, which is impossible.

**Hint 5: The next step**

So either $a_n=n$, or $a_{n-1}=n$ and then $a_n=n-1$. Check that the remaining conditions are exactly the problem for $n-1$ or $n-2$.

**Solution**

Let $P_n$ be the number of such permutations. Clearly $P_1=1$ and $P_2=2$ (both $1,2$ and $2,1$ work).

**Lemma.** For $n\ge3$, either $a_n=n$, or $a_{n-1}=n$ and $a_n=n-1$.

*Proof.* Let $a_k=n$.
- If $k=n-1$: $(n-1)n=(n-1)a_{n-1}\le na_n$ gives $a_n\ge n-1$, and $a_n\ne n$, so $a_n=n-1$.
- If $k\le n-2$: for $k<i<n$ we have $ia_i\ge ka_k=kn$, so $a_i\ge kn/i>k$. Also $na_n\ge(n-1)a_{n-1}\ge(n-1)(k+1)=nk+(n-1-k)>nk$, so $a_n>k$. Thus the $n-k+1$ distinct numbers $a_k,a_{k+1},\dots,a_n$ all lie in $\{k+1,\dots,n\}$, which has only $n-k$ elements. Contradiction. $\square$

**Counting.** Let $n\ge3$.
- If $a_n=n$, then $a_1,\dots,a_{n-1}$ is a permutation of $1,\dots,n-1$ satisfying the chain up to $(n-1)a_{n-1}$, and the last inequality $(n-1)a_{n-1}\le(n-1)^2<n^2=na_n$ holds automatically. This gives $P_{n-1}$ permutations.
- If $(a_{n-1},a_n)=(n,n-1)$, then $a_1,\dots,a_{n-2}$ is a permutation of $1,\dots,n-2$ satisfying the chain up to $(n-2)a_{n-2}$, and the last two inequalities $(n-2)a_{n-2}\le(n-2)^2<n(n-1)=(n-1)a_{n-1}=na_n$ hold automatically. This gives $P_{n-2}$ permutations.

So $P_n=P_{n-1}+P_{n-2}$ for $n\ge3$, with $P_1=1=F_2$ and $P_2=2=F_3$, where $F_1=F_2=1$, $F_{k+1}=F_k+F_{k-1}$ are the Fibonacci numbers. By induction the answer is $\boxed{P_n=F_{n+1}}$.

---

## o53 · difficulty 3 · Symmetry and WLOG
*original*

**Statement**

Let $f(x)=\dfrac{4^x}{4^x+2}$. Evaluate
$$f\!\left(\tfrac1{100}\right)+f\!\left(\tfrac2{100}\right)+\dots+f\!\left(\tfrac{99}{100}\right).$$

**Hint 1: What is being asked**

Find the exact value of the sum of these $99$ function values.

**Hint 2: The technique**

Pair the terms that are mirror images around the middle of the range and see what each pair adds to.

**Hint 3: The key idea**

The arguments $\frac k{100}$ and $\frac{100-k}{100}$ add up to $1$. Compute $f(x)+f(1-x)$.

**Hint 4: The next step**

Use $4^{1-x}=\dfrac4{4^x}$ to simplify $f(1-x)$. Then count the pairs and don't forget the middle term $k=50$.

**Solution**

First, for any real $x$, using $4^{1-x}=\frac{4}{4^x}$,
$$f(1-x)=\frac{4/4^x}{4/4^x+2}=\frac{4}{4+2\cdot4^x}=\frac2{2+4^x}.$$
Therefore
$$f(x)+f(1-x)=\frac{4^x}{4^x+2}+\frac2{4^x+2}=1.$$

The $99$ terms $k=1,\dots,99$ split into the $49$ pairs $\{k,100-k\}$ for $k=1,\dots,49$, plus the middle term $k=50$. Each pair adds up to $1$, and $f(\tfrac12)=\dfrac{2}{2+2}=\dfrac12$. The sum is
$$49\cdot1+\frac12=\boxed{\dfrac{99}{2}}.$$

---

## o66 · difficulty 3 · AM-GM and mean inequalities
*original*

**Statement**

Positive real numbers $x$ and $y$ satisfy $x+y=12$. Find the maximum possible value of $x^2y$.

**Hint 1: What is being asked**

Find the largest value that $x^2y$ can take, and where it is attained.

**Hint 2: The technique**

Apply the inequality between arithmetic and geometric means to three numbers whose sum is the fixed total $12$ and whose product is a constant multiple of $x^2y$.

**Hint 3: The key idea**

You need three positive terms whose sum is $x+y$ and whose product is proportional to $x^2y$. Two of them should be equal.

**Hint 4: The next step**

Use the three numbers $\frac x2,\frac x2,y$. Their sum is $12$, and equality in AM-GM needs them to be equal.

**Solution**

By AM-GM on the three positive numbers $\frac x2,\frac x2,y$:
$$\frac{\frac x2+\frac x2+y}{3}\ge\sqrt[3]{\frac x2\cdot\frac x2\cdot y}.$$
The left side is $\frac{12}{3}=4$, so $\frac{x^2y}{4}\le4^3=64$ and $x^2y\le256$.

Equality holds when $\frac x2=y$, i.e. $x=2y$; with $x+y=12$ this gives $y=4$, $x=8$, and indeed $8^2\cdot4=256$. The maximum is $\boxed{256}$.

---

## m19 · difficulty 6 · Cauchy–Schwarz and Titu's lemma, AM-GM and mean inequalities
*2008 Shortlist JBMO (JBMO), MathNet 08l7*

**Statement**

Show that
$$(x+y+z)\left(\frac1x+\frac1y+\frac1z\right)\ge4\left(\frac x{xy+1}+\frac y{yz+1}+\frac z{zx+1}\right)^2$$
for all positive real numbers $x,y,z$.

**Hint 1: What is being asked**

Prove the inequality for all positive reals.

**Hint 2: The technique**

Use [[cauchy-schwarz]] to bound the left side from below by a perfect square, and [[am-gm]] to bound each fraction on the right.

**Hint 3: The key idea**

Find an expression whose square sits between the two sides. Try $\sqrt{x/y}+\sqrt{y/z}+\sqrt{z/x}$.

**Hint 4: The next step**

For the left side, apply Cauchy–Schwarz to $(\sqrt x,\sqrt y,\sqrt z)$ and $(1/\sqrt y,1/\sqrt z,1/\sqrt x)$.

**Hint 5: The next step**

For the right side show $\sqrt{x/y}\ge\frac{2x}{xy+1}$ by AM-GM.

**Solution**

Let $S=\sqrt{\frac xy}+\sqrt{\frac yz}+\sqrt{\frac zx}$.

**Left $\ge S^2$.** By Cauchy–Schwarz with the vectors $(\sqrt x,\sqrt y,\sqrt z)$ and $\left(\frac1{\sqrt y},\frac1{\sqrt z},\frac1{\sqrt x}\right)$,
$$(x+y+z)\left(\frac1y+\frac1z+\frac1x\right)\ge\left(\sqrt{\tfrac xy}+\sqrt{\tfrac yz}+\sqrt{\tfrac zx}\right)^2=S^2.$$
**$S\ge$ the bracket.** AM-GM gives $xy+1\ge2\sqrt{xy}$, so
$$\frac{2x}{xy+1}\le\frac{2x}{2\sqrt{xy}}=\sqrt{\frac xy}.$$
Adding the three cyclic versions, $S\ge2\left(\frac x{xy+1}+\frac y{yz+1}+\frac z{zx+1}\right)$, and squaring (both sides positive) gives $S^2\ge4(\dots)^2$.

Combining, the left side is at least $S^2\ge4\left(\frac x{xy+1}+\dots\right)^2$. $\blacksquare$

---

## m12 · difficulty 8 · Graph theory basics, Extremal principle
*Romanian Master of Mathematics (Romania), MathNet 0c8t*

**Statement**

In a country there are $n$ airports and $n$ air companies operating return flights. Each company operates an odd number of flights forming a closed route. Prove that a traveller can complete a closed route consisting of an odd number of flights operated by pairwise distinct companies.

**Hint 1: What is being asked**

Each company's flights form an odd closed route (parallel flights of different companies count as different edges). Show that there is an odd closed route in which no two flights belong to the same company.

**Hint 2: The technique**

Translate to [[graph-theory]]: you have $n$ odd cycles on the same $n$ vertices and want an odd cycle with edges taken from different cycles. Use an [[extremal]] choice: a largest "rainbow" forest.

**Hint 3: The key idea**

Call a set of edges rainbow if no two come from the same company. Take a largest rainbow set of edges containing no cycle.

**Hint 4: The next step**

A forest on $n$ vertices has fewer than $n$ edges, so some company contributes no edge to it. Look at that company's odd cycle.

**Hint 5: The next step**

Show every edge of that cycle joins two vertices in the same tree of the forest, and use that trees are bipartite.

**Solution**

Each company's closed route is an odd cycle on the vertex set of $n$ airports. Call a set of edges *rainbow* if its edges come from different companies. Let $F$ be a rainbow set of edges with no cycle (a rainbow forest) of maximum size.

$F$ has at most $n-1$ edges (it is a forest on $n$ vertices), and its edges come from distinct companies, so some company $C$ has no edge in $F$. Consider the odd cycle of $C$.

No edge $e$ of this cycle joins two different components of $F$ (components include isolated vertices): otherwise $F\cup\{e\}$ would be a larger rainbow forest. So all vertices of the cycle lie in the same component of $F$, a tree $T$. A tree is bipartite: its vertices split into two parts with all tree edges between them. The cycle of $C$ has odd length, so it cannot be properly 2-colored by these parts; hence it has an edge $e$ whose endpoints are in the same part.

The path in $T$ between the endpoints of $e$ has even length (same part), so together with $e$ it forms a cycle of odd length. Its edges are tree edges (from distinct companies) plus $e$ (from $C$, which has no edge in $F$). So it is an odd closed route with pairwise distinct companies. $\blacksquare$

---

## o30 · difficulty 5 · Expectation and probabilistic method
*original*

**Statement**

A fair six-sided die is rolled three times. What is the expected number of distinct values that appear?

**Hint 1: What is being asked**

Find the average number of different faces seen in three rolls.

**Hint 2: The technique**

Use [[expectation]]: linearity of expectation with indicator variables, one per face.

**Hint 3: The key idea**

For each face value $v$, let $I_v=1$ if $v$ appears at least once. The number of distinct values is $\sum_vI_v$.

**Hint 4: The next step**

Compute $P(I_v=1)$ using the complement: $v$ never appears in three rolls. Then add over the six faces.

**Solution**

Let $I_v=1$ if value $v$ shows up at least once, else $0$. The number of distinct values is $\sum_{v=1}^6I_v$, so by linearity the expectation is $6\,P(I_1=1)$.

The probability that $1$ never shows up is $\left(\frac56\right)^3=\frac{125}{216}$, so $P(I_1=1)=\frac{91}{216}$. The expected number is $6\cdot\frac{91}{216}=\boxed{\dfrac{91}{36}}$.

---

## o39 · difficulty 3 · Invariants and monovariants
*original*

**Statement**

The numbers $1,2,\dots,10$ are written on a board. A move consists of erasing two numbers $a$ and $b$ and writing the number $ab+a+b$ in their place. After nine moves, a single number remains. Find this number.

**Hint 1: What is being asked**

Show that the final number does not depend on the order of the moves, and compute it.

**Hint 2: The technique**

Look for a quantity built from the numbers on the board that no move can change.

**Hint 3: The key idea**

Compute $ab+a+b$ for a few small pairs and compare with $a+b$ and $ab$. Try adding $1$ to the result.

**Hint 4: The next step**

Since $ab+a+b+1=(a+1)(b+1)$, consider the product of $(x+1)$ over all numbers $x$ on the board.

**Solution**

Note that $ab+a+b+1=(a+1)(b+1)$. Consider the quantity
$$P=\prod_{x\text{ on the board}}(x+1).$$
A move replaces the factors $(a+1)(b+1)$ by the single factor $(ab+a+b)+1=(a+1)(b+1)$, so $P$ does not change. $P$ is an invariant.

At the start, $P=2\cdot3\cdots11=11!=39916800$. At the end the board holds one number $N$, and $P=N+1$. Therefore $N=11!-1=\boxed{39916799}$, whatever order of moves is used.

---

## m57 · difficulty 7 · Functional equations
*Baltic Way 2011 Problem Shortlist (Baltic Way), MathNet 0182*

**Statement**

Find all functions $f:\mathbb R\to\mathbb R$ such that
$$f(x+f(y))-f(x)=(x+f(y))^3-x^3$$
for all $x,y\in\mathbb R$.

**Hint 1: What is being asked**

Determine every real function for which shifting the argument by any value $f(y)$ changes $f$ by exactly as much as it changes $x\mapsto x^3$.

**Hint 2: The technique**

Subtract the cube: $g(x)=f(x)-x^3$ turns the equation into "every value of $f$ is a period of $g$". Then study the set of periods, which is closed under addition and subtraction.

**Hint 3: The key idea**

Show $g(x+f(y))=g(x)$ for all $x,y$, where $g(x)=f(x)-x^3$.

**Hint 4: The next step**

The periods of $g$ form a group under addition. If $a=f(y_0)\ne0$, then both $f(y)$ and $f(y+a)$ are periods for every $y$. What is their difference?

**Hint 5: The next step**

$(y+a)^3-y^3$ takes every value on a half-line. A group of reals containing a half-line is all of $\mathbb R$.

**Solution**

**Answer:** $f\equiv0$, and $f(x)=x^3+c$ for any real constant $c$.

Let $g(x)=f(x)-x^3$. The equation reads $f(x+f(y))-(x+f(y))^3=f(x)-x^3$, i.e.
$$g(x+f(y))=g(x)\quad\text{for all }x,y.$$
Let $G$ be the set of periods of $g$, i.e. the $p$ with $g(x+p)=g(x)$ for all $x$. If $p,q\in G$ then $g(x+p-q)=g(x-q)=g(x)$, so $p-q\in G$: $G$ is an additive subgroup of $\mathbb R$, and it contains every value of $f$.

If $f\equiv0$, the equation holds ($0=x^3-x^3$). Otherwise pick $y_0$ with $a=f(y_0)\ne0$. For any $y$, both $f(y)$ and $f(y+a)$ lie in $G$, and since $a\in G$ we have $g(y+a)=g(y)$, so
$$f(y+a)-f(y)=(y+a)^3-y^3=3a\left(y+\tfrac a2\right)^2+\tfrac{a^3}4\in G.$$
As $y$ runs over $\mathbb R$ this takes every value in $[\frac{a^3}4,\infty)$ if $a>0$, or in $(-\infty,\frac{a^3}4]$ if $a<0$. So $G$ contains a half-line $H$. For any real $r$, choose $u\in H$ with $u+r\in H$ (take $u$ far enough into the half-line); then $r=(u+r)-u\in G$. Hence $G=\mathbb R$, every real number is a period of $g$, and $g$ is constant, say $g\equiv c$. Thus $f(x)=x^3+c$.

Check: if $f(x)=x^3+c$, then $f(x+f(y))-f(x)=(x+f(y))^3+c-x^3-c=(x+f(y))^3-x^3$. So the solutions are $\boxed{f\equiv0\ \text{ and }\ f(x)=x^3+c\ (c\in\mathbb R)}$.

---

## o20 · difficulty 4 · Extremal principle
*original*

**Statement**

Let $S$ be a finite set of at least two points in the plane. Prove that it is impossible for every point of $S$ to be the midpoint of two other points of $S$.

**Hint 1: What is being asked**

You must show that in any finite set of points, some point is not the midpoint of two other points of the set.

**Hint 2: The technique**

Look at the point that is most extreme in some direction.

**Hint 3: The key idea**

Among the points of $S$, look at those with the largest $x$-coordinate. Pick the one with the largest $y$-coordinate among them.

**Hint 4: The next step**

Suppose this point $P$ is the midpoint of $Q$ and $R$, both in $S$ and different from $P$. Compare the coordinates of $Q$ and $R$ with those of $P$.

**Solution**

Among the points of $S$ take $P=(p,q)$ with the largest $x$-coordinate, and among those the largest $y$-coordinate. Suppose $P$ is the midpoint of two other points $Q=(x_1,y_1)$ and $R=(x_2,y_2)$ of $S$. Then $x_1+x_2=2p$ and $y_1+y_2=2q$.

Since $x_1,x_2\le p$ and $x_1+x_2=2p$, we get $x_1=x_2=p$. Then $Q$ and $R$ have the same $x$-coordinate as $P$, so by the choice of $P$, $y_1,y_2\le q$. With $y_1+y_2=2q$ this gives $y_1=y_2=q$. So $Q=R=P$, contradicting that they are different from $P$. $\blacksquare$

---

## o83 · difficulty 6 · Complex numbers in geometry
*original*

**Statement**

Let $ABCD$ be a convex quadrilateral. On each of its four sides construct a square lying outside the quadrilateral, and let $P,Q,R,S$ be the centers of the squares on $AB,BC,CD,DA$ respectively. Prove that $PR=QS$ and that the lines $PR$ and $QS$ are perpendicular.

**Hint 1: What is being asked**

Show that the segments joining the centers of opposite squares have equal length and are perpendicular.

**Hint 2: The technique**

Treat the plane as the complex numbers, where rotating a vector by $90^\circ$ is multiplication by $i$. Then each center is an explicit expression in the vertices.

**Hint 3: The key idea**

Orient $ABCD$ counterclockwise. The outside of the quadrilateral is then to the right of each directed side $A\to B$, $B\to C$, and so on. Express the center of the square on $AB$ as the midpoint plus half of the vector $\overrightarrow{AB}$ rotated by $-90^\circ$.

**Hint 4: The next step**

With $a,b,c,d$ the complex numbers of the vertices, the center is $p=\frac{(1+i)a+(1-i)b}{2}$, and similarly for $q,r,s$. Compare $s-q$ with $r-p$.

**Solution**

Reflecting the figure if necessary (which preserves lengths and perpendicularity), assume $A,B,C,D$ are in counterclockwise order. Because $ABCD$ is convex, its interior lies to the left of each directed side, and the exterior to the right.

Let $a,b,c,d$ be the complex numbers of the vertices. The square on $AB$ lying to the right of $A\to B$ has its center at distance $\frac{|AB|}{2}$ from the midpoint of $AB$, perpendicular to $AB$ and on the right. Rotating a vector by $-90^\circ$ means multiplying by $-i$, which sends the direction of $\overrightarrow{AB}$ to the right, so
$$p=\frac{a+b}{2}-i\,\frac{b-a}{2}=ua+vb,\qquad u=\frac{1+i}2,\ v=\frac{1-i}2.$$
In the same way $q=ub+vc$, $r=uc+vd$, $s=ud+va$.

Note $iu=\frac{i-1}{2}=-v$ and $iv=\frac{i+1}{2}=u$. Then
$$i(r-p)=i\big(uc+vd-ua-vb\big)=-vc+ud+va-ub=(ud+va)-(ub+vc)=s-q.$$
So $s-q=i(r-p)$: the vector $\overrightarrow{QS}$ is the vector $\overrightarrow{PR}$ rotated by $90^\circ$, so $QS=PR$ and $QS\perp PR$. (We need $P\ne R$ for the lines to be defined. If $p=r$, then $b-d=-i(a-c)$, so $\operatorname{Im}\big((b-d)\overline{(a-c)}\big)=-|a-c|^2<0$; but for a convex counterclockwise quadrilateral this imaginary part is positive, because the diagonals cross.) $\blacksquare$

---

## o64 · difficulty 3 · Generating functions
*original*

**Statement**

Four fair six-sided dice, one red, one blue, one green and one yellow, are rolled. In how many of the $6^4$ equally likely outcomes (the colors keep the dice distinguishable) is the sum of the four numbers equal to $14$?

**Hint 1: What is being asked**

Count the outcomes (ordered quadruples of numbers from $1$ to $6$) whose sum is $14$.

**Hint 2: The technique**

Encode the possible values of one die as a polynomial, so that multiplying polynomials adds the values. Then the answer is a single coefficient.

**Hint 3: The key idea**

One die has generating polynomial $x+x^2+\dots+x^6=x\cdot\frac{1-x^6}{1-x}$. The sum of four dice corresponds to the fourth power. You want the coefficient of $x^{14}$.

**Hint 4: The next step**

Pull out $x^4$, so you need the coefficient of $x^{10}$ in $\left(\frac{1-x^6}{1-x}\right)^4=(1-x^6)^4\cdot(1-x)^{-4}$. Expand each factor.

**Solution**

The number of outcomes with sum $14$ is the coefficient of $x^{14}$ in
$$(x+x^2+\dots+x^6)^4=x^4\frac{(1-x^6)^4}{(1-x)^4}.$$
So we need the coefficient of $x^{10}$ in $(1-x^6)^4(1-x)^{-4}$.

We have $(1-x^6)^4=1-4x^6+6x^{12}-\dots$, and $(1-x)^{-4}=\sum_{m\ge0}\binom{m+3}{3}x^m$. The coefficient of $x^{10}$ is
$$\binom{13}{3}-4\binom{7}{3}+6\cdot 0=286-4\cdot35=146,$$
where the $x^{12}$ term cannot contribute to $x^{10}$. The answer is $\boxed{146}$.

---

## o15 · difficulty 3 · Induction
*original*

**Statement**

Prove that $n!>2^n$ for every integer $n\ge4$.

**Hint 1: What is being asked**

Factorials eventually outgrow powers of $2$. You must prove this from $n=4$ on.

**Hint 2: The technique**

Use [[induction]], starting at $n=4$ (not at $1$).

**Hint 3: The key idea**

Check $n=4$ directly: compare $24$ with $16$.

**Hint 4: The next step**

Assume $n!>2^n$. To get $(n+1)!$ multiply by $n+1$. Compare $n+1$ with $2$.

**Solution**

**Base case.** $4!=24>16=2^4$.

**Step.** Assume $n!>2^n$ for some $n\ge4$. Then
$$(n+1)!=(n+1)\,n!>(n+1)\,2^n\ge2\cdot2^n=2^{n+1},$$
because $n+1\ge5>2$. So the claim holds for $n+1$. $\blacksquare$

---

## m104 · difficulty 7 · Complex numbers in geometry
*THE Fifteenth ROMANIAN MASTER OF MATHEMATICS (Romania), MathNet 0cd9*

**Statement**

Given a triangle $ABC$, let $H$ and $O$ be its orthocentre and circumcentre, respectively. Let $K$ be the midpoint of the segment $AH$. Let $\ell$ be any line through $O$, and let $P$ and $Q$ be the orthogonal projections of $B$ and $C$ onto $\ell$, respectively. Prove that $KP+KQ\ge BC$.

**Hint 1: What is being asked**

Show that the sum of the distances from the midpoint of $AH$ to the feet of the perpendiculars from $B$ and $C$ to any line through the circumcentre is at least $BC$.

**Hint 2: The technique**

Put the circumcircle as the unit circle in the complex plane; the orthocentre, the midpoint $K$ and the projections onto a line through the origin all have short formulas there.

**Hint 3: The key idea**

With $O=0$ and $|a|=|b|=|c|=1$, the orthocentre is $h=a+b+c$, so $k=a+\frac{b+c}2$. If $\ell$ has unit direction $u$, the projection of $z$ onto $\ell$ is $\frac12(z+u^2\bar z)$.

**Hint 4: The next step**

Compute $k-p$ and multiply by $b$ (which does not change the modulus). Do the same for $k-q$ with $c$.

**Hint 5: The next step**

You should get $KP=\frac12|2ab+bc-u^2|$ and $KQ=\frac12|2ac+bc-u^2|$. Now one application of the triangle inequality finishes.

**Solution**

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

---

## m32 · difficulty 8 · Induction, Extremal principle
*IMO 2019 Shortlisted Problems (IMO), MathNet 06va*

**Statement**

You are given a set of $n$ blocks, each weighing at least $1$; their total weight is $2n$. Prove that for every real number $r$ with $0\le r\le2n-2$ you can choose a subset of the blocks whose total weight is at least $r$ but at most $r+2$.

**Hint 1: What is being asked**

With $n$ blocks of weight at least $1$ and total $2n$, show that every interval $[r,r+2]$ with $0\le r\le 2n-2$ contains the weight of some sub-collection.

**Hint 2: The technique**

The statement is awkward to induct on directly. Prove a stronger version by [[induction]] on $n$, removing the heaviest block ([[extremal]]).

**Hint 3: The key idea**

Strengthen: if $n$ blocks of weight at least $1$ have total $s\le2n$, then for every $r\in[-2,s]$ some subset has weight in $[r,r+2]$.

**Hint 4: The next step**

Remove the heaviest block $x$. The rest satisfy the hypothesis with $n-1$ blocks. Which values of $r$ does the induction hypothesis handle, with and without $x$?

**Hint 5: The next step**

You cover $[-2,s-x]$ and $[x-2,s]$. Show $x-2\le s-x$ using $x\le s-(n-1)$ and $s\le2n$.

**Solution**

We prove the stronger **Claim:** if $n\ge1$ blocks each weigh at least $1$ and their total is $s\le2n$, then for every real $r$ with $-2\le r\le s$ some subset (possibly empty) has total weight in $[r,r+2]$.

The problem follows by taking $s=2n$, since $[0,2n-2]\subset[-2,2n]$.

**Base $n=1$.** One block of weight $s$ with $1\le s\le2$. If $-2\le r\le0$, the empty set (weight $0$) works since $r\le0\le r+2$. If $0<r\le s$, the block works since $r\le s\le2<r+2$.

**Step.** Let $n\ge2$ and let $x$ be the largest weight. Then $x\ge s/n$, so the other $n-1$ blocks have total $s-x\le s\frac{n-1}n\le2(n-1)$, and each weighs at least $1$. By the induction hypothesis:
- for every $r\in[-2,s-x]$ some subset of the other blocks has weight in $[r,r+2]$;
- for every $r\in[x-2,s]$ we have $r-x\in[-2,s-x]$, so some subset $T$ of the other blocks has weight in $[r-x,r-x+2]$, and $T$ together with the heavy block has weight in $[r,r+2]$.

These two intervals cover $[-2,s]$ provided $x-2\le s-x$, i.e. $2x\le s+2$. The other $n-1$ blocks weigh at least $n-1$, so $x\le s-(n-1)$. Also $x\le s-(n-1)\le2n-(n-1)=n+1$. Adding, $2x\le s-(n-1)+n+1=s+2$. This completes the induction. $\blacksquare$

---

## o99 · difficulty 4 · Symmetry and WLOG
*original*

**Statement**

A round table has $2024$ chairs placed at equal distances around it. Alice and Bob take turns, Alice first. On a turn, a player seats a guest on an empty chair, subject to the rule that the chair must not be next to a chair that already has a guest (the two neighbours of a chair are the chairs immediately to its left and right). A player who cannot make a move loses. Which player has a winning strategy?

**Hint 1: What is being asked**

Decide who wins this game with best play from both sides, and describe the winning strategy.

**Hint 2: The technique**

Think about what structure of the table one of the players could exploit.

**Hint 3: The key idea**

Number the chairs $0,1,\dots,2023$ around the table. Which chair is exactly opposite chair $x$?

**Hint 4: The next step**

Suppose the player who moves second always answers by taking the chair opposite to the one the opponent just took. Show that this reply is always legal. What do you know about the guests seated before the opponent's move?

**Hint 5: The next step**

For legality you must check three things about the opposite chair $x'$: it is empty, it is not adjacent to an occupied chair, and it is not adjacent to the chair $x$ just taken.

**Solution**

Number the chairs $0,1,\dots,2023$ around the table, with arithmetic modulo $2024$. For a chair $x$ let $x'=x+1012$ be the opposite chair. Then $(x')'=x$, and $x'$ is a neighbour of $y$ exactly when $x$ is a neighbour of $y'$ (shifting everything by $1012$ preserves neighbourhood).

**Bob (the second player) wins.** His strategy: whenever Alice seats a guest on chair $x$, Bob seats a guest on $x'$.

We prove by induction that Bob can always do this legally. Before each of Alice's moves, the set $T$ of occupied chairs is *symmetric*: $y\in T\iff y'\in T$ (at the start $T=\emptyset$, and each round adds $x$ and $x'$ together). Suppose Alice legally takes $x$, so $x\notin T$ and neither neighbour of $x$ is in $T$. We check that $x'$ is legal for Bob, in the position $T\cup\{x\}$:
- $x'$ is empty: $x'\ne x$ because $1012\not\equiv0\pmod{2024}$, and $x'\notin T$ since otherwise $x=(x')'\in T$ by symmetry.
- $x'$ is not adjacent to a chair of $T$: if a neighbour $z$ of $x'$ were in $T$, then $z'\in T$ by symmetry, and $z'$ is a neighbour of $x$, contradicting the legality of Alice's move.
- $x'$ is not adjacent to $x$: that would need $1012\equiv\pm1\pmod{2024}$, which is false.

So Bob's reply is legal, and the occupied set is symmetric again. Every move of Alice is thus followed by a legal move of Bob. The game is finite (at most $2024$ guests), so it ends, and the player who cannot move must be Alice (Bob always has a move after Alice's). Hence Bob wins: $\boxed{\text{the second player (Bob)}}$.

---

## o13 · difficulty 3 · Polynomials and Vieta
*original*

**Statement**

The quadratic $x^2-5x+k$ has two roots $r$ and $s$ with $r^2+s^2=13$. Find $k$.

**Hint 1: What is being asked**

Find the constant term $k$ so that the sum of the squares of the roots is $13$.

**Hint 2: The technique**

This uses [[polynomials|Vieta's formulas]], which relate the roots to the coefficients without finding the roots.

**Hint 3: The key idea**

Express $r+s$ and $rs$ using the coefficients of the quadratic.

**Hint 4: The next step**

Write $r^2+s^2$ in terms of $r+s$ and $rs$.

**Solution**

By Vieta, $r+s=5$ and $rs=k$. Then
$$r^2+s^2=(r+s)^2-2rs=25-2k.$$
Setting $25-2k=13$ gives $k=\boxed{6}$. (Check: $x^2-5x+6$ has roots $2,3$, and $4+9=13$.)

---

## m58 · difficulty 8 · Functional equations
*48th International Mathematical Olympiad Vietnam 2007 Shortlisted Problems with Solutions (IMO), MathNet 06p9*

**Statement**

Find all functions $f:\mathbb R^+\to\mathbb R^+$ such that
$$f(x+f(y))=f(x+y)+f(y)$$
for all $x,y\in\mathbb R^+$. ($\mathbb R^+$ denotes the set of positive real numbers.)

**Hint 1: What is being asked**

Determine every function from the positive reals to the positive reals satisfying the equation.

**Hint 2: The technique**

First show $f(y)>y$, then study $g(y)=f(y)-y>0$.

**Hint 3: The key idea**

If $f(y)<y$, put $x=y-f(y)$. If $f(y)=y$, compare both sides directly.

**Hint 4: The next step**

With $g(y)=f(y)-y$ and $t=x+y$, show $g(t+g(y))=g(t)+y$ for all $t>y>0$. Deduce that $g$ is injective.

**Hint 5: The next step**

For $t>u+v$ compute $g(t+g(u)+g(v))$ in two steps and compare with $g(t+g(u+v))$. This gives additivity; then show $g(g(y))=y$.

**Solution**

**Answer:** $f(x)=2x$.

**Step 1: $f(y)>y$.** Since $f(y)>0$, the equation gives $f(x+f(y))>f(x+y)$ for all $x$. If $f(y)=y$ this reads $f(x+y)>f(x+y)$, impossible. If $f(y)<y$, put $x=y-f(y)>0$: then $f(y)=f(x+f(y))=f(2y-f(y))+f(y)>f(y)$, impossible. So $f(y)>y$.

**Step 2.** Let $g(y)=f(y)-y>0$. For $t>y>0$ put $x=t-y>0$ in the equation: $f(t-y+f(y))=f(t)+f(y)$, i.e. $f(t+g(y))=f(t)+f(y)$. Writing $f=g+\mathrm{id}$:
$$g(t+g(y))+t+g(y)=g(t)+t+g(y)+y,\quad\text{so}\quad g(t+g(y))=g(t)+y\quad(t>y>0).\tag{1}$$
**Injective.** If $g(y_1)=g(y_2)$, take $t>\max(y_1,y_2)$; (1) gives $g(t)+y_1=g(t)+y_2$, so $y_1=y_2$.

**Additive.** Let $u,v>0$ and $t>u+v$. Applying (1) with $(t+g(u),v)$ (valid as $t+g(u)>v$) and then with $(t,u)$:
$$g(t+g(u)+g(v))=g(t+g(u))+v=g(t)+u+v.$$
Also (1) with $(t,u+v)$ gives $g(t+g(u+v))=g(t)+u+v$. By injectivity $t+g(u)+g(v)=t+g(u+v)$, so $g(u+v)=g(u)+g(v)$. Since $g>0$, this implies $g$ is strictly increasing: $g(u+v)>g(u)$.

**Involution.** By (1) and additivity, $g(t)+y=g(t+g(y))=g(t)+g(g(y))$ for $t>y$, so $g(g(y))=y$ for all $y$.

**Conclusion.** If $g(x)>x$ for some $x$, then since $g$ is increasing, $x=g(g(x))>g(x)$, a contradiction. If $g(x)<x$, then $x=g(g(x))<g(x)$, again a contradiction. So $g(x)=x$ and $f(x)=2x$.

Check: $f(x+f(y))=2x+4y$ and $f(x+y)+f(y)=2x+2y+2y=2x+4y$. The only solution is $\boxed{f(x)=2x}$.

---

## m40 · difficulty 6 · Symmetry and WLOG
*Baltic Way (Baltic Way), MathNet 01bf*

**Statement**

Two players play a game on an $N\times N$ board. The players alternately mark a cell in such a way that there is never a diagonal on the board containing two marked cells. A player who cannot move loses. For which $N>0$ does the starting player have a winning strategy?

**Hint 1: What is being asked**

A diagonal means any line of cells parallel to one of the two main diagonals. Players alternately mark cells so that no diagonal (of either direction) ever holds two marks; whoever cannot move loses. For which $N$ does the first player win?

**Hint 2: The technique**

Use a mirror strategy ([[symmetry]]): one player answers each move by its image under a suitable symmetry of the board. Choose the symmetry depending on the parity of $N$.

**Hint 3: The key idea**

The game is finite, so a player who can always answer wins.

**Hint 4: The next step**

For even $N$, let the second player copy each move in the vertical mid-line of the board. Why is the copy always legal?

**Hint 5: The next step**

For odd $N$, the first player takes the centre and then answers with the point reflection in the centre.

**Solution**

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

---

## m13 · difficulty 6 · Angle chasing and cyclic quadrilaterals
*Estonian Mathematical Olympiad (Estonia), MathNet 05cw*

**Statement**

In an isosceles triangle $ABC$ with $AB=AC$, the bisector of the angle $BAC$ intersects $BC$ at $D$. The bisector of the angle $ABC$ intersects the perpendicular bisector of $AD$ at $E$. Prove that the bisector of the angle $ACB$ is perpendicular to $DE$.

**Hint 1: What is being asked**

Show that the line $DE$ meets the bisector from $C$ at a right angle.

**Hint 2: The technique**

First prove $A,B,D,E$ are concyclic, then chase angles at $D$ and at the incenter.

**Hint 3: The key idea**

In an isosceles triangle the bisector $AD$ is also an altitude, so $\angle ADB=90^\circ$. Which circle passes through $A,B,D$?

**Hint 4: The next step**

Let the bisector of $\angle ABC$ meet that circle again at $E'$. Show $E'A=E'D$, so $E'=E$.

**Hint 5: The next step**

Let $I$ be the incenter, on $AD$. Compute $\angle EDI$ using the circle and $\angle CID$ in the right triangle $CDI$, and add them.

**Solution**

Let $\gamma=\angle ABC=\angle ACB$. Since $AB=AC$, the bisector $AD$ is also the altitude, so $\angle ADB=90^\circ$ and $A,B,D$ lie on the circle $\omega$ with diameter $AB$. The incenter $I$ lies on $AD$.

Let the bisector of $\angle ABC$ meet $\omega$ again at $E'$. Since $BE'$ bisects $\angle ABD$, the arcs $AE'$ and $E'D$ are equal, so $E'A=E'D$ and $E'$ is on the perpendicular bisector of $AD$. This line meets $BI$ in one point, so $E'=E$. Thus $ABDE$ is cyclic, with $E$ the midpoint of arc $AD$ not containing $B$, so $E$ and $C$ lie on the same side of $AD$.

Now $\angle EDI=\angle EDA=\angle EBA=\frac\gamma2$ (inscribed angles on arc $EA$). In the right triangle $CDI$, $\angle DCI=\frac\gamma2$ because $CI$ bisects $\angle ACB$, so $\angle CID=90^\circ-\frac\gamma2$.

Since $\angle IDC=90^\circ$ and $E$ is on the same side of $AD$ as $C$ with $\angle EDI=\frac\gamma2<90^\circ$, the ray $DE$ lies inside the right angle $IDC$, so it meets segment $IC$ at a point $X$. In triangle $DIX$ the angles at $D$ and $I$ are $\frac\gamma2$ and $90^\circ-\frac\gamma2$, so the angle at $X$ is $90^\circ$. Hence $CI\perp DE$. $\blacksquare$

---

## o38 · difficulty 4 · Pigeonhole principle, Constructive arguments
*original*

**Statement**

Find the smallest positive integer $n$ with the following property: every $n$-element subset of $\{1,2,\dots,20\}$ contains two numbers whose difference is exactly $3$.

**Hint 1: What is being asked**

Find the least $n$ such that any $n$ numbers chosen from $1$ to $20$ must include a pair differing by $3$.

**Hint 2: The technique**

Organise the numbers into groups in which the forbidden pairs have a simple structure, and see how many you can take from each group.

**Hint 3: The key idea**

Write $1,\dots,20$ in three lists according to the remainder mod $3$, each in increasing order. A pair differing by $3$ is a pair of neighbours in one list.

**Hint 4: The next step**

A list of length $7$ can be cut into three pairs of neighbours and one leftover element. How many elements of the list can you keep without two neighbours? Then build an example that shows the bound is sharp.

**Solution**

Split $\{1,\dots,20\}$ by remainder mod $3$ into three chains:
$$A:\ 1,4,7,10,13,16,19\ (7),\quad B:\ 2,5,8,11,14,17,20\ (7),\quad C:\ 3,6,9,12,15,18\ (6).$$
Two numbers differ by exactly $3$ if and only if they are neighbours in the same chain.

**A subset with no such pair has at most $11$ elements.** Cut chain $A$ into the boxes $\{1,4\},\{7,10\},\{13,16\},\{19\}$. A box of two neighbours holds at most one element of the subset, so at most $3+1=4$ elements of $A$ are chosen. The same boxes work for $B$: at most $4$. Chain $C$ splits into three pairs, so at most $3$. In total at most $4+4+3=11$.

Hence any $12$ numbers contain two differing by $3$.

**$11$ is attained.** Take $1,7,13,19$ from $A$, $2,8,14,20$ from $B$, and $3,9,15$ from $C$. Within a chain these are non-neighbours, and numbers in different chains have different remainders mod $3$, so no difference equals $3$. So an $11$-element subset without the property exists, and $n\ge12$.

Therefore the answer is $\boxed{12}$.

---

## m07 · difficulty 6 · AM-GM and mean inequalities
*Junior Balkan Mathematical Olympiad Shortlist (JBMO), MathNet 08mq*

**Statement**

Let $x_i>1$ for all $i\in\{1,2,\dots,2011\}$. Prove the inequality
$$\sum_{i=1}^{2011}\frac{x_i^2}{x_{i+1}-1}\ge8044,$$
where $x_{2012}=x_1$. When does equality hold?

**Hint 1: What is being asked**

Prove the cyclic inequality and find the equality case.

**Hint 2: The technique**

Use [[am-gm]] twice: once to bound each numerator from below by a multiple of $x_i-1$, and once on a cyclic product that telescopes to $1$.

**Hint 3: The key idea**

Compare $x_i^2$ with $4(x_i-1)$. What square is involved?

**Hint 4: The next step**

After that replacement, the sum has terms $\frac{x_i-1}{x_{i+1}-1}$. What is the product of all of them?

**Solution**

For every $i$, $(x_i-2)^2\ge0$ gives $x_i^2\ge4(x_i-1)$. All denominators are positive, so
$$\sum\frac{x_i^2}{x_{i+1}-1}\ge4\sum_{i=1}^{2011}\frac{x_i-1}{x_{i+1}-1}.$$
The $2011$ positive numbers $\frac{x_i-1}{x_{i+1}-1}$ have product $1$ (it telescopes around the cycle), so by AM-GM their sum is at least $2011$. Hence the original sum is at least $4\cdot2011=8044$.

Equality needs $x_i=2$ for every $i$ (from the first step), and then every ratio is $1$, so the second step is also tight. Equality holds exactly when all $x_i=2$.

---

## o06 · difficulty 2 · AM-GM and mean inequalities
*original*

**Statement**

For positive real $x$, what is the minimum value of $x+\dfrac9x$?

**Hint 1: What is being asked**

Over all positive $x$, find the smallest value that $x+\frac9x$ can take.

**Hint 2: The technique**

The two terms multiply to a constant.

**Hint 3: The key idea**

Apply the inequality "arithmetic mean $\ge$ geometric mean" to the two positive numbers $x$ and $\frac9x$.

**Hint 4: The next step**

Compute their product. Then find the $x$ at which the two terms are equal, and check that the bound is actually reached.

**Solution**

By AM-GM, $\dfrac{x+\frac9x}{2}\ge\sqrt{x\cdot\frac9x}=3$, so $x+\frac9x\ge6$.

Equality holds when $x=\frac9x$, i.e. $x=3$, which is allowed. So the minimum is $\boxed{6}$.

---

## o36 · difficulty 3 · Modular arithmetic, Casework
*original*

**Statement**

Find all primes $p$ such that $8p^2+1$ is also prime.

**Hint 1: What is being asked**

Find every prime $p$ for which $8p^2+1$ is prime too.

**Hint 2: The technique**

Use [[modular-arithmetic]] with [[casework]]: look at $p$ modulo $3$.

**Hint 3: The key idea**

Check $p=2$ and $p=3$ directly. What is $8p^2+1$ mod $3$ for a prime $p\neq3$?

**Hint 4: The next step**

If $3\nmid p$ then $p^2\equiv1\pmod3$. Deduce that $3\mid8p^2+1$.

**Solution**

If $p=3$: $8\cdot9+1=73$, which is prime. ✓

If $p\ne3$: then $p^2\equiv1\pmod3$ (as $p\equiv\pm1$), so $8p^2+1\equiv8+1=9\equiv0\pmod3$. And $8p^2+1>3$, so it is composite. (This includes $p=2$: $33=3\cdot11$.)

So the only such prime is $\boxed{p=3}$.

---

## m38 · difficulty 7 · Casework, Divisibility and gcd
*Benelux Mathematical Olympiad (Benelux Mathematical Olympiad), MathNet 020b*

**Statement**

Find all positive integers $n>1$ with the following property: for each two positive divisors $k,\ell<n$ of $n$, at least one of the numbers $2k-\ell$ and $2\ell-k$ is a (not necessarily positive) divisor of $n$ as well.

**Hint 1: What is being asked**

Find all $n>1$ such that for any proper positive divisors $k,\ell$ of $n$, one of $2k-\ell$, $2\ell-k$ divides $n$ (negative divisors allowed; $0$ never divides $n$).

**Hint 2: The technique**

Apply the condition to cleverly chosen pairs, starting with $1$ and the largest proper divisor, and split into cases ([[casework]]) using [[divisibility]].

**Hint 3: The key idea**

Primes work. For composite $n$ let $p$ be its smallest prime factor and $m=n/p$, the largest proper divisor. Apply the condition to $(1,m)$.

**Hint 4: The next step**

$2m-1$ lies strictly between $m$ and $n$, so it is not a divisor. Deduce $m-2\mid 2p$.

**Hint 5: The next step**

Go through $m-2\in\{1,2,p,2p\}$; in the case $m=p+2$ use the pair $(1,p)$. Finally test the few candidates.

**Solution**

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

---

## m70 · difficulty 7 · Coordinate geometry, Symmetry and WLOG
*The 16th Japanese Mathematical Olympiad - The First Round (Japan), MathNet 08rn*

**Statement**

The triangle $ABC$ satisfies $BC=5$, $CA=7$ and $AB=8$. Let $O$ be a point inside the triangle $ABC$ such that the triangles $OBC$, $OCA$ and $OAB$ have the same circumradius. Find this common circumradius.

**Hint 1: What is being asked**

A point inside the $5$-$7$-$8$ triangle makes the three triangles it forms with the sides have equal circumradii. Find that radius.

**Hint 2: The technique**

Use vectors (or complex coordinates). Two circles of equal radius through the same two points have centres symmetric about the midpoint of those points; this lets you write $A,B,C$ in terms of $O$ and the three centres.

**Hint 3: The key idea**

Let $O_1,O_2,O_3$ be the circumcentres of $OBC,OCA,OAB$ and $\rho$ the common radius. $O_1$ and $O_2$ are both at distance $\rho$ from $O$ and from $C$. Show $O_1+O_2=O+C$ as vectors.

**Hint 4: The next step**

So $C=O_1+O_2-O$, and similarly for $A$ and $B$. Find a point at distance $\rho$ from all of $A,B,C$.

**Hint 5: The next step**

Conclude $\rho$ is the circumradius of $ABC$; compute it, and check that a valid $O$ exists.

**Solution**

**Answer:** $\dfrac{7\sqrt3}3$.

Let $\rho$ be the common circumradius and $O_1,O_2,O_3$ the circumcentres of $OBC,OCA,OAB$. Treat points as vectors.

**$O_1\ne O_2$.** Otherwise the circles $OBC$ and $OCA$ coincide (same centre and radius), so $A,B,C,O$ lie on one circle, the circumcircle of $ABC$. But a point strictly inside the triangle is strictly inside its circumcircle. So $O_1\ne O_2$, and likewise the three centres are distinct.

**Expressing the vertices.** $O_1$ and $O_2$ are two different points at distance $\rho$ from both $O$ and $C$, so they are the two intersection points of the circles of radius $\rho$ about $O$ and about $C$. These two intersection points are symmetric about the midpoint of $OC$ (the configuration is symmetric in the line $OC$ and in the perpendicular bisector of $OC$). Hence $O_1+O_2=O+C$, i.e. $C=O_1+O_2-O$. Similarly $A=O_2+O_3-O$ and $B=O_3+O_1-O$.

**The circumradius.** Let $K=O_1+O_2+O_3-2O$. Then $K-A=O_1-O$, $K-B=O_2-O$, $K-C=O_3-O$, all of length $\rho$. So $K$ is the circumcentre of $ABC$ and $\rho$ equals its circumradius $R$.

**Computing $R$.** By the law of cosines, $\cos B=\frac{8^2+5^2-7^2}{2\cdot8\cdot5}=\frac12$, so $B=60^\circ$ and $R=\frac{CA}{2\sin B}=\frac7{\sqrt3}=\frac{7\sqrt3}3$.

**Existence.** The triangle is acute ($5^2+7^2>8^2$), so its orthocentre $H$ lies inside it. Since $\angle BHC=180^\circ-\angle A$, the circumradius of $HBC$ is $\frac{BC}{2\sin\angle BHC}=\frac{a}{2\sin A}=R$, and likewise for $HCA$ and $HAB$. So $O=H$ is such a point, and the common circumradius is $\boxed{\tfrac{7\sqrt3}{3}}$.

---

## m03 · difficulty 7 · Extremal principle, Graph theory basics, Pigeonhole principle
*53. Bulgarian Mathematical Olympiad (Bulgaria), MathNet 032t*

**Statement**

Let $m\ge3$ and $n\ge2$ be integers. Prove that in a group of $N=mn-n+1$ people such that there are two familiar people among any $m$, there is a person who is familiar with $n$ people. Does the statement remain true if $N<mn-n+1$?

**Hint 1: What is being asked**

Among $N$ people, any $m$ contain an acquainted pair. Show someone knows at least $n$ people, and decide whether that still holds for smaller groups.

**Hint 2: The technique**

Model the group as a graph ([[graph-theory]]) and use an [[extremal]] choice: take the largest set of people who all pairwise do not know each other.

**Hint 3: The key idea**

The condition says there are never $m$ mutual strangers. Take a largest group of mutual strangers, of size $l\le m-1$.

**Hint 4: The next step**

By maximality, every outside person knows someone in the group. Count how many outside people the members of the group know in total, and use pigeonhole.

**Hint 5: The next step**

For the second question, try $m-1$ cliques of people who know exactly their own clique.

**Solution**

Take a largest set $S$ of people who pairwise do not know each other, with $|S|=l$. Among any $m$ people two know each other, so $l\le m-1$.

By maximality of $S$, each of the other $N-l$ people knows at least one member of $S$ (otherwise we could add them). So the members of $S$ together know at least $N-l$ people outside $S$, and by pigeonhole one member knows at least $\frac{N-l}{l}=\frac Nl-1$ of them. Since $l\le m-1$,
$$\frac Nl-1\ge\frac{mn-n+1}{m-1}-1=n-1+\frac1{m-1}>n-1.$$
The number of people known is an integer greater than $n-1$, so it is at least $n$.

**Smaller $N$: not true.** Let $N\le(m-1)n$. Split the people into $m-1$ groups of at most $n$ people each, where people know exactly those in their own group. Among any $m$ people two lie in the same group (pigeonhole), so they know each other. But everyone knows at most $n-1$ people. So the statement fails for $N\le(m-1)n=mn-n$, i.e. for every $N<mn-n+1$.

---

## o74 · difficulty 3 · Divisibility and gcd
*original*

**Statement**

Find all positive integers $n$ such that $n+3$ divides $n^2+3$.

**Hint 1: What is being asked**

List every positive integer $n$ for which $n^2+3$ is a multiple of $n+3$.

**Hint 2: The technique**

Reduce the numerator modulo the divisor, so that the question becomes whether $n+3$ divides a fixed number.

**Hint 3: The key idea**

Write $n^2+3=(n+3)(n-3)+r$ for a constant $r$. What is $r$?

**Hint 4: The next step**

Then $n+3$ divides $n^2+3$ exactly when it divides $r$. List the divisors of $r$ that are at least $4$.

**Solution**

Since $n^2-9=(n+3)(n-3)$, we have $n^2+3=(n+3)(n-3)+12$. Thus $n+3\mid n^2+3$ if and only if $n+3\mid12$.

For positive $n$, $n+3\ge4$. The divisors of $12$ that are at least $4$ are $4,6,12$, giving $n=1,3,9$.

Check: $n=1$: $4\mid4$. $n=3$: $6\mid12$. $n=9$: $12\mid84$. The answer is $\boxed{n=1,\,3,\,9}$.

---

## m54 · difficulty 7 · Cauchy–Schwarz and Titu's lemma, Double counting
*North Macedonia (North Macedonia), MathNet 0ag3*

**Statement**

Let $p_1,p_2,\dots,p_{2009}$ be positive real numbers. Prove the inequality
$$\sum_{i=1}^{2009}\frac{p_i}{p_{i+1}+p_{i+2}+\dots+p_{i+1004}}\ge\frac{2009}{1004},$$
where the indices are taken modulo $2009$.

**Hint 1: What is being asked**

Each $p_i$ is divided by the sum of the next $1004$ numbers around the circle. Show the total is at least $\frac{2009}{1004}$.

**Hint 2: The technique**

Turn each fraction into a square over a product and apply Cauchy-Schwarz in Engel form. The denominator that appears can be identified exactly by counting pairs ([[double-counting]]).

**Hint 3: The key idea**

Write $\frac{p_i}{S_i}=\frac{p_i^2}{p_iS_i}$, where $S_i$ is the denominator, and apply Engel form.

**Hint 4: The next step**

In $\sum_ip_iS_i$, each product $p_ip_j$ with $i\ne j$ appears how many times? Think about the two "distances" from $i$ to $j$ and from $j$ to $i$ around the circle.

**Hint 5: The next step**

You need $\big(\sum p_i\big)^2\ge\frac{2009}{1004}\sum_{i<j}p_ip_j$. Compare $\sum_{i<j}p_ip_j$ with $\sum p_i^2$.

**Solution**

Let $S_i=p_{i+1}+\dots+p_{i+1004}$ (indices mod $2009$), $T=\sum p_i$ and $e=\sum_{i<j}p_ip_j$. By Cauchy-Schwarz in Engel form,
$$\sum_i\frac{p_i}{S_i}=\sum_i\frac{p_i^2}{p_iS_i}\ge\frac{T^2}{\sum_ip_iS_i}.$$
**The denominator equals $e$.** $\sum_ip_iS_i$ is the sum of $p_ip_j$ over ordered pairs $(i,j)$ with $j-i\equiv d\pmod{2009}$ for some $d\in\{1,\dots,1004\}$. For an unordered pair $\{i,j\}$ with $i\ne j$, the residues of $j-i$ and $i-j$ lie in $\{1,\dots,2008\}$ and add to $2009$, so exactly one of them lies in $\{1,\dots,1004\}$. Hence each unordered pair is counted exactly once, and $\sum_ip_iS_i=e$.

**Comparison.** From $\sum_{i<j}(p_i-p_j)^2\ge0$ we get $2008\sum p_i^2\ge2e$, i.e. $\sum p_i^2\ge\frac{e}{1004}$. Therefore
$$T^2=\sum p_i^2+2e\ge\frac e{1004}+2e=\frac{2009}{1004}\,e.$$
Combining, $\sum_i\frac{p_i}{S_i}\ge\frac{T^2}{e}\ge\frac{2009}{1004}$. (Equality holds when all $p_i$ are equal: each term is then $\frac1{1004}$.) $\blacksquare$

---

## o56 · difficulty 3 · Double counting
*original*

**Statement**

At a camp there are $15$ students. The staff splits them into teams of three students each (a student may be on several teams) in such a way that every pair of students is together on exactly one team. How many teams are there?

**Hint 1: What is being asked**

Find the total number of teams.

**Hint 2: The technique**

Count, in two different ways, the pairs consisting of a student and a team that student is on. First find how many teams one student is on.

**Hint 3: The key idea**

Fix a student $S$. Each of the other $14$ students shares exactly one team with $S$. How many other students does one team containing $S$ include?

**Hint 4: The next step**

Once you know how many teams each student is on, count all (student, team) memberships in two ways: by students and by teams.

**Solution**

Fix a student $S$. Each of the other $14$ students is on exactly one team with $S$, and each team containing $S$ has exactly $2$ other students. So the teams containing $S$ partition the other $14$ students into pairs: $S$ is on $14/2=7$ teams.

Now count the pairs (student, team on which the student plays) in two ways. Each of the $15$ students is on $7$ teams, giving $15\cdot7=105$ pairs. Each team has $3$ students, so with $T$ teams there are $3T$ pairs. Hence $3T=105$ and $T=\boxed{35}$.

(Such a system of teams exists: take the $15$ nonzero vectors of $\mathbb F_2^4$ as students and the triples $\{a,b,a+b\}$ as teams.)

---

## o77 · difficulty 5 · Diophantine equations, Modular arithmetic
*original*

**Statement**

Find all pairs $(a,b)$ of non-negative integers with $3^a-2^b=1$.

**Hint 1: What is being asked**

Determine every pair of non-negative integers $(a,b)$ satisfying the equation.

**Hint 2: The technique**

Handle small exponents directly. For large $b$, look at the equation modulo $4$ to learn about the parity of $a$, which lets you factor.

**Hint 3: The key idea**

Check $a=0$, $b=0$ and $b=1$ by hand. For $b\ge2$, what is $3^a$ modulo $4$, and what does that force about $a$?

**Hint 4: The next step**

If $a=2k$, then $2^b=3^{2k}-1=(3^k-1)(3^k+1)$. Both factors are divisors of a power of $2$, so both are powers of $2$. Which two powers of $2$ differ by $2$?

**Solution**

Rewrite as $3^a=2^b+1$.

*Small cases.* If $a=0$ then $2^b=0$, impossible. If $b=0$ then $3^a=2$, impossible. If $b=1$ then $3^a=3$, so $a=1$: the pair $(1,1)$.

*Case $b\ge2$.* Then $3^a=2^b+1\equiv1\pmod4$. Since $3^a\equiv(-1)^a\pmod 4$, $a$ is even; and $a\ge2$ because $3^a\ge5$. Write $a=2k$ with $k\ge1$. Then
$$2^b=3^{2k}-1=(3^k-1)(3^k+1).$$
Both factors are positive divisors of $2^b$, hence powers of $2$: say $3^k-1=2^s$, $3^k+1=2^t$ with $t>s$. Subtracting, $2^t-2^s=2$, so $2^s(2^{t-s}-1)=2$. As $2^{t-s}-1$ is odd and positive, $2^{t-s}-1=1$ and $2^s=2$: $s=1$, $t=2$. So $3^k=3$, $k=1$, $a=2$, and $2^b=8$, $b=3$.

The solutions are $\boxed{(a,b)=(1,1)\text{ and }(2,3)}$. (Check: $3-2=1$, $9-8=1$.)

---

## m62 · difficulty 6 · Polynomials and Vieta
*Benelux Mathematical Olympiad (Benelux Mathematical Olympiad), MathNet 01zv*

**Statement**

Find all polynomials $p(x)$ with real coefficients such that
$$p(a+b-2c)+p(b+c-2a)+p(c+a-2b)=3p(a-b)+3p(b-c)+3p(c-a)$$
for all $a,b,c\in\mathbb R$.

**Hint 1: What is being asked**

Determine every real polynomial satisfying the identity for all real $a,b,c$.

**Hint 2: The technique**

Specialize the variables to get a one-variable identity $p(-2x)=p(x)+3p(-x)$, and compare coefficients of each power of $x$.

**Hint 3: The key idea**

Put $a=b=c$, then put $b=c=0$.

**Hint 4: The next step**

In $p(-2x)=p(x)+3p(-x)$, the coefficient of $x^k$ gives $(-2)^k a_k=(1+3(-1)^k)a_k$. For which $k$ can $a_k\ne0$?

**Solution**

**Answer:** $p(x)=\alpha x^2+\beta x$ with $\alpha,\beta\in\mathbb R$.

**Necessity.** With $a=b=c$ we get $3p(0)=9p(0)$, so $p(0)=0$. With $b=c=0$ the arguments on the left are $a,-2a,a$ and on the right $a,0,-a$, so
$$p(-2a)+2p(a)=3p(a)+3p(0)+3p(-a),\quad\text{i.e.}\quad p(-2x)=p(x)+3p(-x)$$
for all $x$. Let $p(x)=\sum a_kx^k$. Comparing coefficients of $x^k$: $(-2)^ka_k=(1+3(-1)^k)a_k$. For even $k$ this says $2^k=4$ or $a_k=0$, so $a_k=0$ unless $k=2$. For odd $k$ it says $-2^k=-2$ or $a_k=0$, so $a_k=0$ unless $k=1$. Hence $p(x)=\alpha x^2+\beta x$.

**Sufficiency.** The condition is linear in $p$, so check $x$ and $x^2$. For $p(x)=x$ both sides are $0$, since the three arguments on each side add to $0$. For $p(x)=x^2$:
$$(a+b-2c)^2+(b+c-2a)^2+(c+a-2b)^2=6(a^2+b^2+c^2)-6(ab+bc+ca),$$
$$3\big((a-b)^2+(b-c)^2+(c-a)^2\big)=6(a^2+b^2+c^2)-6(ab+bc+ca).$$
So the solutions are $\boxed{p(x)=\alpha x^2+\beta x}$.

---

## o95 · difficulty 5 · Coloring arguments, Constructive arguments
*original*

**Statement**

Number the rows and columns of a $7\times7$ board $1,2,\dots,7$. Sixteen non-overlapping $1\times3$ tiles are placed on the board, each covering three cells in a row or three cells in a column, so that exactly one cell is left uncovered. Determine all cells that can be the uncovered cell.

**Hint 1: What is being asked**

Find every cell (row, column) of the board that can be the single uncovered cell in such a placement of sixteen tiles.

**Hint 2: The technique**

Colour the cells so that every tile covers a known pattern of colours, then compare with the colour counts of the board. You also need to show that each cell you allow really occurs.

**Hint 3: The key idea**

Colour the cell in row $i$ and column $j$ by the remainder of $i+j$ modulo $3$. What colours does one tile cover, horizontal or vertical?

**Hint 4: The next step**

Count how many cells of each colour the board has. Sixteen tiles cover equally many cells of each colour, so the uncovered cell has a colour that is determined by the counts.

**Hint 5: The next step**

Repeat with the remainder of $i-j$ modulo $3$ and combine the two conditions. Then show, with explicit tilings, that all the cells you found are possible. Symmetry reduces the number of tilings to draw.

**Solution**

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

---

## m23 · difficulty 4 · Cauchy–Schwarz and Titu's lemma
*Estonian Mathematical Olympiad (Estonia), MathNet 05bw*

**Statement**

Anna, Berta and Carol make fruit drinks from syrup. Anna makes $a$ litres of drink by mixing water and syrup in the proportion of $a:1$. Berta makes $b$ litres of drink by mixing water and syrup in the proportion of $b:1$. Carol makes $c$ litres of drink by mixing water and syrup in the proportion of $c:1$. (It is not known if $a$, $b$ and $c$ are integers.) They make $6$ litres of drink in total. Prove that they use at most $2$ litres of syrup.

**Hint 1: What is being asked**

Translate to an inequality in $a,b,c$ with $a+b+c=6$ and prove it.

**Hint 2: The technique**

After translating, apply [[cauchy-schwarz]] (Titu's form) to the sum of reciprocals.

**Hint 3: The key idea**

In $a$ litres of drink with water : syrup $=a:1$, what fraction is syrup? So how much syrup is in Anna's drink?

**Hint 4: The next step**

You want $\sum\frac a{a+1}\le2$. Rewrite it using $\frac a{a+1}=1-\frac1{a+1}$.

**Hint 5: The next step**

Apply Titu's lemma to $\sum\frac1{a+1}$ with $\sum(a+1)=9$.

**Solution**

In Anna's drink the syrup is $\frac1{a+1}$ of the volume, so she uses $\frac a{a+1}$ litres of syrup; similarly for the others. We must show that $a+b+c=6$ with $a,b,c>0$ implies
$$\frac a{a+1}+\frac b{b+1}+\frac c{c+1}\le2.$$
Since $\frac a{a+1}=1-\frac1{a+1}$, this is equivalent to $\frac1{a+1}+\frac1{b+1}+\frac1{c+1}\ge1$. By Cauchy–Schwarz (Titu's lemma),
$$\frac1{a+1}+\frac1{b+1}+\frac1{c+1}\ge\frac{(1+1+1)^2}{(a+1)+(b+1)+(c+1)}=\frac9{6+3}=1.\ \blacksquare$$

---

## o97 · difficulty 5 · Graph theory basics, Extremal principle
*original*

**Statement**

A country has several cities, and some pairs of cities are joined by a direct two-way road (at most one road between two cities). Every city has direct roads to at least three other cities. Prove that one can start in some city, travel along a closed route that uses at least three different roads, visits an even number of different cities, never visits a city twice (except returning to the start), and comes back to the start.

**Hint 1: What is being asked**

Prove that the road network contains a cycle with an even number of cities (equivalently, an even number of roads).

**Hint 2: The technique**

Look at an extreme object in the network, such as a route that cannot be extended, and use what the degree condition says about its end.

**Hint 3: The key idea**

Take a route (a path without repeated cities) with as many cities as possible. Where can the neighbours of its first city lie?

**Hint 4: The next step**

The first city $v_0$ has at least three neighbours, all on the path $v_0,v_1,\dots,v_m$. Besides $v_1$ there are two more, $v_i$ and $v_j$ with $2\le i<j$. Each of them closes a cycle with the path.

**Hint 5: The next step**

There are three natural cycles using $v_0$, $v_i$, $v_j$. Compute their numbers of cities, and see what happens if all of them are odd.

**Solution**

Because there are finitely many cities, we can choose a longest path $v_0v_1\dots v_m$ (the cities $v_0,\dots,v_m$ are all different, consecutive ones are joined by roads, and $m$ is as large as possible).

Every neighbour of $v_0$ lies on this path. Indeed, if $v_0$ had a neighbour $w$ outside the path, then $w v_0 v_1\dots v_m$ would be a longer path.

The city $v_0$ has at least three neighbours, all among $v_1,\dots,v_m$. One of them is $v_1$ (it is joined to $v_0$ by the path), so at least two others exist; call them $v_i$ and $v_j$ with $2\le i<j\le m$.

Consider these three closed routes:
1. $v_0v_1\dots v_iv_0$, which visits $i+1$ cities ($i+1\ge3$);
2. $v_0v_1\dots v_jv_0$, which visits $j+1$ cities;
3. $v_0v_iv_{i+1}\dots v_jv_0$, which visits $(j-i+1)+1=j-i+2$ cities ($\ge3$ since $j>i$).

Each is a cycle: the cities in each list are distinct and consecutive ones are joined (using the roads $v_0v_i$ and $v_0v_j$ for the closing steps).

Suppose all three numbers of cities were odd. Then $i+1$ odd gives $i$ even, and $j+1$ odd gives $j$ even. But then $j-i+2$ is even, a contradiction. So at least one of the three cycles has an even number of cities. $\blacksquare$

---

## m49 · difficulty 7 · Diophantine equations, Divisibility and gcd
*20th Korean Mathematical Olympiad Final Round (South Korea), MathNet 0eu6*

**Statement**

Find all triplets $(x,y,z)$ of positive integers satisfying $1+4^x+4^y=z^2$.

**Hint 1: What is being asked**

Find all positive integers $x,y,z$ with $1+4^x+4^y=z^2$.

**Hint 2: The technique**

Compare $z^2$ with the squares next to $(2^y)^2$, and when that fails, factor $z^2-1$ and count powers of $2$ ([[diophantine]], [[divisibility]]).

**Hint 3: The key idea**

By symmetry let $x\le y$. Compare $1+4^x+4^y$ with $(2^y+1)^2=4^y+2^{y+1}+1$.

**Hint 4: The next step**

This settles $2x\le y+1$. For $2x>y+1$, write $(z-1)(z+1)=4^x(1+4^{y-x})$. What is $\gcd(z-1,z+1)$?

**Hint 5: The next step**

One of $z\pm1$ is divisible by $2^{2x-1}$. Compare the resulting lower bound for $z^2$ with the actual size of $1+4^x+4^y$.

**Solution**

**Answer:** $(x,y,z)=\boxed{(t,\,2t-1,\,2^{2t-1}+1)\ \text{and}\ (2t-1,\,t,\,2^{2t-1}+1)}$ for positive integers $t$.

The equation is symmetric in $x,y$, so let $x\le y$. Note $z^2>4^y=(2^y)^2$, so $z\ge2^y+1$, while $(2^y+1)^2=4^y+2^{y+1}+1$.

**Case $2x<y+1$.** Then $4^x<2^{y+1}$, so $(2^y)^2<z^2<(2^y+1)^2$. Impossible.

**Case $2x=y+1$.** Then $z^2=4^y+2^{y+1}+1=(2^y+1)^2$, so $z=2^y+1$. With $x=t$ we get $y=2t-1\ge t$ and the solution $(t,2t-1,2^{2t-1}+1)$.

**Case $2x>y+1$.** Since $y\ge x$, this gives $x\ge2$, and $y\le2x-2$. Write $(z-1)(z+1)=4^x(1+4^{y-x})$. The number $z$ is odd, so $z-1,z+1$ are even with $\gcd(z-1,z+1)=2$; one of them is $\equiv2\pmod4$, so the other carries all remaining factors of $2$. The right side is divisible by $2^{2x}$, hence the other factor is divisible by $2^{2x-1}$, and $z+1\ge2^{2x-1}$. Since $x\ge2$, $2^{2x-1}-1>0$, so
$$z^2\ge(2^{2x-1}-1)^2=4\cdot4^{2x-2}-4^x+1.$$
But $z^2=1+4^x+4^y\le1+4^x+4^{2x-2}$. Together: $3\cdot4^{2x-2}\le2\cdot4^x$, i.e. $3\cdot4^{x-2}\le2$, so $x<2$. Contradiction.

Swapping $x$ and $y$ gives the second family. (For $t=1$ both give $(1,1,3)$.)

---

## m86 · difficulty 7 · Invariants and monovariants, Constructive arguments
*International Mathematical Olympiad (IMO), MathNet 06x0*

**Statement**

Let $n$ be a positive integer. We start with $n$ piles of pebbles, each initially containing a single pebble. One can perform moves of the following form: choose two piles, take an equal number of pebbles from each pile and form a new pile out of these pebbles. For each positive integer $n$, find the smallest number of non-empty piles that one can obtain by performing a finite sequence of moves of this form.

**Hint 1: What is being asked**

A move takes $c\ge1$ pebbles from each of two piles and puts these $2c$ pebbles into a new pile. Starting from $n$ single pebbles, find the fewest non-empty piles that can be reached.

**Hint 2: The technique**

Small cases suggest the answer. For impossibility, look for a property of the whole configuration that moves can never create.

**Hint 3: The key idea**

If $n$ is a power of $2$, one pile is reachable by merging equal piles repeatedly.

**Hint 4: The next step**

Let $m$ be an odd divisor of $n$ greater than $1$. Show that if every pile is divisible by $m$ after a move, then every pile was divisible by $m$ before it. Run this backwards from a single pile.

**Hint 5: The next step**

For two piles when $2^N<n<2^{N+1}$: make a pile of $2^N$, then use it and pairs of pebbles to bring it down to $n-2^N$ while the removed pebbles regroup into another power of $2$.

**Solution**

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

---

## m37 · difficulty 6 · Modular arithmetic, Diophantine equations
*48th Austrian Mathematical Olympiad (Austria), MathNet 00lz*

**Statement**

Find all pairs $(a,b)$ of non-negative integers such that
$$2017^a=b^6-32b+1.$$

**Hint 1: What is being asked**

Determine all non-negative integers $a,b$ with $2017^a=b^6-32b+1$.

**Hint 2: The technique**

Reduce modulo a suitable power of $2$ ([[modular-arithmetic]]) to learn something about $a$, then compare sizes.

**Hint 3: The key idea**

Parity forces $b$ to be even. Write $b=2c$ and look at the equation modulo $64$.

**Hint 4: The next step**

$2017\equiv33\pmod{64}$ and $33^2\equiv1\pmod{64}$. What does this say about $a$?

**Hint 5: The next step**

For larger $b$, compare $b^6-32b+1$ with $(b^3)^2$ and $(b^3-1)^2$.

**Solution**

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

---
