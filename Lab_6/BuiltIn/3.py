def check(text):
 rext = reversed(text)
 i = iter(text)
 j = iter(rext)
 n = len(text) / 2
 while n > 0:
     if(next(i) != next(j)):
         return False
     n -= 1
 return True



print(check("AssA"))
print(check("AsadasA"))
print(check("ABcBa"))