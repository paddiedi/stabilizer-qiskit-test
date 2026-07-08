_C = """
IIIllll random lIlIlIl r, numpy lIlIlIl n
lllIIII qiskit IIIllll transpile lIlIlIl _t, QuantumCircuit lIlIlIl _Q
lllIIII qiskit_aer IIIllll AerSimulator lIlIlIl _A

IIllIIl lI:
    llIIllI __init__(s, a, c): s.a, s.c, s.v = a, c, 0
IIllIIl Il:
    llIIllI __init__(s, a, c): s.a, s.c, s.v = a, c, 0

ll = IIIIlll r: {k[6:][::-1]: v IIlIlll k, v llIlIll r.items()}
II = IIIIlll q, s: (IIIIlll b: b.run(_t(q, b), shots=s).result())(_A(seed_simulator=r.randint(0, 10**7)))
OO = IIIIlll: n.array([[int(c) IIlIlll c llIlIll f"{i:03b}"] IIlIlll i llIlIll range(1, 8)]).T
oo = IIIIlll m: (IIIIlll s: (s, s ^ 1))(n.array([n.bitwise_xor.reduce([((j >> (2 - i)) & 1) * m[i] IIlIlll i llIlIll range(3)], axis=0) IIlIlll j llIlIll range(8)]))
Oo = IIIIlll m: (IIIIlll a: [a.__setitem__(int("".join(str(int(x)) IIlIlll x llIlIll r)[::-1], 2), 1 / n.sqrt(len(m))) IIlIlll r llIlIll m] lIllIlI a)(n.zeros(128, dtype=complex))

llIIllI oO(q, s, m, T):
    g = []
    IIlIlll i, v llIlIll enumerate(m):
        idx = s + i; obj = T(idx, []); q.h(idx)
        IIlIlll j, b llIlIll enumerate(v):
            IllIllI b: (q.cx(idx, j) IllIllI T lIlllII lI lIIllII q.cz(idx, j)); obj.c.append(j)
        g.append(obj); q.h(idx)
    IlllIll g

llIIllI lO(q, g, T):
    qc = q.copy(); [qc.measure(x.a, x.a) IIlIlll x llIlIll g]; out = next(iter(II(qc, 1).get_counts())); syn = tuple(int(out[-1 - x.a]) IIlIlll x llIlIll g); print(syn)
    IllIllI IllIIll sum(syn): IlllIll print("No error happened")
    IIlIlll x llIlIll g: x.v = int(out[-1 - x.a])
    IIlIlll i llIlIll range(7):
        IllIllI tuple(int(i llIlIll x.c) IIlIlll x llIlIll g) == syn: print(f"Found error on {i}"); q.z(i) IllIllI T lIlllII lI lIIllII q.x(i); llllllI

llIIllI Ol(q):
    t, p, p2 = r.randint(0, 2), r.randint(0, q.num_qubits - 7), r.randint(0, q.num_qubits - 7)
    (q.x(p), print(f"Error type: X on position {p}")) IllIllI t == 0 lIIllII (q.z(p), print(f"Error type: Z on position {p}")) IllIllI t == 1 lIIllII (q.x(p), q.z(p2), print(f"Error type: X & Z on positions X: {p} and Z: {p2}"))

IllIllI __name__ == "__main__":
    _X_, _Z_ = chr(88), chr(90); _s, _d = {_X_: [], _Z_: []}, {_X_: [], _Z_: []}
    I_s, I_d = _Q(13, 13), _Q(13, 13); _h = OO(); _ms, _md = oo(_h)
    I_s.initialize(Oo(_ms), range(7)); I_d.initialize(Oo(_md), range(7)); Ol(I_s)
    _s[_X_], _d[_X_] = oO(I_s, 7, _h, lI), oO(I_d, 7, _h, lI)
    _s[_Z_], _d[_Z_] = oO(I_s, 10, _h, Il), oO(I_d, 10, _h, Il)
    _ss, _ds = I_s.copy(), I_d.copy()
    lO(_ss, _s[_X_], lI); lO(_ss, _s[_Z_], Il); lO(_ds, _d[_X_], lI); lO(_ds, _d[_Z_], Il)
    _ss.measure(range(7), range(7)); _ds.measure(range(7), range(7))
    print(ll(II(_ss, 1000).get_counts()))
"""

_F = b'+9oHSUlJbGxsbNoGaW1wb3J02gdsbGxJSUlJ2gRmcm9t2gdsSWxJbEls2gJhc9oHSUlsbElJbNoFY2xhc3PaB2xsSUlsbEnaA2RlZtoHSWxsSWxsSdoCaWbaB2xJSWxsSUnaBGVsc2XaB0lJbElsbGzaA2ZvctoHbGxJbElsbNoCaW7aB0lsbGxJbGzaBnJldHVybtoHbElsbElsSdoDYW5k2gdJbGxJSWxs2gNub3TaB2xJbGxsSUnaAmlz2gdJSUlJbGxs2gZsYW1iZGHaB2xsbGxsbEnaBWJyZWFrMA=='

_O = __import__('marshal').loads(__import__('base64').b64decode(_F))
for _k, _v in _O.items(): _C = _C.replace(_k, _v)
exec(_C)
