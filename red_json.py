import json
fname='nubmers.json'
with open(fname) as fdi:
    k=json.load(fdi)
print(k)