pokerA, pokerB = input().strip().split('-')
pokerA_list = pokerA.split()
pokerB_list = pokerB.split()
pokerSEQ = '3 4 5 6 7 8 9 10 J Q K A 2  joker JOKER'.split()
if len(pokerA_list) == len(pokerB_list):
    if pokerSEQ.index(pokerA_list[0]) > pokerSEQ.index(pokerB_list[0]):
        print(pokerA)
    else:
        print(pokerB)
elif pokerA == 'joker JOKER': print(pokerA)
elif pokerB == 'joker JOKER': print(pokerB)
elif len(pokerA_list) == 4: print(pokerA)
elif len(pokerB_list) == 4: print(pokerB)
else: print('ERROR')