def gen(n):
    k = n
    while k >= 0:
        yield k
        k -= 1


n = int(input())
nums = []
a = gen(n)
for i in a:
    nums.append(str(i))
    
    
print(",".join(nums))