def primeornot(n):
    if n < 0:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
def sumprimes(l):
    sum = 0
    for j in l:
        if primeornot(j):
            sum = sum + j
    return sum

