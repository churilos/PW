class Encoder:
    def encode(self, string):
        pass

    def decode(self, string):
        pass

class HuffmanEncoder(Encoder):
    def __init__(self):
        self.compressionCoef = 0

    def encode(self, string):
        # Implement the Huffman encoding algorithm here
        # ...
        self.__setCompressionCoef()

    def decode(self, string):
        # Implement the Huffman decoding algorithm here
        # ...

    def __setCompressionCoef(self):
        # Calculate the compression coefficient for the Huffman algorithm here
        # ...
        pass

    def getCompressionCoef(self):
        return self.compressionCoef

class LZEncoder(Encoder):
    def __init__(self):
        self.compressionCoef = 0

    def encode(self, string):
        # Implement the Lempel-Ziv encoding algorithm here
        # ...
        self.__setCompressionCoef()

    def decode(self, string):
        # Implement the Lempel-Ziv decoding algorithm here
        # ...

    def __setCompressionCoef(self):
        # Calculate the compression coefficient for the Lempel-Ziv algorithm here
        # ...
        pass

    def getCompressionCoef(self):
        return self.compressionCoef
