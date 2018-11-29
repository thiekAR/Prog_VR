
my_list = [11, 22, 33, 44]

for item in my_list:
    print(item)

squares = [value**2 for value in range(1, 11)]
print(squares)

for a in range(0, 101, 5):
    print(a)

my_list_2 = [val*11 for val in range(1, 5)]
print(my_list_2)

val = 0
list = [val+11 for val in range(val, 5)]
print(list)

my_list_3 = [val**n for n in range(1, 5)]
print(my_list_3)

mylist2 = [mylist, 'abc', mylist, [1, 2, 3]]
item1 = mylist[3][4]
item2 = mylist[0][4]

