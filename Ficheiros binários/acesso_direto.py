"""
Programa para ler os dados de um registo com base no nº do registo
Cada registo ocupa 28 bytes (20sif - nome idade saldo)
"""
import os
import struct

TAMANHO_REGISTO = 28

#calcular o tamanho do ficheiro
tamanho_ficheiro = os.path.getsize("dados.bin")
#calcular o nr de registos
numero_registos = tamanho_ficheiro / TAMANHO_REGISTO
print(f"{tamanho_ficheiro} {numero_registos}")

numero_a_ler = int(input(f"Tem {numero_registos} qual o que pretende ler? "))

if numero_a_ler > numero_registos:
    print("Não existe esse registo")
else:
    #abrir o ficheiro para leitura em modo binário
    with open("dados.bin","rb") as ficheiro:
        #posicionar o cursor no byte correspondente ao registo a ler
        byte_ler = (numero_a_ler -1) * TAMANHO_REGISTO
        ficheiro.seek(byte_ler)
        #ler o registo
        dados_binarios = ficheiro.read(28)
        #faz o empacotamento
        dados = struct.unpack("20sif",dados_binarios) 
        print(dados[0].decode('utf-8').rstrip("\x00"))
        print(dados[1])
        print(dados[2])       