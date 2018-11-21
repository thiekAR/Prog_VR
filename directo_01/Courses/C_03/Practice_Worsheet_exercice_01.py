import decimal
# exercice Practice worksheet 7 questions

# Question 1
age = 20
age2 = age
print(str(age + age2))

# Question 2
name = "champlain"
print("I am taking this course at " + name)

# Question 3
Sale1 = "1.40"
Sale2 = "2.30"
sale1 = decimal.Decimal(Sale1)
sale2 = decimal.Decimal(Sale2)
result = float(sale1 + sale2)
result1 = result % 0.10
if result1 > 0.05:
    result2 = (result - result1) + 0.10
else:
    result2 = (result - result1)
print("The total sale price is $" + str(result2))

# Question 4
total = 34.00
increase_rate = 15.56
v1 = ((total * increase_rate)/100) + total
print("The total amount increased by the percentage rate is : " + str(v1))

# Question 5
var1 = "hello"
var2 = "you"
print("The length of both of the variables var1 and var2 is : " + str(len(var1) + len(var2)))

# Question 6
for a in range(1, 11):
    print(a * a)


# Question 7
A = "0"
B = "1"
n1 = ""

#for c in range(8):

    #for d in range(3):


message = ""
while message != "quit":
    message = input("Enter your command : ")
    print(message)


while True:
    message1 = input("enter command : ")
    if message == "quit":
        break
print(message1)
