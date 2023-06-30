d1 = {
 "day": 18,
 "month": 6,
 "year": 1983
}
d2 = dict(bananas=3,apples=5,oranges=2,bag="basket")
d3 = dict([("street","Kronverksky pr."), ("house", 
49)])
d4 = dict.fromkeys(["1","2"], 3)
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

myInfo = {
    'surname': 'Ivanov',
    'name': 'Ivan',
    'middlename': 'Ivanovich',
    'day': 12,
    'month': 2,
    'year': 2003,
    'university': 'NIU BelSU'
}

print("Keys of myInfo dictionary: ", list(myInfo.keys()))
print("Values of myInfo dictionary: ", list(myInfo.values()))
