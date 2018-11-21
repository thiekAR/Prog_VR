a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]


for a in range(len(a_list)):

    print(str(a) + ":", end=" ")

    if a % 3 == 0:
        print("Fizz", end="")


    if a % 5 == 0:
        print("Buzz")

    else:
       print("")




