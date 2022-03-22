def match(reg, i, str, j):
    if i == len(reg) and j == len(str): return True
    if i == len(reg) or j == len(str): return False
    if reg[i] == '?': return match(reg, i+1, str, j+1)
    elif reg[i] == '*': return match(reg, i+1, str, j) or match(reg, i+1, str, j+1) or match(reg, i, str, j+1)
    elif reg[i] == str[j]: return match(reg, i+1, str, j+1)
    else: return False

while True:
    try:
        reg = input().strip()
        str = input().strip()
        if match(reg, 0, str, 0): print('true')
        else: print('false')
    except:
        break
