while True:
    try:
        n = int(input().strip())
        tmp_begin = 1
        for i in range(1, n+1):
            begin = tmp_begin
            if i == n:
                print(begin)
            else:
                print(begin, end=" ")
            for j in range(i+1, n+1):
                begin += j
                if j == n:
                    print(begin)
                else:
                    print(begin, end=" ")
            tmp_begin += i
    except:
        break
