
import random
alist = []

alist.append(random.randint(1, 101))


for a in range(len(alist)):

    print(a)

# MIN FCT
    min = alist[0]
    for b in alist:
        if b < min:
          min = b
    print("MIN is : ", min)

# MAX FCT
    max = alist[0]
    for c in alist:
        if c > max:
            c = max
    print("MAX is : ", max)

# SUM FCT
    total = 0
    for d in alist:
            total += d
    print("SUM is : ", total)

# AVERAGE FCT
    average = total/len(alist)
    print("AVERAGE is : ", average)

# COUNT FCT
    length = 0
    for e in alist:
        length += 1
    print("COUNT is : ", length)

