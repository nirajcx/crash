num = int(input('Enter the integer.\n'))
flage = False
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flage = True
            break
if flage:
    print(num, 'is Not prime')
else:
    print(num, "is prime number")
