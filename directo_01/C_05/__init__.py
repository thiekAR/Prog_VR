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
