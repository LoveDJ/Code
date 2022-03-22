while True:
    try:
        a, b = map(int, input().split("/"))
        if a >0 and b>0 and b>a:
            output = ""
            while a-1:
                if not b%(a-1):
                    output += "1/{}+".format(b//(a-1))
                    a = 1
                else:
                    c = b//a+1
                    output += "1/{}+".format(c)
                    a, b = a-b%a, b*(c)
                    if not b%a:
                        a, b = 1, b//a
            output += "1/{}".format(b)
            print(output)
        else:
            print('error')
    except:
        break