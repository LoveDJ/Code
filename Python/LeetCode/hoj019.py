import re
s = input().strip()
s = re.sub(r'[^a-zA-Z]', ' ', s)
s_arr = s.split()
print(' '.join(s_arr[::-1]))
