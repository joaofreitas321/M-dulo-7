"""
Programa que grava um dicionário com o módulo pickle
"""
import pickle

#ler dados
nome = input("Nome: ")
idade = input("Idade: ")
email = input("Email: ")

#criar dicionário
registo = {
    'nome'  : nome,
    'idade' : idade,
    'email' : email
}

#guardar num ficheiro
with open("so_um.dat","ab") as ficheiro:
    #serialização
    pickle.dump(registo,ficheiro)

print("Dados adicionados.")