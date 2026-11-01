#!/usr/bin/env python3
"""Code checks for batch2-hard-c (m75-m89, adapted from MathNet)."""
import itertools, math, random
from fractions import Fraction
from functools import lru_cache
import sympy as sp

ok = []


def check(name, cond):
    assert cond, name
    ok.append(name)


random.seed(2026)


def is_bipartite(n, adj):
    col = [-1] * n
    for s in range(n):
        if col[s] >= 0:
            continue
        col[s] = 0
        st = [s]
        while st:
            u = st.pop()
            for v in range(n):
                if adj[u] >> v & 1:
                    if col[v] < 0:
                        col[v] = col[u] ^ 1
                        st.append(v)
                    elif col[v] == col[u]:
                        return False
    return True


# ---------------- m75 (09jl) triangle-free, min degree > 2n/5 => bipartite ----------------
def triangle_free_graphs(n):
    """All labelled triangle-free graphs on n vertices (adjacency bitmasks), built vertex by vertex:
    the new vertex is joined to an independent set of the old ones."""
    graphs = [[]]
    for k in range(n):
        new = []
        for g in graphs:
            for S in range(1 << k):
                # S must be independent in g
                if any((S >> i & 1) and (g[i] & S) for i in range(k)):
                    continue
                h = [g[i] | ((S >> i & 1) << k) for i in range(k)] + [S]
                new.append(h)
        graphs = new
    return graphs


good = True
tight = False
for n in range(3, 8):
    for g in triangle_free_graphs(n):
        degs = [bin(x).count("1") for x in g]
        if 5 * min(degs) > 2 * n:
            good &= is_bipartite(n, g)
        if 5 * min(degs) == 2 * n and not is_bipartite(n, g):
            tight = True
