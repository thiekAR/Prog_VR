a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
b = 0

for a in a_list:

    print(str(b + 1) + ":", end=" ")
    print(a)
    if a % 3 == 0:
        print("Fizz", end="")
        print(a % 3 == 0)
    if a % 5 == 0:
        print("Buzz")
        print(a % 5 == 0)
    else:
        print("")
    b = b + 1



