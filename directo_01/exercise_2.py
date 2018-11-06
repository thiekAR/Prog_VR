# exercise with input FCT
#7-1. Rental Car: Write a program that asks the user what
#kind of rental car they would like. Print a message about
#that car, such as “Let me see if I can find you a Subaru.”'



#x = input("what is your favorite car ?")
#print("Let me see if I can find you a" + x)

#x = input("\n" + "what is your favorite car ? ")
#print("Let me see if I can find you a  {}".format(x))

#y = input("\n" + "Enter a number : ")
#z = input("\n" + "Enter another number : ")
#w = int(y)/int(z) #Possibility to divise by 0



y = int(input("\n" + "Enter a number : "))
z = int(input("\n" + "Enter another number : "))

try:
   result_1 = (int(y) / int(z))  # Possibility to divide by 0

except ZeroDivisionError:
    print("You can't divide by zero!")

except Exception:
    print("A unknow error has occured")

except ValueError:
    print("Please only use values between 0 - 9")

else:
    print(result_1)

