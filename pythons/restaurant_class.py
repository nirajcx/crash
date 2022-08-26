from unicodedata import name


class Restaurant():
    def __init__(self,name,cuisine):
        self.name=name
        self.cuisine=cuisine
    
    def describe_restaurant(self):
        print('Name= ',self.name,'type= ',self.cuisine)

    def open_restaurant(self):
        print(self.name,"is open")
shree=Restaurant('shree','soft')
shree.describe_restaurant()
shree.open_restaurant()