n01 = int(input().strip())
arr01 = input().strip().split()
n02 = int(input().strip())
arr02 = input().strip().split()
arr = []
for ch in arr01:
    num = int(ch)
    if num not in arr: arr.append(num)
for ch in arr02:
    num = int(ch)
    if num not in arr: arr.append(num)
arr = sorted(arr)
res = ""
for number in arr:
    res += str(number)
print(res)