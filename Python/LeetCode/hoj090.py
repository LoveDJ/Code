def LIS(nums):
    dp = [1]* len(nums)
    for i, num in enumerate(nums):
        if i > 0:
            tem = []
            for j in range(i):
                if num > nums[j]:
                    tem.append(dp[j])
            if tem: dp[i] = max(tem)+1
    return max(dp)

n = int(input().strip())
nums = list(map(int, input().strip().split()))
maxN = 1
for i, num in enumerate(nums):
    temN = 1
    numListLeft = [x for x in nums[:i] if x < num]
    numListRight = [x for x in nums[i+1:] if x < num]
    if len(numListLeft)>0: temN += LIS(numListLeft)
    if len(numListRight)>0: temN += LIS(numListRight[::-1])
    maxN = max(maxN, temN)
print(n - maxN)