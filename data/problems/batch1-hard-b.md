### m50
source: mathnet
mathnet_id: 0aj0
country: North Macedonia
competition: European Mathematical Cup
type: proof
difficulty: 6
techniques: am-gm
statement:
Let $a,b,c$ be positive real numbers such that $abc=1$. Prove that
$$\frac{a+b+c+3}{4}\ge\frac1{a+b}+\frac1{b+c}+\frac1{c+a}.$$
asked:
For positive $a,b,c$ with product $1$, show that the sum of the reciprocals of the pairwise sums is at most $\frac{a+b+c+3}4$.
technique:
Bound each fraction on the right from above by applying AM-GM to its denominator, and use $abc=1$ to rewrite that bound in terms of the third variable.
hint:
$a+b\ge2\sqrt{ab}$, and $ab=\frac1c$. What upper bound does this give for $\frac1{a+b}$?
hint:
After this step it is enough to prove $\frac{a+b+c+3}4\ge\frac{\sqrt a+\sqrt b+\sqrt c}2$.
hint:
Move everything to one side and group the terms belonging to each variable. Each group is a perfect square.
solution:
By AM-GM, $a+b\ge2\sqrt{ab}=\dfrac{2}{\sqrt c}$, because $ab=\frac1c$. Hence $\dfrac1{a+b}\le\dfrac{\sqrt c}2$, and similarly $\dfrac1{b+c}\le\dfrac{\sqrt a}2$ and $\dfrac1{c+a}\le\dfrac{\sqrt b}2$. Adding,
$$\frac1{a+b}+\frac1{b+c}+\frac1{c+a}\le\frac{\sqrt a+\sqrt b+\sqrt c}2.$$
It remains to show that this is at most $\frac{a+b+c+3}4$. Indeed,
$$\frac{a+b+c+3}4-\frac{\sqrt a+\sqrt b+\sqrt c}2=\frac{(\sqrt a-1)^2+(\sqrt b-1)^2+(\sqrt c-1)^2}4\ge0.$$
Combining the two inequalities proves the claim. (Equality holds for $a=b=c=1$, where both sides equal $\frac32$.) $\blacksquare$

### m51
source: mathnet
mathnet_id: 0gqo
country: Turkey
competition: Team Selection Test
type: proof
difficulty: 6
techniques: am-gm
statement:
Show that for all positive real numbers $x,y,z$ satisfying $x^2+y^2+z^2\le x+y+z$ the following inequality holds:
$$\frac{x^2+3}{x^3+1}+\frac{y^2+3}{y^3+1}+\frac{z^2+3}{z^3+1}\ge6.$$
asked:
Under the constraint $x^2+y^2+z^2\le x+y+z$ on positive reals, prove that the three fractions add up to at least $6$.
technique:
Replace each fraction by a simpler lower bound whose denominators are tied to the constraint, then finish with the inequality between arithmetic and harmonic means.
hint:
In the numerator use $t^2+1\ge2t$, and factor $t^3+1=(t+1)(t^2-t+1)$.
hint:
You get $\frac{t^2+3}{t^3+1}\ge\frac{2}{t^2-t+1}$. What does the constraint say about the sum of the three numbers $t^2-t+1$?
hint:
For positive $p,q,r$: $\frac1p+\frac1q+\frac1r\ge\frac9{p+q+r}$.
solution:
For $t>0$, since $t^2+1\ge2t$ and $t^3+1=(t+1)(t^2-t+1)>0$,
$$\frac{t^2+3}{t^3+1}\ge\frac{2t+2}{t^3+1}=\frac{2}{t^2-t+1}.$$
Let $p=x^2-x+1$, $q=y^2-y+1$, $r=z^2-z+1$. These are positive (since $t^2-t+1=(t-\tfrac12)^2+\tfrac34$), and the constraint gives
$$p+q+r=(x^2+y^2+z^2)-(x+y+z)+3\le3.$$
By the AM-HM inequality (equivalently, Cauchy-Schwarz $(p+q+r)(\frac1p+\frac1q+\frac1r)\ge9$),
$$\frac{x^2+3}{x^3+1}+\frac{y^2+3}{y^3+1}+\frac{z^2+3}{z^3+1}\ge2\left(\frac1p+\frac1q+\frac1r\right)\ge\frac{18}{p+q+r}\ge\frac{18}3=6.$$
Equality holds at $x=y=z=1$. $\blacksquare$

### m52
source: mathnet
mathnet_id: 0gn2
country: Turkey
competition: 14th Turkish Mathematical Olympiad
type: proof
difficulty: 6
techniques: cauchy-schwarz
statement:
Let $n\ge2$ and let $a_1,a_2,\dots,a_n$ be positive real numbers such that
$$t=a_1+a_2+\dots+a_n=a_1^2+a_2^2+\dots+a_n^2.$$
Show that
$$\sum_{i\neq j}\frac{a_i}{a_j}\ge\frac{(n-1)^2\,t}{t-1},$$
where the sum runs over all ordered pairs $(i,j)$ with $i\ne j$.
asked:
The numbers have equal sum and sum of squares, both called $t$. Prove the lower bound for the sum of all ratios $a_i/a_j$ with $i\ne j$ (and note that the bound makes sense, i.e. $t>1$).
technique:
Group the sum by the denominator and write each group as a square over a positive quantity, so that Cauchy-Schwarz in Engel form applies.
hint:
For fixed $j$, $\sum_{i\ne j}a_i=t-a_j$. So the sum equals $\sum_j\frac{t-a_j}{a_j}$.
hint:
Write $\frac{t-a_j}{a_j}=\frac{(t-a_j)^2}{a_j(t-a_j)}$ and apply $\sum\frac{x_j^2}{y_j}\ge\frac{(\sum x_j)^2}{\sum y_j}$.
hint:
Use the hypothesis to compute $\sum_ja_j(t-a_j)$.
solution:
For each $j$, $\sum_{i\ne j}a_i=t-a_j$, so
$$\sum_{i\neq j}\frac{a_i}{a_j}=\sum_{j=1}^n\frac{t-a_j}{a_j}.$$
Since $n\ge2$ and all $a_i>0$, each $t-a_j>0$. Also
$$\sum_{j=1}^na_j(t-a_j)=t\sum a_j-\sum a_j^2=t^2-t.$$
The left side is positive, so $t^2-t>0$ and $t>1$; the right-hand side of the claim is well defined.

By the Cauchy-Schwarz inequality in Engel form ($\sum\frac{x_j^2}{y_j}\ge\frac{(\sum x_j)^2}{\sum y_j}$ for $y_j>0$),
$$\sum_{j=1}^n\frac{t-a_j}{a_j}=\sum_{j=1}^n\frac{(t-a_j)^2}{a_j(t-a_j)}\ge\frac{\left(\sum_j(t-a_j)\right)^2}{\sum_ja_j(t-a_j)}=\frac{\big((n-1)t\big)^2}{t^2-t}=\frac{(n-1)^2t}{t-1}.$$
$\blacksquare$

### m53
source: mathnet
mathnet_id: 065m
country: Greece
competition: SELECTION EXAMINATION
type: answer
difficulty: 6
techniques: cauchy-schwarz
statement:
Find all triples of real numbers $(x,y,z)$, each greater than $3$, that satisfy
$$\frac{(x+2)^2}{y+z-2}+\frac{(y+4)^2}{z+x-4}+\frac{(z+6)^2}{x+y-6}=36.$$
asked:
Determine every triple with $x,y,z>3$ for which the sum of the three fractions equals exactly $36$.
technique:
Show that the left side is always at least $36$ by Cauchy-Schwarz in Engel form; then a solution must make every inequality used an equality.
hint:
The denominators are positive. Apply $\sum\frac{u_k^2}{v_k}\ge\frac{(\sum u_k)^2}{\sum v_k}$ and express the result through $s=x+y+z$.
hint:
Show $\frac{(s+12)^2}{2s-12}\ge36$, with equality only for one value of $s$.
hint:
Equality in Engel form needs $\frac{u_1}{v_1}=\frac{u_2}{v_2}=\frac{u_3}{v_3}$. What is this common ratio?
solution:
Since $x,y,z>3$, the denominators $y+z-2$, $z+x-4$, $x+y-6$ are all positive. Let $s=x+y+z$. The numerators' bases add to $s+12$ and the denominators add to $2s-12>0$. By Cauchy-Schwarz in Engel form,
$$\frac{(x+2)^2}{y+z-2}+\frac{(y+4)^2}{z+x-4}+\frac{(z+6)^2}{x+y-6}\ge\frac{(s+12)^2}{2s-12}.$$
Moreover $(s+12)^2-36(2s-12)=s^2-48s+576=(s-24)^2\ge0$, so the right side is at least $36$, with equality only for $s=24$.

So a solution needs equality in both steps: $s=24$, and equality in Engel form, which holds exactly when
$$\frac{x+2}{y+z-2}=\frac{y+4}{z+x-4}=\frac{z+6}{x+y-6}.$$
The common value equals the ratio of the sums, $\frac{s+12}{2s-12}=\frac{36}{36}=1$. Hence $x+2=y+z-2=22-x$, so $x=10$; $y+4=z+x-4=20-y$, so $y=8$; $z+6=x+y-6=18-z$, so $z=6$.

