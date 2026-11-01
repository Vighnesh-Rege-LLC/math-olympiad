#!/usr/bin/env python3
"""Code checks for batch2-hard-d (m100-m114, adapted from MathNet)."""
import itertools, math, cmath, random
from fractions import Fraction
import sympy as sp

ok = []


def check(name, cond):
    assert cond, name
    ok.append(name)


random.seed(2026)

# ---------------- m100 (0cgm) cyclic pentagon AB=BC=CD, vertex centroid = centre ----------------
g = lambda t: 4 * math.cos(t / 2) * math.cos(t)
check("m100 cos36 cos72 = 1/4", sp.nsimplify(sp.cos(sp.pi / 5) * sp.cos(2 * sp.pi / 5) - sp.Rational(1, 4)) == 0)
check("m100 g(2pi/5)=1", abs(g(2 * math.pi / 5) - 1) < 1e-12)
ts = [i * (math.pi / 2) / 10000 for i in range(1, 10000)]
check("m100 g strictly decreasing on (0,pi/2)", all(g(ts[i]) > g(ts[i + 1]) for i in range(len(ts) - 1)))
# formula e = -a e^{3i t/2} 4cos(t/2)cos t equals -(a+b+c+d)
for _ in range(100):
    a = cmath.exp(1j * random.uniform(0, 2 * math.pi)); t = random.uniform(0.01, 2 * math.pi / 3 - 0.01); w = cmath.exp(1j * t)
    lhs = -(a + a * w + a * w * w + a * w ** 3)
    rhs = -a * cmath.exp(1.5j * t) * 4 * math.cos(t / 2) * math.cos(t)
    assert abs(lhs - rhs) < 1e-12
check("m100 factorisation of e", True)
# brute force: scan theta, keep those with |e|=1 and E strictly between D and A (ccw); only 2pi/5 survives
sols = []
N = 200000
prev = None
for i in range(1, N):
    t = i * (2 * math.pi / 3) / N
    val = abs(1 + cmath.exp(1j * t) + cmath.exp(2j * t) + cmath.exp(3j * t)) - 1
    if prev is not None and prev[1] * val <= 0:
        sols.append((prev[0] + t) / 2)
    prev = (t, val)
good = []
for t in sols:
    e = -(1 + cmath.exp(1j * t) + cmath.exp(2j * t) + cmath.exp(3j * t))
    ang = cmath.phase(e) % (2 * math.pi)
    if 3 * t < ang < 2 * math.pi:
        good.append(t)
check("m100 roots of |1+w+w^2+w^3|=1 in (0,2pi/3)", len(sols) >= 1)
check("m100 only theta=2pi/5 has E on arc DA", len(good) == 1 and abs(good[0] - 2 * math.pi / 5) < 1e-4)

# ---------------- m101 (099r) subsets of {1..2009} with sum divisible by 2009 ----------------
def count_dp(n):
    cnt = [0] * n; cnt[0] = 1
    for j in range(1, n + 1):
        new = cnt[:]
        for r in range(n):
            new[(r + j) % n] += cnt[r]
        cnt = new
    return cnt[0]


