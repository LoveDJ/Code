while True:
    try:
        n  = int(input().strip())
        s = ''
        for i in range(n):
            s += 'ABCD'
        print(s)
    except:
        break
