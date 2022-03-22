def count(n, m):
    if n == 0: return 1
    if m == 0: return 1
    return count(n-1, m)+count(n, m-1)
n = int(input().strip())
m = int(input().strip())
print(count(n, m))