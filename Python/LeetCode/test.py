while True:
    try:
        s = input().replace('{', '(').replace('}', ')').replace('[', '(').replace(']', ')')
        res = eval(s)
        print(int(res) if res == int(res) else res)
    except:
        break