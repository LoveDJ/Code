in_str = input()
ch_dic = {' ': 0}
for i in range(10):
    ch_dic[str(i)] = 0
for ch in range(ord('A'), ord('Z')+1):
    ch_dic[chr(ch)] = 0
for ch in range(ord('a'), ord('z')+1):
    ch_dic[chr(ch)] = 0
ch_keys = list(ch_dic.keys())
for ch in in_str:
    if ch in ch_keys: ch_dic[ch] += 1
ch_val = list(ch_dic.values())
idx_arr = sorted(enumerate(ch_val), key=lambda x:x[1], reverse=True)
res = ""
for idx in idx_arr:
    if ch_val[idx[0]] == 0 : break
    res += ch_keys[idx[0]]
print(res)