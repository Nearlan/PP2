def check(list):
    for x in list:
        if x == 0:
            continue
        chk = True
        for y in range(2, x):
            if x % y == 0 or x == 1:
                chk = False
                break
        if chk:
            print(x," ", end = "")
                

list = list(map(int, input().split()))
check(list)