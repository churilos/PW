'''
Множества
'''
# создание множества
b1 = set()
print("Set b1 = ", b1)
b2 = {"bear", "fox", "squirrel", "woodpecker",
"woodpecker", "wolf", "hedgehog"}
print("Set b2 = ", b2)
# создание множества из строки
b3 = set("abcdabcdefg")
print("Set b3 from string: ", set(b3))
print("\n")

vowel_dictionary = {"e","o","a","i","u","y"}

s = "Electricity is the set of physical phenomena associated \
with the presence of electric charge. Lightning is one of \
the most dramatic effects of electricity"

set1 = set(s)
print(set1, end="\n{ ")
for element in set(set1):
  if element.lower() in vowel_dictionary:
    print(f"\"{element}\"", end=" ")
print("}")
