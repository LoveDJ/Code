def is_recyle(strs):
    if len(strs) == 1: return True
    elif len(strs) == 2:
        if strs[0] == strs[1]: return True
        else: return False
    else:
        if (strs[0] == strs[-1]) and is_recyle(strs[1:-1]): return True
        else: return False


in_str = input().strip()
dp = [1]*len(in_str)
for i in range(1, len(in_str)):
    for j in range(i):
        if is_recyle(in_str[j:i+1]):
            dp[i] = i - j + 1
            break
print(max(dp))