def formula(n):
    tot = sum(sp.totient(m) * 2 ** (n // m) for m in sp.divisors(n))
    assert tot % n == 0
    return tot // n


check("m101 formula matches DP for odd n<60", all(count_dp(n) == formula(n) for n in range(1, 60, 2)))
check("m101 product (1+zeta) over m-th roots is 2 for odd m", all(abs(complex(sp.N(sp.prod([1 + sp.exp(2 * sp.pi * sp.I * k / m) for k in range(m)]))) - 2) < 1e-9 for m in range(1, 16, 2)))
ans101 = (2 ** 2009 + 6 * 2 ** 287 + 42 * 2 ** 41 + 40 * 2 ** 49 + 240 * 2 ** 7 + 1680 * 2) // 2009
check("m101 n=2009 value", count_dp(2009) == formula(2009) == ans101 and (2 ** 2009 + 6 * 2 ** 287 + 42 * 2 ** 41 + 40 * 2 ** 49 + 240 * 2 ** 7 + 1680 * 2) % 2009 == 0)
check("m101 totients", [sp.totient(m) for m in (1, 7, 49, 41, 287, 2009)] == [1, 6, 42, 40, 240, 1680])

# ---------------- m102 (0k5h) TSTST: red 75 of 100, parity of red coordinates in T_n ----------------
def xy_counts(red, n, M=100):
    # vectors indexed by residue: number of tuples with even / odd red count
    ev = [0] * M; od = [0] * M; ev[0] = 1
    for _ in range(n):
        ne = [0] * M; no = [0] * M
        for r in range(M):
            if ev[r] == 0 and od[r] == 0:
                continue
            for s_ in range(1, M + 1):
                t = (r + s_) % M
                if s_ in red:
                    ne[t] += od[r]; no[t] += ev[r]
                else:
                    ne[t] += ev[r]; no[t] += od[r]
        ev, od = ne, no
    return ev[0], od[0]


def allblue(blue, n, M=100):
    v = [0] * M; v[0] = 1
    for _ in range(n):
        w = [0] * M
        for r in range(M):
            if v[r]:
                for b in blue:
                    w[(r + b) % M] += v[r]
        v = w
    return v[0]


okf = True
for trial in range(12):
    red = set(random.sample(range(1, 101), 75))
    blue = [x for x in range(1, 101) if x not in red]
    for n in range(1, 6):
        X, Y = xy_counts(red, n)
        Z = allblue(blue, n)
        if 100 * (X - Y) != ((-50) ** n - 50 ** n) + 100 * 2 ** n * Z:
            okf = False
        if n % 2 == 0 and X < Y:
            okf = False
check("m102 identity X-Y = ((-50)^n-50^n)/100 + 2^n Z and even n works (random colourings)", okf)
red = set(range(1, 101)) - set(range(1, 101, 4))
check("m102 blue = 1 mod 4 has 25 elements", len(red) == 75)
check("m102 odd n fail for that colouring", all((lambda XY: XY[0] < XY[1] and XY[1] - XY[0] == 50 ** (n - 1))(xy_counts(red, n)) for n in (1, 3, 5)))

# ---------------- m103 (06ip) alien branching process, extinction probability ----------------
x = sp.Symbol('x')
check("m103 factorisation", sp.expand((x - 1) * (x ** 2 + 2 * x - 1) - (x ** 3 + x ** 2 - 3 * x + 1)) == 0)
q = sp.sqrt(2) - 1
check("m103 q is fixed point", sp.simplify((1 + q + q ** 2 + q ** 3) / 4 - q) == 0)
pn = Fraction(0)
seq = []
for _ in range(200):
    pn = (1 + pn + pn ** 2 + pn ** 3) / 4
    pn = Fraction(float(pn))  # keep it small
    seq.append(float(pn))
check("m103 p_n increasing, bounded by q, converging to q", all(seq[i] <= seq[i + 1] + 1e-15 for i in range(len(seq) - 1)) and all(v <= math.sqrt(2) - 1 + 1e-12 for v in seq) and abs(seq[-1] - (math.sqrt(2) - 1)) < 1e-9)
# Monte Carlo: extinct within 60 days, population cap 1000 counts as survival
random.seed(7)
ext = 0; T = 6000
for _ in range(T):
    pop = 1
    for day in range(60):
        if pop == 0 or pop > 1000:
            break
        new = 0
        for _a in range(pop):
            new += random.choice((0, 2, 3, 1))
        pop = new
    ext += (pop == 0)
check("m103 Monte Carlo near sqrt2-1", abs(ext / T - (math.sqrt(2) - 1)) < 0.03)

# ---------------- m104 (0cd9) RMM: KP + KQ >= BC ----------------
def foot(z, u):  # projection of z onto the line through 0 with unit direction u
    return u * (z * u.conjugate()).real


def orthocentre(A, B, C):
    # H satisfies Re((H-A) conj(C-B)) = 0 and Re((H-B) conj(A-C)) = 0; Cramer's rule
    d1, d2 = C - B, A - C
    m11, m12, r1 = d1.real, d1.imag, (d1 * A.conjugate()).real
    m21, m22, r2 = d2.real, d2.imag, (d2 * B.conjugate()).real
    det = m11 * m22 - m12 * m21
    return complex((r1 * m22 - m12 * r2) / det, (m11 * r2 - m21 * r1) / det)


okf = True; minratio = 10
for _ in range(20000):
    a, b, c = [cmath.exp(1j * random.uniform(0, 2 * math.pi)) for _ in range(3)]
    if min(abs(a - b), abs(b - c), abs(c - a)) < 1e-3:
        continue
    R = random.uniform(0.5, 3); shift = complex(random.uniform(-2, 2), random.uniform(-2, 2))
    A, B, C = R * a + shift, R * b + shift, R * c + shift
    O = shift; H = orthocentre(A, B, C)
    if abs(H - (A + B + C - 2 * O)) > 1e-6 * max(1, abs(H)):
        okf = False
    K = (A + H) / 2
    u = cmath.exp(1j * random.uniform(0, 2 * math.pi))
    P = O + foot(B - O, u); Q = O + foot(C - O, u)
    lhs = abs(K - P) + abs(K - Q)
    if lhs < abs(B - C) - 1e-9:
        okf = False
    # identity KP = R|2ab + bc - u^2| / 2
    if abs(abs(K - P) - R * abs(2 * a * b + b * c - u * u) / 2) > 1e-9 * R:
        okf = False
    minratio = min(minratio, lhs / abs(B - C))
check("m104 KP+KQ >= BC and identities (random, with H formula)", okf)
check("m104 bound is tight (ratio close to 1 occurs)", minratio < 1.01)

# ---------------- m105 (0grr) Turkey TST: max of b_1+...+b_N given a_N <= a_0 ----------------
def run105(a0, pattern):
    a = a0; S = 0.0
    for ch in pattern:
        if ch == 0:
            S += 0.5 - a; a = a / 2
        else:
            S += a; a = 2 * a * a
        if abs(a) > 1e12:
            return None, None
    return a, S


okf = True; best = {}
grid = [i / 400 for i in range(-400, 801)]
for N in range(1, 9):
    for pattern in itertools.product((0, 1), repeat=N):
        for a0 in grid:
            aN, S = run105(a0, pattern)
            if aN is None:
                continue
            if aN <= a0 + 1e-15:
                if S > N / 2 + 1e-9:
                    okf = False
                best[N] = max(best.get(N, -1e9), S)
check("m105 S <= N/2 whenever a_N <= a_0 (N<=8, grid of a_0, all choices)", okf)
check("m105 max N/2 attained", all(abs(best[N] - N / 2) < 1e-12 for N in range(1, 9)))
aN, S = run105(0.5, [1] * 100)
check("m105 equality a_i = 1/2 for N=100", aN == 0.5 and abs(S - 50) < 1e-12)
check("m105 negative a_0 never returns", all(run105(a0, pat)[0] is None or run105(a0, pat)[0] > a0 for a0 in [-1.5, -0.7, -0.01] for pat in itertools.product((0, 1), repeat=6)))
A, Bv = sp.symbols('A B', positive=True)
check("m105 identity", sp.simplify(((Bv - A / 2) * (Bv - 2 * A ** 2)) / (A * Bv) - (Bv / A + A ** 2 / Bv - 2 * A - sp.Rational(1, 2))) == 0)

# ---------------- m106 (0kus) TSTST: sum(1/k^2+1/k^3) >= m (sum 1/k^2)^2 ----------------
okf = True
for m in range(1, 30):
    for n in range(m, 45):
        L = sum(Fraction(1, k * k) + Fraction(1, k ** 3) for k in range(m, n + 1))
        A2 = sum(Fraction(1, k * k) for k in range(m, n + 1))
        tel = sum(Fraction(1, k * (k + 1)) for k in range(m, n + 1))
        if not (L > m * A2 * A2 and tel == Fraction(1, m) - Fraction(1, n + 1) and L * tel >= A2 * A2):
            okf = False
check("m106 inequality (strict), telescoping sum and CS step, exact for m<30, n<45", okf)
kk = sp.Symbol('k', positive=True)
check("m106 (1/k^2)^2/(1/k^2+1/k^3) = 1/(k(k+1))", sp.simplify((1 / kk ** 2) ** 2 / (1 / kk ** 2 + 1 / kk ** 3) - 1 / (kk * (kk + 1))) == 0)

# ---------------- m107 (03bh) Bulgaria TST: angles 108, 36, 36 ----------------
def tri_from_sides(a, b, c):
    B = complex(0, 0); C = complex(a, 0)
    x_ = (a * a + c * c - b * b) / (2 * a); y_ = math.sqrt(max(c * c - x_ * x_, 0))
    return complex(x_, y_), B, C


def line_inter(P1, P2, Q1, Q2):
    d1, d2 = P2 - P1, Q2 - Q1
    den = (d1.conjugate() * d2).imag
    t = ((Q1 - P1).conjugate() * d2).imag / den
    return P1 + t * d1


def ang(P, V, Q):
    return abs(cmath.phase((P - V) / (Q - V)))


def config107(b, c):
    a = (b + math.sqrt(b * b + 4 * c * c)) / 2  # a^2 = c^2 + a b
    A, B, C = tri_from_sides(a, b, c)
    s_ = (a + b + c) / 2
    A1 = B + (s_ - b) / a * (C - B)
    B1 = C + (s_ - c) / b * (A - C)
    X = line_inter(A1, B1, A, B)
    return a, A, B, C, A1, B1, X


okf = True
for _ in range(3000):
    b = random.uniform(0.2, 3); c = random.uniform(0.2, 3)
    a, A, B, C, A1, B1, X = config107(b, c)
    if not (a < b + c and c < a + b and b < a + c):
        continue
    # concyclic X, A, A1, C (cross ratio real) and X beyond A
    cr = ((X - A) * (A1 - C)) / ((X - C) * (A1 - A))
    if abs(cr.imag) > 1e-7 * max(1, abs(cr)):
        okf = False
    t = ((X - B) / (A - B)).real
    if not t > 1:
        okf = False
check("m107 for every triangle with a^2=c^2+ab: X beyond A and X,A,A1,C concyclic", okf)
a, A, B, C, A1, B1, X = config107(1.0, 1.0)
angs = sorted([math.degrees(ang(B, A, C)), math.degrees(ang(A, B, C)), math.degrees(ang(A, C, B))])
check("m107 b=c gives angles 36,36,108 and angle CXB = 90", abs(angs[0] - 36) < 1e-9 and abs(angs[1] - 36) < 1e-9 and abs(angs[2] - 108) < 1e-9 and abs(math.degrees(ang(C, X, B)) - 90) < 1e-9)
# angle CXB = 90 only when b = c (scan)
bad = 0
for _ in range(3000):
    b = random.uniform(0.2, 3); c = random.uniform(0.2, 3)
    a, A, B, C, A1, B1, X = config107(b, c)
    if not (a < b + c and c < a + b and b < a + c):
        continue
    if abs(math.degrees(ang(C, X, B)) - 90) < 1e-6 and abs(b - c) > 1e-4:
        bad += 1
check("m107 right angle forces b=c (random scan)", bad == 0)

# ---------------- m108 (07fs) Iran: PK = PH ----------------
def proj(Pt, L1, L2):
    d = L2 - L1
    return L1 + d * (((Pt - L1) * d.conjugate()).real / abs(d) ** 2)


def dang(P1, V, P2):  # directed angle from line V P1 to line V P2, mod 180 degrees
    return math.degrees(cmath.phase((P2 - V) / (P1 - V))) % 180


def circle_line_second(Pt, d, Oc, R):
    # points Pt + t d on circle |z - Oc| = R ; return both
    a_ = abs(d) ** 2; b_ = 2 * ((Pt - Oc) * d.conjugate()).real; c_ = abs(Pt - Oc) ** 2 - R * R
    disc = math.sqrt(b_ * b_ - 4 * a_ * c_)
    return [Pt + d * (-b_ + sg * disc) / (2 * a_) for sg in (1, -1)]


okf = True; cnt = 0
while cnt < 3000:
    A, B, C = [cmath.exp(1j * random.uniform(0, 2 * math.pi)) for _ in range(3)]
    if not all(ang(*t) < math.pi / 2 - 1e-3 for t in ((B, A, C), (A, B, C), (A, C, B))):
        continue
    cnt += 1
    H = A + B + C
    E = proj(B, A, C); F = proj(C, A, B)
    d = (F - E) * 1j
    cands = circle_line_second(H, d, 0, 1)
    # K on arc BC not containing A: A and K on opposite sides of BC
    side = lambda Z: ((Z - B) * (C - B).conjugate()).imag
    K = [Z for Z in cands if side(Z) * side(A) < 0][0]
    P = line_inter(A, K, B, C)
    if abs(abs(P - K) - abs(P - H)) > 1e-8:
        okf = False
    # AO perpendicular to EF, reflection of H in BC on circle, directed-angle lemma in circle centred 0
    Hp = 2 * proj(H, B, C) - H
    if abs(((A - 0) * (F - E).conjugate()).real) > 1e-9 or abs(abs(Hp) - 1) > 1e-9:
        okf = False
    if abs(((dang(0, A, K) - (dang(A, Hp, K) - 90)) + 90) % 180 - 90) > 1e-7:
        okf = False
check("m108 PK = PH, AO perp EF, H' on circle, lemma (random acute triangles)", okf)

# ---------------- m109 (07hp) Iran: angle BKC = 90 ----------------
def circumcentre(P1, P2, P3):
    # solve |z-P1|=|z-P2|=|z-P3|
    m1, m2 = (P1 + P2) / 2, (P2 + P3) / 2
    return line_inter(m1, m1 + (P2 - P1) * 1j, m2, m2 + (P3 - P2) * 1j)


okf = True; cnt = 0
while cnt < 3000:
    a_, b_, c_ = [cmath.exp(1j * random.uniform(0, 2 * math.pi)) for _ in range(3)]
    if min(abs(a_ - b_), abs(b_ - c_), abs(c_ - a_)) < 0.05 or abs(abs(b_ - c_) - abs(b_ - a_)) < 0.02 or abs(ang(b_, a_, c_) - math.pi / 2) < 0.02:
        continue
    cnt += 1
    S = 2 * b_ * c_ / (b_ + c_)  # tangents at B, C meet here
    # symmedian check: angle(BA, AS) == angle(MA..) isogonal to median
    Mm = (b_ + c_) / 2
    if abs((dang(b_, a_, S) - dang(Mm, a_, c_) + 90) % 180 - 90) > 1e-7:
        okf = False
    T = [Z for Z in circle_line_second(a_, S - a_, 0, 1) if abs(Z - a_) > 1e-9][0]
    if abs(T - (2 * b_ * c_ - a_ * b_ - a_ * c_) / (b_ + c_ - 2 * a_)) > 1e-8:
        okf = False
    D = 2 * proj(b_, a_, c_) - a_
    O1 = circumcentre(a_, D, T); O2 = circumcentre(D, c_, T)
    tdir = (D - O1) * 1j
    Ks = circle_line_second(D, tdir, O2, abs(D - O2))
    K = [Z for Z in Ks if abs(Z - D) > 1e-9][0]
    if abs(abs(ang(b_, K, c_)) - math.pi / 2) > 1e-6:
        okf = False
    if abs(K - (2 * b_ * c_ + b_ * b_ - c_ * c_) / (2 * b_)) > 1e-7:
        okf = False
check("m109 angle BKC = 90 and k = (2bc+b^2-c^2)/(2b) (random triangles)", okf)
av, bv, cv = sp.symbols('a b c')
tt = (2 * bv * cv - av * bv - av * cv) / (bv + cv - 2 * av)
lam = (cv - tt) / (av - tt)
dd = cv + bv - av * cv / bv
kk_ = cv + lam * (dd - av)
check("m109 symbolic k", sp.simplify(kk_ - (2 * bv * cv + bv ** 2 - cv ** 2) / (2 * bv)) == 0 and sp.simplify(lam - (cv - bv) / (2 * (av - bv))) == 0)

# ---------------- m110 (0hgg) Ukraine: XH = HO = OY gives angle A = 60 ----------------
def tri_angles(Aa, Bb):
    A = cmath.exp(1j * 0); B = cmath.exp(2j * Aa * 0)  # placeholder
    # place on unit circle: arcs opposite to angles are 2A, 2B, 2C
    A = 1 + 0j; B = cmath.exp(2j * (math.pi - Bb - Aa) + 0j)  # arc AB (not containing C) = 2C
    C = cmath.exp(-2j * Bb)  # arc AC (not containing B) = 2B, other side
    return A, B, C


def hxoy(A, B, C):
    O = 0; H = A + B + C
    X = line_inter(H, O, A, B); Y = line_inter(H, O, A, C)
    return O, H, X, Y


Aa = math.pi / 3; Bb = math.atan(5 / math.sqrt(3)); Cc = math.atan(2 / math.sqrt(3))
check("m110 angles sum to 180", abs(Aa + Bb + Cc - math.pi) < 1e-12)
A, B, C = tri_angles(Aa, Bb)
check("m110 placement has the right angles", abs(ang(B, A, C) - Aa) < 1e-9 and abs(ang(A, B, C) - Bb) < 1e-9)
O, H, X, Y = hxoy(A, B, C)
seg = lambda P, U, V: abs(abs(P - U) + abs(P - V) - abs(U - V)) < 1e-9
check("m110 XH = HO = OY with X, Y on the sides and H on OX", abs(abs(X - H) - abs(H - O)) < 1e-9 and abs(abs(O - Y) - abs(H - O)) < 1e-9 and seg(X, A, B) and seg(Y, A, C) and seg(H, O, X))
check("m110 exact cosines", abs(math.cos(Bb) - math.sqrt(21) / 14) < 1e-12 and abs(math.cos(Cc) - math.sqrt(21) / 7) < 1e-12)
# grid scan over acute triangles (X, Y on the sides, H on OX): record cells where both ratios are near 1
hits = []
steps = 600
for i_ in range(1, steps):
    Aa_ = i_ * (math.pi / 2) / steps
    for j_ in range(1, steps):
        Bb_ = j_ * (math.pi / 2) / steps; Cc_ = math.pi - Aa_ - Bb_
        if not (0 < Cc_ < math.pi / 2):
            continue
        A, B, C = tri_angles(Aa_, Bb_)
        O, H, X, Y = hxoy(A, B, C)
        if abs(H - O) < 1e-6:
            continue
        segl = lambda P, U, V: abs(abs(P - U) + abs(P - V) - abs(U - V)) < 1e-7 * (1 + abs(U - V))
        r1 = abs(X - H) / abs(H - O); r2 = abs(O - Y) / abs(H - O)
        if abs(r1 - 1) < 0.02 and abs(r2 - 1) < 0.02 and segl(H, O, X) and segl(X, A, B) and segl(Y, A, C):
            hits.append(math.degrees(Aa_))
check("m110 grid: near-solutions (X, Y on the sides) all have A close to 60", len(hits) > 0 and all(abs(h - 60) < 2 for h in hits))

# ---------------- m111 (06wa) ISL 2021: sum a_k/(1-a_k) s_{k-1}^2 < 1/3 ----------------
okf = True
for _ in range(3000):
    n = random.randint(2, 12)
    w = [random.random() ** random.choice((1, 3, 6)) for _ in range(n)]
    a = [Fraction(int(x * 10 ** 6) + 1, 1) for x in w]
    tot = sum(a); a = [x / tot for x in a]
    S = Fraction(0); prev = Fraction(0); total = Fraction(0)
    for x in a:
        term = x / (1 - x) * prev ** 2
        nxt = prev + x
        if not term < (nxt ** 3 - prev ** 3) / 3:
            okf = False
        total += term; prev = nxt
    if not total < Fraction(1, 3):
        okf = False
check("m111 termwise bound and total < 1/3 (exact, random)", okf)
n = 2000
val = sum((1 / n) / (1 - 1 / n) * ((k - 1) / n) ** 2 for k in range(1, n + 1))
check("m111 constant 1/3 is approached (equal parts)", 1 / 3 - val < 1e-3 and val < 1 / 3)
xx, aa = sp.symbols('x a', positive=True)
check("m111 algebra: x^2+ax+a^2/3 - x^2/(1-a) = a(x(1-a-x)/(1-a)) + a^2/3", sp.simplify(xx ** 2 + aa * xx + aa ** 2 / 3 - xx ** 2 / (1 - aa) - (aa * xx * (1 - aa - xx) / (1 - aa) + aa ** 2 / 3)) == 0)

# ---------------- m112 (01v6) Belarus: four circles through points of y = 1/x ----------------
def pair_with_product(prod):
    while True:
        u = random.choice((-1, 1)) * random.uniform(0.2, 4)
        v = prod / u
        if abs(u - v) > 1e-3:
            return [u, v]


okf = True
for _ in range(2000):
    q = random.choice((-1, 1)) * random.uniform(0.2, 4)
    xs = pair_with_product(q) + pair_with_product(1 / q) + pair_with_product(q) + pair_with_product(1 / q)
    if len(set(round(x, 6) for x in xs)) < 8:
        continue
    Z = [complex(x, 1 / x) for x in xs]
    groups = [(0, 1, 2, 3), (2, 3, 4, 5), (4, 5, 6, 7), (6, 7, 0, 1)]
    Rs = []
    for g in groups:
        Oc = circumcentre(Z[g[0]], Z[g[1]], Z[g[2]])
        R = abs(Z[g[0]] - Oc)
        if abs(abs(Z[g[3]] - Oc) - R) > 1e-6 * max(1, R):
            okf = False
        # Vieta: centre = half the sum of the four points
        if abs(Oc - sum(Z[i] for i in g) / 2) > 1e-6 * max(1, abs(Oc)):
            okf = False
        Rs.append(R)
        if abs(4 * R * R - sum(abs(Z[i]) ** 2 for i in g)) > 1e-6 * max(1, R * R):
            okf = False
    if abs(Rs[3] ** 2 - (Rs[0] ** 2 - Rs[1] ** 2 + Rs[2] ** 2)) > 1e-6 * max(1, Rs[0] ** 2 + Rs[1] ** 2 + Rs[2] ** 2):
        okf = False
check("m112 R4^2 = R1^2 - R2^2 + R3^2, 4R^2 = sum |Z|^2, centre = half-sum (random configurations)", okf)
X, aa, bb, RR = sp.symbols('X a b R')
check("m112 quartic", sp.expand(X ** 2 * ((X - aa) ** 2 + (1 / X - bb) ** 2 - RR ** 2)) == sp.expand(X ** 4 - 2 * aa * X ** 3 + (aa ** 2 + bb ** 2 - RR ** 2) * X ** 2 - 2 * bb * X + 1))
pA, pB, qq = sp.symbols('p_A p_B q')
expr = (pA + pB) ** 2 + (pA / qq + qq * pB) ** 2 - 4 * (qq + 1 / qq + pA * pB)
check("m112 4R^2 formula", sp.simplify(expr - (pA ** 2 * (1 + 1 / qq ** 2) + pB ** 2 * (1 + qq ** 2) - 4 * (qq + 1 / qq))) == 0)

# ---------------- m113 (0gtt) Turkey TST 2023: trapezoid, KL parallel to AB ----------------
def second_on_circle(P0, Q0, centre, R):
    # second intersection of line P0 Q0 with the circle, other than P0 (P0 on circle)
    d = Q0 - P0
    t = -2 * ((P0 - centre) * d.conjugate()).real / abs(d) ** 2
    return P0 + t * d


def second_from_line_point(Pon, Pdir, centre, R):
    return second_on_circle(Pon, Pdir, centre, R)


okf = True; cnt = 0; tries = 0
while cnt < 400 and tries < 20000:
    tries += 1
    h = random.uniform(0.5, 2)
    A = complex(random.uniform(-2, -0.3), 0); B = complex(random.uniform(0.3, 2), 0)
    D = complex(random.uniform(-2.5, 0), h); C = complex(random.uniform(0.1, 2.5), h)
    if (C - D).real <= 0.2:
        continue
    f = lambda T: ang(A, T, D) - ang(C, T, B)
    y0 = random.uniform(0.1, 0.9) * h
    # left/right ends of the horizontal chord at height y0 inside the trapezoid
    xl = A.real + (D.real - A.real) * y0 / h; xr = B.real + (C.real - B.real) * y0 / h
    lo, hi = complex(xl + 1e-6, y0), complex(xr - 1e-6, y0)
    if f(lo) * f(hi) > 0:
        continue
    for _ in range(100):
        mid = (lo + hi) / 2
        if f(lo) * f(mid) <= 0:
            hi = mid
        else:
            lo = mid
    T = (lo + hi) / 2
    if abs(f(T)) > 1e-9:
        continue
    cnt += 1
    O1 = circumcentre(A, C, D); O2 = circumcentre(B, C, D); O3 = circumcentre(T, C, D)
    K = second_on_circle(A, T, O1, abs(A - O1)); L = second_on_circle(B, T, O2, abs(B - O2))
    A2 = second_on_circle(T, A, O3, 0); B2 = second_on_circle(T, B, O3, 0)
    if abs(K - L) < 1e-6:
        continue
    if abs(((K - L) / (B - A)).imag) > 1e-6 * abs(K - L) or abs(((A2 - B2) / (C - D)).imag) > 1e-6 * (1 + abs(A2 - B2)):
        okf = False
check("m113 KL parallel AB and A2B2 parallel CD (random trapezoids, T solved)", okf and cnt >= 100)

# ---------------- m114 (0bmu) Romania TST: 1/R_A + 1/R_B + 1/R_C <= 2/r ----------------
def dist_line(Pt, U, V):
    return abs(((Pt - U) * (V - U).conjugate()).imag) / abs(V - U)


def RA_numeric(A, B, C):
    # circle internally tangent to circumcircle at A, tangent to line BC: bisection on t
    O = circumcentre(A, B, C); R = abs(A - O)
    g = lambda t: dist_line(A + t * (O - A), B, C) - t * R
    lo, hi = 1e-12, 1 - 1e-12
    for _ in range(200):
        mid = (lo + hi) / 2
        if g(mid) > 0:
            lo = mid
        else:
            hi = mid
    return lo * R, R


okf = True; worst = 0
for _ in range(4000):
    A, B, C = [complex(random.uniform(-3, 3), random.uniform(-3, 3)) for _ in range(3)]
    area = abs(((B - A).conjugate() * (C - A)).imag) / 2
    if area < 0.05:
        continue
    a, b, c = abs(B - C), abs(C - A), abs(A - B)
    r = 2 * area / (a + b + c)
    tot = 0
    for (P, Q, S_, side) in ((A, B, C, a), (B, C, A, b), (C, A, B, c)):
        RA, R = RA_numeric(P, Q, S_)
        h = 2 * area / side
        cosP = ((Q - P).conjugate() * (S_ - P)).real / (abs(Q - P) * abs(S_ - P))
        if abs(1 / RA - (1 / R + (1 - cosP) / h)) > 1e-6 * (1 / RA):
            okf = False
        tot += 1 / RA
    if tot > 2 / r * (1 + 1e-9):
        okf = False
    worst = max(worst, tot * r / 2)
check("m114 formula 1/R_A = 1/R + (1-cos A)/h_a and inequality (random triangles)", okf)
check("m114 inequality nearly tight somewhere (near equilateral)", worst > 0.97)
Aq, Bq = sp.symbols('A B')
Cq = sp.pi - Aq - Bq
check("m114 sum sin 2A = 4 prod sin A", sp.simplify(sp.expand_trig(sp.sin(2 * Aq) + sp.sin(2 * Bq) + sp.sin(2 * Cq) - 4 * sp.sin(Aq) * sp.sin(Bq) * sp.sin(Cq))) == 0)
check("m114 sum sin A = 4 prod cos(A/2)", all(abs(math.sin(x) + math.sin(y) + math.sin(math.pi - x - y) - 4 * math.cos(x / 2) * math.cos(y / 2) * math.cos((math.pi - x - y) / 2)) < 1e-12 for x, y in [(random.uniform(0.1, 1.5), random.uniform(0.1, 1.5)) for _ in range(100)]))

print(f"{len(ok)} checks passed")
