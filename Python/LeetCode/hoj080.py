def put(a,b):
    if a == 0 or b == 1:
        return 1
    elif b > a:
        return put(a, a)
    else:
        return put(a, b-1) + put(a-b, b)

while True:
    try:
        a, b = map(int, input().strip().split())
        print(put(a,b))
    except:
        break