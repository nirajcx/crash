def greeting(user):
    '''Printing hello user'''
    print('Hello '+ user.title())
greeting('Niraj')
def animal(type='horse',pet_name='ajuba'):
    '''Pet name and type'''
    print('My pet is '+ type.title() + '\n')
    print('My pet name is '+ pet_name.title()+ '\n')
animal('Dog','Pitbull')
animal(type='cat',pet_name='persian')
animal('mouse','chiller')