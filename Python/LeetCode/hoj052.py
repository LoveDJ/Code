n = int(input().strip())
num_arr = [int(x) for x in  input().strip().split()]
sort_type = False if input().strip() == "0" else True
res_str = ""
for num in sorted(num_arr, reverse=sort_type): res_str += str(num)+" "
print(res_str.strip())
