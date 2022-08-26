
def doi(a):
    #a = int(input('Enter the integer for factorial \n'))
    b = 1
    if a < 0:
        print('There is no factorial for negative numbers \n')
    elif a == 0:
        print('Factorial for 0 is 1 \n')
    else:
        for i in range(1, a+1):
            b = b*i
    print(b)

doi(int(input()))