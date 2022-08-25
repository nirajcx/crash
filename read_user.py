import json
fname = 'username.json'
try:
    with open(fname) as fdi:
        k = json.load(fdi)
except FileNotFoundError:
    print("File not found but now remembered")
    user = input('Enter the username')
    with open(fname) as fdi:
        json.dump(user, fdi)
else:
    print(k.title() + ' Welcome Back!')
