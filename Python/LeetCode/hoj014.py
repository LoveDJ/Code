n = int(input().strip())
a = []
for i in range(n):
    a.append(input().strip())
a.sort()
for s in a:
    print(s)