dic = {'reset':'reset what', 'reset board':'board fault', 'board add':'where to add',
       'board delet':'no board at all', 'reboot backplane':'impossible', 'backplane abort':'install first'}
while True:
    try:
        cmd = input().strip().split()
        temCmd = ''
        res = 'unkonw command'
        if len(cmd) == 1:
            for item in dic.keys():
                if item.startswith(cmd[0]) and len(item.split()) == 1:
                    res = dic[item]
        elif len(cmd) == 2:
            count = 0
            for item in dic.keys():
                items = item.split()
                if len(items) > 1:
                    if items[0].startswith(cmd[0]) and items[1].startswith(cmd[1]):
                        count += 1
                        res = dic[item]
            if count > 1: res = 'unkonw command'
        print(res)
    except:
        break


