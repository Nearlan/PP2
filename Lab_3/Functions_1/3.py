def solve(numberheads, numberlegs):
    b = 0
    c = 0
    while (b * 2 + c * 4) != numberlegs:
        c = numberheads - b
        if b > numberheads:
            print("There is no solution!")
            return 
        b += 1
    print("Number of chickens: ", b,"Number of rabbits: ", c)
    
    


legs, heads = int(input()), int(input())
solve(heads, legs)