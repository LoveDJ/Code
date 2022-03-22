n = int(input().strip())
x = []
for i in range(n):
    idx, val = map(int, input().strip().split())
    #去重
    is_same = False
    for item in x:
        if item[0] == idx and item[1] == val:
            is_same = True
    if not is_same: x.append((idx, val))

#合并
dic = {}
for item in x:
    if item[0] not in dic.keys():
        dic[item[0]] = item[1]
    else:
        dic[item[0]] += item[1]

#排序
res_arr = sorted(dic.items(), key= lambda kv:(kv[0], kv[1]))
#打印
for item in res_arr:
    print(str(item[0])+" "+str(item[1]))