check("m75 triangle-free & min deg > 2n/5 => bipartite (all n<=7)", good)
check("m75 C5 is tight (deg = 2n/5, not bipartite)", tight)
# blow-ups of C5 are tight for every multiple of 5
for t in range(1, 5):
    n = 5 * t
    g = [0] * n
    for u in range(n):
        for v in range(n):
            if (u // t - v // t) % 5 in (1, 4):
                g[u] |= 1 << v
    tri = any(g[u] >> v & 1 and g[v] >> w & 1 and g[u] >> w & 1 for u in range(n) for v in range(n) for w in range(n))
    check(f"m75 C5 blow-up t={t} triangle-free, 2n/5-regular, not bipartite",
          not tri and all(bin(x).count("1") * 5 == 2 * n for x in g) and not is_bipartite(n, g))


# ---------------- m76 (00hd) Dreamland: functional graph, reach within d flights ----------------
def chromatic(n, nbrs):
    order = sorted(range(n), key=lambda v: -len(nbrs[v]))
    best = n
    for k in range(1, n + 1):
        col = {}
        def bt(i):
            if i == n:
                return True
            v = order[i]
            used = {col[u] for u in nbrs[v] if u in col}
            for c in range(k):
                if c not in used:
                    col[v] = c
                    if bt(i + 1):
                        return True
                    del col[v]
            return False
        if bt(0):
            return k
    return best


def dream_max(n, d):
    worst = 0
    for f in itertools.product(range(n), repeat=n):
        if any(f[i] == i for i in range(n)):
            continue
        nbrs = [set() for _ in range(n)]
        for u in range(n):
            x = u
            for _ in range(d):
                x = f[x]
                if x != u:
                    nbrs[u].add(x); nbrs[x].add(u)
        worst = max(worst, chromatic(n, nbrs))
    return worst


check("m76 analogue d=1, n=5: worst case needs exactly 3 = 2d+1 groups", dream_max(5, 1) == 3)
check("m76 analogue d=2, n=6: worst case needs exactly 5 = 2d+1 groups", dream_max(6, 2) == 5)
check("m76 57-cycle: every pair within 28 one way", all(min((j - i) % 57, (i - j) % 57) <= 28 for i in range(57) for j in range(57) if i != j))


# ---------------- m77 (0gtu) regular graph, non-friends have k-1 common friends ----------------
def regular_graphs_fixed0(N, m):
    """m-regular graphs on N vertices with N(0) = {1..m} (WLOG up to relabelling)."""
    pairs = [(i, j) for i in range(1, N) for j in range(i + 1, N)]
    adj = [set() for _ in range(N)]
    for v in range(1, m + 1):
        adj[0].add(v); adj[v].add(0)
    out = []
    def bt(idx):
        if idx == len(pairs):
            if all(len(a) == m for a in adj):
                out.append([set(a) for a in adj])
            return
        i, j = pairs[idx]
        # remaining capacity check for i when its last pair passes
        if len(adj[i]) < m and len(adj[j]) < m:
            adj[i].add(j); adj[j].add(i)
            bt(idx + 1)
            adj[i].discard(j); adj[j].discard(i)
        # skipping: vertex i must still be able to reach degree m with later pairs
        rest_i = sum(1 for (a, b) in pairs[idx + 1:] if a == i or b == i)
        if len(adj[i]) + rest_i >= m:
            bt(idx + 1)
    bt(0)
    return out


def comp_is_cocktail(adj, N, m):
    seen = set()
    for s0 in range(N):
        if s0 in seen:
            continue
        comp = {s0}; st = [s0]
        while st:
            u = st.pop()
            for v in adj[u]:
                if v not in comp:
                    comp.add(v); st.append(v)
        seen |= comp
        if len(comp) != m + 2:
            return False
        # each vertex non-adjacent to exactly one other vertex of the component
        if any(len(comp - adj[u] - {u}) != 1 for u in comp):
            return False
    return True


good = True
found_any = 0
for N in range(4, 9):
    for m in range(3, N):
        for adj in regular_graphs_fixed0(N, m):
            if all(len(adj[u] & adj[v]) == m - 2 for u in range(N) for v in adj[u]):
                found_any += 1
                good &= comp_is_cocktail(adj, N, m)
check("m77 m>=3, lambda=m-2  =>  components are K_{m+2} minus perfect matching (N<=8)", good and found_any > 0)

# identity: common G-neighbours of H-adjacent u,v = n - 2m + lambda for m-regular H
good = True
for trial in range(200):
    N = random.randint(5, 9)
    # random regular graph by rejection: circulant
    S = random.sample(range(1, N // 2 + 1), random.randint(1, (N - 1) // 2))
    adjH = [set() for _ in range(N)]
    for u in range(N):
        for d in S:
            adjH[u].add((u + d) % N); adjH[u].add((u - d) % N)
    m = len(adjH[0])
    for u in range(N):
        for v in adjH[u]:
            commonG = sum(1 for x in range(N) if x not in (u, v) and x not in adjH[u] and x not in adjH[v])
            good &= commonG == N - 2 * m + len(adjH[u] & adjH[v])
check("m77 complement identity", good)

ans = {2024, 2026}
for d in sp.divisors(2022):
    if d % 2 == 0 and d >= 6:
        b = 2022 // d + 1
        ans.add(b * d)
check("m77 answer set", ans == {2024, 2026, 2028, 2696, 4044})
# direct check for n=2028: 338 copies of K6 minus perfect matching, complement degree and common friends
a = 3; b = 338; n = 2 * a * b
def H_adj(u, v):
    return u != v and u // (2 * a) == v // (2 * a) and (u ^ 1) != v
u, v = 0, 2  # H-adjacent
deg_G = sum(1 for x in range(n) if x != u and not H_adj(u, x))
common = sum(1 for x in range(n) if x not in (u, v) and not H_adj(u, x) and not H_adj(v, x))
check("m77 n=2028 construction: degree 2023, non-friends share 2022", deg_G == 2023 and common == 2022)

# ---------------- m78 (06pe) monochromatic divisible triples ----------------
def mono_div(n, red):
    cnt = 0
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            z = (-x - y) % n or n
            if (x in red) == (y in red) == (z in red):
                cnt += 1
    return cnt


good = True
for n in range(1, 13):
    for _ in range(15):
        red = {x for x in range(1, n + 1) if random.random() < 0.5}
        r = len(red); b = n - r
        good &= mono_div(n, red) == r * r - r * b + b * b
check("m78 formula r^2-rb+b^2 (random colourings, n<=12)", good)
sols = sorted({r + b for r in range(0, 200) for b in range(0, 200) if r * r - r * b + b * b == 2007})
check("m78 only n=69,84", sols == [69, 84])
check("m78 actual colouring n=69", mono_div(69, set(range(1, 52))) == 2007)
check("m78 actual colouring n=84", mono_div(84, set(range(1, 52))) == 2007)
check("m78 discriminants", 225 - 8 == 217 and 256 - 132 == 124 and not sp.sqrt(217).is_integer and not sp.sqrt(124).is_integer and sp.isprime(223))

# ---------------- m79 (0j80) eleven 45-sets ----------------
U = list(itertools.combinations(range(11), 3))
Ai = [{T for T in U if i in T} for i in range(11)]
check("m79 equality example sizes", all(len(a) == 45 for a in Ai) and all(len(Ai[i] & Ai[j]) == 9 for i in range(11) for j in range(i + 1, 11)) and len(set().union(*Ai)) == 165 and 165 + 60 == 225)
check("m79 sums", 11 * 45 == 495 and math.comb(11, 2) * 9 == 495 and Fraction(495 ** 2, 1485) == 165)

# ---------------- m80 (0j2i) number of good subsets is odd ----------------
good = True
for _ in range(300):
    T = random.sample(range(2, 40), random.randint(0, 9))
    cnt = 0
    P = 0
    subsets = [S for k in range(len(T) + 1) for S in itertools.combinations(T, k)]
    for S in subsets:
        if all(any(math.gcd(s_, t) > 1 for s_ in S) for t in T):
            cnt += 1
    for X in subsets:
        for Y in subsets:
            if all(math.gcd(x, y) == 1 for x in X for y in Y):
                P += 1
    good &= cnt % 2 == 1 and P % 2 == 1
check("m80 good-subset count odd and pair count odd (random T)", good)

# ---------------- m81 (0hxm) tournament edge colouring ----------------
def min_colours_some_tournament(n, kmax):
    pairs = list(itertools.combinations(range(n), 2))
    best = None
    for k in range(1, kmax + 1):
        for orient in itertools.product((0, 1), repeat=len(pairs)):
            edges = [(a, b) if o == 0 else (b, a) for (a, b), o in zip(pairs, orient)]
            for col in itertools.product(range(k), repeat=len(edges)):
                bad = False
                outc = [set() for _ in range(n)]
                inc = [set() for _ in range(n)]
                for (u, v), c in zip(edges, col):
                    outc[u].add(c); inc[v].add(c)
                if all(not (outc[v] & inc[v]) for v in range(n)):
                    return k
    return None


check("m81 f(2)=1, f(3)=2, f(4)=2", [min_colours_some_tournament(n, 3) for n in (2, 3, 4)] == [1, 2, 2])
check("m81 f(5)=3 (no tournament on 5 vertices works with 2 colours)", min_colours_some_tournament(5, 3) == 3)
good = True
for n in range(2, 130):
    k = math.ceil(math.log2(n))
    outc = [set() for _ in range(n)]; inc = [set() for _ in range(n)]
    for i in range(n):
        for j in range(i):
            c = (i ^ j).bit_length() - 1
            assert (i >> c) & 1 == 1 and (j >> c) & 1 == 0 and c < k
            outc[i].add(c); inc[j].add(c)
    good &= all(not (outc[v] & inc[v]) for v in range(n))
check("m81 binary construction valid with ceil(log2 n) colours, n<130", good)

# ---------------- m82 (0gqd) three cities reachable within two flights ----------------
def central_count(n, beats):
    cnt = 0
    for a in range(n):
        if all(x == a or beats[x][a] or any(beats[x][y] and beats[y][a] for y in range(n)) for x in range(n)):
            cnt += 1
    return cnt


good = True
mins = {}
for n in range(4, 7):
    pairs = list(itertools.combinations(range(n), 2))
    mn = n
    for orient in itertools.product((0, 1), repeat=len(pairs)):
        beats = [[False] * n for _ in range(n)]
        for (a, b), o in zip(pairs, orient):
            if o == 0:
                beats[a][b] = True
            else:
                beats[b][a] = True
        if any(not any(beats[x]) for x in range(n)):
            continue
        indeg = [sum(beats[y][x] for y in range(n)) for x in range(n)]
        # the three-step construction from the solution
        A1 = max(range(n), key=lambda x: indeg[x])
        U1 = [x for x in range(n) if beats[A1][x]]
        A2 = max(U1, key=lambda x: indeg[x])
        U2 = [x for x in range(n) if beats[A2][x]]
        A3 = max(U2, key=lambda x: indeg[x])
        def central(a):
            return all(x == a or beats[x][a] or any(beats[x][y] and beats[y][a] for y in range(n)) for x in range(n))
        good &= len({A1, A2, A3}) == 3 and central(A1) and central(A2) and central(A3)
        mn = min(mn, central_count(n, beats))
    mins[n] = mn
check("m82 procedure gives 3 distinct central cities (n=4..6, all tournaments without sink)", good)
check("m82 minimum number of central cities is exactly 3 (n=4..6)", all(v == 3 for v in mins.values()))

# ---------------- m83 (0gpe) degree-balanced tournaments are strongly connected ----------------
def strongly_connected(n, out_mask):
    def reach(start, nb):
        seen = 1 << start; frontier = 1 << start
        while frontier:
            new = 0
            for v in range(n):
                if frontier >> v & 1:
                    new |= nb[v]
            frontier = new & ~seen; seen |= new
        return seen
    full = (1 << n) - 1
    in_mask = [sum(1 << u for u in range(n) if out_mask[u] >> v & 1) for v in range(n)]
    return reach(0, out_mask) == full and reach(0, in_mask) == full


good = True
for n in range(3, 7):
    pairs = list(itertools.combinations(range(n), 2))
    M = None
    for orient in itertools.product((0, 1), repeat=len(pairs)):
        out_mask = [0] * n
        for (a, b), o in zip(pairs, orient):
            if o == 0:
                out_mask[a] |= 1 << b
            else:
                out_mask[b] |= 1 << a
        if not strongly_connected(n, out_mask):
            od = [bin(x).count("1") for x in out_mask]
            md = max(abs(2 * d - (n - 1)) for d in od)
            M = md if M is None else min(M, md)
    good &= M == n - 1 - 2 * ((n - 2) // 4)
check("m83 small n: least max|out-in| of a non-strong tournament = n-1-2*floor((n-2)/4)", good)
check("m83 formula at n=2011 gives 1006", 2010 - 2 * (2009 // 4) == 1006)
# the k=1006 counterexample
n = 2011
outd = [0] * n; ind = [0] * n
X = list(range(1005)); Y = list(range(1005, 2011))
edges = 0
for i in range(1005):
    for d in range(1, 503):
        outd[i] += 1; ind[(i + d) % 1005] += 1; edges += 1
for i in range(1006):
    for d in range(1, 503):
        outd[1005 + i] += 1; ind[1005 + (i + d) % 1006] += 1; edges += 1
for i in range(503):
    outd[1005 + i] += 1; ind[1005 + i + 503] += 1; edges += 1
for x in X:
    for y in Y:
        outd[x] += 1; ind[y] += 1; edges += 1
check("m83 counterexample is a tournament with max |out-in| = 1006", edges == math.comb(2011, 2) and all(outd[v] + ind[v] == 2010 for v in range(n)) and max(abs(outd[v] - ind[v]) for v in range(n)) == 1006)
check("m83 bound |V1| >= 1007", min(s_ for s_ in range(1, 2012) if math.comb(s_, 2) >= 503 * s_) == 1007)

# ---------------- m84 (0j02) USAMO 2010 switches ----------------
def max_switches(n):
    import sys
    sys.setrecursionlimit(100000)
    @lru_cache(None)
    def longest(state):
        best = 0
        for p_ in range(n):
            q_ = (p_ + 1) % n  # q_ is directly in front of p_
            if state[q_] <= state[p_] - 2:
                s_ = list(state); s_[p_], s_[q_] = s_[q_], s_[p_]
                best = max(best, 1 + longest(tuple(s_)))
        return best
    return max(longest(perm) for perm in itertools.permutations(range(1, n + 1)))


check("m84 longest switch sequence equals C(n,3) for n=3..7", all(max_switches(n) == math.comb(n, 3) for n in range(3, 8)))
check("m84 sum (j-i-1) = C(n,3)", all(sum(j - i - 1 for i in range(1, n + 1) for j in range(i + 1, n + 1)) == math.comb(n, 3) for n in range(1, 40)))

# ---------------- m85 (06se) separating red and blue points by lines ----------------
def hull(pts):
    pts = sorted(pts)
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lo = []; hi = []
    for p_ in pts:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], p_) <= 0:
            lo.pop()
        lo.append(p_)
    for p_ in reversed(pts):
        while len(hi) >= 2 and cross(hi[-2], hi[-1], p_) <= 0:
            hi.pop()
        hi.append(p_)
    return lo[:-1] + hi[:-1]


def side(line, p_):
    (a, b, c) = line  # a x + b y + c
    return a * p_[0] + b * p_[1] + c


def strip_lines(A, B, others):
    a, b = B[1] - A[1], A[0] - B[0]
    c = -(a * A[0] + b * A[1])
    nrm = math.hypot(a, b)
    delta = min(abs(side((a, b, c), q)) / nrm for q in others)
    return [(a, b, c - delta / 2 * nrm), (a, b, c + delta / 2 * nrm)]


def cut_off(P, pts, Q=None):
    """line with only P (and Q if given, Q adjacent hull vertex) on one side"""
    others = [q for q in pts if q != P and q != Q]
    if Q is None:
        # supporting line through P: use direction perpendicular to (P - centroid of others) won't always work;
        # instead use the bisector of the two hull edges at P
        H = hull(pts); i = H.index(P)
        Pm, Pp = H[i - 1], H[(i + 1) % len(H)]
        a, b = Pp[1] - Pm[1], Pm[0] - Pp[0]  # direction parallel to chord of neighbours
    else:
        a, b = Q[1] - P[1], P[0] - Q[0]
    c = -(a * P[0] + b * P[1])
    sgnP = side((a, b, c), others[0])
    assert all(side((a, b, c), q) * sgnP > 0 for q in others)
    nrm = math.hypot(a, b)
    eps = min(abs(side((a, b, c), q)) / nrm for q in others) / 2
    return (a, b, c - (eps * nrm if sgnP > 0 else -eps * nrm))


good = True
for trial in range(300):
    r = random.choice([1, 3, 5, 7])
    pts = []
    while len(pts) < 2 * r + 1:
        q = (random.random(), random.random())
        pts.append(q)
    red, blue = pts[:r], pts[r:]
    H = hull(pts)
    lines = []
    hr = [P for P in H if P in red]
    if hr:
        R = hr[0]; lines.append(cut_off(R, pts)); rest = [q for q in red if q != R]
    else:
        B1, B2 = H[0], H[1]; lines.append(cut_off(B1, pts, B2)); rest = [q for q in blue if q not in (B1, B2)]
    for i in range(0, len(rest), 2):
        A, B = rest[i], rest[i + 1]
        lines += strip_lines(A, B, [q for q in pts if q not in (A, B)])
    good &= len(lines) == r
    good &= all(abs(side(L, q)) > 1e-12 for L in lines for q in pts)
    good &= all(any(side(L, x) * side(L, y) < 0 for L in lines) for x in red for y in blue)
check("m85 construction separates colours with r lines (random configurations)", good)
cols = ["R" if i % 2 == 1 else "B" for i in range(4027)]  # B,R,B,...,B : 2013 R, 2014 B
check("m85 alternating circle: 2013 red, 4026 bichromatic sides", cols.count("R") == 2013 and sum(cols[i] != cols[(i + 1) % 4027] for i in range(4027)) == 4026)

# ---------------- m86 (06x0) pebble piles ----------------
def min_piles(n):
    start = tuple([1] * n)
    seen = {start}; stack = [start]; best = n
    while stack:
        st = stack.pop(); best = min(best, len(st))
        L = list(st)
        for i in range(len(L)):
            for j in range(i + 1, len(L)):
                for c in range(1, min(L[i], L[j]) + 1):
                    M = [x for k, x in enumerate(L) if k not in (i, j)] + [L[i] - c, L[j] - c, 2 * c]
                    t = tuple(sorted(x for x in M if x > 0))
                    if t not in seen:
                        seen.add(t); stack.append(t)
    return best


check("m86 exhaustive n<=12: 1 pile iff power of 2, else 2", all(min_piles(n) == (1 if n & (n - 1) == 0 else 2) for n in range(1, 13)))


def construct(n):
    N = n.bit_length() - 1
    m = n - 2 ** N
    piles = {"L": 2 ** N, "two": 0}
    singles = m
    # step 2
    piles["L"] -= 1; singles -= 1; piles["two"] = 2
    for _ in range(2 ** N - 1 - m):
        piles["L"] -= 1; singles += 1  # old pile of 2 becomes a single, new pile of 2
    assert piles["L"] == m and singles == 2 ** N - 2
    total_twos = singles // 2 + 1
    return sorted([piles["L"], 2 * total_twos]), m


check("m86 construction ends with piles m and 2^N", all(construct(n)[0] == sorted([n - 2 ** (n.bit_length() - 1), 2 ** (n.bit_length() - 1)]) for n in range(3, 3000) if n & (n - 1)))

# ---------------- m87 (03u9) IMO 2007 P5 ----------------
check("m87 no a!=b with 4ab-1 | (4a^2-1)^2 for a,b<=400",
      all(a == b for a in range(1, 401) for b in range(1, 401) if (4 * a * a - 1) ** 2 % (4 * a * b - 1) == 0))
check("m87 equivalence with 4ab-1 | (a-b)^2 for a,b<=200",
      all(((4 * a * a - 1) ** 2 % (4 * a * b - 1) == 0) == ((a - b) ** 2 % (4 * a * b - 1) == 0) for a in range(1, 201) for b in range(1, 201)))

# ---------------- m88 (0ix6) mn-1 | (n^2-n+1)^2 ----------------
LIM = 1500
sol = {(m, n) for m in range(1, LIM) for n in range(1, LIM) if m * n > 1 and (n * n - n + 1) ** 2 % (m * n - 1) == 0}
fam = {(2, 2)} | {(t * t + 1, (t + 1) ** 2 + 1) for t in range(60)} | {((t + 1) ** 2 + 1, t * t + 1) for t in range(60)}
fam = {p_ for p_ in fam if max(p_) < LIM}
check("m88 brute force solutions = (2,2) and consecutive t^2+1 pairs (m,n<1500)", sol == fam)
check("m88 equivalent symmetric form", all(((n * n - n + 1) ** 2 % (m * n - 1) == 0) == ((m + n - 1) ** 2 % (m * n - 1) == 0) for m in range(1, 150) for n in range(1, 150) if m * n > 1))
check("m88 k>=3 always and k in {3,4} for solutions", all((m + n - 1) ** 2 >= 3 * (m * n - 1) for m in range(1, 200) for n in range(1, 200)) and {(m + n - 1) ** 2 // (m * n - 1) for (m, n) in sol} == {3, 4})
t = sp.symbols("t")
check("m88 identity (t^2+1)((t+1)^2+1)-1=(t^2+t+1)^2", sp.expand((t**2 + 1) * ((t + 1) ** 2 + 1) - 1 - (t**2 + t + 1) ** 2) == 0)
check("m88 (2n-1)^2 < 4(n^2-1) for n>=2", all((2 * n - 1) ** 2 < 4 * (n * n - 1) for n in range(2, 1000)))

# ---------------- m89 (0d33) sequence with all terms and all gaps exactly once ----------------
seq = [1]
for rnd in range(40):
    M = max(seq); vals = set(seq)
    x = next(v for v in range(1, M + 3) if v not in vals)
    A = 2 * M + 2
    seq += [A, x]
    M = max(seq); gaps = {abs(seq[i] - seq[i + 1]) for i in range(len(seq) - 1)}
    y = next(v for v in range(1, M + 2) if v not in gaps)
    A = 2 * M + 2
    seq += [A, A + y]
gaps = [abs(seq[i] - seq[i + 1]) for i in range(len(seq) - 1)]
check("m89 construction: distinct terms, distinct gaps", len(set(seq)) == len(seq) and len(set(gaps)) == len(gaps))
check("m89 construction: first 40 integers appear as terms and as gaps after 40 rounds", set(range(1, 41)) <= set(seq) and set(range(1, 41)) <= set(gaps))

print(f"{len(ok)} checks passed")