Check: for $(10,8,6)$ every numerator base and every denominator equals $12$, so the sum is $12+12+12=36$, and all three numbers exceed $3$. The only solution is $\boxed{(x,y,z)=(10,8,6)}$.

### m54
source: mathnet
mathnet_id: 0ag3
country: North Macedonia
competition: North Macedonia
type: proof
difficulty: 7
techniques: cauchy-schwarz, double-counting
statement:
Let $p_1,p_2,\dots,p_{2009}$ be positive real numbers. Prove the inequality
$$\sum_{i=1}^{2009}\frac{p_i}{p_{i+1}+p_{i+2}+\dots+p_{i+1004}}\ge\frac{2009}{1004},$$
where the indices are taken modulo $2009$.
asked:
Each $p_i$ is divided by the sum of the next $1004$ numbers around the circle. Show the total is at least $\frac{2009}{1004}$.
technique:
Turn each fraction into a square over a product and apply Cauchy-Schwarz in Engel form. The denominator that appears can be identified exactly by counting pairs ([[double-counting]]).
hint:
Write $\frac{p_i}{S_i}=\frac{p_i^2}{p_iS_i}$, where $S_i$ is the denominator, and apply Engel form.
hint:
In $\sum_ip_iS_i$, each product $p_ip_j$ with $i\ne j$ appears how many times? Think about the two "distances" from $i$ to $j$ and from $j$ to $i$ around the circle.
hint:
You need $\big(\sum p_i\big)^2\ge\frac{2009}{1004}\sum_{i<j}p_ip_j$. Compare $\sum_{i<j}p_ip_j$ with $\sum p_i^2$.
solution:
Let $S_i=p_{i+1}+\dots+p_{i+1004}$ (indices mod $2009$), $T=\sum p_i$ and $e=\sum_{i<j}p_ip_j$. By Cauchy-Schwarz in Engel form,
$$\sum_i\frac{p_i}{S_i}=\sum_i\frac{p_i^2}{p_iS_i}\ge\frac{T^2}{\sum_ip_iS_i}.$$
**The denominator equals $e$.** $\sum_ip_iS_i$ is the sum of $p_ip_j$ over ordered pairs $(i,j)$ with $j-i\equiv d\pmod{2009}$ for some $d\in\{1,\dots,1004\}$. For an unordered pair $\{i,j\}$ with $i\ne j$, the residues of $j-i$ and $i-j$ lie in $\{1,\dots,2008\}$ and add to $2009$, so exactly one of them lies in $\{1,\dots,1004\}$. Hence each unordered pair is counted exactly once, and $\sum_ip_iS_i=e$.

**Comparison.** From $\sum_{i<j}(p_i-p_j)^2\ge0$ we get $2008\sum p_i^2\ge2e$, i.e. $\sum p_i^2\ge\frac{e}{1004}$. Therefore
$$T^2=\sum p_i^2+2e\ge\frac e{1004}+2e=\frac{2009}{1004}\,e.$$
Combining, $\sum_i\frac{p_i}{S_i}\ge\frac{T^2}{e}\ge\frac{2009}{1004}$. (Equality holds when all $p_i$ are equal: each term is then $\frac1{1004}$.) $\blacksquare$

### m55
source: mathnet
mathnet_id: 0czu
country: Saudi Arabia
competition: Saudi Arabia Mathematical Competitions
type: answer
difficulty: 6
techniques: telescoping
statement:
Let $f_n=2^{2^n}+1$, $n=1,2,3,\dots$, be the Fermat numbers. Find the least real number $C$ such that
$$\frac1{f_1}+\frac2{f_2}+\frac{2^2}{f_3}+\dots+\frac{2^{n-1}}{f_n}<C$$
for all positive integers $n$.
asked:
Find the smallest constant that strictly bounds every partial sum $\sum_{k=1}^n\frac{2^{k-1}}{f_k}$.
technique:
Use $(X-1)(X+1)=X^2-1$ with $X=2^{2^k}$ to write each term as a difference of two consecutive terms of another sequence, so that the partial sums telescope.
hint:
With $x_k=2^{2^k}-1$, note $x_{k+1}=x_k\,f_k$. Express $\frac1{f_k}$ through $\frac1{x_k}$ and $\frac1{x_{k+1}}$.
hint:
Verify $\frac1{f_k}=\frac1{x_k}-\frac2{x_{k+1}}$ (use $f_k-2=x_k$), then multiply by $2^{k-1}$.
hint:
The partial sum becomes $\frac13-\frac{2^n}{x_{n+1}}$. What happens as $n\to\infty$?
solution:
Let $x_k=2^{2^k}-1$. Since $(2^{2^k}-1)(2^{2^k}+1)=2^{2^{k+1}}-1$, we have $x_{k+1}=x_kf_k$, and
$$\frac1{x_k}-\frac2{x_{k+1}}=\frac{f_k-2}{x_kf_k}=\frac{x_k}{x_kf_k}=\frac1{f_k},$$
because $f_k-2=x_k$. Multiplying by $2^{k-1}$:
$$\frac{2^{k-1}}{f_k}=\frac{2^{k-1}}{x_k}-\frac{2^k}{x_{k+1}}.$$
Summing for $k=1,\dots,n$, the sum telescopes:
$$\sum_{k=1}^n\frac{2^{k-1}}{f_k}=\frac{1}{x_1}-\frac{2^n}{x_{n+1}}=\frac13-\frac{2^n}{2^{2^{n+1}}-1}.$$
The subtracted term is positive, so every partial sum is less than $\frac13$; thus $C=\frac13$ works. Since $2^{2^{n+1}}-1\ge2^{2n+2}-1>2^{2n}$, the subtracted term is less than $2^{-n}$, which tends to $0$; so the partial sums get arbitrarily close to $\frac13$, and no $C<\frac13$ works. The answer is $\boxed{C=\tfrac13}$.

### m56
source: mathnet
mathnet_id: 0law
country: Vietnam
competition: Vijetnam 2011
type: proof
difficulty: 7
techniques: telescoping, recursion
statement:
A sequence of real numbers $(x_n)$ is given by
$$x_1=1\quad\text{and}\quad x_n=\frac{2n}{(n-1)^2}\sum_{i=1}^{n-1}x_i\quad\text{for all }n\ge2.$$
For each positive integer $n$ let $y_n=x_{n+1}-x_n$. Show that the sequence $(y_n)$ has a finite limit as $n\to\infty$.
asked:
Prove that the consecutive differences $x_{n+1}-x_n$ converge to a finite number.
technique:
Work with the partial sums $S_n=x_1+\dots+x_n$: the recurrence becomes a product formula for $S_n$. After dividing by the obvious growth factor $n^2$ you get a product with factors $1+\frac1{k^2}$, which converges.
hint:
Show $S_n=S_{n-1}\cdot\frac{n^2+1}{(n-1)^2}$ for $n\ge2$.
hint:
Let $P_n=S_n/n^2$. Show $P_n=P_{n-1}\left(1+\frac1{n^2}\right)$, so $P_n=\prod_{k=2}^n\left(1+\frac1{k^2}\right)$, and prove that $P_n$ converges.
hint:
Express $x_{n+1}$ through $P_n$, and then $y_n$ through $P_n$ and $P_{n-1}$.
solution:
Let $S_n=x_1+\dots+x_n$. For $n\ge2$ the definition gives $x_n=\frac{2n}{(n-1)^2}S_{n-1}$, so
$$S_n=S_{n-1}+x_n=S_{n-1}\cdot\frac{(n-1)^2+2n}{(n-1)^2}=S_{n-1}\cdot\frac{n^2+1}{(n-1)^2}.$$
Put $P_n=\frac{S_n}{n^2}$. Dividing by $n^2$,
$$P_n=\frac{S_{n-1}}{(n-1)^2}\cdot\frac{n^2+1}{n^2}=P_{n-1}\left(1+\frac1{n^2}\right),\qquad P_1=1,$$
so $P_n=\prod_{k=2}^n\left(1+\frac1{k^2}\right)$. This sequence is increasing, and since $1+u\le e^u$,
$$P_n\le\exp\Big(\sum_{k=2}^n\frac1{k^2}\Big)<\exp\Big(\sum_{k=2}^n\frac1{k(k-1)}\Big)=\exp\Big(1-\frac1n\Big)<e.$$
An increasing bounded sequence converges, so $P_n\to P$ for some finite $P$.

Now for $n\ge1$, $x_{n+1}=\frac{2(n+1)}{n^2}S_n=2(n+1)P_n$. Hence for $n\ge2$, using $P_{n}-P_{n-1}=\frac{P_{n-1}}{n^2}$,
$$y_n=2(n+1)P_n-2nP_{n-1}=2P_n+2n(P_n-P_{n-1})=2P_n+\frac{2P_{n-1}}{n}.$$
As $n\to\infty$, $2P_n\to2P$ and $\frac{2P_{n-1}}n\to0$ (as $P_{n-1}<e$). Therefore $y_n\to2P=2\prod_{k\ge2}\left(1+\frac1{k^2}\right)$, a finite limit. $\blacksquare$

