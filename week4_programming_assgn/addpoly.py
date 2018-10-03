import collections
def ctr(c):
    p = [(coeff, exp) for exp, coeff in c.items() if coeff != 0]
    p.sort(key = lambda pair: pair[1], reverse = True)
    return p
def addpoly(p, q):
    r = collections.Counter()
    for coeff, exp in (p + q):
        r[exp] += coeff
    return ctr(r)
def mulpoly(p, q):
    r = collections.Counter()
    for (c1, e1), (c2, e2) in itertools.product(p, q):
        r[e1 + e2] += c1 * c2
    return ctr(r)
