while True:
    try:
        money = input().strip()
        CnUnit = ['壹','贰','叁','肆','伍','陆','柒','捌','玖', '拾']
        integralUnit = ['元', '拾', '佰', '仟', '万', '拾', '佰', '仟', '亿', '拾', '佰', '仟']
        integerPart = money
        if money.find('.') != -1:
            integerPart = money[:-3]
        zero = 0
        a_output = "人民币"
        if integerPart != '0':
            for i in range(len(integerPart)):
                if zero > 0 and int(integerPart[i]) != 0:#当前面有一个或多个数字为0，且当前数字不
                #为0时，输出“零”，并且重置zero
                    a_output += '零'
                    zero = 0
                if int(integerPart[i]) >= 1:
                    res = CnUnit[int(integerPart[i])-1]+integralUnit[len(integerPart)-i-1]
                    res = res.replace('壹拾', '拾') #如果是“壹拾”，则按照要求替换为“拾”
                    a_output += res
                else: #如果当前数字是0的话，zero加1
                    zero += 1
                length = len(integerPart)-i-1
                #下面的第一个条件是为了区分上面的if条件，非零时已做处理，下面是处理当前数字为0的情况
                #比如输入数字105000.00，下面这个判断语句就是输出“万”字
                if int(integerPart[i]) == 0 and length != 0 and length % 4 == 0:
                    a_output += integralUnit[len(integerPart)-i-1]
            if money[-4] == '0':
                a_output += '元'
        #小数部分
        if money.find('.') != -1:
            if money[-2:] == '00':
                a_output += '整'
            elif money[-2] == '0':
                a_output += CnUnit[int(money[-1])-1] + '分'
            elif money[-1] == '0':
                a_output += CnUnit[int(money[-2])-1] + '角'
            else:
                a_output += CnUnit[int(money[-2])-1] + '角'+ CnUnit[int(money[-1])-1] + '分'
        else:
            a_output += '整'
        print(a_output)
    except:
        break
