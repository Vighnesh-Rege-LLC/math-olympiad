import itertools, random, math
from fractions import Fraction as Fr
from math import comb, gcd, sin, cos, pi, radians, hypot, atan2, degrees
import sympy as sp

n_checks = 0
def ok(cond, msg):
    global n_checks
    assert cond, "FAILED: " + msg
    n_checks += 1

# o62
s = sum(k * math.factorial(k) for k in range(1, 10))
ok(s == 3628799 == math.factorial(10) - 1, "o62")
for n in range(1, 12):
    ok(sum(k * math.factorial(k) for k in range(1, n + 1)) == math.factorial(n + 1) - 1, f"o62 id {n}")

# o63
tot = sum(Fr(k, k**4 + k**2 + 1) for k in range(1, 11))
ok(tot == Fr(55, 111), "o63 value")
for k in range(1, 30):
    ok(Fr(k, k**4 + k**2 + 1) == Fr(1, 2) * (Fr(1, k*k - k + 1) - Fr(1, k*k + k + 1)), "o63 split")
    ok((k + 1)**2 - (k + 1) + 1 == k*k + k + 1, "o63 shift")

# o64
cnt = sum(1 for t in itertools.product(range(1, 7), repeat=4) if sum(t) == 14)
ok(cnt == 146, "o64 brute")
x = sp.symbols('x')
ok(sp.Poly(sp.expand((x + x**2 + x**3 + x**4 + x**5 + x**6)**4), x).coeff_monomial(x**14) == 146, "o64 gf")
ok(comb(13, 3) - 4 * comb(7, 3) == 146, "o64 incl-excl")

# o65: Euler partitions, small cases
def distinct_parts(n, maxp=None):
    if maxp is None: maxp = n
    if n == 0: return 1
    return sum(distinct_parts(n - k, k - 1) for k in range(1, min(n, maxp) + 1))
def odd_parts(n, maxp=None):
    if maxp is None: maxp = n
    if n == 0: return 1
    return sum(odd_parts(n - k, k) for k in range(1, min(n, maxp) + 1) if k % 2 == 1)
for n in range(1, 41):
    ok(distinct_parts(n) == odd_parts(n), f"o65 n={n}")

# o66
best = max(Fr(a, 100) ** 2 * (12 - Fr(a, 100)) for a in range(1, 1200))
ok(best == 256, "o66 grid max")
ok(8**2 * 4 == 256, "o66 value")

# o67
fm = min(Fr(a, 1000)**2 + 16 / (Fr(a, 1000)) for a in range(100, 10000))
ok(fm == 12, "o67 grid min at x=2")
ok(all(Fr(a, 1000)**2 + 16 / Fr(a, 1000) >= 12 for a in range(1, 20000)), "o67 bound")

# o68: maximize x+2y+3z s.t. x^2+2y^2+3z^2=6
random.seed(1)
mx = -1e9
for _ in range(200000):
    v = [random.gauss(0, 1) for _ in range(3)]
    c = math.sqrt(6 / (v[0]**2 + 2*v[1]**2 + 3*v[2]**2))
    a, b, d = [c*t for t in v]
    mx = max(mx, a + 2*b + 3*d)
ok(mx <= 6 + 1e-9 and mx > 5.99, "o68 numeric max")
ok(1 + 2 + 3 == 6 and 1**2 + 2*1 + 3*1 == 6, "o68 equality point")

# o69: numeric
for _ in range(100000):
    a, b, c = [random.uniform(0.001, 10) for _ in range(3)]
    ok_ = a*a/(a+b) + b*b/(b+c) + c*c/(c+a) >= (a+b+c)/2 - 1e-12
    assert ok_, "o69"
ok(True, "o69 numeric 100000 samples")

# o70
xs = sp.symbols('xs', nonzero=True)
f = lambda t: 2/t - t
ok(sp.simplify(f(xs) + 2*f(1/xs) - 3*xs) == 0, "o70 verify")
F1, F2 = sp.symbols('F1 F2')
sol = sp.solve([F1 + 2*F2 - 3*xs, F2 + 2*F1 - 3/xs], [F1, F2])
ok(sp.simplify(sol[F1] - (2/xs - xs)) == 0, "o70 derive")

