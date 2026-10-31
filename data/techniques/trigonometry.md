---
id: trigonometry
name: Trigonometry in geometry
group: Geometry
related: [coordinates, complex-numbers, angle-chasing, similar-triangles]
---
## What it is
Use trigonometric relations to turn angles into lengths and back. In a triangle with sides $a,b,c$, opposite angles $A,B,C$, circumradius $R$ and area $K$:
- **Law of sines:** $\dfrac a{\sin A}=\dfrac b{\sin B}=\dfrac c{\sin C}=2R$.
- **Law of cosines:** $c^2=a^2+b^2-2ab\cos C$.
- **Area:** $K=\tfrac12ab\sin C=\dfrac{abc}{4R}$.
- **Identities:** $\sin(A\pm B)$, $\cos(A\pm B)$, $\sin2A=2\sin A\cos A$, $\sin^2A+\cos^2A=1$.

It works because the law of sines and cosines connect angles to side lengths, so a problem that mixes them becomes an equation in a few unknowns.

## Recognize
- A triangle given by sides and angles together.
- Ratios of lengths governed by angles, like the angle bisector theorem.
- Conditions such as $a\cos B=b\cos A$ that mix sides and angles.
- A circle through the vertices (circumradius).

## Example: Showing a triangle is isosceles
**Problem.** In triangle $ABC$ suppose $a\cos B=b\cos A$. Show that $CA=CB$.
1. By the law of sines, $a=2R\sin A$ and $b=2R\sin B$.
2. Substitute: $2R\sin A\cos B=2R\sin B\cos A$, so $\sin A\cos B-\cos A\sin B=0$, i.e. $\sin(A-B)=0$.
3. Since $A$ and $B$ are angles of a triangle, $-180^\circ<A-B<180^\circ$, so $A-B=0$ and $A=B$.
4. Equal angles mean equal opposite sides: $a=b$, i.e. $CB=CA$.

## Example: Angle bisector ratio
**Problem.** In triangle $ABC$ the bisector from $A$ meets $BC$ at $D$. Show that $\dfrac{BD}{DC}=\dfrac{AB}{AC}$.
1. Let $\angle BAD=\angle DAC=\alpha$ and let $\theta=\angle ADB$, so $\angle ADC=180^\circ-\theta$.
2. Law of sines in triangle $ABD$: $\dfrac{BD}{\sin\alpha}=\dfrac{AB}{\sin\theta}$, so $BD=\dfrac{AB\sin\alpha}{\sin\theta}$.
3. Law of sines in triangle $ACD$: $\dfrac{DC}{\sin\alpha}=\dfrac{AC}{\sin(180^\circ-\theta)}=\dfrac{AC}{\sin\theta}$, so $DC=\dfrac{AC\sin\alpha}{\sin\theta}$.
4. Dividing, $\dfrac{BD}{DC}=\dfrac{AB}{AC}$.

## Example: A circumradius
**Problem.** Find the circumradius of the triangle with sides $13,14,15$.
1. Heron's formula: $s=21$, and $K=\sqrt{21\cdot8\cdot7\cdot6}=\sqrt{7056}=84$.
2. Use $K=\dfrac{abc}{4R}$: $R=\dfrac{13\cdot14\cdot15}{4\cdot84}=\dfrac{2730}{336}=\dfrac{65}8$.

## Mistakes
- Using the law of sines in the ambiguous case ($SSA$) without checking for two triangles.
- Concluding $A=B$ from $\sin A=\sin B$ in general. For two angles of one triangle it does give $A=B$, because the other possibility $A+B=180^\circ$ is impossible.
- Degree/radian mix-ups.
- Trying trigonometry when a clean synthetic argument exists. Check [[angle-chasing]] first, but do not hesitate to compute.

## Variations
- **Trigonometric Ceva:** for points $D,E,F$ on sides $BC,CA,AB$, the lines $AD,BE,CF$ are concurrent iff $\dfrac{\sin\angle BAD}{\sin\angle DAC}\cdot\dfrac{\sin\angle CBE}{\sin\angle EBA}\cdot\dfrac{\sin\angle ACF}{\sin\angle FCB}=1$.
- **Trigonometric identities in triangles:** $\tan A+\tan B+\tan C=\tan A\tan B\tan C$ when $A+B+C=180^\circ$ and no angle is $90^\circ$.
- **Product-to-sum / telescoping:** for sums of sines and cosines ([[telescoping]]).
- **Substitution:** replace variables by $\sin$ or $\tan$ to simplify an algebraic constraint.
