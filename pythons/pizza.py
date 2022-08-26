def making_pizza(size,*toppings):
    print('making pizza of size '+str(size)+' inches'+' with following toppings')
    for i in toppings:
        print(i)
making_pizza(4,"chilli","butter","smooth")
