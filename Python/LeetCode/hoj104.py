def dfs(i, dis, nums, tar):
    if i == len(nums):
        return abs(dis) == tar
    else:
        return dfs(i+1, dis - nums[i], nums, tar) or dfs(i+1, dis + nums[i], nums, tar)


n = int(input().strip())
nums = []
nums_left = []
for i in range(n):
    nums.append(int(input().strip()))
sum3 = 0
sum5 = 0
for num in nums:
    if num%3 == 0: sum3 += num
    elif num%5 == 0: sum5 += num
    else: nums_left.append(num)
if dfs(0, 0, nums_left, abs(sum3 - sum5)): print('true')
else: print('false')