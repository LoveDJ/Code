while True:
    try:
        s = bin(int(input().strip())).lstrip('0b')
        print(s)
        maxN = 0
        tempN = 0
        for ch in s:
            if ch != '0':
                tempN += 1
            else:
                if tempN > maxN: maxN = tempN
                tempN = 0
        if tempN > maxN: maxN = tempN
        print(maxN)
    except:
        break

