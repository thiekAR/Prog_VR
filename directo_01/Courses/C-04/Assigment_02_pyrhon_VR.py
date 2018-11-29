# find the length. max. min, sum, and
# average of a list of 10 random numbers

import random

# Create an empty list
alist = []


alist.append.random.randint(1, 10)
for y in alist:
    print(alist)
    for z in range(len(alist)):
        z -= 1
    if y == alist[z]:
        alist.remove(y)




print(alist)

mini = alist[0]
maxi = alist[0]
total = 0
length = 0
average = 0

for a in alist:

    # MIN FCT
    if a < mini:
        mini = a

    # MAX FCT
    if a > maxi:
        maxi = a

    # SUM FCT
    total += a

    # COUNT FCT
    length += 1

    # AVERAGE FCT
    average = total / length

print("MIN is : ", mini)
print("MAX is : ", maxi)
print("SUM is : ", total)
print("LENGTH is : ", length)
print("AVERAGE is : ", average)

students = [[88, 99, 100], [99, 90, 90], [12, 13, 14]]

print(students[0][1])

print(max(students[1]))

print(sum(students[2])/len(students[2]))

students2 = [[[40, 50], [55, 30]], [[30, 40], [22, 10]]]

# what
print(students2[0][0][0])

students3 = [[88, 95, 45], [45, 67, 89], [12, 56, 90], [19, 50, 49]]

for h in students3[3]:
    print(h)

