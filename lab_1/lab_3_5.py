d5 = d2.copy() # создание копии словаря
print("Dict d5 copying d2 = ", d5)
40
# получение значения по ключу
print("Get dict value by key d5['bag']: ", d5["bag"])
print("Get dict value by key d5.get('bag'): ", 
d5.get('bag'))
print("Get dict keys d5.keys(): ", d5.keys()) # 
список ключей
print("Get dict values d5.values(): ", d5.values()) # 
список значений
print("\n")

# Creating myInfo dictionary
myInfo = {
    'surname': 'YourSurname',
    'name': 'YourName',
    'middlename': 'YourMiddleName',
    'day': 1,
    'month': 1,
    'year': 2000,
    'university': 'YourUniversity'
}

# Printing keys and values of myInfo dictionary
print("Keys of myInfo dictionary: ", list(myInfo.keys()))
print("Values of myInfo dictionary: ", list(myInfo.values()))
