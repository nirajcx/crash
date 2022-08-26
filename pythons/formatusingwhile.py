def formating(fname,lname):
    name=fname +' ' + lname
    return name.title()
'''while True:
    print('\nTell me your name:')
    fname=input('\nEnter your first name: ')
    if fname=='q':
        break
    lname=input('\n Enter your lastt name: ')
    if lname=='q':
        break
    print(formating(fname,lname))
    break'''
def cal_list(name):
    for i in name:
        print('Hello'+ ' ' + str(i) + '!')
namess=['green','hell','hulk',"spider"]
cal_list(namess)