def arbi(*ins):
    for a in ins:
        print('adding the ' + str(a))


print("enter the args")
arbi('apple', 'grapes', 'banana', 'berries')


def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
print("==========================\n")


def build_profile(fname, lname, **user_info):
    profile = {}
    profile['fname'] = fname
    profile['lname'] = lname
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')
print(user_profile)
