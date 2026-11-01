import itertools, random, math, cmath
from fractions import Fraction
from math import comb, factorial
import sympy as sp

N = 0
def ok(cond, msg):
    global N
    assert cond, "FAILED: " + msg
    N += 1

def close(a, b, tol=1e-9):
    return abs(a - b) < tol

def ang(P, Q, R):
    """angle PQR in degrees"""
    v = (P[0]-Q[0], P[1]-Q[1]); w = (R[0]-Q[0], R[1]-Q[1])
    c = (v[0]*w[0]+v[1]*w[1]) / (math.hypot(*v)*math.hypot(*w))
    return math.degrees(math.acos(max(-1, min(1, c))))

random.seed(11)

# o102: AB=AC, A=40, D on AC with BD=BC; angle ABD = 30
A = (0.0, 0.0); C = (1.0, 0.0)
B = (math.cos(math.radians(40)), math.sin(math.radians(40)))
BC = math.dist(B, C)
# D=(t,0): (t-Bx)^2 + By^2 = BC^2
roots = [B[0] + s*math.sqrt(BC**2 - B[1]**2) for s in (1, -1)]
Ds = [t for t in roots if 0 <= t <= 1 and abs(t - C[0]) > 1e-9]
ok(len(Ds) == 1, "o102 unique D on segment AC, D != C")
D = (Ds[0], 0.0)
ok(close(ang(A, B, D), 30, 1e-7), "o102 angle ABD = 30")
ok(close(ang(B, D, C), 70, 1e-7) and close(ang(D, B, C), 40, 1e-7), "o102 intermediate angles")

# o103: square in right triangle, legs 6, 8 -> side 24/7
s = sp.symbols('s', positive=True)
sol = sp.solve(sp.Eq((6 - s)/6, s/8), s)
ok(sol == [sp.Rational(24, 7)], "o103 side 24/7")
# coordinates: C=(0,0), A=(0,6), B=(8,0); square vertex E=(s,s) on AB: x/8 + y/6 = 1
sv = sp.Rational(24, 7)
ok(sv/8 + sv/6 == 1, "o103 E=(s,s) on hypotenuse")

# o104: z+1/z=1 -> z^2025 + z^-2025 = -2
for z in (cmath.exp(1j*math.pi/3), cmath.exp(-1j*math.pi/3)):
    ok(abs(z + 1/z - 1) < 1e-12, "o104 z solves z+1/z=1")
    ok(abs(z**3 + 1) < 1e-12, "o104 z^3=-1")
    ok(abs(z**2025 + z**-2025 + 2) < 1e-9, "o104 value -2")
ok(2025 % 6 == 3 and 2025 == 3*675 and 675 % 2 == 1, "o104 arithmetic")

