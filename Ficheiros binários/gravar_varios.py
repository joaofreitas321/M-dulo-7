"""
Guardar num ficheiro binário os dados de um cliente: nome, idade e saldo
"""
import struct

#ler os dados
nome = input("Qual o nome:")
idade = int(input("Indique a idade:"))
saldo = float(input("Qual o saldo:"))

#adicionar ao ficheiro (dados.bin)
with open("dados.bin","ab") as ficheiro:
    #nome -> string -> cada letra 1 byte -> 20bytes
    dados_empacotados = struct.pack("20s",nome.encode("utf-8"))
    ficheiro.write(dados_empacotados)
    #idade -> int -> 4 bytes
    dados_empacotados = struct.pack("i",idade)
    ficheiro.write(dados_empacotados)
    #saldo -> float -> 4 bytes
    dados_empacotados = struct.pack("f",saldo)
    ficheiro.write(dados_empacotados)
print("Dados guardados com sucesso.")