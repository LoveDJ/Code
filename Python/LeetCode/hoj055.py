in_str01 = input().strip()
in_str02 = input().strip()
str02_set = set()
for ch in in_str02:
    str02_set.add(ch)
flag = 'true'
for ch in in_str01:
    if ch not in str02_set:
        flag = 'false'
        break
print(flag)