### m57
source: mathnet
mathnet_id: 0182
country: Baltic Way
competition: Baltic Way 2011 Problem Shortlist
type: answer
difficulty: 7
techniques: functional-equations
statement:
Find all functions $f:\mathbb R\to\mathbb R$ such that
$$f(x+f(y))-f(x)=(x+f(y))^3-x^3$$
for all $x,y\in\mathbb R$.
asked:
Determine every real function for which shifting the argument by any value $f(y)$ changes $f$ by exactly as much as it changes $x\mapsto x^3$.
technique:
Subtract the cube: $g(x)=f(x)-x^3$ turns the equation into "every value of $f$ is a period of $g$". Then study the set of periods, which is closed under addition and subtraction.
hint:
Show $g(x+f(y))=g(x)$ for all $x,y$, where $g(x)=f(x)-x^3$.
hint:
The periods of $g$ form a group under addition. If $a=f(y_0)\ne0$, then both $f(y)$ and $f(y+a)$ are periods for every $y$. What is their difference?
hint:
$(y+a)^3-y^3$ takes every value on a half-line. A group of reals containing a half-line is all of $\mathbb R$.
solution:
**Answer:** $f\equiv0$, and $f(x)=x^3+c$ for any real constant $c$.

Let $g(x)=f(x)-x^3$. The equation reads $f(x+f(y))-(x+f(y))^3=f(x)-x^3$, i.e.
$$g(x+f(y))=g(x)\quad\text{for all }x,y.$$
Let $G$ be the set of periods of $g$, i.e. the $p$ with $g(x+p)=g(x)$ for all $x$. If $p,q\in G$ then $g(x+p-q)=g(x-q)=g(x)$, so $p-q\in G$: $G$ is an additive subgroup of $\mathbb R$, and it contains every value of $f$.

If $f\equiv0$, the equation holds ($0=x^3-x^3$). Otherwise pick $y_0$ with $a=f(y_0)\ne0$. For any $y$, both $f(y)$ and $f(y+a)$ lie in $G$, and since $a\in G$ we have $g(y+a)=g(y)$, so
$$f(y+a)-f(y)=(y+a)^3-y^3=3a\left(y+\tfrac a2\right)^2+\tfrac{a^3}4\in G.$$
As $y$ runs over $\mathbb R$ this takes every value in $[\frac{a^3}4,\infty)$ if $a>0$, or in $(-\infty,\frac{a^3}4]$ if $a<0$. So $G$ contains a half-line $H$. For any real $r$, choose $u\in H$ with $u+r\in H$ (take $u$ far enough into the half-line); then $r=(u+r)-u\in G$. Hence $G=\mathbb R$, every real number is a period of $g$, and $g$ is constant, say $g\equiv c$. Thus $f(x)=x^3+c$.

Check: if $f(x)=x^3+c$, then $f(x+f(y))-f(x)=(x+f(y))^3+c-x^3-c=(x+f(y))^3-x^3$. So the solutions are $\boxed{f\equiv0\ \text{ and }\ f(x)=x^3+c\ (c\in\mathbb R)}$.

### m58
source: mathnet
mathnet_id: 06p9
country: IMO
competition: 48th International Mathematical Olympiad Vietnam 2007 Shortlisted Problems with Solutions
type: answer
difficulty: 8
techniques: functional-equations
statement:
Find all functions $f:\mathbb R^+\to\mathbb R^+$ such that
$$f(x+f(y))=f(x+y)+f(y)$$
for all $x,y\in\mathbb R^+$. ($\mathbb R^+$ denotes the set of positive real numbers.)
asked:
Determine every function from the positive reals to the positive reals satisfying the equation.
technique:
First show $f(y)>y$, then study $g(y)=f(y)-y>0$.
hint:
If $f(y)<y$, put $x=y-f(y)$. If $f(y)=y$, compare both sides directly.
hint:
With $g(y)=f(y)-y$ and $t=x+y$, show $g(t+g(y))=g(t)+y$ for all $t>y>0$. Deduce that $g$ is injective.
hint:
For $t>u+v$ compute $g(t+g(u)+g(v))$ in two steps and compare with $g(t+g(u+v))$. This gives additivity; then show $g(g(y))=y$.
solution:
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

### m59
source: mathnet
mathnet_id: 0d29
country: Saudi Arabia
competition: Selection tests for the International Mathematical Olympiad 2013
type: answer
difficulty: 7
techniques: functional-equations, induction
statement:
Let $S=\{0,1,2,3,\dots\}$ be the set of non-negative integers. Find all strictly increasing functions $f:S\to S$ such that $n+f(f(n))\le2f(n)$ for every $n\in S$.
asked:
Determine all strictly increasing maps of the non-negative integers to themselves with $n+f(f(n))\le2f(n)$ for all $n$.
technique:
Look at the excess $g(n)=f(n)-n$. Strict increase makes $g$ non-negative and non-decreasing, and the inequality then pins down $g$ almost completely.
hint:
For integers, strictly increasing means $f(n+1)\ge f(n)+1$. What does that say about $g(n)=f(n)-n$?
hint:
Rewrite the condition as $g(f(n))\le g(n)$. Since $f(n)\ge n$ and $g$ is non-decreasing, conclude $g(n+g(n))=g(n)$.
hint:
Let $n_0$ be the first index with $g(n_0)=k>0$. Show $g(n_0+jk)=k$ for all $j$, and use monotonicity.
solution:
**Answer:** for any $n_0\in S$ and any integer $k\ge0$,
$$f(n)=\begin{cases}n,&n<n_0,\\ n+k,&n\ge n_0.\end{cases}$$
(For $k=0$ this is the identity.)

Let $g(n)=f(n)-n$. Since $f$ is strictly increasing with integer values, $f(n+1)\ge f(n)+1$, so $g(n+1)\ge g(n)$: $g$ is non-decreasing. Also $g(0)=f(0)\ge0$, so $g\ge0$ and $f(n)\ge n$.

The condition $f(f(n))-f(n)\le f(n)-n$ says $g(f(n))\le g(n)$. But $f(n)\ge n$ and $g$ is non-decreasing, so $g(f(n))\ge g(n)$. Hence
$$g(n+g(n))=g(f(n))=g(n)\quad\text{for all }n.\tag{1}$$
If $g\equiv0$, $f$ is the identity. Otherwise let $n_0$ be the least $n$ with $g(n)>0$ and let $k=g(n_0)$. Then $g(n)=0$ for $n<n_0$. By induction on $j$, $g(n_0+jk)=k$ for all $j\ge0$: the case $j=0$ is the definition, and if $g(m)=k$ for $m=n_0+jk$, then (1) gives $g(m+k)=g(m)=k$. Every $n\ge n_0$ lies between $n_0+jk$ and $n_0+(j+1)k$ for some $j$, and $g$ is non-decreasing, so $g(n)=k$. Thus $f$ has the stated form.

**Check.** Such $f$ is strictly increasing: on each piece it is $n\mapsto n+\text{const}$, and $f(n_0-1)=n_0-1<n_0+k=f(n_0)$. For $n<n_0$: $f(f(n))=n$ and $n+n\le2n$. For $n\ge n_0$: $f(n)=n+k\ge n_0$, so $f(f(n))=n+2k$ and $n+(n+2k)=2(n+k)=2f(n)$. So all these functions work. $\boxed{f(n)=n\ (n<n_0),\ f(n)=n+k\ (n\ge n_0)}$

### m60
source: mathnet
mathnet_id: 0bd7
country: Romania
competition: 64th NMO Selection Tests for the Balkan and International Mathematical Olympiads
type: proof
difficulty: 7
techniques: polynomials, modular-arithmetic
statement:
Given an integer $n\ge2$, let $a_n,b_n,c_n$ be integers such that
$$\left(\sqrt[3]{2}-1\right)^n=a_n+b_n\sqrt[3]{2}+c_n\sqrt[3]{4}.$$
Show that $c_n\equiv1\pmod3$ if and only if $n\equiv2\pmod3$.
asked:
Writing $(\sqrt[3]2-1)^n$ in the basis $1,\sqrt[3]2,\sqrt[3]4$ with integer coefficients, show that the coefficient of $\sqrt[3]4$ is $1$ mod $3$ exactly when $n$ is $2$ mod $3$.
technique:
The coefficients are the remainder of $(t-1)^n$ on division by $t^3-2$. Reduce this polynomial identity modulo $3$, where $t^3-2$ becomes a perfect cube.
hint:
Divide $(t-1)^n$ by $t^3-2$ with remainder $r(t)$. Why are the coefficients of $r$ exactly $a_n,b_n,c_n$?
hint:
Modulo $3$, $t^3-2\equiv t^3+1=(t+1)^3$. Substitute $s=t+1$.
hint:
Then $t-1\equiv s+1$, and $(s+1)^n\equiv1+ns+\binom n2s^2$ modulo $s^3$. Read off the coefficient of $t^2$.
solution:
**The coefficients are unique.** The polynomial $t^3-2$ has no rational root, so (being cubic) it is irreducible over $\mathbb Q$ and is the minimal polynomial of $\theta=\sqrt[3]2$. Hence $1,\theta,\theta^2$ are linearly independent over $\mathbb Q$, and $a_n,b_n,c_n$ are uniquely determined.

