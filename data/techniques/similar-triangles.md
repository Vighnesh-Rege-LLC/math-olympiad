---
id: similar-triangles
name: Similar triangles and power of a point
group: Geometry
related: [angle-chasing, trigonometry, coordinates]
---
## What it is
Triangles are **similar** when their angles are equal; then corresponding sides are proportional. The criteria: AA (two equal angles), SAS (an equal included angle between two pairs of proportional sides), SSS (proportional sides).

Equal ratios turn into equations: if $\triangle XYZ\sim\triangle X'Y'Z'$ then $\dfrac{XY}{X'Y'}=\dfrac{YZ}{Y'Z'}=\dfrac{XZ}{X'Z'}$.

**Power of a point:** for a point $P$ and a circle, for any line through $P$ meeting the circle at $X$ and $Y$, the product $PX\cdot PY$ is the same. If $P$ is outside and $PT$ is a tangent, $PT^2=PX\cdot PY$.

It works because proportionality links lengths that are far apart in the figure. Similar triangles are often hidden in circles, parallel lines, and right triangles with an altitude.

## Recognize
- Parallel lines (equal corresponding angles).
- A right triangle with an altitude to the hypotenuse.
- Two lines through a point meeting a circle in a secant-secant or secant-tangent pattern.
- A claim of the form $AB\cdot CD=EF\cdot GH$ (a product of lengths), which suggests two ratios.

## Example: Tangent and secant
**Problem.** From a point $P$ outside a circle, a tangent $PT$ touches the circle at $T$, and a secant through $P$ meets the circle at $A$ then $B$ ($A$ is nearer $P$). Show $PT^2=PA\cdot PB$. Then find $AB$ if $PT=6$ and $PA=4$.
1. Triangles $PTA$ and $PBT$ share the angle at $P$.
2. By the tangent-chord angle, $\angle PTA=\angle PBT$ (both subtend chord $TA$).
3. So $\triangle PTA\sim\triangle PBT$ (AA), and $\dfrac{PT}{PB}=\dfrac{PA}{PT}$, i.e. $PT^2=PA\cdot PB$.
4. With $PT=6$ and $PA=4$: $36=4\cdot PB$, so $PB=9$.
5. Since $A$ lies between $P$ and $B$, $AB=PB-PA=5$.

## Example: Altitude of a right triangle
**Problem.** In right triangle $ABC$ (right angle at $C$) let $CH$ be the altitude to the hypotenuse, with $AH=p$ and $HB=q$. Show that $CH^2=pq$.
1. In right triangle $AHC$ the angles are $A$ at vertex $A$, $90^\circ$ at $H$, and $90^\circ-A$ at $C$.
2. In right triangle $CHB$ the angles are $B=90^\circ-A$ at vertex $B$, $90^\circ$ at $H$, and $A$ at $C$.
3. So $\triangle AHC\sim\triangle CHB$ (with $A\leftrightarrow C$, $H\leftrightarrow H$, $C\leftrightarrow B$). Corresponding sides give $\dfrac{AH}{CH}=\dfrac{CH}{HB}$, i.e. $\dfrac p{CH}=\dfrac{CH}q$.
4. Hence $CH^2=pq$.

## Mistakes
- Matching vertices in the wrong order. Write the similarity as $\triangle ABC\sim\triangle DEF$ with correspondences, and read ratios from it.
- Assuming similarity from one equal angle only.
- Using power of a point with inside/outside confusion: for a point inside the circle, $PA\cdot PB$ uses the two parts of the chord.
- Forgetting that a tangent is a limit case of a secant.

## Variations
- **Homothety:** a scaling from a point maps one figure to a similar one.
- **Ratios of areas:** areas of similar figures scale by the square of the ratio.
- **Radical axis:** the set of points with equal power with respect to two non-concentric circles is a line.
- **Menelaus and Ceva:** ratio conditions for collinearity and concurrency.
- **Trigonometric form:** the law of sines is a similarity statement in disguise ([[trigonometry]]).
