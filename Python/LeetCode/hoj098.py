n = int(input().strip())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().strip().split())))
expStr = input().strip()
stack = []
calCount = 0
for str in expStr:
    if str == '(': continue
    elif str == ')':
        matrix02 = stack.pop()
        matrix01 = stack.pop()
        calCount += matrix01[0]*matrix01[1]*matrix02[1]
        newMatrix = [matrix01[0], matrix02[1]]
        stack.append(newMatrix)
    else:
        stack.append(matrix[ord(str)-ord('A')])
print(calCount)
