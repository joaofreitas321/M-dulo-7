"""
Ficheiros
r - Leitura
w - Escrever (destrói tudo do ficheiro caso exista)
a - Escrever no final do ficheiro
r+ - Leitura / Escrita
w+ - Leitura / Escrita (Cria ficheiro)
a+ - Leitura / Escrita (No final)
"""

ficheiro = open("Alunos.txt","r",encoding="UTF-8")
texto = ficheiro.readlines()
print(texto)

ficheiro.close()