def matched(s):
  a = 0
  for i in range(0, len(s)):
    if s[i] == '(':
      if a >= 0:
        a = a + 1
    elif s[i] == ')':
      a = a - 1
  if a == 0:
    return True
  else :
    return False
def nestingdepth(n):
    if matched(n) == False:
        return -1
    count = 0
    for i in n:
        if i == "(":
            count+=1
    if count == 0:
        return 0
    else:
        ct = 0
        maxi = 0
        for j in n:
            if j == "(":
                ct +=1
                if ct > maxi:
                    maxi = ct
            elif j == ")":
                ct -=1
        return maxi
print(nestingdepth("zb%78"))
print(nestingdepth("(7)(a"))
print(nestingdepth("a)*(?"))
print(nestingdepth("((jkl)78(A)&l(8(dd(FJI:),):)?)"))
