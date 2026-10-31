"""Checks for data/problems/batch1-hard-b.md (m50-m74)."""
import itertools
import math
import random
from fractions import Fraction as Fr

import sympy as sp

random.seed(12345)
N = 0


def ok(cond, msg):
    global N
    if not cond:
        raise AssertionError(msg)
    N += 1


def close(x, y, tol=1e-9):
    return abs(x - y) <= tol * max(1.0, abs(x), abs(y))


# ---------- m50 (0aj0): abc=1, (a+b+c+3)/4 >= sum 1/(a+b)
for _ in range(20000):
    a, b = math.exp(random.uniform(-4, 4)), math.exp(random.uniform(-4, 4))
    c = 1 / (a * b)
    lhs = (a + b + c + 3) / 4
    mid = (math.sqrt(a) + math.sqrt(b) + math.sqrt(c)) / 2
    rhs = 1 / (a + b) + 1 / (b + c) + 1 / (c + a)
    ok(rhs <= mid + 1e-12 and mid <= lhs + 1e-12, "m50 chain")
    ok(close(lhs - mid, sum((math.sqrt(t) - 1) ** 2 for t in (a, b, c)) / 4), "m50 identity")
    ok(1 / (a + b) <= math.sqrt(c) / 2 + 1e-12, "m50 amgm step")
ok(close((1 + 1 + 1 + 3) / 4, 3 / 2), "m50 equality")

# ---------- m51 (0gqo)
t = sp.symbols('t', positive=True)
ok(sp.simplify((t**2 + 3) / (t**3 + 1) - 2 / (t**2 - t + 1) - (t - 1)**2 / (t**3 + 1)) == 0, "m51 identity")
f51 = lambda u: (u * u + 3) / (u**3 + 1)
cnt = 0
while cnt < 20000:
    x, y, z = (random.uniform(0, 1.4) for _ in range(3))
    if x * x + y * y + z * z <= x + y + z and min(x, y, z) > 0:
        cnt += 1
        ok(f51(x) + f51(y) + f51(z) >= 6 - 1e-12, "m51 ineq")
ok(f51(1) * 3 == 6, "m51 equality")

# ---------- m52 (0gn2)
for _ in range(3000):
    n = random.randint(2, 7)
    w = [random.uniform(0.05, 3) for _ in range(n)]
    # scale so sum = sum of squares: lambda*S1 = lambda^2*S2
    lam = sum(w) / sum(v * v for v in w)
    a = [lam * v for v in w]
    tt = sum(a)
    ok(close(tt, sum(v * v for v in a)), "m52 constraint")
    ok(tt > 1, "m52 t>1")
    lhs = sum(a[i] / a[j] for i in range(n) for j in range(n) if i != j)
    ok(lhs >= (n - 1) ** 2 * tt / (tt - 1) - 1e-9, "m52 ineq")
    ok(close(sum(a[i] * a[j] for i in range(n) for j in range(n) if i != j), tt * tt - tt), "m52 pair sum")
# equality: all equal a_i = 1 gives t = n
n = 5
ok(close(n * (n - 1), (n - 1) ** 2 * n / (n - 1)), "m52 equality")

# ---------- m53 (065m)
def L53(x, y, z):
    return (x + 2)**2 / (y + z - 2) + (y + 4)**2 / (z + x - 4) + (z + 6)**2 / (x + y - 6)
ok(L53(10, 8, 6) == 36, "m53 solution")
s = sp.symbols('s')
ok(sp.expand((s + 12)**2 - 36 * (2 * s - 12) - (s - 24)**2) == 0, "m53 identity")
for _ in range(50000):
    x, y, z = (random.uniform(3, 30) for _ in range(3))
    v = L53(x, y, z)
    ok(v >= 36 - 1e-9, "m53 min")
    if abs(v - 36) < 1e-6:
        ok(abs(x - 10) + abs(y - 8) + abs(z - 6) < 1e-2, "m53 unique")
# denominators of 3 sum to 2s-12
ok(all(v > 0 for v in (8 + 6 - 2, 6 + 10 - 4, 10 + 8 - 6)), "m53 positive")

