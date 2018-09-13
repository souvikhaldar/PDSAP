def orangecap(a):
    sum = {}
    for i in a.values():
        for j in i.keys():
            sum[j] = 0
    for i in a.values():
        for j in i.keys():
            sum[j] = sum[j] + i[j]
    maximum = max(sum.values())
    for i in sum.keys():
        if sum[i] == maximum:
            req = (i,maximum)
            print(tuple(req))
            break
