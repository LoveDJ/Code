all_money,num=map(int,input().split())
price_arr=[[0 for i in range(4)] for j in range(num+1)]
value_arr=[[0 for i in range(4)] for j in range(num+1)]
all_money = all_money

# 初始化每组中所有的组合
for i in range(1, num+1):
    price,degree,id = map(int,input().split())
    price = price
    if id == 0:
        for j in range(4):
            price_arr[i][j] += price
            value_arr[i][j] += price*degree
    elif price_arr[id][0] == price_arr[id][1]:
        price_arr[id][1] += price
        price_arr[id][3] += price
        value_arr[id][1] += price*degree
        value_arr[id][3] += price*degree
    else:
        price_arr[id][2] += price
        price_arr[id][3] += price
        value_arr[id][2] += price*degree
        value_arr[id][3] += price*degree

dp = [0]*(all_money+1)
for i in range(1, num+1):
    for j in range(all_money, -1, -1):
        for v in range(4):
            if j >= price_arr[i][v]:
                dp[j] = max(dp[j], dp[j-price_arr[i][v]] + value_arr[i][v])
print(dp[all_money])