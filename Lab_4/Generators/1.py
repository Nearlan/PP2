def gen(n):
    k = 1
    while k * k <= n:
        yield k * k
        k += 1


n = int(input())
a = gen(n)
for i in a:
    print(i)