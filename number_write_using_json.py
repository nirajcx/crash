import json
valu = [1, 2, 3, 66, 7, 8, 9, 44, 33, 22, 65, 77]
fname = 'nubmers.json'
with open(fname,'w') as fdi:
    json.dump(valu,fdi)
