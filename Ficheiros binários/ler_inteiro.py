"""
Ler o número inteiro do ficheiro binário
"""
import struct

with open("int.dat","rb") as ficheiro:
    numero = struct.unpack("i",ficheiro.read(4))

print(numero) #mostra um tuple (1234,)
print(numero[0]) #mostra 1234