"""
Programa para gravar um nº inteiro num ficheiro binário
"""
import struct

numero = 1234

#gravar o nº no ficheiro int.dat
with open("int.dat","wb") as ficheiro:
    #empacotar o número no formato inteiro e escrever no ficheiro
    ficheiro.write(struct.pack("i",numero))

print("Inteiro gravado com sucesso")