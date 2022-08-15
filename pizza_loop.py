from ipaddress import ip_interface


pizzas=[]
b=eval(input('Enter types number \n'))
for a in range(b) :
    note=input("Enter pizza name \n")
    pizzas.append(note)
print(pizzas)
for count in range(b):
    print(pizzas[count])