# ---------- m54 (0ag3)
def check54(m, trials):
    n = 2 * m + 1
    for _ in range(trials):
        p = [random.uniform(0.01, 5) for _ in range(n)]
        S = [sum(p[(i + k) % n] for k in range(1, m + 1)) for i in range(n)]
        lhs = sum(p[i] / S[i] for i in range(n))
        ok(lhs >= n / m - 1e-9, "m54 ineq")
        e2 = sum(p[i] * p[j] for i in range(n) for j in range(i + 1, n))
        ok(close(sum(p[i] * S[i] for i in range(n)), e2), "m54 denominator = e2")
for m in (1, 2, 3, 5):
    check54(m, 400)
check54(1004, 3)
ok(close(sum(1 / 1004 for _ in range(2009)), 2009 / 1004), "m54 equality")

# ---------- m55 (0czu)
for n in range(1, 7):
    ssum = sum(Fr(2**(k - 1), 2**(2**k) + 1) for k in range(1, n + 1))
    ok(ssum == Fr(1, 3) - Fr(2**n, 2**(2**(n + 1)) - 1), "m55 closed form")
    ok(ssum < Fr(1, 3), "m55 bound")
ok(Fr(1, 3) - sum(Fr(2**(k - 1), 2**(2**k) + 1) for k in range(1, 6)) < Fr(1, 10**9), "m55 approaches 1/3")

# ---------- m56 (0law)
x = {1: Fr(1)}
Ssum = Fr(1)
for n in range(2, 70):
    x[n] = Fr(2 * n, (n - 1)**2) * Ssum
    Ssum += x[n]
P = {1: Fr(1)}
for n in range(2, 70):
    P[n] = P[n - 1] * (1 + Fr(1, n * n))
for n in range(2, 69):
    ok(sum(x[i] for i in range(1, n + 1)) == n * n * P[n], "m56 S_n = n^2 P_n")
    ok(x[n + 1] == 2 * (n + 1) * P[n], "m56 x_{n+1}")
    ok(x[n + 1] - x[n] == 2 * P[n] + 2 * P[n - 1] / n, "m56 y_n formula")
ok(x[2] == 4, "m56 x2")
Pinf = 1.0
for k in range(2, 2000000):
    Pinf *= 1 + 1 / (k * k)
ok(abs(2 * Pinf - math.sinh(math.pi) / math.pi) < 1e-5, "m56 limit value")
ok(Pinf < math.e, "m56 bound")
yN = float(x[69] - x[68])
ok(abs(yN - 2 * Pinf) < 0.1, "m56 convergence")

# ---------- m57 (0182)
X, Y, C = sp.symbols('x y c', real=True)
f57 = lambda u: u**3 + C
ok(sp.expand(f57(X + f57(Y)) - f57(X) - ((X + f57(Y))**3 - X**3)) == 0, "m57 cubic works")
a57 = sp.symbols('a', nonzero=True)
ok(sp.expand((Y + a57)**3 - Y**3 - (3 * a57 * (Y + a57 / 2)**2 + a57**3 / 4)) == 0, "m57 completing square")

# ---------- m58 (06p9)
for _ in range(1000):
    xx, yy = random.uniform(0.01, 10), random.uniform(0.01, 10)
    ok(close(2 * (xx + 2 * yy), 2 * (xx + yy) + 2 * yy), "m58 f=2x")
for c58 in (0.5, 1.5, 3):
    xx, yy = 1.0, 2.0
    ok(not close(c58 * (xx + c58 * yy), c58 * (xx + yy) + c58 * yy), "m58 other linear fail")

# ---------- m59 (0d29)
def fam(n0, k):
    return lambda n: n if n < n0 else n + k
for n0 in range(0, 8):
    for k in range(0, 6):
        f = fam(n0, k)
        for n in range(0, 200):
            ok(f(n + 1) > f(n), "m59 increasing")
            ok(n + f(f(n)) <= 2 * f(n), "m59 condition")
