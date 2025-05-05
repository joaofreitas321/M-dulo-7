"""
Ficheiros
r - Leitura
w - Escrever (destrói tudo do ficheiro caso exista)
a - Escrever no final do ficheiro
r+ - Leitura / Escrita
w+ - Leitura / Escrita (Cria ficheiro)
a+ - Leitura / Escrita (No final)
"""

with open("Alunos.txt","r",encoding="UTF-8") as f:
    texto = f.readline()
    print(texto)
    f.seek(0)
    texto = f.readline()
    print(texto)