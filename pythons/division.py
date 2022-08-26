print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    a=input('Enter the first number\n')
    if a=='q':
        break
    b=input('Enter the second number \n')
    if b=='q':
        break
    try:
        print(int(a)/int(b))
    except ZeroDivisionError:
        print('Not divisible by zero')
   # else:
      #  print(c)