ip = input().strip()
res = "true"
ip_arr = ip.split('.')
if len(ip_arr) == 4:
    for i in range(4):
        ip_str = ip_arr[i]
        #仅由数字构成
        if not ip_str.isdigit():
            res = "false"
            break
        #开头没有0
        if len(ip_str) > 1 and ip_str[0]=="0":
            res = "false"
            break
        #0~255
        if int(ip_str)>255:
            res = "false"
            break
        # # 0.x.x.x 为非法地址
        # if int(ip_arr[0])==0 and i != 0 and int(ip_str)!=0:
        #     res = "false"
        #     break
        # #1.0.0.0 为非法地址
        # if i==3 and "1.0.0.0"==ip:
        #     res = "false"
        #     break
else: res = "false"
print(res)
