"""
Programa para ler até ao final do ficheiro
"""
import os

NOME_FICHEIRO = "Pessoas.txt"

if os.path.exists(NOME_FICHEIRO) == False:
    print("O ficheiro não existe")
else:
    with open("Pessoas.txt","r",encoding="UTF-8") as ficheiro:
        texto = ficheiro.readlines()
    for linha in texto:
        print(linha,end="")

#versão 2
with open(NOME_FICHEIRO,"r",encoding="UTF-8") as ficheiro:
    while True:
        linha = ficheiro.readline()
        #verificar se encontrou o fim do ficheiro (EOF)
        if not linha:
            break
        print(linha,end="")