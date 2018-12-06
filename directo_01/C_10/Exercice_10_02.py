class Cat:
    name = ""
    age = 0
    registered = False

    def __init__(self, input_name, input_age):
        self.name = input_name
        self.age = input_age

        if input_age > 2:
           self.registered = True


c1 = Cat("Jack", 2)
c2 = Cat("Bob", 9)

print("Cat c1 is " + str(c1.registered))
print("Cat c2 is " + str(c2.registered))