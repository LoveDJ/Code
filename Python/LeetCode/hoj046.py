in_str = input().strip()
if len(in_str) > 0:
    in_arr = in_str.split()
    people_num = int(in_arr[0])
    sort_type = True if in_arr[1]=="0" else False
    score_dic = {}
    for i in range(people_num):
        score_dic[in_arr[i*2+2]] = int(in_arr[i*2+3])
    score_arr = sorted(score_dic.items(), key = lambda kv:(kv[1], kv[0]), reverse=sort_type)

    for item in score_arr: print(item[0]+" "+str(item[1]))