def reverse(x):
    y = x[:]
    siz = len(y)
    for i in range(siz//2):
        y[i],y[siz-i-1] = y[siz-i-1],y[i]
    return y
def matrixflip(m,d):
    f = m[:]
    if d == 'h':
        for l in range(len(f)):
            new_l = reverse(f[l])
            f[l] = new_l
        return f
    elif d == 'v':
        new_l = reverse(f)
        return(new_l)
    else:
        return f

