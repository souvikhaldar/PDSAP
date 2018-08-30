def matched(s):
 flag = 0
 for i in s:
  if i == '(':
   flag +=1
  if flag >0 and i == ')':
   flag -= 1
   continue
  if flag <= 0 and i == ')':
   return False
 if flag == 0:
  return True
 else:
  return False