**Polynomial division.** Since $t^3-2$ is monic, $(t-1)^n=q(t)(t^3-2)+r(t)$ with $q,r\in\mathbb Z[t]$ and $\deg r\le2$. Substituting $t=\theta$ gives $(\theta-1)^n=r(\theta)$, so by uniqueness $r(t)=a_n+b_nt+c_nt^2$.

**Reduction mod 3.** Reduce the identity modulo $3$ (in $\mathbb F_3[t]$). There $t^3-2=t^3+1=(t+1)^3$. Put $s=t+1$; then $t-1=s-2\equiv s+1$, so
$$(s+1)^n\equiv\bar q\cdot s^3+\bar r\pmod 3,\qquad\deg\bar r\le2.$$
By the binomial theorem $(s+1)^n=1+ns+\binom n2s^2+s^3(\dots)$, and the remainder of division by $s^3$ is unique, so
$$\bar r=1+ns+\binom n2s^2=1+n(t+1)+\binom n2(t^2+2t+1).$$
The coefficient of $t^2$ is $\binom n2$. Hence $c_n\equiv\binom n2=\frac{n(n-1)}2\pmod3$.

**Cases.** If $n\equiv0$ or $n\equiv1\pmod3$, then $3$ divides $n(n-1)$, and since $2$ is invertible mod $3$, $\binom n2\equiv0$. If $n\equiv2\pmod3$, then $n(n-1)\equiv2\cdot1=2$, so $\binom n2\equiv2\cdot2^{-1}=1\pmod3$. Therefore $c_n\equiv1\pmod3$ exactly when $n\equiv2\pmod3$. $\blacksquare$

### m61
source: mathnet
mathnet_id: 03qn
country: China
competition: International Mathematical Olympiad
type: answer
difficulty: 8
techniques: polynomials
statement:
Find all polynomials $P(x)$ with real coefficients which satisfy the equation
$$P(a-b)+P(b-c)+P(c-a)=2P(a+b+c)$$
for all real numbers $a,b,c$ such that $ab+bc+ca=0$.
asked:
Determine every real polynomial satisfying the identity on the surface $ab+bc+ca=0$.
technique:
Simple choices of $(a,b,c)$ on the surface force $P$ to be even with $P(0)=0$. Then one well-chosen one-parameter family gives a condition on each coefficient separately.
hint:
Try $a=b=c=0$, then $b=c=0$ with $a$ arbitrary.
hint:
Find a family like $(a,b,c)=(x,2x,\lambda x)$ on the surface. With $\lambda=-\frac23$ the four arguments become multiples of $\frac x3$.
hint:
For $P(x)=x^{2k}$ the family gives the number $3^{2k}+8^{2k}+5^{2k}-2\cdot7^{2k}$. For which $k$ is it zero?
solution:
**Answer:** $P(x)=\alpha x^4+\beta x^2$ with $\alpha,\beta\in\mathbb R$.

**Necessity.** $a=b=c=0$ gives $3P(0)=2P(0)$, so $P(0)=0$. For $b=c=0$ (allowed, since $ab+bc+ca=0$) we get $P(a)+P(0)+P(-a)=2P(a)$, so $P(-a)=P(a)$: $P$ is even. Write $P(x)=\sum_{k\ge1}p_kx^{2k}$.

Take $(a,b,c)=(x,2x,-\frac23x)$: then $ab+bc+ca=2x^2-\frac43x^2-\frac23x^2=0$, and $a-b=-x$, $b-c=\frac83x$, $c-a=-\frac53x$, $a+b+c=\frac73x$. Since $P$ is even, the identity becomes
$$\sum_{k\ge1}p_k\,\frac{c_k}{3^{2k}}\,x^{2k}=0\quad\text{for all }x,\qquad c_k=3^{2k}+8^{2k}+5^{2k}-2\cdot7^{2k}.$$
A polynomial vanishing for all $x$ has all coefficients zero, so $p_kc_k=0$ for every $k$. We have $c_1=9+64+25-98=0$ and $c_2=81+4096+625-4802=0$. For $k\ge3$, $(8/7)^{2k}\ge(8/7)^6=\frac{262144}{117649}>2$, so $8^{2k}>2\cdot7^{2k}$ and $c_k>0$, forcing $p_k=0$. Hence $P(x)=\alpha x^4+\beta x^2$.

**Sufficiency.** The condition is linear in $P$, so it suffices to check $x^2$ and $x^4$. Let $ab+bc+ca=0$, $s=a+b+c$, and $u=a-b$, $v=b-c$, $w=c-a$, so $u+v+w=0$. Then
$$u^2+v^2+w^2=2(a^2+b^2+c^2)-2(ab+bc+ca)=2(s^2-2\cdot0)-0=2s^2.$$
For $u+v+w=0$ we have $uv+vw+wu=-\frac12(u^2+v^2+w^2)$ and $(uv+vw+wu)^2=u^2v^2+v^2w^2+w^2u^2+2uvw(u+v+w)=u^2v^2+v^2w^2+w^2u^2$. Writing $Q=u^2+v^2+w^2$,
$$u^4+v^4+w^4=Q^2-2(u^2v^2+v^2w^2+w^2u^2)=Q^2-\tfrac{Q^2}2=\tfrac{Q^2}2=2s^4.$$
So $x^2$ and $x^4$ both satisfy the identity, and the solutions are $\boxed{P(x)=\alpha x^4+\beta x^2,\ \alpha,\beta\in\mathbb R}$.

### m62
source: mathnet
mathnet_id: 01zv
country: Benelux Mathematical Olympiad
competition: Benelux Mathematical Olympiad
type: answer
difficulty: 6
techniques: polynomials
statement:
Find all polynomials $p(x)$ with real coefficients such that
$$p(a+b-2c)+p(b+c-2a)+p(c+a-2b)=3p(a-b)+3p(b-c)+3p(c-a)$$
for all $a,b,c\in\mathbb R$.
asked:
Determine every real polynomial satisfying the identity for all real $a,b,c$.
technique:
Specialize the variables to get a one-variable identity $p(-2x)=p(x)+3p(-x)$, and compare coefficients of each power of $x$.
hint:
Put $a=b=c$, then put $b=c=0$.
hint:
In $p(-2x)=p(x)+3p(-x)$, the coefficient of $x^k$ gives $(-2)^k a_k=(1+3(-1)^k)a_k$. For which $k$ can $a_k\ne0$?
solution:
**Answer:** $p(x)=\alpha x^2+\beta x$ with $\alpha,\beta\in\mathbb R$.

**Necessity.** With $a=b=c$ we get $3p(0)=9p(0)$, so $p(0)=0$. With $b=c=0$ the arguments on the left are $a,-2a,a$ and on the right $a,0,-a$, so
$$p(-2a)+2p(a)=3p(a)+3p(0)+3p(-a),\quad\text{i.e.}\quad p(-2x)=p(x)+3p(-x)$$
for all $x$. Let $p(x)=\sum a_kx^k$. Comparing coefficients of $x^k$: $(-2)^ka_k=(1+3(-1)^k)a_k$. For even $k$ this says $2^k=4$ or $a_k=0$, so $a_k=0$ unless $k=2$. For odd $k$ it says $-2^k=-2$ or $a_k=0$, so $a_k=0$ unless $k=1$. Hence $p(x)=\alpha x^2+\beta x$.

**Sufficiency.** The condition is linear in $p$, so check $x$ and $x^2$. For $p(x)=x$ both sides are $0$, since the three arguments on each side add to $0$. For $p(x)=x^2$:
$$(a+b-2c)^2+(b+c-2a)^2+(c+a-2b)^2=6(a^2+b^2+c^2)-6(ab+bc+ca),$$
$$3\big((a-b)^2+(b-c)^2+(c-a)^2\big)=6(a^2+b^2+c^2)-6(ab+bc+ca).$$
So the solutions are $\boxed{p(x)=\alpha x^2+\beta x}$.

### m63
source: mathnet
mathnet_id: 06jk
country: Hong Kong
competition: CHKMO
type: answer
difficulty: 6
techniques: generating-functions, complex-numbers
statement:
Let $k$ be a positive integer. Find the number of nonnegative integers $n\le10^k$ satisfying both conditions:
(i) $n$ is divisible by $3$;
(ii) each decimal digit of $n$ is one of the digits $2$, $0$, $1$ or $7$.
asked:
Count the multiples of $3$ in $[0,10^k]$ whose decimal digits all lie in $\{0,1,2,7\}$.
technique:
Encode the digit strings in the polynomial $(1+x+x^2+x^7)^k$, whose exponents are digit sums, and extract the exponents divisible by $3$ with a cube root of unity.
hint:
$10^k$ itself fails (its digit sum is $1$). Pad the other numbers with leading zeros to exactly $k$ digits. Divisibility by $3$ depends only on the digit sum.
hint:
If $F(x)=\sum c_jx^j$, then $\sum_{3\mid j}c_j=\frac13\big(F(1)+F(\omega)+F(\omega^2)\big)$ with $\omega=e^{2\pi i/3}$.
hint:
Compute $1+\omega+\omega^2+\omega^7$.
solution:
**Answer:** $\dfrac{4^k+2}3$ if $3\mid k$, and $\dfrac{4^k-1}3$ otherwise.

