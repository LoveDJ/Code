input_str = input().strip()
str_arr = []
para = ""
flag = 0
for ch in input_str:
    if ch == " " and flag == 0:
        str_arr.append(para)
        para = ""
    elif (ch == "\"" or ch == "“") and flag == 0:
        flag = 1
    elif (ch == "\"" or ch == "”") and flag == 1:
        flag = 0
    else:
        para += ch
str_arr.append(para)
print(len(str_arr))
for ch in str_arr: print(ch)

