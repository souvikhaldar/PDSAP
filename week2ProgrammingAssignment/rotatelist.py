def rotatelist(l,n):
    nl = []
    if n > len(l):
        init = n % len(l)
        for i in range(init,len(l)):
            nl.append(l[i])
        for j in range(init):
            nl.append(l[j])
    else:
        for i in range(n,len(l)):
            nl.append(l[i])
        for j in range(n):
            nl.append(l[j])
    return nl
print(rotatelist([1,2,3,4,5],1))
print(rotatelist([1,2,3,4,5],3))
print(rotatelist([1,2,3,4,5],12))
