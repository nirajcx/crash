a = 1 #int(input('Enter the starting range'))
b = 99 #int(input('Enter the end range'))
prime = []

for i in range(a, b+1):
    for c in range(2, i):
        if (i % c) == 0:
            break
        
    else:
            print(i)
