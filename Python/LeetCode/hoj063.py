n = int(input().strip())
for i in range(n):
    s = input().replace(' ','')
    while s != "":
        if len(s) <= 8:
            print(s+"0"*(8-len(s)))
            s = ""
        else:
            print(s[0:8])
            s = s[8:]