x = input().strip()[::-1]
res = ""
for ch in x:
    if ch not in res:
        res += ch
print(int(res))