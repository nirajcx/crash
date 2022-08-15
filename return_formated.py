def withmidname(fname, lastname, midname=''):
    if midname:
        correct = fname + ' ' + midname + ' ' + lastname
    else:
        correct = fname + " "+lastname
    return correct.title()

sed = withmidname('niraj','singh')
print(sed)
sed = withmidname('niraj', 'singh','kumar')
print(sed)

def build_person(fname,lname):
    di={'first':fname,'last':lname}
    return di
a=build_person('niraj','kumar')
print(a)
