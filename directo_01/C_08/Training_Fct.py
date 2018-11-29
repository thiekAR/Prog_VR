def evaluation_of_number(num, denum):
    if num % denum == 0:
        return True
    return False

for num in range(0, 12):
    print(str(num) + ": ", end="")

    if evaluation_of_number(num, 3):
       print("Fizz", end="")

    if  evaluation_of_number(num, 5):
       print("Buzz", end="")

    print("")