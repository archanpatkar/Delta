import math
import ctypes

def readFile(filename):
    return open(filename,"rb").read()

def writeFile(filename,data):
    return open(filename,"wb").write(data)

def delta_encode(data):
    last = 0
    encoded = []
    for curr in data:
        encoded.append(ctypes.c_ubyte(curr - last).value)
        last = curr
    return encoded

def delta_decode(data):
    last = 0
    decoded = []
    for delta in data:
        curr = ctypes.c_byte(delta + last).value
        decoded.append(curr)
        last = curr
    return decoded

encoded = delta_encode(readFile("test.txt"))
writeFile("encoded.txt",bytearray(encoded))
print(encoded)

decoded = bytearray(delta_decode(encoded))
writeFile("decoded.txt",decoded)
print(decoded)