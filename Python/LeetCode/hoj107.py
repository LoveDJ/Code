import itertools


def calc_24points(data):
    map2 = {'J': '11', 'Q': '12', 'K': '13', 'A': '1'}
    new_data = []
    for d in data:
        if d in map2:
            new_data.append(map2[d])
        else:
            new_data.append(d)

    map1 = {'0': '+', '1': '-', '2': '*', '3': '/'}
    for o in (''.join(x) for x in itertools.product(map(str, range(4)), repeat=3)):
        for i in itertools.permutations(range(4), 4):
            temp1 = '((' + new_data[i[0]] + map1[o[0]] + new_data[i[1]] + ')' + map1[o[1]] + new_data[i[2]] + ')' + \
                    map1[o[2]] + new_data[i[3]]
            temp2 = data[i[0]] + map1[o[0]] + data[i[1]] + map1[o[1]] + data[i[2]] + map1[o[2]] + data[i[3]]
            if eval(temp1) == 24:
                print(temp2)
                return
    print('NONE')


data = input().strip()
if data.find('joker') != -1 or data.find('JOKER') != -1:
    print('ERROR')
else:
    data = list(map(str, data.split()))
    calc_24points(data)