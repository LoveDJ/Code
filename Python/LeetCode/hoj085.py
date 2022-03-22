n = int(input().strip())
nega_num = 0
posi_num = 0
posi_sum = 0
for i in range(n):
    num = int(input().strip())
    if num < 0: nega_num+=1
    elif num > 0:
        posi_num += 1
        posi_sum += num

print('%d %.1f'%(nega_num, posi_sum/posi_num))
