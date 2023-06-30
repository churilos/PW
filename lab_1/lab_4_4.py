import math

class HammingEncoder:
    def __init__(self, dataBits):
        self.dataBits = dataBits
        self.controlBits = 0
        while (2 ** self.controlBits) <= (self.controlBits + self.dataBits):
            self.controlBits += 1

    def encode(self, data):
        data = list(data)
        c = self.controlBits
        n = len(data) + c
        res = [''] * (n + 1)
        j = 0
        for i in range(1, n + 1):
            if i == (2 ** j):
                res[i] = '0'
                j += 1
            else:
                res[i] = data[-1]
                data.pop()
        for i in range(c):
            val = 0
            for j in range(1, n + 1):
                if j & (2 ** i) == (2 ** i):
                    val = val ^ int(res[-1 * j])
            res[(2 ** i)] = str(val)
        return ''.join(res[::-1])

    def decode(self, data):
        n = len(data)
        c = self.controlBits
        res = [''] * (n + 1)
        for i in range(n):
            res[i + 1] = data[i]
        b = [0] * c
        for i in range(c):
            val = 0
            for j in range(1, n + 1):
                if j & (2 ** i) == (2 ** i):
                    val = val ^ int(res[-1 * j])
            b[i] = val
        err = sum(b[i] * (2 ** i) for i in range(c))
        if err != 0:
            res[err] = '0' if res[err] == '1' else '1'
        decoded_data = ''
        for i in range(1, n + 1):
            if not math.log(i, 2).is_integer():
                decoded_data += res[i]
        return decoded_data


hamming_encoder = HammingEncoder(4)
encoded_string = hamming_encoder.encode("0101")
decoded_string = hamming_encoder.decode(encoded_string)
print(4, '\n', hamming_encoder, '\n', encoded_string, '\n', decoded_string)
