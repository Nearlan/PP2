
def gen(n):
    k = 0
    while k <= n:
        if k % 12 == 0:
         yield k
        k += 1


n = int(input())
nums = []
a = gen(n)
for i in a:
    nums.append(str(i))
    
    
print(",".join(nums))