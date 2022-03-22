def trainOut(waitList, inList, outList, resList):
    if not waitList and not inList:
        resList.append(outList)
    if inList:
        trainOut(waitList[:], inList[:-1], outList+[inList[-1]], resList)
    if waitList:
        trainOut(waitList[1:], inList+[waitList[0]], outList[:], resList)
n = int(input().strip())
waitList = input().strip().split()
inList = []
outList = []
resList = []
trainOut(waitList, inList, outList, resList)
for line in resList:
    print(*line)
