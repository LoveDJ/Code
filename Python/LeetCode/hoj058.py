num_arr = input().strip().split('.')
is_ip = 'YES'
if len(num_arr) == 4:
    for i in range(4):
        try:
            num = int(num_arr[i])
            if (num >= 0) and (num <= 255):
                continue
            else:
                is_ip = 'NO'
                break
        except:
            is_ip = 'NO'
            break

else: is_ip = 'NO'
print(is_ip)
