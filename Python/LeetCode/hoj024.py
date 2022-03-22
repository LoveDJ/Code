import sys
outstring=''
for line in sys.stdin:
    s = line
    #分开字母和数字
    alph = ""
    for ch in s:
        if ch.isalpha(): alph += ch

    low_alph = alph.lower()
    low_alph = sorted(low_alph)
    res = [""]*len(alph)
    #将排序后的小写字母还原
    j = 0
    for i,ch in enumerate(low_alph):
        if i != 0 and low_alph[i] != low_alph[i-1]:
            j = 0
        while j < len(alph):
            if ch == alph[j].lower():
                res[i] = alph[j]
                j += 1
                break
            else: j += 1
    for i,ch in enumerate(s):
        if not ch.isalpha():
            res.insert(i, ch)
    outstring+=''.join(res)
print(outstring)
