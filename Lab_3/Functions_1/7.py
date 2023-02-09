def check(nums):
    for x in range(0, len(nums) - 2):
        if(nums[x] == 3 and nums[x + 1] == 3):
            print("yes")
            return
    print("no")
        


list = list(map(int, input().split()))
check(list)