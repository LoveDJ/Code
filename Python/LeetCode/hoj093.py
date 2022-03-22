n = int(input().strip())
head = input().strip()
list = [head]
#insert
for i in range(n-1):
    newNode, curNode = input().strip().split()
    if newNode in list:
        continue
    for j, node in enumerate(list):
        if curNode == node:
            list.insert(j+1, newNode)
            break
#delete
delNode = input().strip()
for node in list:
    if node == delNode:
        list.remove(node)
#print
if list:
    print(' '.join(list))
else:
    print('null')

