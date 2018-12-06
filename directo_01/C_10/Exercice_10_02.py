class Cat:
    name = ""
    age = 0
    registered = False

    def __init__(self, input_name, input_age):
        self.name = input_name
        self.age = input_age

        if input_age > 2:
           self.registered = True


    def meow(self, number_times):
        for m in range(number_times):
            print("Meow")


    def meow(self, number_time, phrase=""):
        for m in range(number_time):
            print("Meow", phrase)


c1 = Cat("Jack", 2)
c2 = Cat("Bob", 9)

print("Cat c1 is " + str(c1.registered))
print("Cat c2 is " + str(c2.registered))

c1.meow(5, "TEST")

