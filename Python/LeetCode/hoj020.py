import sys
outstring = ''
dic = {'a':'2','b':'2','c':'2','d':'2','e':'3','f':'3','g':'3','h':'4','i':'4',
       'j':'4','k':'4','l':'5','m':'5','n':'5','o':'6', 'p':'6','q':'7','r':'7',
       's':'7','t':'8','u':'8','v':'8','w':'9','x':'9','y':'9','z':'9'}
for line in sys.stdin:
    res = ''
    s = line.strip()
    for ch in s:
        if ord(ch) >= ord('a') and ord(ch)<=ord('z'):
            res += dic[ch]
        elif ord(ch) >= ord('A') and ord(ch) < ord('Z'):
            res += chr(ord(ch)+33)
        elif ch == 'Z':
            res += 'a'
        else:
            res += ch
    res += '\n'
    outstring += res
print(outstring)