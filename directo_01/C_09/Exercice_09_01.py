# Ex. 8.5


def city_country(name_of_city, its_country):
    # print('{0}, {1}'.format(name_of_city.title(), its_country.title()))
    print(name_of_city + ', ' + its_country)


print(city_country('Boston', 'USA'))
print(city_country('Montréal', 'Canada'))
print(city_country('Mexico', 'Mexique'))

# Ex. 8.6


def city_country(name_of_city, its_country):
    # return '{0}, {1}'.format(name_of_city.title(), its_country.title())
    return str(name_of_city) + ', ' + str(its_country)


print(city_country('Boston', 'USA'))
print(city_country('Montréal', 'Canada'))
print(city_country('Mexico', 'Mexique'))

# Ex. 8.9

list_magicians = ['bob', 'robert', 'georges', 'pipi', 'caca']


def show_magicians(list_magicians):
    for magician in list_magicians:
        print(str(magician))


show_magicians(list_magicians)


# something new in python. *PLUS_NEW_NAME_OF_LIST in parameters
# of the fct name it despite it miss [] in the parameters of input


def create_order(customer, *skus):
    print('The customer name is : ' + str(customer))

    for sku in skus:
        print(str(sku))

create_order('bob', "customer1", 1234, 43547, 65)







