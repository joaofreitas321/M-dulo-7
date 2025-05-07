"""
Programa para inverter as linhas de um ficheiro
"""
NOME_FICHEIRO_LER = "linha_comandos.py"
NOME_FICHEIRO_ESCREVER = "linha_comandos_copia.py"

#ler o ficheiro
with open(NOME_FICHEIRO_LER,"r",encoding="utf-8") as ficheiro:
    linhas = ficheiro.readlines()

#criar o ficheiro para escrever
with open(NOME_FICHEIRO_ESCREVER,"w",encoding="utf-8") as ficheiro:
    for i in range(len(linhas)-1,-1,-1):
        if linhas[i][len(linhas[i])-1] != "\n":
            linhas[i] += "\n"
        ficheiro.write(linhas[i])

print("Cópia criada com sucesso")