def calRatio(s):
    count = 0
    for ch in s:
        if ch =='C' or ch =='c' or ch=='G' or ch=='g':
            count += 1
    return count/len(s)


s = input().strip()
n = int(input().strip())
if len(s) <= n: print(s)
else:
    res = ""
    maxRatio = 0
    for i in range(len(s)-n+1) :
        ratio = calRatio(s[i:i+n])
        if ratio > maxRatio:
            maxRatio = ratio
            res = s[i:i+n]
    print(res)

