def check(nums):
    for x in nums:
        chc = True
        for y in nums:
            if(x == y):
                if not chc:
                    nums.remove(y)
                chc = False
    print(nums)
    
         
    
        


list = list(input().split())
check(list)