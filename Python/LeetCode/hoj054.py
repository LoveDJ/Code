n = int(input().strip())
num_arr = []
for i in range(n): num_arr.append(int(input().strip()))
dp = [1]*n
for i in range(1, n):
    tem = []
    for v in range(i):
        if num_arr[i] > num_arr[v]: tem.append(dp[v])
    if tem: dp[i] = max(tem) + 1
print(max(dp))

