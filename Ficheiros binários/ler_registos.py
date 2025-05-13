"""
Programa para ler vários registos do ficheiro.
Cada registo tem 28 bytes (20sif -> nome,idade,saldo)
"""

import struct

with open("dados.bin","rb") as ficheiro:
    while True:
        try:
            #ler os dados todos de uma vex só
            dados_binarios = ficheiro.read(28)
            if not dados_binarios:
                break
            dados = struct.unpack("20sif",dados_binarios)
            #converter a string binária numa string
            nome = dados[0].decode('utf-8').rstrip("\x00")
            print("Nome: ",nome)
            print("Idade: ",dados[1])
            print("Saldo: ",dados[2])
        except EOFError:
            break