records = []
while True:
    try:
        path, line = list(input().strip().split())
        isSame = False
        for rec in records:
            if path == rec[0] and line == rec[1]:
                rec[2] += 1
                isSame = True
                break
        if not isSame: records.append([path, line, 1])
    except:
        break
for rec in records:
    print(rec[0].split('\\')[-1][-16:]+' '+str(rec[1])+' '+str(rec[2]))