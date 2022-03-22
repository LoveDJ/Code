s = input().strip().replace(' ','')
res = ""
a = ""
n = 0
for i, ch in enumerate(s):
    if ch.isdigit():
        a += ch
        n += 1
        if n > len(res):
            res = a
    else:
        a = ""
        n = 0
if res != "":
    print(res+","+str(len(res)))