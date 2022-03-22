import sys
outstring=''
for line in sys.stdin:
    s = line.strip()
    dic = {}
    min_num = len(s)
    for ch in s:
        if ch in dic.keys():dic[ch] += 1
        else:dic[ch] = 1
    for v in dic.values():
        if v < min_num:
            min_num = v
    res = ""
    for ch in s:
        if dic[ch] != min_num:
            res += ch
    res+='\n'
    outstring += res
print(outstring)
