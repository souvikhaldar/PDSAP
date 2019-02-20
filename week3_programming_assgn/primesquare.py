import math
def prime_check(n):
    flag = 0
    for i in range(2,n-1):
        if n % i == 0:
            flag = 1
    if flag == 0:
        return True
    else:
        return False
def is_square(n):
    if math.sqrt(n) % 1 == 0:
        return True
    else:
        return False

def primesquare(l):
    flag = 0
    if len(l) == 1:
        if is_square(l[0]) or prime_check(l[0]):
            return True
        else:
            return False
    if is_square(l[0]):
        for i in range(1,len(l)):
            if i % 2 == 0:
                if not is_square(l[i]):
                    flag = 1
                    break
            elif i %2 != 0:
                if not prime_check(l[i]):
                    flag = 1
                    break
        if flag == 0:
            return True
        else:
            return False 
    elif prime_check(l[0]):
        for i in range(1,len(l)):
            if i % 2 == 0:
                if not prime_check(l[i]):
                    flag = 1
                    break
            elif i % 2 != 0:
                if not is_square(l[i]):
                    flag = 1
                    break
        if flag == 0:
            return True
        else:
            return False 
    else:
        return False
    


