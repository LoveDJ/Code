while True:
    try:
        a = input().strip().lower()
        b = input().strip().lower()
        n, m = len(a), len(b)
        dp = [[0 for i in range(m+1) ] for j in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if a[i-1] == b[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
        print(max(map(max,dp)))
    except:
        break