# brute force on a truncated domain
Lm = 7
cnt59 = 0
for vals in itertools.combinations(range(0, 2 * Lm + 3), Lm + 1):
    f = list(vals)  # strictly increasing
    good = all(n + f[f[n]] <= 2 * f[n] for n in range(Lm + 1) if f[n] <= Lm)
    if not good:
        continue
    cnt59 += 1
    g = [f[n] - n for n in range(Lm + 1)]
    ok(min(g) >= 0, "m59 f(n)>=n")
    if max(g) == 0:
        continue
    n0 = next(i for i in range(Lm + 1) if g[i] > 0)
    k = g[n0]
    ok(all(g[i] == 0 for i in range(n0)), "m59 zero prefix")
    J = (Lm - n0) // k
    ok(all(g[i] == k for i in range(n0, n0 + J * k + 1)), "m59 forced constant block")
ok(cnt59 > 0, "m59 brute force ran")

# ---------- m60 (0bd7)
def mul_mod(p, q):
    # polynomials as [c0,c1,c2] modulo t^3 - 2
    r = [0] * 5
    for i in range(3):
        for j in range(3):
            r[i + j] += p[i] * q[j]
    # t^3 = 2, t^4 = 2t
    return [r[0] + 2 * r[3], r[1] + 2 * r[4], r[2]]
cur = [1, 0, 0]
base = [-1, 1, 0]
cr = 2 ** (1 / 3)
for n in range(1, 80):
    cur = mul_mod(cur, base)
    if n <= 20:
        ok(close(cur[0] + cur[1] * cr + cur[2] * cr * cr, (cr - 1) ** n, 1e-7), "m60 representation")
    if n >= 2:
        ok(cur[2] % 3 == math.comb(n, 2) % 3, "m60 c_n = C(n,2) mod 3")
        ok((cur[2] % 3 == 1) == (n % 3 == 2), "m60 statement")

# ---------- m61 (03qn)
a, b = sp.symbols('a b', real=True)
cc = -a * b / (a + b)
for k in (2, 4):
    expr = (a - b)**k + (b - cc)**k + (cc - a)**k - 2 * (a + b + cc)**k
    ok(sp.simplify(sp.together(expr)) == 0, "m61 x^%d works" % k)
expr6 = (a - b)**6 + (b - cc)**6 + (cc - a)**6 - 2 * (a + b + cc)**6
ok(sp.simplify(sp.together(expr6)) != 0, "m61 x^6 fails")
ok(1 * 2 + (2 * (-sp.Rational(2, 3))) + (-sp.Rational(2, 3)) * 1 == 0, "m61 substitution ab+bc+ca=0")
for k in range(1, 15):
    ck = 3**(2 * k) + 8**(2 * k) + 5**(2 * k) - 2 * 7**(2 * k)
    if k <= 2:
        ok(ck == 0, "m61 c_k zero")
    else:
        ok(ck > 0, "m61 c_k positive")
ok(8**6 > 2 * 7**6, "m61 8^6 > 2*7^6")

# ---------- m62 (01zv)
A, B, Cc = sp.symbols('A B C', real=True)
def lhs62(p):
    return p(A + B - 2 * Cc) + p(B + Cc - 2 * A) + p(Cc + A - 2 * B) - 3 * (p(A - B) + p(B - Cc) + p(Cc - A))
ok(sp.expand(lhs62(lambda u: u)) == 0, "m62 x")
ok(sp.expand(lhs62(lambda u: u**2)) == 0, "m62 x^2")
ok(sp.expand(lhs62(lambda u: u**3)) != 0, "m62 x^3 fails")
ok(sp.expand(lhs62(lambda u: 1)) != 0, "m62 const fails")
for k in range(0, 40):
    ok(((-2)**k == 1 + 3 * (-1)**k) == (k in (1, 2)), "m62 degree equation")

# ---------- m63 (06jk)
for k in range(1, 7):
    count = 0
    for digs in itertools.product((0, 1, 2, 7), repeat=k):
        nval = int(''.join(map(str, digs)))
        if nval % 3 == 0:
            count += 1
    formula = (4**k + 2) // 3 if k % 3 == 0 else (4**k - 1) // 3
    ok(count == formula, "m63 count k=%d" % k)
    # direct count over all n <= 10^k (only feasible small k)
    if k <= 4:
        direct = sum(1 for nval in range(0, 10**k + 1)
                     if nval % 3 == 0 and set(str(nval)) <= set('0127'))
        ok(direct == formula, "m63 direct k=%d" % k)

