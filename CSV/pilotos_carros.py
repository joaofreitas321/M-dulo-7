"""
Programa para ler e guardar dados em ficheiros csv para carros e pilotos de corridas.
carros.csv : marca, modelo, matrícula
pilotos.csv: nome, idade, país

Funcionalidades:
    Adicionar: carros, pilotos
    Listar   : carros, pilotos
    Pesquisar: Pilotos de um carro, carro de um piloto
"""
import csv
import os

FICHEIRO_PILOTOS = "pilotos.csv"
FICHEIRO_CARROS = "carros.csv"

lista_pilotos = []
lista_carros  = []

def LerFicheiro(nome_ficheiro):
    """Função para ler o ficheiro csv e devolver uma lista com os dados"""
    #lista vazia para guardar os dados do ficheiro
    dados = []
    #verificar se o ficheiro existe
    if os.path.exists(nome_ficheiro) == False:
        return dados
    
    #abrir ficheiro para leitura
    with open(nome_ficheiro,"r",encoding="utf-8") as ficheiro:
        #criar o objeto para ler o csv
        ler = csv.DictReader(ficheiro)

        #ler cada linha do ficheiro e adicionar à lista
        for linha in ler:
            dados.append(linha)
    #devolver a lista com os dados do ficheiro
    return dados

def Escrever(lista,nome):
    """Função para escrever os dados de uma lista num ficheiro csv"""
    chaves = lista[0].keys()

    with open(nome,"w",encoding="utf-8",newline="") as ficheiro:
        #variável para gravar no ficheiro (ficheiro,campos do dicionário)
        escrever = csv.DictWriter(ficheiro,fieldnames=chaves)
        #gravar o cabeçalho
        escrever.writeheader()
        for i in range(len(lista)):
            escrever.writerow(lista[i]) #grava os dados correspondentes às chaves

def ValidarMatricula(matricula):
    """Devolve True se a matrícula existe ou False se não existir"""
    for carro in lista_carros:
        if carro["matricula"] == matricula:
            return True
    return False

def ValidarNrMatriculas(matricula):
    """Devolve o número de pilotos de um carro"""
    contar = 0
    for p in lista_pilotos:
        if p["matricula"] == matricula:
            contar += 1
    return contar

def Adicionar():
    op = input("Adicionar [P]iloto ou [C]arro?")
    if op in "cC":
        #ler os dados do carro
        marca = input("Qual a marca do carro?")
        modelo = input("Qual o modelo do carro?")
        matricula = input("Qual a matrícula do carro")
        if ValidarMatricula(matricula) == True:
            print("Matrícula já existe")
            return
        #criar um dicionário
        carros = {
            "marca"    : marca,
            "modelo"   : modelo, 
            "matricula": matricula
        }
        #adicionar à lista
        lista_carros.append(carros)
        #escrever no ficheiro dos carros
        Escrever(lista_carros,FICHEIRO_CARROS)
        print("Carro foi adicionado com sucesso.")
    if op in "pP":
        #ler os dados do piloto
        matricula = input("Introduza a matrícula do veículo:")
        #verificar se a matrícula do veículo existe
        if ValidarMatricula(matricula) == False:
            print("Matrícula introduzida não existe.")
            return
        #verificar quantos pilotos estão no carro
        if ValidarNrMatriculas(matricula) >= 2:
            print("Já existem 2 pilotos no carro.")
            return
        nome = input("Qual o nome do piloto?")
        idade = input("Qual a idade do piloto?")
        pais = input("Qual o país do piloto?")
        #criar um dicionário
        pilotos = {
            "nome"      : nome,
            "idade"     : idade,
            "país"      : pais,
            "matricula" : matricula
        }
        #adicionar à lista
        lista_pilotos.append(pilotos)
        #escrever no ficheiro dos pilotos
        Escrever(lista_pilotos,FICHEIRO_PILOTOS)
        print("Piloto foi adicionado com sucesso.")

def Listar():
    op = input("Adicionar [P]iloto ou [C]arro?")
    if op in "cC":
        print(lista_carros)
    if op in "pP":
        print(lista_pilotos)

def Pesquisar():
    matricula = input("Qual a mtrícula do carro a pesquisar:")
    if matricula:
        #mostrar os pilotos do carro
        for piloto in lista_pilotos:
            if piloto["matricula"] == matricula:
                print(piloto)
    piloto = input("Qual o nome do piloto a pesquisar:")
    if piloto:
        for p in lista_pilotos:
            if p["nome"] == piloto:
            #mostrar o carro do piloto
                for c in lista_carros:
                    if p ["matricula"] == c["matricula"]:
                        print(c)

def Menu():
    global lista_carros, lista_pilotos
    lista_carros = LerFicheiro(FICHEIRO_CARROS)
    lista_pilotos = LerFicheiro(FICHEIRO_PILOTOS)
    op = 0
    while op != 4:
        op = int(input("1.Adicionar\n2.Listar\n3.Pesquisar\n4.Sair"))
        if op == 1:
            Adicionar()
        if op == 2:
            Listar()
        if op == 3:
            Pesquisar()

if __name__=='__main__':
    Menu()