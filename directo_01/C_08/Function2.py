import this
print(this)


def print_separator(width):
    for w in range(width):
        print("*", end="")


def print_separator_2(width):
        print("*" * width)


print("This is line 1")

print_separator(50)

print("\n")

print_separator_2(50)