The number $10^k$ has digit sum $1$, so it is not divisible by $3$. Every $n<10^k$ can be written with exactly $k$ digits using leading zeros, and since $0$ is an allowed digit, the numbers satisfying (ii) correspond bijectively to strings $d_1d_2\cdots d_k$ with each $d_i\in\{0,1,2,7\}$. Such a number is divisible by $3$ iff its digit sum is.

Let $F(x)=(1+x+x^2+x^7)^k=\sum_jc_jx^j$. Expanding the product, $c_j$ is the number of strings with digit sum $j$, so we need $N=\sum_{3\mid j}c_j$. Let $\omega=e^{2\pi i/3}$. Then $1+\omega^j+\omega^{2j}$ equals $3$ if $3\mid j$ and $0$ otherwise, so
$$3N=\sum_jc_j(1+\omega^j+\omega^{2j})=F(1)+F(\omega)+F(\omega^2).$$
Now $F(1)=4^k$. Since $\omega^3=1$ and $1+\omega+\omega^2=0$: $1+\omega+\omega^2+\omega^7=0+\omega=\omega$, and $1+\omega^2+\omega^4+\omega^{14}=1+\omega^2+\omega+\omega^2=\omega^2$. So
$$3N=4^k+\omega^k+\omega^{2k}.$$
If $3\mid k$, $\omega^k=\omega^{2k}=1$ and $N=\frac{4^k+2}3$. If $3\nmid k$, $\omega^k$ is a primitive cube root of unity and $\omega^k+\omega^{2k}=-1$, so $N=\frac{4^k-1}3$.
$$\boxed{N=\tfrac{4^k+2}{3}\ \text{if }3\mid k,\qquad N=\tfrac{4^k-1}{3}\ \text{if }3\nmid k}$$

### m64
source: mathnet
mathnet_id: 09eu
country: Mongolia
competition: Mongolian Mathematical Olympiad
type: proof
difficulty: 8
techniques: generating-functions, polynomials
statement:
For a finite set $A=\{a_1,a_2,\dots,a_n\}$ of positive integers let $A^*$ be the multiset $\{a_i+a_j\mid1\le i<j\le n\}$. For instance, if $A=\{1,2,3,4\}$ then $A^*=\{3,4,5,5,6,7\}$. Let $A$ and $B$ be two different sets of positive integers, each with at least two elements, such that $A^*=B^*$. Prove that $|A|=|B|$ and that this common size is a power of $2$.
asked:
Two different sets with at least two elements have the same multiset of pairwise sums. Show they have the same size, and that the size is a power of $2$.
technique:
Encode each set by $f(x)=\sum_{a\in A}x^a$. The pairwise sums are encoded by $\frac{f(x)^2-f(x^2)}2$, so the hypothesis becomes a polynomial identity. Then look at the order of vanishing at $x=1$.
hint:
Show $\sum_{s\in A^*}x^s=\frac{f(x)^2-f(x^2)}2$, so $f(x)^2-g(x)^2=f(x^2)-g(x^2)$ where $g$ encodes $B$.
hint:
$f-g$ is a nonzero polynomial with $f(1)-g(1)=0$. Write $f(x)-g(x)=(x-1)^kh(x)$ with $h(1)\ne0$.
hint:
Factor $f(x^2)-g(x^2)$ the same way, cancel $(x-1)^k$, and set $x=1$.
solution:
Let $n=|A|$ and $m=|B|$. The multiset $A^*$ has $\binom n2$ elements and $B^*$ has $\binom m2$. Since $x\mapsto\binom x2$ is strictly increasing for integers $x\ge1$ and $n,m\ge2$, $A^*=B^*$ gives $n=m$.

Let $f(x)=\sum_{a\in A}x^a$ and $g(x)=\sum_{b\in B}x^b$. Expanding the square,
$$f(x)^2=\sum_{a\in A}x^{2a}+2\sum_{i<j}x^{a_i+a_j}=f(x^2)+2\sum_{s\in A^*}x^s,$$
where the last sum counts multiplicities. The same holds for $B$, so $A^*=B^*$ gives $f(x)^2-f(x^2)=g(x)^2-g(x^2)$, i.e.
$$\big(f(x)-g(x)\big)\big(f(x)+g(x)\big)=f(x^2)-g(x^2).\tag{1}$$
Since $A\ne B$, the polynomial $f-g$ is not zero. Also $f(1)-g(1)=n-n=0$, so $x-1$ divides it. Write $f(x)-g(x)=(x-1)^kh(x)$ with $k\ge1$, $h$ a polynomial and $h(1)\ne0$. Replacing $x$ by $x^2$, $f(x^2)-g(x^2)=(x^2-1)^kh(x^2)=(x-1)^k(x+1)^kh(x^2)$. Substituting in (1) and cancelling the nonzero factor $(x-1)^k$ (polynomials over $\mathbb R$ have no zero divisors):
$$h(x)\big(f(x)+g(x)\big)=(x+1)^kh(x^2).$$
At $x=1$: $h(1)\cdot2n=2^kh(1)$, and since $h(1)\ne0$, $n=2^{k-1}$. So $|A|=|B|=2^{k-1}$ is a power of $2$ (and $k\ge2$ because $n\ge2$). $\blacksquare$

### m65
source: mathnet
mathnet_id: 07fm
country: Iran
competition: 37th Iranian Mathematical Olympiad
type: proof
difficulty: 6
techniques: complex-numbers
statement:
Let $A_1,A_2,\dots,A_k$ be points on the unit circle. Prove that
$$\sum_{1\le i<j\le k}d(A_i,A_j)^2\le k^2,$$
where $d(A_i,A_j)$ denotes the distance between $A_i$ and $A_j$.
asked:
For $k$ points on a circle of radius $1$, show that the sum of the squared distances over all pairs is at most $k^2$.
technique:
Put the points in the complex plane as $z_i$ with $|z_i|=1$ and expand $|z_i-z_j|^2=(z_i-z_j)(\bar z_i-\bar z_j)$. The sum of the cross terms is controlled by $|z_1+\dots+z_k|^2$.
hint:
$|z_i-z_j|^2=2-(\bar z_iz_j+z_i\bar z_j)$ when $|z_i|=|z_j|=1$.
hint:
Expand $\left|\sum z_i\right|^2=\left(\sum z_i\right)\left(\sum\bar z_i\right)$ and identify the cross terms.
solution:
Place the unit circle in the complex plane and let $A_i$ correspond to $z_i$ with $|z_i|=1$. Then $d(A_i,A_j)^2=|z_i-z_j|^2=(z_i-z_j)(\bar z_i-\bar z_j)=2-(\bar z_iz_j+z_i\bar z_j)$. Summing over $i<j$:
$$\sum_{i<j}|z_i-z_j|^2=2\binom k2-\sum_{i\ne j}\bar z_iz_j,$$
where the last sum is over ordered pairs. On the other hand,
$$\Big|\sum_{i=1}^kz_i\Big|^2=\Big(\sum_iz_i\Big)\Big(\sum_j\bar z_j\Big)=\sum_i|z_i|^2+\sum_{i\ne j}\bar z_iz_j=k+\sum_{i\ne j}\bar z_iz_j.$$
Therefore
$$\sum_{i<j}d(A_i,A_j)^2=k(k-1)-\Big(\Big|\sum z_i\Big|^2-k\Big)=k^2-\Big|\sum_{i=1}^kz_i\Big|^2\le k^2.$$
Equality holds exactly when $z_1+\dots+z_k=0$, i.e. when the centroid of the points is the centre of the circle. $\blacksquare$

### m66
source: mathnet
mathnet_id: 0bnr
country: Romania
competition: 66th ROMANIAN MATHEMATICAL OLYMPIAD
type: answer
difficulty: 6
techniques: complex-numbers, coordinates
statement:
Find all complex numbers $z$ such that
$$|z|+|z-5i|=|z-2i|+|z-3i|.$$
asked:
Determine every complex $z$ whose distances to $0$ and $5i$ add up to the same total as its distances to $2i$ and $3i$.
technique:
The points $2i$ and $3i$ are weighted averages of $0$ and $5i$. Write $z-2i$ and $z-3i$ as the same weighted averages of $z$ and $z-5i$ and use the triangle inequality; the problem becomes its equality case.
hint:
$2i=\frac35\cdot0+\frac25\cdot5i$. So $z-2i=\frac35z+\frac25(z-5i)$. Do the same for $3i$.
hint:
The triangle inequality gives $|z-2i|+|z-3i|\le|z|+|z-5i|$ for every $z$. When is it an equality?
hint:
Equality in $|u+v|\le|u|+|v|$ needs $u$ and $v$ to point in the same direction (or one of them to be $0$).
solution:
**Answer:** $z=yi$ with $y$ real and $y\le0$ or $y\ge5$.

Since $z-2i=\frac35z+\frac25(z-5i)$ and $z-3i=\frac25z+\frac35(z-5i)$, the triangle inequality gives
$$|z-2i|\le\tfrac35|z|+\tfrac25|z-5i|,\qquad|z-3i|\le\tfrac25|z|+\tfrac35|z-5i|.$$
Adding: $|z-2i|+|z-3i|\le|z|+|z-5i|$ for every $z$. So the equation holds iff both inequalities are equalities.

