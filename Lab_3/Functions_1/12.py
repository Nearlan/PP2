def histogram(nums):
    for x in nums:
        for y in range(x):
            print("*", end ="")
        print("")
n = int(input())
nums = []
for x in range(n):
    a = int(input())
    nums.append(a)
histogram(nums)