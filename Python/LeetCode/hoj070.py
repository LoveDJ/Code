n = int(input().strip())
can = input().strip().split()
dic = {}
for c in can:
    dic[c] = 0
m = int(input().strip())
peo = input().strip().split()
invalid = 0
for p in peo:
    if p in can:  dic[p] += 1
    else: invalid += 1
for c in can:
    print(c + " : " + str(dic[c]))
print("Invalid : " + str(invalid))
