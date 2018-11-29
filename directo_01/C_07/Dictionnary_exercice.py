province_list = {'QC': "Quebec", 'ON': 'Ontario'}
prov = input("Enter the province code : ")

if prov.upper() not in province_list:
    print("sorry")
else:
    result = province_list[prov.upper()]
print("province is {0}".format(result))


try:

    if prov.upper() not in province_list:
        print("sorry")
    else: result = province_list[prov.upper()]

except:

    print("province is {0}".format(result))

countries = {'us': 'USA',
'fr': 'France',
'uk': 'United Kingdom'}
for k in countries.items():
    print(k[1])

for k, v in countries.items():
    print(k, v)

for k, v in countries.items():
    print(v)


for k, v in countries.items():
    print(k)


for k, v in countries.keys():
    print(k)

for k, v in countries.keys():
    print(v)

for k, v in countries.items():
    print(k)