Equality in $|u+v|\le|u|+|v|$ holds iff $u=0$, $v=0$, or $v=\lambda u$ with $\lambda>0$. Positive scalar factors do not change this, so both equalities hold iff $z=0$, or $z=5i$, or $z-5i=\lambda z$ for some $\lambda>0$. In the last case $\lambda\ne1$ (as $5i\ne0$), and $z=\frac{5i}{1-\lambda}=yi$ with $y=\frac5{1-\lambda}$; for $0<\lambda<1$ this gives all $y>5$, and for $\lambda>1$ all $y<0$. Together with $z=0$ and $z=5i$, the equality cases are exactly $z=yi$ with $y\le0$ or $y\ge5$.

Check directly: for $z=yi$ with $y\le0$ both sides equal $5-2y$, and for $y\ge5$ both sides equal $2y-5$. So
$$\boxed{z=yi,\ y\in(-\infty,0]\cup[5,\infty)}.$$

### m67
source: mathnet
mathnet_id: 0a7l
country: Nordic Mathematical Olympiad
competition: Nordic Mathematical Contest, NMC 7
type: proof
difficulty: 6
techniques: trigonometry
statement:
A hexagon is inscribed in a circle of radius $r$. Two of the sides of the hexagon have length $1$, two have length $2$ and two have length $3$. Show that $r$ satisfies the equation
$$2r^3-7r-3=0.$$
asked:
A cyclic hexagon has sides $1,1,2,2,3,3$ in some order. Show that its circumradius $r$ is a root of $2r^3-7r-3$.
technique:
A chord of length $\ell$ cuts off an arc whose half-angle $\phi$ satisfies $\ell=2r\sin\phi$. The six arcs fill the circle, which gives one trigonometric relation among three half-angles.
hint:
Let the arcs cut off by the sides have measures $2\phi_1,\dots,2\phi_6$ summing to $360^\circ$. Show that sides of equal length cut off equal arcs, all less than $180^\circ$.
hint:
With half-angles $\alpha,\beta,\gamma$ for lengths $1,2,3$ you get $\alpha+\beta+\gamma=90^\circ$. Then $\sin\gamma=\cos(\alpha+\beta)$.
hint:
Expand $\cos(\alpha+\beta)$, isolate the product of cosines and square.
solution:
The six vertices split the circle into six arcs (each not containing other vertices), with measures adding to $360^\circ$. A side cutting off an arc of measure $\theta\in(0^\circ,360^\circ)$ has length $2r\sin\frac\theta2$.

**Equal sides cut off equal arcs.** Two sides of the same length $\ell$ cut off arcs $\theta,\theta'$ with $\sin\frac\theta2=\sin\frac{\theta'}2$, so $\theta'=\theta$ or $\theta'=360^\circ-\theta$. The second option would make these two arcs fill the whole circle, leaving nothing for the other four arcs; so $\theta'=\theta$. Hence the arcs are $2\alpha,2\alpha,2\beta,2\beta,2\gamma,2\gamma$ for the lengths $1,2,3$, with $4(\alpha+\beta+\gamma)=360^\circ$, i.e. $\alpha+\beta+\gamma=90^\circ$. All of $\alpha,\beta,\gamma$ lie in $(0^\circ,90^\circ)$ and
$$\sin\alpha=\frac1{2r},\qquad\sin\beta=\frac1r,\qquad\sin\gamma=\frac3{2r}.$$
**The equation.** Since $\gamma=90^\circ-(\alpha+\beta)$, $\sin\gamma=\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta$, so
$$\cos\alpha\cos\beta=\frac3{2r}+\frac1{2r^2}=\frac{3r+1}{2r^2}.$$
The cosines are positive, $\cos\alpha=\sqrt{1-\frac1{4r^2}}$ and $\cos\beta=\sqrt{1-\frac1{r^2}}$. Squaring and multiplying by $4r^4$:
$$(4r^2-1)(r^2-1)=(3r+1)^2\iff4r^4-5r^2+1=9r^2+6r+1\iff2r(2r^3-7r-3)=0.$$
As $r>0$, we get $2r^3-7r-3=0$. $\blacksquare$

### m68
source: mathnet
mathnet_id: 0cyu
country: Saudi Arabia
competition: Saudi Arabia Mathematical Competitions
type: answer
difficulty: 7
techniques: trigonometry
statement:
Pentagon $ABCDE$ is inscribed in a circle. The distances from point $E$ to the lines $AB$, $BC$ and $CD$ are equal to $a$, $b$ and $c$, respectively. Find the distance from point $E$ to the line $AD$.
asked:
For a point $E$ on the circle through $A,B,C,D$, express its distance to line $AD$ in terms of its distances $a,b,c$ to lines $AB,BC,CD$.
technique:
Find a formula for the distance from a point of the circle to a chord in terms of the distances from that point to the chord's endpoints. The law of sines in the inscribed triangle does this.
hint:
For a chord $XY$ and a point $E$ of the circle, the distance from $E$ to line $XY$ is $EX\sin\angle EXY$.
hint:
By the extended law of sines in triangle $EXY$, $EY=2R\sin\angle EXY$, where $R$ is the radius. So the distance equals $\frac{EX\cdot EY}{2R}$.
hint:
Multiply the distances to $AB$ and $CD$, and compare with the product of the distances to $BC$ and $AD$.
solution:
**Answer:** $\dfrac{ac}b$.

Let $R$ be the radius of the circle. **Lemma.** If $X,Y,E$ are distinct points of the circle, the distance from $E$ to line $XY$ equals $\frac{EX\cdot EY}{2R}$.

*Proof.* The distance is $EX\sin\angle EXY$, where $\angle EXY\in(0^\circ,180^\circ)$ is the angle of triangle $EXY$ at $X$. The circle is the circumcircle of triangle $EXY$, so by the extended law of sines $EY=2R\sin\angle EXY$. Substituting $\sin\angle EXY=\frac{EY}{2R}$ gives the claim. $\square$

The vertices $A,B,C,D,E$ are distinct points of the circle, so the lemma applies to each of the chords $AB,BC,CD,DA$:
$$a\cdot c=\frac{EA\cdot EB}{2R}\cdot\frac{EC\cdot ED}{2R}=\frac{EA\cdot EB\cdot EC\cdot ED}{4R^2}=\frac{EB\cdot EC}{2R}\cdot\frac{ED\cdot EA}{2R}=b\cdot d,$$
where $d$ is the distance from $E$ to $AD$. Since $E$ is not on line $BC$ (a line meets the circle in at most two points), $b>0$, and so $d=\boxed{\dfrac{ac}{b}}$.

### m69
source: mathnet
mathnet_id: 01b7
country: Baltic Way
competition: Baltic Way
type: answer
difficulty: 7
techniques: trigonometry
statement:
Positive real numbers $a,b,c,d$ satisfy
$$a^2+d^2-ad=b^2+c^2+bc\quad\text{and}\quad a^2+b^2=c^2+d^2.$$
Find all possible values of the expression $\dfrac{ab+cd}{ad+bc}$.
asked:
Under the two given equations, determine every value the ratio $\frac{ab+cd}{ad+bc}$ can take.
technique:
The second equation says $(a,b)$ and $(c,d)$ have the same length. Parametrize both by angles on a circle of that radius, and turn the first equation into a trigonometric equation.
hint:
Let $T^2=a^2+b^2=c^2+d^2$ and write $a=T\sin\alpha$, $b=T\cos\alpha$, $c=T\sin\beta$, $d=T\cos\beta$ with $\alpha,\beta\in(0,\frac\pi2)$.
hint:
The first equation becomes $\cos2\beta-\cos2\alpha=\sin(\alpha+\beta)$. Use a sum-to-product formula.
hint:
Express both $ab+cd$ and $ad+bc$ through $\sin(\alpha+\beta)$ and $\cos(\alpha-\beta)$.
solution:
**Answer:** $\dfrac{\sqrt3}2$.

Let $T>0$ with $T^2=a^2+b^2=c^2+d^2$. Since $a,b,c,d>0$ there are $\alpha,\beta\in(0,\frac\pi2)$ with $a=T\sin\alpha$, $b=T\cos\alpha$, $c=T\sin\beta$, $d=T\cos\beta$. Dividing the first equation by $T^2$:
$$\sin^2\alpha+\cos^2\beta-\sin\alpha\cos\beta=\sin^2\beta+\cos^2\alpha+\cos\alpha\sin\beta.$$
Since $\cos^2\beta-\sin^2\beta=\cos2\beta$ and $\sin^2\alpha-\cos^2\alpha=-\cos2\alpha$, this is
$$\cos2\beta-\cos2\alpha=\sin\alpha\cos\beta+\cos\alpha\sin\beta=\sin(\alpha+\beta).$$
By the sum-to-product formula, $\cos2\beta-\cos2\alpha=2\sin(\alpha+\beta)\sin(\alpha-\beta)$. As $0<\alpha+\beta<\pi$, $\sin(\alpha+\beta)>0$, so $\sin(\alpha-\beta)=\frac12$. Since $-\frac\pi2<\alpha-\beta<\frac\pi2$, $\alpha-\beta=\frac\pi6$.

