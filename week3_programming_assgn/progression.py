def progression(l):
    flag = 0
    if len(l) == 1:
        return True
    for i in range(len(l)-2):
        if l[i+1] - l[i] != l[i+2] - l[i+1]:
            flag = 1
            break
    if flag == 0:
        return True
    else:
        return False


