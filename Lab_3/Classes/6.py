def boolc(x):
    if x == 1 or x == 0:
        return False
    for i in range(2,x-1):
        if x % i == 0:
            return True
    return False
        
    
nmbrs = list(map(int, input().split()))
filnums = list(filter(lambda x: (boolc(x)), nmbrs))
print(filnums)