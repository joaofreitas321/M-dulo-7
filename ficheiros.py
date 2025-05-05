"""
Ficheiros
r - Leitura
w - Escrever (destrói tudo do ficheiro caso exista)
a - Escrever no final do ficheiro
r+ - Leitura / Escrita
w+ - Leitura / Escrita (Cria ficheiro)
a+ - Leitura / Escrita (No final)
"""

ficheiro = open("Alunos.txt","a",encoding="UTF-8")
ficheiro.write("Olá mundo\n")
ficheiro.write("Fim")
ficheiro.close()