# ---------- m64 (09eu)
from collections import Counter, defaultdict
for size in range(2, 6):
    buckets = defaultdict(list)
    for S in itertools.combinations(range(1, 15 if size <= 4 else 12), size):
        key = tuple(sorted(Counter(x + y for x, y in itertools.combinations(S, 2)).items()))
        buckets[key].append(S)
    collisions = sum(1 for v in buckets.values() if len(v) > 1)
    if size in (2, 4):
        ok(collisions > 0, "m64 examples exist for size %d" % size)
    else:
        ok(collisions == 0, "m64 no collision for size %d" % size)
ok(sorted(x + y for x, y in itertools.combinations((1, 4, 6, 7), 2)) ==
   sorted(x + y for x, y in itertools.combinations((2, 3, 5, 8), 2)), "m64 example size 4")

# ---------- m65 (07fm)
for _ in range(2000):
    k = random.randint(1, 9)
    zs = [complex(math.cos(th), math.sin(th)) for th in (random.uniform(0, 2 * math.pi) for _ in range(k))]
    lhs = sum(abs(zs[i] - zs[j])**2 for i in range(k) for j in range(i + 1, k))
    ok(close(lhs, k * k - abs(sum(zs))**2, 1e-9), "m65 identity")
    ok(lhs <= k * k + 1e-9, "m65 bound")

# ---------- m66 (0bnr)
def F66(z):
    return abs(z) + abs(z - 5j) - abs(z - 2j) - abs(z - 3j)
for _ in range(50000):
    z = complex(random.uniform(-10, 10), random.uniform(-10, 15))
    ok(F66(z) >= -1e-12, "m66 inequality")
    if abs(z.real) > 1e-3:
        ok(F66(z) > 0, "m66 strict off axis")
for yv in [-5, -1, 0, 5, 6, 10]:
    ok(abs(F66(complex(0, yv))) < 1e-12, "m66 solutions")
for yv in [0.5, 2, 2.5, 4, 4.9]:
    ok(F66(complex(0, yv)) > 1e-6, "m66 non-solutions on axis")

# ---------- m67 (0a7l)
r = sp.symbols('r', positive=True)
ok(sp.expand((4 * r**2 - 1) * (r**2 - 1) - (3 * r + 1)**2 - 2 * r * (2 * r**3 - 7 * r - 3)) == 0, "m67 algebra")
g67 = lambda rr: math.asin(1 / (2 * rr)) + math.asin(1 / rr) + math.asin(3 / (2 * rr)) - math.pi / 2
lo, hi = 1.5, 10.0
ok(g67(lo) > 0 and g67(hi) < 0, "m67 bracket")
for _ in range(200):
    mid = (lo + hi) / 2
    if g67(mid) > 0:
        lo = mid
    else:
        hi = mid
r0 = lo
ok(abs(2 * r0**3 - 7 * r0 - 3) < 1e-9, "m67 radius satisfies cubic")

# ---------- m68 (0cyu)
def dist_line(Pt, U, V):
    (px, py), (ux, uy), (vx, vy) = Pt, U, V
    return abs((vx - ux) * (py - uy) - (vy - uy) * (px - ux)) / math.hypot(vx - ux, vy - uy)
for _ in range(3000):
    R = random.uniform(0.5, 3)
    angs = sorted(random.uniform(0, 2 * math.pi) for _ in range(5))
    Apt, Bpt, Cpt, Dpt, Ept = [(R * math.cos(q), R * math.sin(q)) for q in angs]
    da, db, dc = dist_line(Ept, Apt, Bpt), dist_line(Ept, Bpt, Cpt), dist_line(Ept, Cpt, Dpt)
    dd = dist_line(Ept, Apt, Dpt)
    if db < 1e-6:
        continue
    ok(close(dd, da * dc / db, 1e-6), "m68 answer")
    ok(close(da, math.dist(Ept, Apt) * math.dist(Ept, Bpt) / (2 * R), 1e-8), "m68 lemma")