Now
$$ab+cd=T^2(\sin\alpha\cos\alpha+\sin\beta\cos\beta)=\tfrac{T^2}2(\sin2\alpha+\sin2\beta)=T^2\sin(\alpha+\beta)\cos(\alpha-\beta),$$
$$ad+bc=T^2(\sin\alpha\cos\beta+\cos\alpha\sin\beta)=T^2\sin(\alpha+\beta).$$
So the ratio is $\cos(\alpha-\beta)=\cos\frac\pi6=\frac{\sqrt3}2$.

The value is attained: $\alpha=\frac\pi3$, $\beta=\frac\pi6$, $T=1$ give $a=d=\frac{\sqrt3}2$, $b=c=\frac12$, and indeed $a^2+d^2-ad=\frac34=b^2+c^2+bc$ and $a^2+b^2=1=c^2+d^2$. The only possible value is $\boxed{\tfrac{\sqrt3}{2}}$.

### m70
source: mathnet
mathnet_id: 08rn
country: Japan
competition: The 16th Japanese Mathematical Olympiad - The First Round
type: answer
difficulty: 7
techniques: coordinates, symmetry
statement:
The triangle $ABC$ satisfies $BC=5$, $CA=7$ and $AB=8$. Let $O$ be a point inside the triangle $ABC$ such that the triangles $OBC$, $OCA$ and $OAB$ have the same circumradius. Find this common circumradius.
asked:
A point inside the $5$-$7$-$8$ triangle makes the three triangles it forms with the sides have equal circumradii. Find that radius.
technique:
Use vectors (or complex coordinates). Two circles of equal radius through the same two points have centres symmetric about the midpoint of those points; this lets you write $A,B,C$ in terms of $O$ and the three centres.
hint:
Let $O_1,O_2,O_3$ be the circumcentres of $OBC,OCA,OAB$ and $\rho$ the common radius. $O_1$ and $O_2$ are both at distance $\rho$ from $O$ and from $C$. Show $O_1+O_2=O+C$ as vectors.
hint:
So $C=O_1+O_2-O$, and similarly for $A$ and $B$. Find a point at distance $\rho$ from all of $A,B,C$.
hint:
Conclude $\rho$ is the circumradius of $ABC$; compute it, and check that a valid $O$ exists.
solution:
**Answer:** $\dfrac{7\sqrt3}3$.

Let $\rho$ be the common circumradius and $O_1,O_2,O_3$ the circumcentres of $OBC,OCA,OAB$. Treat points as vectors.

**$O_1\ne O_2$.** Otherwise the circles $OBC$ and $OCA$ coincide (same centre and radius), so $A,B,C,O$ lie on one circle, the circumcircle of $ABC$. But a point strictly inside the triangle is strictly inside its circumcircle. So $O_1\ne O_2$, and likewise the three centres are distinct.

**Expressing the vertices.** $O_1$ and $O_2$ are two different points at distance $\rho$ from both $O$ and $C$, so they are the two intersection points of the circles of radius $\rho$ about $O$ and about $C$. These two intersection points are symmetric about the midpoint of $OC$ (the configuration is symmetric in the line $OC$ and in the perpendicular bisector of $OC$). Hence $O_1+O_2=O+C$, i.e. $C=O_1+O_2-O$. Similarly $A=O_2+O_3-O$ and $B=O_3+O_1-O$.

**The circumradius.** Let $K=O_1+O_2+O_3-2O$. Then $K-A=O_1-O$, $K-B=O_2-O$, $K-C=O_3-O$, all of length $\rho$. So $K$ is the circumcentre of $ABC$ and $\rho$ equals its circumradius $R$.

**Computing $R$.** By the law of cosines, $\cos B=\frac{8^2+5^2-7^2}{2\cdot8\cdot5}=\frac12$, so $B=60^\circ$ and $R=\frac{CA}{2\sin B}=\frac7{\sqrt3}=\frac{7\sqrt3}3$.

**Existence.** The triangle is acute ($5^2+7^2>8^2$), so its orthocentre $H$ lies inside it. Since $\angle BHC=180^\circ-\angle A$, the circumradius of $HBC$ is $\frac{BC}{2\sin\angle BHC}=\frac{a}{2\sin A}=R$, and likewise for $HCA$ and $HAB$. So $O=H$ is such a point, and the common circumradius is $\boxed{\tfrac{7\sqrt3}{3}}$.

### m71
source: mathnet
mathnet_id: 0g3u
country: Switzerland
competition: Final round
type: answer
difficulty: 6
techniques: coordinates
statement:
Let $k$ be a circle with centre $M$ and let $AB$ be a diameter of $k$. Let $C$ be a point on $k$ such that $AC=AM$. Let $D$ be the point on the line $AC$ such that $CD=AB$ and $C$ lies between $A$ and $D$. Let $E$ be the second intersection of the circumcircle of $BCD$ with the line $AB$, and let $F$ be the intersection of the lines $ED$ and $BC$. The line $AF$ cuts the segment $BD$ in $X$. Determine the ratio $BX/XD$.
asked:
Following the construction, find the ratio in which $X$ divides the segment $BD$.
technique:
Every point here is easy to place in coordinates once you see that triangle $AMC$ is equilateral. The only point needing an idea is $E$: think about what the circle $BCD$ tells you about the point $A$.
hint:
Take radius $1$, $A=(0,0)$, $B=(2,0)$, $M=(1,0)$. Then $AC=AM=MC=1$; find $C$ and $D$.
hint:
The power of $A$ with respect to circle $BCD$ equals $AC\cdot AD$, and also $AB\cdot AE$. This gives $E$.
hint:
Line $ED$ turns out to be vertical. Find $F$ on $BC$, then intersect line $AF$ with $BD$.
solution:
**Answer:** $\dfrac16$.

Scale so that the radius is $1$, and put $A=(0,0)$, $M=(1,0)$, $B=(2,0)$. Since $AC=AM=1=MC$, triangle $AMC$ is equilateral; by symmetry in line $AB$ we may take $C=\left(\frac12,\frac{\sqrt3}2\right)$. Then $AD=AC+CD=1+2=3$ with $D$ on ray $AC$, so $D=3C=\left(\frac32,\frac{3\sqrt3}2\right)$.

**The point $E$.** Write the circle $BCD$ as $x^2+y^2+ux+vy+w=0$. Its points on the $x$-axis satisfy $x^2+ux+w=0$, whose roots are $2$ (for $B$) and the abscissa $e$ of $E$, so $2e=w$. Also $w$ is the power of $A=(0,0)$ with respect to this circle. Line $AC$ meets the circle at $C$ and $D$, both on the same side of $A$, so this power is $AC\cdot AD=1\cdot3=3$. Hence $w=3$, $e=\frac32$, and $E=\left(\frac32,0\right)$, which is different from $B$.

**The point $F$.** $E$ and $D$ both have abscissa $\frac32$, so line $ED$ is $x=\frac32$. Points of line $BC$ are $B+t(C-B)=\left(2-\frac32t,\frac{\sqrt3}2t\right)$; $x=\frac32$ gives $t=\frac13$, so $F=\left(\frac32,\frac{\sqrt3}6\right)$.

**The point $X$.** Points of segment $BD$ are $B+u(D-B)=\left(2-\frac u2,\frac{3\sqrt3}2u\right)$ with $0\le u\le1$; points of line $AF$ are $\lambda\left(\frac32,\frac{\sqrt3}6\right)$. Equating second coordinates gives $\lambda=9u$, and then the first coordinates give $2-\frac u2=\frac{27u}2$, so $u=\frac17$. Hence $X$ divides $BD$ with $BX=\frac17BD$ and $XD=\frac67BD$, and
$$\frac{BX}{XD}=\boxed{\frac16}.$$

### m72
source: mathnet
mathnet_id: 0ebb
country: Slovenia
competition: Selection Examinations for the IMO 2015
type: proof
difficulty: 8
techniques: similar-triangles, trigonometry
statement:
Let $P$ and $Q$ be two points in the interior of the triangle $ABC$ such that $\angle PAC=\angle BAQ$ and $\angle CBP=\angle QBA$. Denote by $P_A,P_B,P_C$ the orthogonal projections of $P$ onto the sides $BC,CA,AB$, and by $Q_A,Q_B,Q_C$ the orthogonal projections of $Q$ onto the sides $BC,CA,AB$. Prove that the points $P_A,P_B,P_C,Q_A,Q_B,Q_C$ lie on one circle.
asked:
For two interior points whose lines from $A$ and from $B$ are reflections of each other in the angle bisectors, show that the six feet of perpendiculars to the side lines are concyclic.
technique:
The natural centre is the midpoint $M$ of $PQ$. The equal angles make right triangles at a vertex similar, which turns into an equality of products of distances from that vertex; read that equality as a statement about powers of the vertex.
hint:
Let $M$ be the midpoint of $PQ$. The projection of $M$ onto a side line is the midpoint of the two feet on that line, so $M$ is equidistant from $P_B$ and $Q_B$. Call this distance $\rho_B$; define $\rho_A,\rho_C$ similarly. You must show $\rho_A=\rho_B=\rho_C$.
hint:
For a point $X$ on line $CA$, show that $XM^2-\rho_B^2$ equals the product of the signed distances $XP_B\cdot XQ_B$ along the line.
hint:
At vertex $A$, the right triangles $APP_B$ and $AQQ_C$ are similar, and so are $APP_C$ and $AQQ_B$. Deduce $AP_B\cdot AQ_B=AP_C\cdot AQ_C$ (with signs).
solution:
Let $M$ be the midpoint of $PQ$ (if $P=Q$, then $M=P$).

