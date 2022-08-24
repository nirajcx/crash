from tkinter import W


with open('programming.txt', 'a') as file_name:
    while True:
        a = input('Enter the name or press q to exit:- ')
        if a == 'q':
            break
        a=a.title()
        file_name.write(a)
        file_name.write('\n')
