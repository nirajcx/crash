a = int(input('Enter the starting range'))
b = int(input('Enter the end range'))
prime = []

for i in range(a, b+1):
    flag = True
    for c in range(2, i):
        if (i % c) == 0:
            flag = False
            break
    if flag:
        prime.append(i)
print(prime)


