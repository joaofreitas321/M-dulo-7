"""
Programa que utiliza o módulo pickle para guardar uma lista num fichiero binário
"""
import pickle

#lista de dados a guardar
minha_lista = [1,2,3,
               "quatro",
               {'nome':'cinco','email':'cinco@gmail.com'},
               6]

#guardar no ficheiro serializando a lista de uma vez só
with open("minha_lista.pkl","wb") as ficheiro:
    pickle.dump(minha_lista,ficheiro)
print("Dados guardados com sucesso.")