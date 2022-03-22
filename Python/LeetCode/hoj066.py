num = float(input().strip())
x = 2.0
for i in range(12):
    x = (num/(x**2)+2*x)/3
print('%.1f'%x)
