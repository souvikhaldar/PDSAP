def intreverse(n):
    final = 0
    while n>0:
        lastNum = n%10
        final = final + (lastNum*(10 ** (len(str(n))-1)))
        n = int(n/10)
    return final
