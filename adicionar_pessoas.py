"""Ler o nome de 10 pessoas e guardar o nome num ficheiro"""

with open("Pessoas.txt","w",encoding="UTF-8") as ficheiro:
    for i in range (10):
        nome = input("Introduza o nome:")
        ficheiro.write(nome)
        ficheiro.write("\n")