def isIp(ip):
    res = "true"
    ip_arr = ip.split('.')
    if len(ip_arr) == 4:
        for i in range(4):
            ip_str = ip_arr[i]
            # 仅由数字构成
            if not ip_str.isdigit():
                res = "false"
                break
            # 开头没有0
            if len(ip_str) > 1 and ip_str[0] == "0":
                res = "false"
                break
            # 0~255
            if int(ip_str) > 255:
                res = "false"
                break
            # 0.x.x.x 为非法地址
            if int(ip_arr[0])==0 and i != 0 and int(ip_str)!=0:
                res = "false"
                break
            #1.0.0.0 为非法地址
            if i==3 and "1.0.0.0"==ip:
                res = "false"
                break
    else:
        res = "false"
    if res == "false": return False
    if res == "true": return True


def isMask(mask):
    if len(mask.split('.'))<4:
        maskArr = mask.split('.')
        maskArr.extend(['0']*(4 - len(maskArr)))
        mask = '.'.join(maskArr)
    if isIp(mask):
        maskArr = mask.split('.')
        mask = ''
        # 将掩码转为二进制字符串
        for maskStr in maskArr:
            temp = bin(int(maskStr)).lstrip('0b')
            temp = (8-len(temp))*'0' + temp
            mask += temp
        mask = int(mask, 2)
        # 判断二进制掩码是否前边全为1
        if mask|mask-1 == 0xffffffff: return True
        else: return False
    else: return False


mask = input().strip()
ip01 = input().strip()
ip02 = input().strip()
if isMask(mask) and isIp(ip01) and isIp(ip02):
    mask = list(map(int, mask.split('.')))
    ip01 = list(map(int, ip01.split('.')))
    ip02 = list(map(int, ip02.split('.')))
    for i in range(4):
        if ip01[i]&mask[i] != ip02[i]&mask[i]:
            print(2)
            break
        if i == 3:
            print(0)
else:
    print(1)