**Step 1: a circle on each side line.** Orthogonal projection onto a line maps midpoints to midpoints, so the foot $N$ of $M$ on line $CA$ is the midpoint of $P_BQ_B$. Hence $MP_B=MQ_B=:\rho_B$. Define $\rho_C=MP_C=MQ_C$ and $\rho_A=MP_A=MQ_A$ in the same way. It suffices to prove $\rho_A=\rho_B=\rho_C$: then all six points lie on the circle with centre $M$.

**Step 2: power along a line.** Give line $CA$ a coordinate, and let $N$, $P_B$, $Q_B$ have coordinates $\nu$, $\nu-\delta$, $\nu+\delta$. For a point $X$ on the line with coordinate $x$, by Pythagoras
$$XM^2-\rho_B^2=\big((x-\nu)^2+MN^2\big)-\big(\delta^2+MN^2\big)=(x-\nu+\delta)(x-\nu-\delta),$$
which is the product of the signed distances from $X$ to $P_B$ and to $Q_B$. The same holds on the other side lines.

**Step 3: the vertex $A$.** Measure signed distances from $A$ along ray $AC$ and along ray $AB$. The foot of $P$ on line $AC$ is at signed distance $\overline{AP_B}=AP\cos\angle PAC$ from $A$, and similarly $\overline{AQ_B}=AQ\cos\angle QAC$, $\overline{AP_C}=AP\cos\angle PAB$, $\overline{AQ_C}=AQ\cos\angle QAB$. (When the angles are acute this is just the similarity of the right triangles $APP_B$ and $AQQ_C$, and of $APP_C$ and $AQQ_B$.) Since $P$ and $Q$ are inside the angle $BAC$, $\angle PAB=\angle BAC-\angle PAC=\angle BAC-\angle BAQ=\angle QAC$. Therefore
$$\overline{AP_B}\cdot\overline{AQ_B}=AP\cos\angle PAC\cdot AQ\cos\angle QAC=AP\cos\angle QAB\cdot AQ\cos\angle PAB=\overline{AP_C}\cdot\overline{AQ_C}.$$
By Step 2 applied at $X=A$ on lines $CA$ and $AB$: $AM^2-\rho_B^2=AM^2-\rho_C^2$, so $\rho_B=\rho_C$.

**Step 4: the vertex $B$.** In the same way, $\angle CBP=\angle QBA$ and $\angle PBA=\angle CBA-\angle CBP=\angle QBC$ give $\overline{BP_A}\cdot\overline{BQ_A}=\overline{BP_C}\cdot\overline{BQ_C}$, hence $BM^2-\rho_A^2=BM^2-\rho_C^2$ and $\rho_A=\rho_C$.

So $\rho_A=\rho_B=\rho_C$, and the six points lie on the circle with centre $M$ and this radius. $\blacksquare$

### m73
source: mathnet
mathnet_id: 0b84
country: Romania
competition: Romanian Mathematical Olympiad
type: proof
difficulty: 6
techniques: similar-triangles
statement:
Prove that a triangle $ABC$ is similar to the triangle whose sides are the medians of $ABC$ if and only if the squares of the side lengths of $ABC$ form an arithmetic sequence.
asked:
Let $m_a,m_b,m_c$ be the medians of a triangle with sides $a,b,c$. Show that the triangle with sides $m_a,m_b,m_c$ is similar to $ABC$ exactly when $a^2,b^2,c^2$ (in some order) form an arithmetic progression.
technique:
Two triangles are similar exactly when their sides, sorted by length, are proportional. The median formula $4m_a^2=2b^2+2c^2-a^2$ tells you how the medians are ordered.
hint:
Assume $a\le b\le c$. Compute $m_a^2-m_b^2$. Which median is shortest?
hint:
Similarity then means $\frac{m_c}a=\frac{m_b}b=\frac{m_a}c$. Use $\frac{m_a^2}{c^2}=\frac{m_c^2}{a^2}$ and factor.
solution:
Recall $m_a^2=\frac14(2b^2+2c^2-a^2)$ and the analogous formulas. Label the sides so that $a\le b\le c$. Since $m_a^2-m_b^2=\frac34(b^2-a^2)\ge0$ and $m_b^2-m_c^2=\frac34(c^2-b^2)\ge0$, we have $m_c\le m_b\le m_a$. Two triangles are similar iff their sides in increasing order are proportional, so the triangles are similar iff
$$\frac{m_c}a=\frac{m_b}b=\frac{m_a}c.\tag{1}$$
Also, since $a^2\le b^2\le c^2$, the squares form an arithmetic sequence (in some order) iff $2b^2=a^2+c^2$.

**If $2b^2=a^2+c^2$:** then $4m_a^2=2b^2+2c^2-a^2=3c^2$, $4m_b^2=2a^2+2c^2-b^2=3b^2$, $4m_c^2=2a^2+2b^2-c^2=3a^2$. So all three ratios in (1) equal $\frac{\sqrt3}2$, and the triangles are similar.

**Conversely, assume (1).** From $\frac{m_a^2}{c^2}=\frac{m_c^2}{a^2}$:
$$a^2(2b^2+2c^2-a^2)=c^2(2a^2+2b^2-c^2)\iff2b^2(a^2-c^2)=a^4-c^4\iff(a^2-c^2)(2b^2-a^2-c^2)=0.$$
If $a^2=c^2$ then $a=b=c$, and the squares form a constant (hence arithmetic) sequence; in this case also $2b^2=a^2+c^2$. Otherwise $2b^2=a^2+c^2$. Either way the squares of the sides form an arithmetic sequence. $\blacksquare$

### m74
source: mathnet
mathnet_id: 08v7
country: Japan
competition: Japan Junior Mathematical Olympiad
type: answer
difficulty: 7
techniques: angle-chasing
statement:
Let $I$ and $O$ be the incenter and circumcenter of a triangle $ABC$, respectively. If $AB=2$, $AC=3$ and $\angle AIO=90^\circ$, what is the area of the triangle $ABC$?
asked:
Given two sides $2$ and $3$ from $A$ and a right angle between $IA$ and $IO$, find the area of the triangle.
technique:
Extend $AI$ to meet the circumcircle again, and ask what the right angle at $I$ says about $I$ on that chord. The rest comes from angle chasing and a classical cyclic-quadrilateral relation.
hint:
Let $AI$ meet the circumcircle again at $L$. The perpendicular from the centre $O$ to a chord bisects it. What does this say about $I$?
hint:
Show $\angle LBI=\angle LIB$, so $LB=LI$; also $LB=LC$.
hint:
Apply Ptolemy's theorem to the cyclic quadrilateral $ABLC$.
solution:
**Answer:** $\dfrac{15\sqrt7}{16}$.

Let $a=BC$, $b=CA=3$, $c=AB=2$, and let $\alpha,\beta$ be the angles at $A$, $B$. Let line $AI$ (the bisector from $A$) meet the circumcircle again at $L$, the midpoint of arc $BC$ not containing $A$. The angle $\angle AIO$ is defined, so $I\ne O$.

**$I$ is the midpoint of $AL$.** $OI\perp AL$ and $I$ lies on the chord $AL$, so $I$ is the foot of the perpendicular from the centre $O$ to this chord, which is its midpoint. Hence $AL=2IL$.

**$LB=LC=LI$.** $LB=LC$ since $L$ is the midpoint of arc $BC$. Inscribed angles give $\angle LBC=\angle LAC=\frac\alpha2$, so $\angle LBI=\frac\alpha2+\frac\beta2$. The exterior angle of triangle $ABI$ at $I$ is $\angle LIB=\angle IAB+\angle IBA=\frac\alpha2+\frac\beta2$. So triangle $LBI$ is isosceles with $LB=LI$.

**Ptolemy.** In the cyclic quadrilateral $ABLC$ (vertices in this order on the circle), $AL\cdot BC=AB\cdot LC+AC\cdot BL$. With $AL=2LB$ and $LC=LB$:
$$2LB\cdot a=LB\,(b+c)\quad\Longrightarrow\quad a=\frac{b+c}2=\frac52.$$
**Area.** Heron's formula with $s=\frac{2+3+\frac52}2=\frac{15}4$:
$$[ABC]^2=\frac{15}4\cdot\frac54\cdot\frac34\cdot\frac74=\frac{1575}{256},\qquad[ABC]=\frac{15\sqrt7}{16}.$$
**Consistency.** Conversely, for the triangle with sides $2,3,\frac52$ the same Ptolemy relation gives $AL=2LB=2LI$, so $I$ is the midpoint of $AL$; the triangle is not equilateral, so $I\ne O$, and since $OA=OL$, $OI\perp AL$, i.e. $\angle AIO=90^\circ$. So the configuration exists, and the area is $\boxed{\tfrac{15\sqrt7}{16}}$.
