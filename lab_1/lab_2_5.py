def unique_permutations(string):
# Функция для нахождения уникальных сочетаний.
  characters = list(string.replace(" ", ""))


  unique_permutations = set()


  for i in range(len(characters)):
    for j in range(i + 1, len(characters) + 1):
      for permutation in _permute("".join(characters[i:j])):
        unique_permutations.add(permutation)


  return sorted(list(unique_permutations))




def _permute(string):
# Функция-генератор для удобства.
  if len(string) == 1:
    yield string
  else:
    for perm in _permute(string[1:]):
      for i in range(len(perm) + 1):
        yield perm[:i] + string[0] + perm[i:]




input_string = input("Enter a string: ")
print(unique_permutations(input_string))