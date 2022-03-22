def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
while True:
    try:
        in_num = int(input().strip())
        num01 = 0
        num02 = in_num
        for i in range(1, in_num//2+1):
            if isPrime(i) and isPrime(in_num - i):
                num01 = i
                num02 = in_num - i
        print(num01)
        print(num02)
    except:
        break