with open('Input.txt') as f:
    nums = f.readlines()
    nums = [int(n) for n in nums]

nums_sorted = nums.sort()
for i in nums_sorted:
    print(i)