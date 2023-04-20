n = int(input())
nums = list(map(int, input().split()))
target = int(input())
complements = {}
for i in range(n):
    complement = target - nums[i]
    if complement in complements:
        print(complements[complement], i)
        break
    else:
        complements[nums[i]] = i