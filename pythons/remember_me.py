import json
fname='username.json'
name=input('Enter the name')
with open(fname,'w') as fdi:
    json.dump(name,fdi)
    print('Name is stored')