a=input('Enter a\n')
b=input('Enter b\n')
try:
    num_a=int(a)
    num_b=int(b)
except ValueError:
    print('Enter the integer only')
else:
    print(num_a + num_b)