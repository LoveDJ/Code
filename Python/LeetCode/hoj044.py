# 大数相加
str01 = input().strip().lstrip('0')[::-1]
str02 = input().strip().lstrip('0')[::-1]
str01_len = len(str01)
str02_len = len(str02)
if str01_len < str02_len: str01 += '0'*(str02_len - str01_len)
else: str02 += '0'*(str01_len - str02_len)

res = ''
i = 0
up = 0
while i < len(str01):
    unit_add = int(str01[i])+int(str02[i]) + up
    if unit_add >= 10:
        up = 1
        res += str(unit_add - 10)
    else:
        up = 0
        res += str(unit_add)
    i += 1
if up == 1: res += str(up)
if res: print(res[::-1])
else: print('0')




