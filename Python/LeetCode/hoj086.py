while True:
    try:
        password = str(input().strip().replace(' ',''))
        score = 0
        if len(password)<=4:
            score=score+5
        elif 5<=len(password)<=7:
            score = score+10
        else:
            score = score+25
        upper_list =[]
        lower_list =[]
        digit_list =[]
        symbol_list=[]
        for item in password:
            if item.isupper():
                upper_list.append(item)
            elif item.islower():
                lower_list.append(item)
            elif item.isdigit():
                digit_list.append(item)
            else:
                symbol_list.append(item)
        if (len(upper_list)>0 and len(lower_list)==0) or (len(upper_list)==0 and len(lower_list)>0):
            score+=10
        if (len(upper_list)>0 and len(lower_list)>0):
            score+=20
        if (len(digit_list)==1):
            score+=10
        if len(digit_list)>1:
            score+=20
        if len(symbol_list)==1:
            score+=10
        if len(symbol_list)>1:
            score+=25
        if (len(upper_list)>0 and len(digit_list)>0) or (len(lower_list)>0 and len(digit_list)>0):
            score+=2
            if len(symbol_list)>0:
                score+=1
                if len(upper_list)>0 and len(lower_list)>0:
                    score+=2
        if score>=90:
            print('VERY_SECURE')
        elif score>=80:
            print('SECURE')
        elif score >=70:
            print("VERY_STRONG")
        elif score >=60:
            print('STRONG')
        elif score >=50:
            print('AVERAGE')
        elif score>=25:
            print('WEAK')
        else:
            print('VERY_WEAK')
    except:
        break