"""
Programa que utiliza os ficheiros intro.txt, desculpa.txt e culpado.txt para gerar uma frase
"""
import os, random

FICHEIRO_INTRO = "intro.txt"
FICHEIRO_CULPADO = "culpado.txt"
FICHEIRO_DESCULPA = "desculpa.txt"

def ParteDesculpa(ficheiro):
    if os.path.exists(ficheiro) == False:
        print(f"Falta o ficheiro {ficheiro}")
        return ""
    with open(ficheiro,"r",encoding="utf-8") as ficheiro:
        linhas = ficheiro.readlines()
    linha = random.choice(linhas)
    linha = linha.replace("\n","")
    return linha

print(ParteDesculpa(FICHEIRO_INTRO)+" ",end="")
print(ParteDesculpa(FICHEIRO_CULPADO)+" ",end="")
print(ParteDesculpa(FICHEIRO_DESCULPA)+" ",end="")