# ---------- m69 (01b7)
for _ in range(2000):
    beta = random.uniform(1e-3, math.pi / 3 - 1e-3)
    alpha = beta + math.pi / 6
    T = random.uniform(0.1, 5)
    a_, b_, c_, d_ = T * math.sin(alpha), T * math.cos(alpha), T * math.sin(beta), T * math.cos(beta)
    ok(close(a_**2 + d_**2 - a_ * d_, b_**2 + c_**2 + b_ * c_), "m69 eq1")
    ok(close(a_**2 + b_**2, c_**2 + d_**2), "m69 eq2")
    ok(close((a_ * b_ + c_ * d_) / (a_ * d_ + b_ * c_), math.sqrt(3) / 2), "m69 ratio")
# conversely: solve random instances. Fix b,c random, solve for a,d
import sympy as _sp
for _ in range(30):
    b_ = random.uniform(0.2, 2); c_ = random.uniform(0.2, 2)
    av, dv = _sp.symbols('av dv', positive=True)
    sols = _sp.solve([av**2 + dv**2 - av * dv - (b_**2 + c_**2 + b_ * c_), av**2 + b_**2 - c_**2 - dv**2], [av, dv], dict=True)
    for so in sols:
        A_, D_ = float(so[av]), float(so[dv])
        if A_ > 0 and D_ > 0:
            ok(close((A_ * b_ + c_ * D_) / (A_ * D_ + b_ * c_), math.sqrt(3) / 2, 1e-7), "m69 ratio solved")
ok(close(3 / 4 + 3 / 4 - 3 / 4, 1 / 4 + 1 / 4 + 1 / 4), "m69 example")

# ---------- m70 (08rn)
Bv = sp.Matrix([0, 0]); Cv = sp.Matrix([5, 0])
xA, yA = sp.symbols('xA yA', real=True)
solA = sp.solve([xA**2 + yA**2 - 64, (xA - 5)**2 + yA**2 - 49], [xA, yA], dict=True)
solA = [s_ for s_ in solA if s_[yA] > 0][0]
Av = sp.Matrix([solA[xA], solA[yA]])
def circumR(P1, P2, P3):
    a1 = (P2 - P3).norm(); b1 = (P1 - P3).norm(); c1 = (P1 - P2).norm()
    area = sp.Abs((P2 - P1)[0] * (P3 - P1)[1] - (P2 - P1)[1] * (P3 - P1)[0]) / 2
    return sp.nsimplify(sp.simplify(a1 * b1 * c1 / (4 * area)))
Rabc = circumR(Av, Bv, Cv)
ok(sp.simplify(Rabc - 7 * sp.sqrt(3) / 3) == 0, "m70 R")
# orthocenter
Hx = Av[0]
Hy = sp.symbols('Hy')
Hy = sp.solve(sp.Eq((sp.Matrix([Hx, Hy]) - Bv).dot(Av - Cv), 0), Hy)[0]
H = sp.Matrix([Hx, Hy])
for tri in ((H, Bv, Cv), (H, Cv, Av), (H, Av, Bv)):
    ok(sp.simplify(circumR(*tri) - 7 * sp.sqrt(3) / 3) == 0, "m70 equal radii at H")
# H inside (acute triangle): check barycentric signs numerically
def inside(Pp, P1, P2, P3):
    def cr(u, v, w):
        return (v[0] - u[0]) * (w[1] - u[1]) - (v[1] - u[1]) * (w[0] - u[0])
    s1, s2, s3 = cr(P1, P2, Pp), cr(P2, P3, Pp), cr(P3, P1, Pp)
    return (s1 > 0 and s2 > 0 and s3 > 0) or (s1 < 0 and s2 < 0 and s3 < 0)
Hn = [float(H[0]), float(H[1])]
ok(inside(Hn, [float(Av[0]), float(Av[1])], [0, 0], [5, 0]), "m70 H inside")
ok(sp.Rational(25 + 64 - 49, 80) == sp.Rational(1, 2), "m70 cos B")
# vector lemma: random centers
for _ in range(500):
    rho = random.uniform(0.5, 2)
    O = complex(random.uniform(-1, 1), random.uniform(-1, 1))
    O1, O2, O3 = (O + rho * complex(math.cos(q), math.sin(q)) for q in (random.uniform(0, 7) for _ in range(3)))
    Cp, Ap, Bp = O1 + O2 - O, O2 + O3 - O, O3 + O1 - O
    ok(close(abs(Cp - O1), rho) and close(abs(Cp - O2), rho), "m70 C on circles 1,2")
    Qp = O1 + O2 + O3 - 2 * O
    ok(close(abs(Qp - Ap), rho) and close(abs(Qp - Bp), rho) and close(abs(Qp - Cp), rho), "m70 circumcentre Q")

