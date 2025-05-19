"""
Módulo de gestão dos leitores - Eduardo Cruz
"""
import utils
import os,pickle

# lista dos leitores
leitores = []

# lista de leitores de exemplo

exemplo_leitores = [{"id":1,"nome":"joaquim","idade":13,"email":"joaquim@gmail.com","datanascimento":"12/9/2009","infracoes":""},
                    {"id":2,"nome":"ana","idade":16,"email":"ana@gmail.com","datanascimento":"18/4/2999","infracoes":""},
                    {"id":3,"nome":"maria","idade":14,"email":"maria@gmail.com","datanascimento":"30/02/2026","infracoes":""}]

# Campos que nao podem ser editados pelo utilizador
lista_campos_privados = ["id","infracoes"]

def Configurar():
    """Insere dados de exemplo"""
    leitores.extend(exemplo_leitores)

# Menu Leitores
def MenuLeitores():
    """Submenu para gerir os leitores"""
    op = 0
    os.system("cls")
    while op != 6:
        op = utils.Menu(["Adicionar","Listar","Editar","Apagar","Pesquisar","Voltar"],"Menu Leitores")
        print("#-------------------------#")
        if op == 6:
            break
        if op == 1:
            Adicionar()
        if op == 2:
            Listar(leitores)
        if op == 3:
            Editar()
        if op == 4:
            Apagar()
        if op == 5:
            Pesquisar_listar()

def GetLeitor(id):
    #devolve o leitor com base no id indicado
    for leitor in leitores:
        if leitor['id'] == id:
            return leitor
    return None

# Adicionar Leitor
def Adicionar():
    print("#### Adicionar leitor novo ###")
    # Nome
    nome = utils.ler_string(3,"Introduza o seu nome: ")
    # email
    email = utils.ler_string(3,"Introduza o seu email: ")
    # idade
    idade = utils.ler_numero_inteiro_limites(6,80,"Introduza a sua idade: ")
    # data nascimento
    data_nascimento = utils.ler_string(10,"Introduza a sua data de nascimento (dd/mm/aaaa): ")
    # id
    id = 1
    if len(leitores)>0:
        id = leitores[len(leitores)-1]["id"]+1 # Codigo vai gerar o id apartir do id do ultimo leitor
    novo = {
        "id":id,
        "nome": nome,
        "email": email,
        "idade" :idade,
        "datanascimento":data_nascimento,
        "infracoes" :"",
    }
    leitores.append(novo)
    print(f"Leitor novo registrado com sucesso. Tem {len(leitores)} leitores")

# Editar Leitor
def Editar():
    # Pesquisar o leitor a editar
    leitores_editar = Pesquisar()
    # mostrar os dados de cada leitor encontrado
    if len(leitores_editar) == 0:
        print("Não foram encontrados leitores com esse nome.")
        return
    # mostrar os leitores encontrados
    for leitor in leitores_editar:
        op = input(f"Deseja editar {leitor["nome"]}?: ")
        if op not in "sS":
            continue
        #mostrar os dados atuais
        print(f"Nome: {leitor['nome']} Idade: {leitor['idade']} Email: {leitor['email']} Data Nascimento: {leitor['datanascimento']}")
        #perguntar qual o camppo a alterar
        op = input("Qual o campo a editar (deixar em branco para cancelar):")
        if op == "":
            return
        #ler o valor e atualizar
        op = op.lower()
        #verificar se o campo existe
        if op not in leitor.keys():
            print("Erro. O campo indicado não existe")
            break
        valor = input(f"Qual o valor para o campo {op}:")
        leitor[op] = valor

# Apagar Leitor
def Apagar(): 
    #verificar se existem leitores
    if len(leitores) == 0:
        print("Não existem leitores")
        return
    print("Pesquisa do leitor a remover")
    l_leitores = Pesquisar()
    #verificar se encontrou pelo menos um
    if len(l_leitores) == 0:
        print("Não foi encontrado nenhum leitor.")
    for leitor in l_leitores:
        print(f"id:{leitor['id']} Nome: {leitor['nome']} Email: {leitor['email']}")
        op = input("Deseja remover este leitor?")
        if op in "sS":
            leitores.remove(leitor)
            break
    print(f"Leitor removido com sucesso. Tem {len(leitores)} leitores.")

# Listar Leitores
def Listar(lista_a_listar):
    """Função para listar todos os Leitores"""
    print("#"*40)
    print("Lista de Leitores")
    print("#"*40)
    for leitor in lista_a_listar:
        print(f"Id:{leitor["id"]} | Nome: {leitor["nome"]} | email: {leitor["email"]} | data de nascimento: {leitor["datanascimento"]} | infrações: {leitor["infracoes"]} ")
        print("-"*80)

# pesquisar e listar
def Pesquisar_listar():
    resultado = Pesquisar()
    Listar(resultado)

# Pesquisar Leitores
def Pesquisar():
    """Devolver a lista dos leitores que correspondem a um critério"""
    pesquisa = utils.ler_string(1,f"{"nome"} a pesquisar: ")
    l_resultados = []
    # Adicionar à lista os leitores que correspondem ao resultado da pesquisa
    for leitor in leitores:
        if pesquisa.lower() in leitor["nome"].lower():
            l_resultados.append(leitor)
    return l_resultados

def GuardarDados():
    with open("leitores.dat","wb") as ficheiro:
        pickle.dump(leitores,ficheiro)

def LerDados():
    global leitores
    if os.path.exists("leitores.dat") == False:
        return
    with open("leitores.dat","rb") as ficheiro:
        leitores = pickle.load(ficheiro)