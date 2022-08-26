paths = 'pi_digi.txt'
with open(paths) as fdi:
    lis = fdi.readlines()


pi_string = ''
for line in lis:
    pi_string += line.rstrip()
print(pi_string[:52] + "...")
print(len(pi_string))
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print('yes')
else:
    print(no)
