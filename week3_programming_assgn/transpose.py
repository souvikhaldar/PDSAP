def transpose(m):
    k = 0
    w, h = len(m), len(m[0])
    arr = [[0 for x in range(w)] for y in range(h)] 
    for i in range(len(m[0])):
        for j in m:
            arr[k].extend(list(j[i]))
        k += 1
    return arr
