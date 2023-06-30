import heapq
import os
from collections import defaultdict

def encodeHuffman(fileIn, fileOut):
    try:
        with open(fileIn, 'r') as f:
            text = f.read()
        if not text:
            return False
        freq = defaultdict(int)
        for ch in text:
            freq[ch] += 1
        heap = [[weight, [char, ""]] for char, weight in freq.items()]
        heapq.heapify(heap)
        while len(heap) > 1:
            lo = heapq.heappop(heap)
            hi = heapq.heappop(heap)
            for pair in lo[1:]:
                pair[1] = '0' + pair[1]
            for pair in hi[1:]:
                pair[1] = '1' + pair[1]
            heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
        codes = dict(sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p)))
        encoded_text = "".join([codes[ch] for ch in text])
        with open(fileOut, 'w') as f:
            for ch in codes:
                f.write(f"{ch} {codes[ch]}\n")
            f.write("\n" + encoded_text)
        return True
    except:
        return False

def decodeHuffman(fileIn, fileOut):
    try:
        with open(fileIn, 'r') as f:
            lines = f.readlines()
        if not lines:
            return False
        codes = {}
        for line in lines:
            if line == "\n":
                break
            ch, code = line.split()
            codes[code] = ch
        encoded_text = lines[-1]
        decoded_text = ""
        code = ""
        for ch in encoded_text:
            code += ch
            if code in codes:
                decoded_text += codes[code]
                code = ""
        with open(fileOut, 'w') as f:
            f.write(decoded_text)
        return True
    except:
        return False

def encodeLZ(fileIn, fileOut):
    try:
        with open(fileIn, 'r') as f:
            text = f.read()
        if not text:
            return False
        i = 0
        dictionary = {text[i:i+1]: i for i in range(256)}
        encoded_text = []
        s = text[i]
        i += 1
        while i < len(text):
            c = text[i]
            if s + c in dictionary:
                s += c
            else:
                encoded_text.append(dictionary[s])
                dictionary[s+c] = len(dictionary)
                s = c
            i += 1
        if s:
            encoded_text.append(dictionary[s])
        with open(fileOut, 'wb') as f:
            for code in encoded_text:
                f.write(code.to_bytes(2, byteorder='big'))
        return True
    except:
        return False

def decodeLZ(fileIn, fileOut):
    try:
        with open(fileIn, 'rb') as f:
            encoded_text = []
            while (byte := f.read(2)):
                encoded_text.append(int.from_bytes(byte, byteorder='big'))
        if not encoded_text:
            return False
        dictionary = {i: chr(i) for i in range(256)}
        decoded_text = ""
        s = dictionary[encoded_text.pop(0)]
        decoded_text += s
        for k in encoded_text:
            if k in dictionary:
                entry = dictionary[k]
            elif k == len(dictionary):
                entry = s + s[0]
            else:
                raise ValueError('Bad compressed k: %s' % k)
            decoded_text += entry
            dictionary[len(dictionary)] = s + entry[0]
            s = entry
        with open(fileOut, 'w') as f:
            f.write(decoded_text)
        return True
    except:
        return False

# Проверка работы функций на произвольном тексте.
textInFile = 'test_text.txt'
textOutFile = 'encoded_text.txt'
decodedTextOutFile = 'decoded_text.txt'

with open(textInFile, 'w') as f:
    f.write('this is some test text')

if encodeHuffman(textInFile, textOutFile):
    print('Huffman encoding successful')
else:
    print('Huffman encoding failed')

if decodeHuffman(textOutFile, decodedTextOutFile):
    print('Huffman decoding successful')
else:
    print('Huffman decoding failed')

with open(decodedTextOutFile, 'r') as f:
    print(f.read())

if encodeLZ(textInFile, textOutFile):
    print('LZ encoding successful')
else:
    print('LZ encoding failed')

if decodeLZ(textOutFile, decodedTextOutFile):
    print('LZ decoding successful')
else:
    print('LZ decoding failed')

with open(decodedTextOutFile, 'r') as f:
    print(f.read())

# Подбор текстов для сравнения методов Хаффмана и Лемпеля-Зива.
text1 = 'aaaaabbbbcccdde'
text2 = 'the quick brown fox jumps over the lazy dog'

with open(textInFile, 'w') as f:
    f.write(text1)

encodeHuffman(textInFile, textOutFile)
huffmanSize = os.path.getsize(textOutFile)
encodeLZ(textInFile, textOutFile)
lzSize = os.path.getsize(textOutFile)
originalSize = os.path.getsize(textInFile)

print(f'Text: {text1}')
print(f'Original size: {originalSize} bytes')
print(f'Huffman size: {huffmanSize} bytes')
print(f'LZ size: {lzSize} bytes')

with open(textInFile, 'w') as f:
    f.write(text2)

encodeHuffman(textInFile, textOutFile)
huffmanSize = os.path.getsize(textOutFile)
encodeLZ(textInFile, textOutFile)
lzSize = os.path.getsize(textOutFile)
originalSize = os.path.getsize(textInFile)

print(f'Text: {text2}')
print(f'Original size: {originalSize} bytes')
print(f'Huffman size: {huffmanSize} bytes')
print(f'LZ size: {lzSize} bytes')
