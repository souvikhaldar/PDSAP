def valley(l):
    upflag = 0
    downflag = 0
    i = 0
    length = len(l)
    if length < 5:
        return False
    while l[i] > l[i+1] and length > 2:
        upflag +=1
        i+=1
        length -= 1
    if upflag >= 2:
        while l[i]<l[i+1] and length > 2:
            downflag +=1
            i+=1
            length -=1
    else:
        return False

    if upflag >=2 and downflag >= 2:
        return True
    else:
        return False

