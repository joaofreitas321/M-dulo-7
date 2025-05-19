"""
Leitura de um ficheiro pickle com uma lista
"""
import pickle

#lista vazia
lista = []

with open("minha_lista.pkl","rb") as ficheiro:
    lista = pickle.load(ficheiro)

print(lista)