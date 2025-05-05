"""
Programa que vai encontrar as pessoas que são sócios de ambos o Tondela e o Académico de Viseu
"""
import os

NOME1 = "academico.txt"
NOME2 = "tondela.txt"

def socios_repetidos():
    #verificar se existem
    if os.path.exists(NOME1) == False or os.path.exists(NOME2) == False:
        print("Os ficheiros dos sócios não existem")
        return
    with open(NOME1,"r",encoding="UTF-8") as ficheiro:
        socios1 = ficheiro.readlines()
    with open(NOME2,"r",encoding="UTF-8") as ficheiro:
        socios2 = ficheiro.readlines()

    encontra = False
    for socio in socios1:
        if socio in socios2:
            print(f"{socio} é sócio dos dois clubes")
            encontra = True
    if encontra == False:
        print("Não existem sóios repetidos nos dois clubes.")

socios_repetidos()