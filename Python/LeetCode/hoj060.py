n = int(input().strip())
count = 0
for num in range(n+1):
    num_2 = str(num**2)
    if num_2.endswith(str(num)): count += 1
print(count)