# o71
y, X = sp.symbols('y X')
g = lambda t: 1 - 2*t
ok(sp.expand(g(X + g(y)) - (4*y - 2*X - 1)) == 0, "o71 verify")
# derive: put x=-f(y): f(0) = 4y+2f(y)-1 ; f(y)=c-2y, c=(f(0)+1)/2, f(0)=c
c = sp.symbols('c')
ok(sp.solve(sp.Eq(c, (c + 1)/2), c) == [1], "o71 c")
# also check linear family a*y+b only matching one
a_, b_ = sp.symbols('a_ b_')
eqs = sp.Poly(sp.expand(a_*(X + a_*y + b_) + b_ - (4*y - 2*X - 1)), X, y).coeffs()
ok(sp.solve(eqs, [a_, b_], dict=True) == [{a_: -2, b_: 1}], "o71 linear family")

# o72
t = sp.symbols('t')
roots = sp.Poly(t**3 - t - 1, t).nroots(n=30)
p5 = sum(r**5 for r in roots)
ok(abs(p5 - 5) < 1e-20, "o72 p5")
p = [3, 0, 2]
for k in range(3, 6):
    p.append(p[k-2] + p[k-3])
ok(p[:6] == [3, 0, 2, 3, 2, 5], "o72 recurrence")

# o73
# divisibility a-b | P(a)-P(b) for random integer polys
for _ in range(2000):
    co = [random.randint(-9, 9) for _ in range(6)]
    P = lambda v: sum(cf * v**i for i, cf in enumerate(co))
    a, b = random.randint(-20, 20), random.randint(-20, 20)
    if a != b:
        assert (P(a) - P(b)) % (a - b) == 0
ok(True, "o73 a-b | P(a)-P(b) random")
ok((8 - 5) % (9 - 2) != 0, "o73 contradiction 7 does not divide 3")

# o74
sols = [n for n in range(1, 5000) if (n*n + 3) % (n + 3) == 0]
ok(sols == [1, 3, 9], "o74")

# o75
for a in range(1, 40):
    for b in range(1, 40):
        ok(gcd(2**a - 1, 2**b - 1) == 2**gcd(a, b) - 1, f"o75 {a},{b}")

# o76
pairs = [(x_, y_) for x_ in range(1, 1100) for y_ in range(1, x_) if x_*x_ - y_*y_ == 2024]
ok(len(pairs) == 4 and set(pairs) == {(507, 505), (255, 251), (57, 35), (45, 1)}, "o76")
ok(sp.divisors(506) == [1, 2, 11, 22, 23, 46, 253, 506], "o76 divisors")

# o77
s77 = [(a, b) for a in range(0, 60) for b in range(0, 100) if 3**a - 2**b == 1]
ok(s77 == [(1, 1), (2, 3)], "o77")

# o78 records in permutations of 1..8
tot = 0
for perm in itertools.permutations(range(8)):
    m = -1
    for v in perm:
        if v > m:
            tot += 1; m = v
ok(Fr(tot, math.factorial(8)) == Fr(761, 280) == sum(Fr(1, k) for k in range(1, 9)), "o78")

# o79 runs in 10 flips
tot = 0
for s in itertools.product([0, 1], repeat=10):
    tot += 1 + sum(1 for i in range(9) if s[i] != s[i+1])
ok(Fr(tot, 2**10) == Fr(11, 2), "o79")

# o80 British flag
xx, yy, w, h = sp.symbols('x y w h', real=True)
d2 = lambda P, Qp: (P[0]-Qp[0])**2 + (P[1]-Qp[1])**2
A, B, C, D = (0, 0), (w, 0), (w, h), (0, h)
Pp = (xx, yy)
ok(sp.expand(d2(Pp, A) + d2(Pp, C) - d2(Pp, B) - d2(Pp, D)) == 0, "o80")

# o81 13-14-15
Bp, Cp, Ap = sp.Point(0, 0), sp.Point(14, 0), sp.Point(5, 12)
ok(Ap.distance(Bp) == 13 and Ap.distance(Cp) == 15, "o81 sides")
tri = sp.Triangle(Ap, Bp, Cp)
O, H = tri.circumcenter, tri.orthocenter
ok(O == sp.Point(7, sp.Rational(33, 8)) and H == sp.Point(5, sp.Rational(15, 4)), "o81 centers")
ok(sp.simplify(O.distance(H) - sp.sqrt(265)/8) == 0, "o81 OH")
ok(tri.circumradius == sp.Rational(65, 8), "o81 R")

# o82
pr = 1.0
for k in range(1, 7):
    pr *= sin(k * pi / 7)
ok(abs(pr - 7/64) < 1e-12, "o82 product")
import cmath
z = cmath.exp(2j*pi/7)
pp = 1
for k in range(1, 7):
    pp *= (1 - z**k)
ok(abs(pp - 7) < 1e-12, "o82 complex product")

