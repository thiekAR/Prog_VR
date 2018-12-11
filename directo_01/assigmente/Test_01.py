# Question 1 - Guess the number

import random

attempt_number = 0

random_number = random.randint(1, 100)

while attempt_number <= 5:
    guessed_number = int(input("Please guess a number between 1 and 100 (attempt {0}): ".format(attempt_number + 1)))

    if attempt_number == 5:
        print("Sorry, you didnt guess the correct number. The correct number was {0}".format(random_number))
        break

    if guessed_number > random_number:
        print("Wrong guess, you guessed too high.")
    elif guessed_number < random_number:
        print("Wrong guess, you guessed too low.")
    else:
        print("Correct! You win")
        break

    attempt_number += 1


# Question 2 - Lists

list = []
compt = 1

while True:
    element_to_add_list = str(input("Please enter an element to add to the list [fin = finished]: "))
    list.append(element_to_add_list)

    if element_to_add_list == "fin":
        print("Te list contains {0} elements, here they are ; ".format(len(list)))
        for ele in list:
            print(str(compt) + ": " + str(ele))
            compt += 1
        break


# Question 3 - Classes and object


class BankAccount:
    balance = 0


    def __init__(self, value_of_balance=0):
        self.balance = value_of_balance


    def deposit(self, add_value):
        self.balance += add_value


    def withdraw(self, subst_value):
        self.balance -= subst_value


b = BankAccount(10)
b.deposit(25)
b.withdraw(1)
print("The balance of the bank account is now " + str(b.balance))


