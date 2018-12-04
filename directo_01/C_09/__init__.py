# def calculate_tax(amount):
#     amount_with_tax = amount * 1.1556
#     return amount_with_tax
#
# value = 101
# print('The value is ' + str(value))
# value_with_tax = calculate_tax(value)
# print('The value with tax is ' + str(value_with_tax))
# value = input('Please enter a value to print out :')
#
# value_plus_tax = int(value) * 1.1556
# print('The value with tax is ' + str(value_plus_tax))

# debugging exercise 1

patients = [[70, 1.8], [80, 1.9], [150, 1.7]]


def calculate_bmi(weight, height):
    return weight / (height ** 2)


for patient in patients:
    weight, height = patient
    bmi = calculate_bmi(weight, height)
    print("Patients BMI is: %f" % bmi)

# bmi = calculate_bmi( height = height, weight = weight)