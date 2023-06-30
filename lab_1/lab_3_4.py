Dict d1 = {'month': 6, 'year': 1983, 'day': 18}
Dict d2 by dict()= {'apples': 5, 'bag': 'basket', 
'bananas': 3, 'oranges': 2}
Dict d3 by dict([])= {'house': 49, 'street': 
'Kronverksky pr.'}
Dict d4 by fromkeys = {'2': 3, '1': 3}


startDict1 = {'ready': 3, 'set': 2, 'go': 1}
print(startDict1)

startDict2 = dict([('ready', 3), ('set', 2), ('go', 1)])
print(startDict2)

startDict3 = dict(ready=3, set=2, go=1)
print(startDict3)

value = input("Enter a value: ")
dict1 = {'key1': value, 'key2': value}
print(dict1)
