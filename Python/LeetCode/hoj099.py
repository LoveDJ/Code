while True:
    try:
        n = int(input().strip())
        index = 0
        start = 0
        control = input().strip()
        l = [i for i in range(1,n+1)]
        for x in control:
            if x == 'U':
                if index == 0:
                    index += -1+n
                    start = n-4
                else:
                    index += -1
                    if index < start:
                        start = index
            if x == 'D':
                if index == n-1:
                    index = 0
                    start = 0
                else:
                    index += 1
                    if index > start+3:
                        start += 1
        if n <= 4 :
            print(*l)
        else:
            print(*l[start:start+4])
        print(l[index])
    except:
        break