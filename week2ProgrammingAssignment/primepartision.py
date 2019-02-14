def primes(n):
    l = []
    for i in range(2,n):
        flag = 0
        for j in range(2,i-1):
            if i % j == 0:
                flag = 1
        if flag == 0:
            l.append(i)
    return l

def prime_check(n):
    flag = 0
    for i in range(2,n-1):
        if n % i == 0:
            flag = 1
    if flag == 0:
        return True
    else:
        return False

def primepartition(n):
    if n < 0:
        return False
    else:
        l = primes(n)
        for i in l:
            check = n - i
            if prime_check(check):
                return True
        return False

