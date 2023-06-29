'''
Условия
'''
# if..else
num = int(input("How many times have you been to the \
Hermitage?\n=> "))
if num > 0:
  print("Wonderful!")
  print("I hope you liked this museum!")
else:
  print("You should definitely visit the\
 Hermitage!")
# if..elif..else
course = int(input("What is your course number?\n=> "))
if course == 1:
  print("You are just at the beginning!")
elif course == 2:
  print("You learned many things, but not all of\
 them!")
elif course == 3:
  print("The basic course is over, it's time for\
 professional disciplines!")
else:
  print("Oh! You need to hurry! June is the month\
 of thesis defense")
x = 5
y = 12
if y % x > 0 : print("%d cannot be evenly divided by\
%d" % (y,x))
z = 3
x = "{} is a divider of {}".format(z,y) if y%z==0 \
else "{} is not a divider of {}".format(z,y)
print(x, "\n\n")


p=int(input("How many laboratory works did you do \
recently in this year?\n=> "))
a=157
b=525


if a>b: print(f"div(a,b)=a%b={a%b}")
elif b>a: print(f"div(b,a)=b%a={b%a}")
else: print(f"a*b={a*b}")
