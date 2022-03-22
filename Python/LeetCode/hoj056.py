in_str = input()
num = 0
for ch in in_str:
    if (ord(ch) >= 65) and (ord(ch) <= 90):
        num += 1
print(num)