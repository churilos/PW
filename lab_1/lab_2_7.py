digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def base2dec(num, base):
  base_dict = dict(zip(digits, range(len(digits))))
  dec = 0
  for digit in num:
    dec = base*dec + base_dict[digit]
  return dec


def dec2base(num, base):
  base_dict = dict(zip(range(len(digits)), digits))
  result = ''
  while num > 0:
    digit = num % base
    result = base_dict[digit] + result
    num = num // base
  return result


def base2base(num, base1, base2):
  if not 1 < base1 <= 36 or not 1 < base2 <= 36:
    raise ValueError(
    "Invalid int number for base (We supports every value from 2 to 36)"
    )
  if base1 != 10:
    num = str(num)
    num = base2dec(num, base1)
  return dec2base(num, base2)


base1 = int(input("Set the number base:\t\t\t\t\t\t\t\t"))
num_str = input("Throw a number in this base now:\t\t\t\t\t")
num = base2dec(num_str, base1)
old_num = num_str
base2 = int(input("Set the base you want to convert your number to:\t"))
new_num_str = dec2base(num, base2)
print(f"Your number[base={base1}]:\t{old_num}\
\nNew number[base={base2}]:\t{new_num_str}")