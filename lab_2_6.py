def num_to_bin(num, base):
  code = { "forward":"", "reversed":"", "additional":"" }
  try:
    current_int = int(num, base)
  except ValueError:
    return """You entered the wrong value! The dictionary of a Hex-numbers is common:
              \n1,2,3,4,5,6,7,8,9,A,B,C,D,E,F"""
  code["forward"] = bin(current_int)[2:]
  code["reversed"] = ''.join([
    '1' if bit == '0' else '0' for bit in code["forward"]
  ])
  code["additional"] = ''.join([
    '1' if bit == '0' else '0' for bit in bin(current_int-1)[2:]
  ])
  return code


hex_num = input("Throw a hex number here: ")
code = num_to_bin(hex_num, 16)
print(f"""Forward code:\t\t{code["forward"]}\
          \nReversed code:\t\t{code["reversed"]}\
          \nAdditional code:\t{code["additional"]}""")