# ---------- m71 (0g3u)
s3 = sp.sqrt(3)
A71 = sp.Matrix([0, 0]); B71 = sp.Matrix([2, 0]); M71 = sp.Matrix([1, 0])
C71 = sp.Matrix([sp.Rational(1, 2), s3 / 2])
ok(sp.simplify((C71 - M71).norm() - 1) == 0 and sp.simplify((C71 - A71).norm() - 1) == 0, "m71 C")
D71 = 3 * C71
ok(sp.simplify((D71 - C71).norm() - 2) == 0, "m71 CD=AB")
E71 = sp.Matrix([sp.Rational(3, 2), 0])
# E on circle BCD: check concyclic via determinant
def concyclic(P1, P2, P3, P4):
    rows = [[p[0]**2 + p[1]**2, p[0], p[1], 1] for p in (P1, P2, P3, P4)]
    return sp.simplify(sp.Matrix(rows).det()) == 0
ok(concyclic(B71, C71, D71, E71), "m71 E on circle")
tpar = sp.symbols('tpar')
F71 = B71 + tpar * (C71 - B71)
tsol = sp.solve(sp.Eq(F71[0], sp.Rational(3, 2)), tpar)[0]
F71 = F71.subs(tpar, tsol)
ok(tsol == sp.Rational(1, 3), "m71 F parameter")
upar, lpar = sp.symbols('upar lpar')
Xpt = B71 + upar * (D71 - B71)
sol71 = sp.solve(list(Xpt - lpar * F71), [upar, lpar], dict=True)[0]
ok(sol71[upar] == sp.Rational(1, 7), "m71 X parameter")
ok(sol71[upar] / (1 - sol71[upar]) == sp.Rational(1, 6), "m71 ratio")

# ---------- m72 (0ebb)
def foot(Pt, U, V):
    d = V - U
    return U + d * ((Pt - U).real * d.real + (Pt - U).imag * d.imag) / abs(d)**2
done72 = 0
while done72 < 2000:
    Ap, Bp, Cp = (complex(random.uniform(-3, 3), random.uniform(-3, 3)) for _ in range(3))
    a1, b1, c1 = abs(Bp - Cp), abs(Cp - Ap), abs(Ap - Bp)
    area = abs(((Bp - Ap).conjugate() * (Cp - Ap)).imag) / 2
    if area < 0.3:
        continue
    u, v, w = (random.uniform(0.05, 1) for _ in range(3))
    Pp = (u * Ap + v * Bp + w * Cp) / (u + v + w)
    uq, vq, wq = a1 * a1 / u, b1 * b1 / v, c1 * c1 / w
    Qp = (uq * Ap + vq * Bp + wq * Cp) / (uq + vq + wq)
    # check isogonality at A
    ang = lambda Z, Vtx, W: abs(math.atan2(((Z - Vtx).conjugate() * (W - Vtx)).imag, ((Z - Vtx).conjugate() * (W - Vtx)).real))
    ok(close(ang(Pp, Ap, Cp), ang(Bp, Ap, Qp), 1e-7), "m72 isogonal A")
    ok(close(ang(Cp, Bp, Pp), ang(Qp, Bp, Ap), 1e-7), "m72 isogonal B")
    Mp = (Pp + Qp) / 2
    pts = [foot(Pp, Bp, Cp), foot(Pp, Cp, Ap), foot(Pp, Ap, Bp), foot(Qp, Bp, Cp), foot(Qp, Cp, Ap), foot(Qp, Ap, Bp)]
    ds = [abs(z - Mp) for z in pts]
    ok(max(ds) - min(ds) < 1e-7 * max(1, max(ds)), "m72 six points on circle centre M")
    # signed power identity at A
    uAC = (Cp - Ap) / abs(Cp - Ap); uAB = (Bp - Ap) / abs(Bp - Ap)
    sp1 = ((pts[1] - Ap) / uAC).real * ((pts[4] - Ap) / uAC).real
    sp2 = ((pts[2] - Ap) / uAB).real * ((pts[5] - Ap) / uAB).real
    ok(close(sp1, sp2, 1e-7), "m72 signed products")
    ok(close(abs(Mp - Ap)**2 - ds[1]**2, sp1, 1e-6), "m72 power of A")
    done72 += 1

