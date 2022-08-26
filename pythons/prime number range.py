a=int(input(' enter starting number'))
b=int(input(' enter ending number'))
for x in range(a,b+1):
    flag=True
    for i in range(2,x):
        if (x%i==0):
            flag=False
            break
    if flag:
        print(x)