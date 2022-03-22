for x in range(15):
    if (100-7*x) % 4 == 0:
        y = (100-7*x)/4
        z = 100 - x - y
        print("%d %d %d"% (x, y, z))