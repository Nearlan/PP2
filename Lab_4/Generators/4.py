def gen(n1, n2):
    k = n1
    while k <= n2:
        yield k * k
        k += 1


n1 = int(input())
n2 = int(input())
nums = []
a = gen(n1, n2)
for i in a:
    nums.append(str(i))
    
    
print(",".join(nums))