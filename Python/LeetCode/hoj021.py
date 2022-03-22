x = input().strip()
while True:
    n = int(input().strip())
    if n == 0: break
    m = 0
    while n > 2:
        m += n//3
        n = n % 3 + n//3
    if n == 2 and x=="1": m += 1
    print(m)


