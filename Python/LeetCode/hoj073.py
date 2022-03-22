n = int(input().strip())
dic = []
for i in range(n):
    a = input().strip()
    dic.append(a)
s = input().strip()
s2 = ''.join(sorted(s))
idx = int(input().strip())

dic_bro = []
num = 0
for ch in dic:
    if ch != s: #排除自身
        ch2 = ''.join(sorted(ch))
        if ch2 == s2: #两个单词排序后相等 则为兄弟单词
            num += 1
            dic_bro.append(ch)
dic_bro = sorted(dic_bro)
print(num)
if num != 0: print(dic_bro[idx-1])