# ---------- m73 (0b84)
a, b, c = sp.symbols('a b c', positive=True)
ok(sp.expand(a**2 * (2 * b**2 + 2 * c**2 - a**2) - c**2 * (2 * a**2 + 2 * b**2 - c**2) - (a**2 - c**2) * (2 * b**2 - a**2 - c**2)) == 0, "m73 factorisation")
ma2 = (2 * b**2 + 2 * c**2 - a**2) / 4
mb2 = (2 * a**2 + 2 * c**2 - b**2) / 4
mc2 = (2 * a**2 + 2 * b**2 - c**2) / 4
ok(sp.expand(ma2 - mb2 - sp.Rational(3, 4) * (b**2 - a**2)) == 0, "m73 median order")
sub = {b: sp.sqrt((a**2 + c**2) / 2)}
ok(sp.simplify(ma2.subs(sub) - sp.Rational(3, 4) * c**2) == 0, "m73 ma")
ok(sp.simplify(mb2.subs(sub) - sp.Rational(3, 4) * b.subs(sub)**2) == 0, "m73 mb")
ok(sp.simplify(mc2.subs(sub) - sp.Rational(3, 4) * a**2) == 0, "m73 mc")
for _ in range(3000):
    sides = sorted(random.uniform(0.2, 3) for _ in range(3))
    a_, b_, c_ = sides
    if a_ + b_ <= c_ + 1e-3:
        continue
    m = sorted([math.sqrt((2 * b_**2 + 2 * c_**2 - a_**2) / 4), math.sqrt((2 * a_**2 + 2 * c_**2 - b_**2) / 4), math.sqrt((2 * a_**2 + 2 * b_**2 - c_**2) / 4)])
    sim = close(m[0] / a_, m[1] / b_, 1e-9) and close(m[1] / b_, m[2] / c_, 1e-9)
    ok(sim == (abs(2 * b_**2 - a_**2 - c_**2) < 1e-9 or abs(a_ - c_) < 1e-12), "m73 random")

# ---------- m74 (08v7)
def angle_AIO(aa, bb=3.0, cc_=2.0):
    # B=(0,0), C=(aa,0), AB=cc_, AC=bb
    xA_ = (aa * aa + cc_ * cc_ - bb * bb) / (2 * aa)
    yA_ = math.sqrt(cc_ * cc_ - xA_ * xA_)
    Apt = complex(xA_, yA_); Bpt = 0j; Cpt = complex(aa, 0)
    I = (aa * Apt + bb * Bpt + cc_ * Cpt) / (aa + bb + cc_)
    # circumcentre
    ox = aa / 2
    oy = (xA_**2 + yA_**2 - aa * xA_) / (2 * yA_)
    O = complex(ox, oy)
    u1, u2 = Apt - I, O - I
    return math.degrees(math.acos((u1.real * u2.real + u1.imag * u2.imag) / (abs(u1) * abs(u2))))
ok(abs(angle_AIO(2.5) - 90) < 1e-9, "m74 a=5/2 gives 90")
grid = [1.001 + i * (3.998 / 4000) for i in range(4001)]
vals = [angle_AIO(g) - 90 for g in grid]
roots = [grid[i] for i in range(len(grid) - 1) if vals[i] == 0 or vals[i] * vals[i + 1] < 0]
ok(len(roots) == 1 and abs(roots[0] - 2.5) < 2e-3, "m74 unique root")
s74 = Fr(15, 4)
area2 = s74 * (s74 - Fr(5, 2)) * (s74 - 3) * (s74 - 2)
ok(area2 == Fr(1575, 256), "m74 heron")
ok(close(math.sqrt(1575 / 256), 15 * math.sqrt(7) / 16), "m74 area")

print(f"{N} checks passed")
