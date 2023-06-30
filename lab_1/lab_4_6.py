class HammingEncoder:
    def __init__(self, dataBits):
        self.dataBits = dataBits
        self.controlBits = 0
        while (2 ** self.controlBits) <= (self.controlBits + self.dataBits):
            self.controlBits += 1

    def encode(self, string):
        # Implement the Hamming encoding algorithm here
        # ...
        pass

    def decode(self, string):
        # Implement the Hamming decoding algorithm here
        # ...
        pass

hamming_encoder = HammingEncoder(4)
encoded_string = hamming_encoder.encode("0101")
decoded_string = hamming_encoder.decode(encoded_string)