# o83 van Aubel / square centres
def centre(Pa, Pb):  # outward for ccw polygon: right of A->B
    return (Pa + Pb)/2 - 1j*(Pb - Pa)/2
cnt = 0
while cnt < 300:
    # random convex quad: random points on ellipse, sorted by angle (ccw)
    ang = sorted(random.uniform(0, 2*pi) for _ in range(4))
    if any(ang[(i+1) % 4] - ang[i] + (2*pi if i == 3 else 0) > pi - 0.05 for i in range(4)):
        continue
    pts = [complex(3*cos(t) + 1, 2*sin(t) - 1) for t in ang]
    a_, b_, c_, d_ = pts
    P_, Q_, R_, S_ = centre(a_, b_), centre(b_, c_), centre(c_, d_), centre(d_, a_)
    assert abs((S_ - Q_) - 1j*(R_ - P_)) < 1e-9
    assert abs(abs(S_ - Q_) - abs(R_ - P_)) < 1e-9
    cnt += 1
ok(True, "o83 300 random convex quads")
# outward check on unit square ccw: bottom side centre below
ok(centre(0j, 1+0j).imag < 0, "o83 outward orientation")

# o84
ok(abs(sin(radians(10))*sin(radians(50))*sin(radians(70)) - 1/8) < 1e-14, "o84")
ok(abs(cos(radians(20))*cos(radians(40))*cos(radians(80)) - 1/8) < 1e-14, "o84 cos form")

# o85
def pt(Rr, deg): return (Rr*cos(radians(deg)), Rr*sin(radians(deg)))
# triangle with angles A=70,B=75,C=35 on unit circumcircle: arcs BC=2A=140, CA=2B=150, AB=2C=70
Ang = 90
Apt = pt(1, Ang)
Bpt = pt(1, Ang + 2*35)       # arc AB = 70
Cpt = pt(1, Ang + 2*35 + 2*70)  # arc BC = 140 ; remaining arc CA = 150
Hh = (Apt[0] + Bpt[0] + Cpt[0], Apt[1] + Bpt[1] + Cpt[1])  # orthocenter, O at origin
def ang_at(Pv, Q0, R0):
    v = (Pv[0]-Q0[0], Pv[1]-Q0[1]); u = (R0[0]-Q0[0], R0[1]-Q0[1])
    return degrees(math.acos((v[0]*u[0] + v[1]*u[1]) / (hypot(*v)*hypot(*u))))
ok(abs(ang_at(Bpt, Apt, Cpt) - 70) < 1e-9 and abs(ang_at(Apt, Bpt, Cpt) - 75) < 1e-9 and abs(ang_at(Apt, Cpt, Bpt) - 35) < 1e-9, "o85 angles")
ok(abs(ang_at((0, 0), Apt, Hh) - 40) < 1e-9, "o85 OAH")
ok(abs(ang_at(Bpt, Apt, (0, 0)) - 55) < 1e-9 and abs(ang_at(Bpt, Apt, Hh) - 15) < 1e-9, "o85 sub-angles")

# o86 trapezoid
for _ in range(500):
    a_, b_ = random.uniform(1, 10), random.uniform(1, 10)
    hh = random.uniform(1, 5); sh = random.uniform(-3, 3)
    # AB on y=0 from (0,0) to (a,0); CD on y=h from (sh, h) to (sh+b, h) ; ABCD in order => D=(sh,h), C=(sh+b,h)
    Ap_, Bp_, Cp_, Dp_ = (0, 0), (a_, 0), (sh + b_, hh), (sh, hh)
    # P = AC ∩ BD at height y: A + t(C-A) with t = a/(a+b)
    tt = a_/(a_ + b_)
    Pq = (tt*Cp_[0], tt*Cp_[1])
    # line y=Pq[1] intersect AD and BC
    yP = Pq[1]
    sM = yP / hh  # fraction along A->D
    M = (sM*Dp_[0], yP)
    N = (a_ + sM*(Cp_[0] - a_), yP)
    assert abs((N[0] - M[0]) - 2*a_*b_/(a_ + b_)) < 1e-9
    assert abs((Pq[0] - M[0]) - (N[0] - Pq[0])) < 1e-9   # P is the midpoint of MN
    assert abs(yP - tt*hh) < 1e-9
    assert abs((a_ + tt*(Dp_[0] - a_)) - Pq[0]) < 1e-9   # P also lies on BD (BP/PD = a/b)
ok(True, "o86 500 random trapezoids")

print(f"{n_checks} checks passed")
