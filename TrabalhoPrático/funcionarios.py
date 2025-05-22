"""
Módulo de gestão dos funcionários
"""
import utils,app
import os,pickle
#lista dos funcionários
funcionarios = []

#lista de exemplos de funcionários
funcionarios_exemplos = [
    {'id': 1, 'nome': 'Carlos Silva', 'idade': 34, 'cargo': 'Tratador', 'animais': ['Leão','Tigre']},
    {'id': 2, 'nome': 'Ana Pereira', 'idade': 40, 'cargo': 'Tratadora', 'animais': ['Girafa']},
    {'id': 3, 'nome': 'João Sousa', 'idade': 25, 'cargo': 'Segurança'},
    {'id': 4, 'nome': 'Joaquim Costa', 'idade': 43, 'cargo': 'Veterinário'}
]

def MenuFuncionarios():
    """Menu que vai gerir os funcionários"""
    op = 0
    while op != 5:
        op = utils.Menu(["Adicionar","Consultar","Editar","Apagar","Voltar"],"Menu de funcionários")
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

def Adicionar():
    """Função para adicionar o funcionário"""
    print("#### Adicionar novo funcionário ####")
    #nome
    nome = utils.ler_string(3,"Introduza o nome do funcionário:")
    #idade
    idade = utils.ler_numero_inteiro_limites(18,60,"Introduza a idade do funcionário:")
    #cargo
    cargo = utils.ler_string(3,"Introduza o cargo que vai ter:")
    #id
    id = 1
    if len(funcionarios) > 0:
        id = funcionarios[len(funcionarios)-1]['id'] + 1 #gerar o id a partir do id do último funcionário
    novo = {
        'id' : id,
        'nome' : nome,
        'idade' : idade,
        'cargo' : cargo
    }     
    #Se o cargo for Tratador perguntar pelos animais que vai tratar
    if cargo.lower() in ['tratador','tratadora']:
        animais_tratados = []
        while True:
            animal = input("Introduza o nome do animal que vai tratar:")
            if animal.strip() == "":
                break
            animais_tratados.append(animal)
        novo['animais'] = animais_tratados
    funcionarios.append(novo)
    print(f"Funcionário registado com sucesso. Tem {len(funcionarios)} funcionários")

def Consultar():
    """Função para consultar os funcionários registados"""
    print("#### Lista de funcionários ####")
    #Verificar se à funcionários registados
    if len(funcionarios) == 0:
        print("Não existem funcionários registados.")
        return
    #Percorrer a lista de funcionários
    for funcionario in funcionarios:
        print(f"Id: {funcionario['id']} Nome: {funcionario['nome']} Idade: {funcionario['idade']} Cargo: {funcionario['cargo']}")
        print("-"*80)

def Editar():
    print("#### Editar funcionário ####")
    #Verificar se à funcionários registados
    if len(funcionarios) == 0:
        print("Não existem funcionários para editar.")
        return
    #Pedir o id do funcionário a editar
    id_funcionario = utils.ler_numero_inteiro("Introduza o id do funcionário a editar:")
    for funcionario in funcionarios:
        if funcionario['id'] == id_funcionario:
            print(f"Editar informações de {funcionario['nome']} (Id: {funcionario['id']})")

            novo_nome = utils.ler_string(3,"Introduza o novo nome do funcionário:")
            nova_idade = utils.ler_numero_inteiro_limites(18,50,"Introduza a nova idade do funcionário:")
            novo_cargo = utils.ler_string(3,"Introduza o novo cargo do funcionário:")
            #Atualizar os atributos do funcionário com os novos valores inseridos pelo utilizador
            if novo_nome:
                funcionario['nome'] = novo_nome
            if nova_idade:
                funcionario['idade'] = nova_idade
            if novo_cargo:
                funcionario['cargo'] = novo_cargo
            print("Funcionário editado com sucesso.")
            return
    #Caso o id não seja encontrado    
    print("Não foi encontrado nenhum funcionário com esse id.")

def Apagar():
    """Função para remover o funcionário"""
    print("#### Apagar funcionário ####")
    #Verificar se à funcionários registados
    if len(funcionarios) == 0:
        print("Não existem funcionários a remover.")
        return
    #Pedir o id do funcionário a apagar
    id_funcionario = utils.ler_numero_inteiro("Introduza o id do funcionário a remover:")
    for funcionario in funcionarios:
        if funcionario['id'] == id_funcionario:
            funcionarios.remove(funcionario)
            print(f"Funcionário com o id {id_funcionario} removido com sucesso.")
            return
    #Caso o id não seja encontrado
    print("Não foi encontrado nenhum funcionário com esse id.")

def GuardarDados():
    with open("funcionarios.dat","wb") as ficheiro:
        pickle.dump(funcionarios,ficheiro)

def LerDados():
    global funcionarios
    if os.path.exists("funcionarios.dat") == False:
        return
    with open("funcionarios.dat","rb") as ficheiro:
        funcionarios = pickle.load(ficheiro)