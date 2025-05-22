"""
Módulo de gestão dos animais
"""
import utils,app
import os,pickle
#lista dos animais
animais = []

#lista de animais como exemplo
animais_exemplos = [
    {'id': 1,'nome': 'Leão','especie': 'Panthera leo','idade': 12,'sexo': 'Masculino','status': 'Saudável'},
    {'id': 2,'nome': 'Girafa','especie': 'Giraffa camelopardalis','idade': 10,'sexo': 'Feminino','status': 'Doente'},
    {'id': 3,'nome': 'Tigre','especie': 'Panthera tigris','idade': 9,'sexo': 'Masculino','status': 'Doente'}
]

def MenuAnimais():
    """Menu que vai gerir os animais"""
    op = 0
    while op != 5:
        op = utils.Menu(["Adicionar","Consultar","Editar","Apagar","Voltar"],"Menu de animais")
        if op == 5:
            break
        if op == 1:
            Adicionar()
        if op == 2:
            Consultar()
        if op == 3:
            Editar()
        if op == 4:
            Apagar()

# set para armazenar nomes únicos dos animais
nomes_animais = {animal['nome'] for animal in animais_exemplos}  # Inicializa com os nomes dos exemplos

def Adicionar():
    """Função para adicionar o animal"""
    print("#### Adicionar novo animal ####")
    #nome
    nome = utils.ler_string(3,"Intoduza o nome do animal:")

    #Verificar se o nome já existe no set
    if nome in nomes_animais:
        print("Já existe um animal com este nome. Escolha outro nome.")
        return
    #espécie
    especie = utils.ler_string(3,"Intoduza o tipo de espécie:")
    #idade
    idade = utils.ler_numero_inteiro_limites(1,20,"Introduza a idade do animal:")
    #sexo
    #Garante que o status do animal só pode ser 'masculino' ou 'feminino'
    while True:
        sexo = utils.ler_string(3,"Intoduza o sexo do animal (masculino/feminino):")
        if sexo.lower() in ['masculino','feminino']:
            sexo = sexo.capitalize()
            break
        print("Erro: Só pode ser masculino ou feminino.")
    #status
    #Garante que o status do animal só pode ser 'saudável' ou 'doente'
    while True:
        status = utils.ler_string(3,"Intoduza o status do animal (saudável/doente):")
        if status.lower() in ['saudável','doente']:
            sexo = sexo.capitalize()
            break
        print("Erro: Só pode ser saudável ou doente.")
    #id
    id = 1
    if len(animais) > 0:
        id = animais[len(animais)-1]['id'] + 1 #gerar o id a partir do id do último animal
    novo = {
        'id' : id,
        'nome' : nome,
        'especie' : especie,
        'idade' : idade,
        'sexo' : sexo,
        'status' : status
    }    
    animais.append(novo)
    nomes_animais.add(nome) #Adicionar o nome ao set
    print(f"Animal registado com sucesso. Tem {len(animais)} animais")

def Consultar():
    """Função para consultar os animais registados"""
    print("#### Lista de animais ####")
    #Verificar se à animais registados
    if len(animais) == 0:
        print("Não existem animais registados.")
        return
    #Percorrer a lista de animais
    for animal in animais:
        print(f"Id: {animal['id']} Nome: {animal['nome']} Espécie: {animal['especie']} Idade: {animal['idade']} Sexo: {animal['sexo']} Status: {animal['status']}")
        print("-"*80)

def Editar():
    """Função para editar o animal desejado"""
    print("#### Editar animal ####")
    #Verificar se à animais registados
    if len(animais) == 0:
        print("Não existem animais para editar.")
        return
    #Pedir o id do animal a editar
    id_animal = utils.ler_numero_inteiro("Introduza o id do animal a editar:")
    for animal in animais:
        if animal['id'] == id_animal:
            print(f"Editar informações de {animal['nome']} (Id: {animal['id']})")

            novo_nome = utils.ler_string(3,"Introduza o novo nome do animal:")
            nova_especie = utils.ler_string(3,"Introduza a nova espécie do animal:")
            nova_idade = utils.ler_numero_inteiro_limites(1,20,"Introduza a nova idade do animal:")
            novo_sexo = utils.ler_string(3,"Introduza o novo sexo do animal:")
            novo_status = utils.ler_string(3,"Introduza o novo status do animal (Saudável/Doente:")
            #Atualizar os atributos do animal com os novos valores inseridos pelo utilizador
            if novo_nome:
                animal['nome'] = novo_nome
            if nova_especie:
                animal['especie'] = nova_especie
            if nova_idade:
                animal['idade'] = nova_idade
            if novo_sexo:
                animal['sexo'] = novo_sexo
            if novo_status:
                animal['status'] = novo_status
            print("Animal editado com sucesso.")
            return
    #Caso o id não seja encontrado    
    print("Não foi encontrado nenhum animal com esse id.")

def Apagar():
    """Função para remover o animal desejado"""
    print("#### Apagar animal ####")
    #Verificar se à animais registados
    if len(animais) == 0:
        print("Não existem animais a remover.")
        return
    #Pedir o id do animal a apagar
    id_animal = utils.ler_numero_inteiro("Introduza o id do animal a apagar.")
    for animal in animais:
        if animal['id'] == id_animal:
            animais.remove(animal)
            print(f"Animal com o id {id_animal} removido com sucesso.")
            return
    #Caso o id não seja encontrado
    print("Não foi encontrado nenhum animal com esse id.")

def GuardarDados():
    with open("animais.dat","wb") as ficheiro:
        pickle.dump(animais,ficheiro)

def LerDados():
    global animais
    if os.path.exists("animais.dat") == False:
        return
    with open("animais.dat","rb") as ficheiro:
        animais = pickle.load(ficheiro)