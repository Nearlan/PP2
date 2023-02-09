def check(a):
    b = len(a) - 1
    for x in range (0, b + 1):
        if(a[x] != a[b - x]):
            print("NO")
            return
    print("YES")
    
        


text = str(input())
check(text)
