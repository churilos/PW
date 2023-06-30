import os
with open(f'{os.getcwd()}/experements/lab_3/text1.txt', 'r+') as f:
    text = f.read()

text = ''.join(c for c in text if c.isalnum() or c.isspace()).lower()
words = text.split()
textDict = {}

for word in words:
    if word in textDict:
        textDict[word] += 1
    else:
        textDict[word] = 1

with open(f'{os.getcwd()}/experements/lab_3/textDict.txt', 'w') as f:
    for key, value in textDict.items():
        f.write(f'{key}: {value}\\n')
