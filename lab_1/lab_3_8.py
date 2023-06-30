import os
'''
 Анонимные функции, lambda-выражения
'''
lfunc = lambda x, y, z = 1: x + y + z
print("lfunc(1,2,3): ",lfunc(1,2,3))
print("lfunc(1,2): ",lfunc(1,2))
print("lfunc(x=1,y=3): ",lfunc(x=1,y=3))
print("lambda result: ", \
 (lambda a,b,sep=", ": 
sep.join((a,b)))("Hello","World!"))
print("\n")

lam = lambda x: print(x) if x % 3 == 0 else None

num = int(input("Enter a number: "))
lam(num)

with open(f'{os.getcwd()}/experements/lab_3/file1.txt', 'w') as f:
    f.write('Hello, World!')

with open(f'{os.getcwd()}/experements/lab_3/file2.txt', 'w') as f:
    f.write("Yesterday all my troubles seemed so far away. Now it looks as though they're here to stay. Oh, I believe in yesterday.")

open(f'{os.getcwd()}/experements/lab_3/file3.txt', 'w').close()
