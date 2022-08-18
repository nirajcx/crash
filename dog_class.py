class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is sitting")

    def roll(self):
        print(self.name.title() + " is roling")

    def age(self):
        print(self.name.title() + "age is" + str(self.age))
tommy=Dog('tommy',5)
rover=Dog('rover',10)
print("My dog's name is " + tommy.name.title() + ".")
print("My dog's age is " + str(tommy.age) + ".")
rover.sit()
rover.roll()