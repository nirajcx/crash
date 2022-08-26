from name_function import formattedname as tt
print("Enter 'q' at any time to quit.")
while True:
    a = input('Enter the first name \n')
    if a == 'q':
        break
    b = input('Enter the last name \n')
    if b == 'q':
        break
    c = tt(a, b)
    print(c)
