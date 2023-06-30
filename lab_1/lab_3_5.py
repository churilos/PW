d5 = d2.copy() # создание копии словаря
print("Dict d5 copying d2 = ", d5)
40
# получение значения по ключу
print("Get dict value by key d5['bag']: ", d5["bag"])
print("Get dict value by key d5.get('bag'): ", 
d5.get('bag'))
print("Get dict keys d5.keys(): ", d5.keys()) 
print("Get dict values d5.values(): ", d5.values()) 
print("\n")

studentInfo = {
    'surname': 'Ivanov',
    'name': 'Ivan',
    'middlename': 'Ivanovich',
    'day': 12,
    'month': 2,
    'year': 2003,
    'university': 'NIU BelSU'
}

print("Keys of myInfo dictionary: ", list(studentInfo.keys()))
print("Values of myInfo dictionary: ", list(studentInfo.values()))
