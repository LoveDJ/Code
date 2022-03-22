negative_n = 0
positive_sum = 0
for i in range(7):
    num = float(input().strip())
    if num < 0: negative_n += 1
    else: positive_sum += num
print(negative_n)
positive_avg = positive_sum/(7-negative_n)
if positive_avg == 0: print(0)
else: print('%.4f'%(positive_avg))

