---
id: complex-numbers
name: Complex numbers in geometry
group: Geometry
related: [coordinates, trigonometry, polynomials]
---
## What it is
Identify the plane with $\mathbb C$: the point $(x,y)$ is $z=x+yi$. Then:
- **Multiplication by $e^{i\theta}$ rotates** a point about $0$ by $\theta$. Multiplication by a real $k>0$ scales it.
- To rotate $B$ about $A$ by $\theta$: $B'=A+e^{i\theta}(B-A)$.
- $|z-w|$ is the distance, and $|z|^2=z\bar z$.
- The $n$th roots of unity $\omega^k=e^{2\pi ik/n}$ are the vertices of a regular $n$-gon, and they satisfy $1+\omega+\dots+\omega^{n-1}=0$.
- A point on the unit circle has $\bar z=1/z$, which removes conjugates from many computations.

It works because rotation and similarity, which are awkward with coordinates, become single multiplications. Regular polygons and unit circles become algebra.

## Recognize
- Rotations, squares, equilateral triangles, or regular polygons.
- A circle, which you can place as the unit circle.
- A statement about angles of $60^\circ$, $90^\circ$ or $120^\circ$ (these correspond to simple multipliers $e^{i\pi/3}$, $i$, $e^{2\pi i/3}$).
- Sums or products over roots of unity.

## Example: An equilateral triangle test
**Problem.** Show that distinct complex numbers $a,b,c$ are the vertices of an equilateral triangle if and only if $a^2+b^2+c^2=ab+bc+ca$.
1. Triangle $abc$ is equilateral exactly when $c-a$ is $b-a$ rotated by $+60^\circ$ or $-60^\circ$. With $\zeta=e^{i\pi/3}$ this means $c-a=\zeta(b-a)$ or $c-a=\bar\zeta(b-a)$.2. Let $u=c-a$ and $v=b-a$. The condition is $(u-\zeta v)(u-\bar\zeta v)=0$.
3. Expand: $u^2-(\zeta+\bar\zeta)uv+\zeta\bar\zeta v^2$. Since $\zeta+\bar\zeta=2\cos60^\circ=1$ and $\zeta\bar\zeta=1$, this is $u^2-uv+v^2=0$.
4. Substitute back: $(c-a)^2-(c-a)(b-a)+(b-a)^2=a^2+b^2+c^2-ab-bc-ca$.
5. So the triangle is equilateral exactly when $a^2+b^2+c^2=ab+bc+ca$.

## Example: A product over roots of unity
**Problem.** Let $\omega=e^{2\pi i/n}$ for $n\ge2$. Show that $\prod_{k=1}^{n-1}|1-\omega^k|=n$. (Geometrically: the product of the distances from one vertex of a regular $n$-gon inscribed in a unit circle to the other vertices is $n$.)
1. The roots of $x^n-1$ are $1,\omega,\dots,\omega^{n-1}$, so $x^n-1=\prod_{k=0}^{n-1}(x-\omega^k)$.
2. Divide by $x-1$: $1+x+\dots+x^{n-1}=\prod_{k=1}^{n-1}(x-\omega^k)$.
3. Put $x=1$: $n=\prod_{k=1}^{n-1}(1-\omega^k)$.
4. Taking absolute values gives $\prod|1-\omega^k|=n$.

## Mistakes
- Using $\bar z=1/z$ for points not on the unit circle.
- Forgetting that rotating about a point other than $0$ needs the shift: $A+e^{i\theta}(B-A)$.
- Mixing up the direction of rotation ($+\theta$ is counterclockwise).
- Treating $|z|^2$ as $z^2$.

## Variations
- **Unit circle setup:** place a circumcircle as the unit circle, so points $a,b,c$ have $\bar a=1/a$, and chord/tangent conditions become algebraic.
- **Roots of unity filters:** see [[generating-functions]].
- **De Moivre:** $(\cos\theta+i\sin\theta)^n=\cos n\theta+i\sin n\theta$ for multiple-angle identities ([[trigonometry]]).
- **Rotation-scaling maps:** directly similar triangles correspond to $z\mapsto az+b$ (oppositely similar ones need $z\mapsto a\bar z+b$).