# o105: ways to pay 20 with 1,2,5 coins = 29
cnt = sum(1 for a in range(21) for b in range(11) for c in range(5) if a + 2*b + 5*c == 20)
ok(cnt == 29, "o105 brute force 29")
x = sp.symbols('x')
ser = sp.series(1/((1-x)*(1-x**2)*(1-x**5)), x, 0, 21).removeO()
ok(sp.Poly(ser, x).coeff_monomial(x**20) == 29, "o105 series coefficient")
ok([20//2+1, 15//2+1, 10//2+1, 5//2+1, 0//2+1] == [11, 8, 6, 3, 1] and 11+8+6+3+1 == 29, "o105 split")

# o106: expected number of ascents in a random permutation of 1..10 is 9/2
for n in (4, 6, 8):
    tot = sum(sum(p[i] < p[i+1] for i in range(n-1)) for p in itertools.permutations(range(n)))
    ok(Fraction(tot, factorial(n)) == Fraction(n-1, 2), f"o106 n={n}")
# n=10 via Eulerian numbers DP over relative order (count ascents exactly)
def eulerian(n):
    A = [[1]]
    row = [1]
    for m in range(2, n+1):
        new = [0]*m
        for k in range(m):
            new[k] = (k+1)*(row[k] if k < len(row) else 0) + (m-k)*(row[k-1] if k >= 1 else 0)
        row = new
    return row
E10 = eulerian(10)
ok(sum(E10) == factorial(10), "o106 Eulerian row sums to 10!")
ok(Fraction(sum(k*e for k, e in enumerate(E10)), factorial(10)) == Fraction(9, 2), "o106 n=10 expectation 9/2")

# o107: sum_{k=1}^{48} 1/(sqrt k + sqrt(k+1)) = 6
tot = sum(1/(math.sqrt(k) + math.sqrt(k+1)) for k in range(1, 49))
ok(close(tot, 6, 1e-9), "o107 numeric 6")
k = sp.symbols('k', positive=True)
ok(sp.simplify(1/(sp.sqrt(k) + sp.sqrt(k+1)) - (sp.sqrt(k+1) - sp.sqrt(k))) == 0, "o107 identity")

# o108: square side 4, M mid BC, N mid CD, cos MAN = 4/5
Av = sp.Matrix([0, 0]); M = sp.Matrix([4, 2]); Nn = sp.Matrix([2, 4])
cosv = (M.dot(Nn)) / (sp.sqrt(M.dot(M)) * sp.sqrt(Nn.dot(Nn)))
ok(sp.simplify(cosv) == sp.Rational(4, 5), "o108 cos = 4/5")
ok(M.dot(M) == 20 and Nn.dot(Nn) == 20 and M.dot(Nn) == 16, "o108 dot products")

# o109: expected number of cycles of a random permutation of 1..n is H_n (n=10: 7381/2520)
def cycles(p):
    seen = [False]*len(p); c = 0
    for i in range(len(p)):
        if not seen[i]:
            c += 1
            j = i
            while not seen[j]:
                seen[j] = True; j = p[j]
    return c
for n in (3, 5, 7):
    tot = sum(cycles(p) for p in itertools.permutations(range(n)))
    ok(Fraction(tot, factorial(n)) == sum(Fraction(1, j) for j in range(1, n+1)), f"o109 brute force n={n}")
# unsigned Stirling numbers of the first kind for n=10
c = {(0, 0): 1}
def stir(n, k):
    if (n, k) in c: return c[(n, k)]
    if n == 0 or k == 0 or k > n: return 0
    v = (n-1)*stir(n-1, k) + stir(n-1, k-1)
    c[(n, k)] = v; return v
tot10 = sum(k*stir(10, k) for k in range(1, 11))
ok(sum(stir(10, k) for k in range(1, 11)) == factorial(10), "o109 stirling row")
ok(Fraction(tot10, factorial(10)) == Fraction(7381, 2520), "o109 n=10 is 7381/2520")
ok(sum(Fraction(1, j) for j in range(1, 11)) == Fraction(7381, 2520), "o109 H_10")
# expected number of k-cycles = 1/k
for k in range(1, 8):
    n = 7
    tot = 0
    for p in itertools.permutations(range(n)):
        seen = [False]*n; cnt = 0
        for i in range(n):
            if not seen[i]:
                L = 0; j = i
                while not seen[j]:
                    seen[j] = True; j = p[j]; L += 1
                cnt += (L == k)
        tot += cnt
    ok(Fraction(tot, factorial(n)) == Fraction(1, k), f"o109 expected k-cycles k={k}")

# o110: expected flips until HTH = 10
e0, eH, eHT = sp.symbols('e0 eH eHT')
sol = sp.solve([sp.Eq(e0, 1 + eH/2 + e0/2), sp.Eq(eH, 1 + eH/2 + eHT/2), sp.Eq(eHT, 1 + 0 + e0/2)], [e0, eH, eHT])
ok(sol[e0] == 10 and sol[eH] == 8 and sol[eHT] == 6, "o110 linear system")
# exact distribution via automaton: states 0,H,HT
dist = {0: 1.0, 1: 0.0, 2: 0.0}
E_T = 0.0
for n in range(1, 4000):
    new = {0: 0.0, 1: 0.0, 2: 0.0}
    done = 0.0
    # from 0: H->1, T->0 ; from 1: H->1, T->2 ; from 2: H->done, T->0
    new[1] += dist[0]*0.5 + dist[1]*0.5
    new[0] += dist[0]*0.5 + dist[2]*0.5
    new[2] += dist[1]*0.5
    done = dist[2]*0.5
    E_T += n*done
    dist = new
ok(abs(E_T - 10) < 1e-6, "o110 numeric expectation")
# brute force: exact P(T<=n) vs enumeration for n=12
def first_hth(seq):
    s = ''.join(seq)
    i = s.find('HTH')
    return None if i < 0 else i + 3
cntT = {}
n = 14
for seq in itertools.product('HT', repeat=n):
    t = first_hth(seq)
    cntT[t] = cntT.get(t, 0) + 1
Eapprox = sum(t*c for t, c in cntT.items() if t is not None) / 2**n
ok(Eapprox < 10, "o110 truncated expectation below 10")
# check distribution recurrence against enumeration
dist = {0: 1.0, 1: 0.0, 2: 0.0}
probs = {}
for m in range(1, n+1):
    new = {0: 0.0, 1: 0.0, 2: 0.0}
    new[1] += dist[0]*0.5 + dist[1]*0.5
    new[0] += dist[0]*0.5 + dist[2]*0.5
    new[2] += dist[1]*0.5
    probs[m] = dist[2]*0.5
    dist = new
ok(all(abs(probs[m] - cntT.get(m, 0)/2**n) < 1e-12 for m in range(1, n+1)), "o110 automaton matches enumeration")

# o111: A=60; BD, CE angle bisectors; I incenter. ID=IE and BE+CD=BC
def tri_with_A60(Bdeg):
    Bd = math.radians(Bdeg); Cd = math.radians(120 - Bdeg)
    a = math.sin(math.radians(60)); b = math.sin(Bd); c = math.sin(Cd)  # law of sines (b opp B)
    # A at origin, AB along x-axis: B=(c,0)? sides: c=AB opposite C -> sin(C)
    Apt = (0.0, 0.0); Bpt = (c, 0.0)
    Cpt = (b*math.cos(math.radians(60)), b*math.sin(math.radians(60)))
    return Apt, Bpt, Cpt
for Bdeg in [5, 20, 33.3, 45, 60, 77, 90, 100, 115]:
    Ap, Bp, Cp = tri_with_A60(Bdeg)
    a = math.dist(Bp, Cp); b = math.dist(Ap, Cp); c = math.dist(Ap, Bp)
    I = ((a*Ap[0] + b*Bp[0] + c*Cp[0])/(a+b+c), (a*Ap[1] + b*Bp[1] + c*Cp[1])/(a+b+c))
    # D on AC with AD/DC = c/a  (bisector from B): AD = b*c/(a+c)
    t = c/(a+c); D = (Ap[0] + t*(Cp[0]-Ap[0]), Ap[1] + t*(Cp[1]-Ap[1]))
    # E on AB with AE/EB = b/a  (bisector from C): AE = c*b/(a+b)
    u = b/(a+b); E = (Ap[0] + u*(Bp[0]-Ap[0]), Ap[1] + u*(Bp[1]-Ap[1]))
    ok(close(ang(Bp, I, Cp), 120, 1e-7), f"o111 BIC=120 (B={Bdeg})")
    ok(close(math.dist(I, D), math.dist(I, E), 1e-9), f"o111 ID=IE (B={Bdeg})")
    ok(close(math.dist(Bp, E) + math.dist(Cp, D), a, 1e-9), f"o111 BE+CD=BC (B={Bdeg})")
    ok(math.dist(Bp, E) < a, f"o111 BE<BC (B={Bdeg})")

# o112: 13-14-15 triangle, orthic triangle area = 16632/845
Bq = sp.Matrix([0, 0]); Cq = sp.Matrix([14, 0]); Aq = sp.Matrix([5, 12])
ok(sp.sqrt((Aq-Bq).dot(Aq-Bq)) == 13 and sp.sqrt((Aq-Cq).dot(Aq-Cq)) == 15, "o112 side lengths")
def foot(P, U, V):
    d = V - U
    t = (P - U).dot(d) / d.dot(d)
    return U + t*d
Dq = foot(Aq, Bq, Cq); Eq = foot(Bq, Aq, Cq); Fq = foot(Cq, Aq, Bq)
def area(P, Q, R):
    return sp.Abs((Q-P)[0]*(R-P)[1] - (Q-P)[1]*(R-P)[0]) / 2
ok(area(Aq, Bq, Cq) == 84, "o112 area 84")
ok(area(Dq, Eq, Fq) == sp.Rational(16632, 845), "o112 orthic area")
ok(area(Aq, Eq, Fq) == 84*sp.Rational(33, 65)**2, "o112 AEF = cos^2 A * area")
ok(area(Bq, Dq, Fq) == 84*sp.Rational(5, 13)**2, "o112 BDF")
ok(area(Cq, Dq, Eq) == 84*sp.Rational(3, 5)**2, "o112 CDE")
ok(area(Aq, Eq, Fq)+area(Bq, Dq, Fq)+area(Cq, Dq, Eq)+area(Dq, Eq, Fq) == 84, "o112 partition")
ok(1 - sp.Rational(33, 65)**2 - sp.Rational(5, 13)**2 - sp.Rational(3, 5)**2 == sp.Rational(198, 845), "o112 fraction")
ok(Dq == sp.Matrix([5, 0]), "o112 D")
ok(all(0 < ((E_ - U).dot(V - U)) / (V-U).dot(V-U) < 1 for E_, U, V in [(Dq, Bq, Cq), (Eq, Aq, Cq), (Fq, Aq, Bq)]), "o112 feet interior to sides")

# o113: regular n-gon on unit circle, P at distance r: sum PA^4 = n(r^4+4r^2+1) (n>=3), sum PA^6 = n(r^6+9r^4+9r^2+1) (n>=4)
for n in range(3, 13):
    for _ in range(5):
        r = random.uniform(0, 3); th = random.uniform(0, 2*math.pi); rot = random.uniform(0, 2*math.pi)
        p = r*cmath.exp(1j*th)
        ws = [cmath.exp(1j*(rot + 2*math.pi*k/n)) for k in range(n)]
        s4 = sum(abs(p - w)**4 for w in ws); s6 = sum(abs(p - w)**6 for w in ws)
        ok(abs(s4 - n*(r**4 + 4*r**2 + 1)) < 1e-8*(1 + s4), f"o113 fourth powers n={n}")
        if n >= 4:
            ok(abs(s6 - n*(r**6 + 9*r**4 + 9*r**2 + 1)) < 1e-8*(1 + s6), f"o113 sixth powers n={n}")
# n=2 and n=3 failures
p = 0.7+0.2j
for n, power in ((2, 4), (3, 6)):
    r = abs(p); vals = set()
    for rot in (0.0, 0.4, 1.1):
        ws = [cmath.exp(1j*(rot + 2*math.pi*k/n)) for k in range(n)]
        vals.add(round(sum(abs(p - w)**power for w in ws), 6))
    ok(len(vals) > 1, f"o113 not constant for n={n}, power {power}")
# symbolic check of the key sums: sum of omega^(jk)
for n in range(3, 10):
    om = cmath.exp(2j*math.pi/n)
    ok(abs(sum(om**k for k in range(n))) < 1e-12 and abs(sum(om**(2*k) for k in range(n))) < 1e-12, f"o113 root sums n={n}")
    if n >= 4:
        ok(abs(sum(om**(3*k) for k in range(n))) < 1e-12, f"o113 cube sum n={n}")
ok(abs(sum(cmath.exp(2j*math.pi*3*k/3) for k in range(3)) - 3) < 1e-12, "o113 cube sum n=3 is n")

# o114: 8-digit strings (leading zeros allowed) with digit sum 36
poly = [1]
for _ in range(8):
    new = [0]*(len(poly)+9)
    for i, c in enumerate(poly):
        for d in range(10):
            new[i+d] += c
    poly = new
ans114 = poly[36]
ok(ans114 == 4816030, "o114 DP value")
ie = sum((-1)**j * comb(8, j) * comb(36 - 10*j + 7, 7) for j in range(0, 4))
ok(ie == 4816030, "o114 inclusion-exclusion")
ok([comb(43, 7), comb(33, 7), comb(23, 7), comb(13, 7)] == [32224114, 4272048, 245157, 1716], "o114 binomials")
ok(32224114 - 8*4272048 + 28*245157 - 56*1716 == 4816030, "o114 arithmetic")
ok(poly[36] == max(poly) and poly[36 + 0] == poly[72 - 36], "o114 central coefficient symmetric")

# o115: subsets of {1..5m} (incl. empty) with sum divisible by 5: (2^(5m) + 4*2^m)/5
def count_div5(Nn):
    dp = [0]*5; dp[0] = 1
    for i in range(1, Nn+1):
        new = dp[:]
        for r in range(5):
            new[(r + i) % 5] += dp[r]
        dp = new
    return dp[0]
for m in range(1, 7):
    ok(count_div5(5*m) == (2**(5*m) + 4*2**m)//5 and (2**(5*m) + 4*2**m) % 5 == 0, f"o115 formula m={m}")
for Nn in range(1, 16):  # brute force small
    bf = sum(1 for mask in range(1 << Nn) if sum(i+1 for i in range(Nn) if mask >> i & 1) % 5 == 0)
    ok(bf == count_div5(Nn), f"o115 DP vs brute N={Nn}")
ok(count_div5(2025) == (2**2025 + 2**407)//5 and (2**2025 + 2**407) % 5 == 0, "o115 N=2025")
om = cmath.exp(2j*math.pi/5)
ok(abs(math.prod(1 + om**r for r in range(5)) - 2) < 1e-12, "o115 product of (1+w^r) is 2")

# o116: x^3 - y^3 = 3xy + 37 -> (3,-1), (1,-3)
sols = [(x_, y_) for x_ in range(-400, 401) for y_ in range(-400, 401) if x_**3 - y_**3 == 3*x_*y_ + 37]
ok(sorted(sols) == [(1, -3), (3, -1)], "o116 brute force")
dd = sp.symbols('dd')
ok(sp.expand(3*dd**2*(dd-1) + 4*(37 - dd**3)) == -dd**3 - 3*dd**2 + 148, "o116 discriminant algebra")
ok(all(not (d_**3 + 3*d_**2 >= 148) for d_ in range(-2000, 1)), "o116 no d<=0")
ok(all((d_**3 + 3*d_**2 <= 148) == (d_ <= 4) for d_ in range(2, 100)), "o116 d bound")
ok(all(Fraction(37 - d_**3, 3*(d_-1)).denominator != 1 for d_ in (2, 3)) and Fraction(37 - 64, 9) == -3, "o116 d=2,3,4")
ok(all((x_ - y_)**3 + 3*(x_*y_)*(x_ - y_) == x_**3 - y_**3 for x_ in range(-5, 6) for y_ in range(-5, 6)), "o116 identity")
print(N, "checks passed")
