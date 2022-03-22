num = int(input().strip())
num_mid = num ** 2
res = ""
if num%2 != 0:
    res = str(num_mid)
    for i in range((num-1)//2):
        res = str(num_mid-(i+1)*2)+"+"+res+"+"+str(num_mid+(i+1)*2)
elif num%2 == 0:
    for i in range(num//2):
        if i==0: res = str(num_mid-1-i*2)+"+"+str(num_mid+1+i*2)
        else:res = str(num_mid-1-i*2)+"+"+res+"+"+str(num_mid+1+i*2)
print(res)