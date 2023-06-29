# /labs/lab1/lab_02_02.py
'''
Циклы
'''
# while
print("Numbers < 10 (while):")
i = 0
while (i<10):
  print(i, end=" ") # print in one line
  i += 1
print("\n")


# for
print("Numbers < 10 (for):")
for i in range(0,10):
  print(i, end=" ")
else:
  print("\nThe next number is 10\n")


# break
sum = 0
for i in range(0,100):
  if i > 10:
    print("\nWe reached the end, final sum: ", sum)
    break
  sum += i


# continue
i = 0
while i<=15:
  if i % 3 == 0:
    i += 1
    continue
  print(i, end=" ")
  i += 1
print("\n")


# pass
print("Let's print numbers again!")
for i in range(0,10):
  pass
  print(i, end=" ")
print("\n\n")


i = 0


for i in range(0,500):
  if i == 0 :
    if i%7==0 : print("{\n"+str(i), end="")
  elif i%7==0 : print(", {}".format(i), end="")
else:
  print("\n}")
i = -1
print("\n{")
while i<500 :  
  if i%7!=0 :
    i=i+1
    continue
  elif i == 0 : print("{}".format(i), end="")
  else : print(", {}".format(i), end="")
  i=i+1
print("\n}\n")
tmp=1
for i in range(0,4):
  for j in range(0,4):
    if i==j :
      print(f"{tmp}", end=" ")
      tmp+=1
    else :
      print(f"0", end=" ")
  print("")
