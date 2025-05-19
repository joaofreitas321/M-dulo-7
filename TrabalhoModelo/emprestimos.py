"""
Módulo Empréstimos e devolucoes
"""
import utils, livros, leitores
from datetime import datetime, timedelta
import os,pickle

# livro ({}), leitor ({}), data_emprestimo, data_devolucao, estado
emprestimos = []

def MenuEmprestimos():
    op = 0
    os.system("cls")
    while op != 4:
        op = utils.Menu(["Empréstimos","Devolução","Listar","Voltar"],"Menu de empréstimos/devolucoes")
        if op == 4:
            break
        if op == 1:
            Emprestimo()
        if op == 2:
            Devolucao()
        if op == 3:
            Listar()

def Emprestimo():
    #dados no empréstimo a adicionar à lista
    novo = {}
    #ler qual o livro a emprestar
    print("Indique o livro a emprestar:")
    livro_emprestar = livros.Pesquisar()
    if len(livro_emprestar) == 0:
        print("Nenhum livro encontrado.Tente novamente.")
        return
    if len(livro_emprestar) > 1:
        #mostrar os livros encontrados
        livros.Listar(livro_emprestar)
        #pedir o id do livro a emprestar
        id = utils.ler_numero_inteiro("Introduza o id do livro a emprestar:")
        for livro in livro_emprestar:
                if livro['id'] == id:
                    if livro['estado'] != 'disponível':
                        print("Esse livro está emprestado.")
                        return
                    novo['livro'] = livro
                    break
        if 'livro' not in novo:
            print("O id indicado não existe")
            return
    else:
        #só encontrou um livro
        if livro_emprestar[0]['estado'] != 'disponível':
            print("Esse livro está emprestado.")
            return
        novo['livro'] = livro_emprestar[0]
        print(novo)
    #ler qual o leitor que leva o livro
    print("Indique o leitor:")
    leitor_emprestimo = leitores.Pesquisar()
    if len(leitor_emprestimo) == 0:
        print("Leitor não encontrado")
        return
    elif len(leitor_emprestimo) > 1:
        print("Leitores encontrados:")
        leitores.Listar(leitor_emprestimo)
        id = utils.ler_numero_inteiro("Indique o id do leitor:")
        for leitor in leitor_emprestimo:
            if leitor['id'] == id:
                novo['leitor'] = leitor
                break
        if 'leitor' not in novo:
            print("o id indicado não existe.")
            return
    else:
        novo['leitor'] = leitor_emprestimo[0]
    # TODO verificar se o leitor pode levar o livro
    #registar o empréstimo com data de devolução
    data_atual = datetime.now()
    #TODO remover o - e colocar um +
    data_entrega = data_atual + timedelta(days=30)
    str_data_atual = data_atual.strftime("%Y-%m-%d")
    str_data_entrega = data_entrega.strftime("%Y-%m-%d")
    novo['data_emprestimo'] = str_data_atual
    novo['data_devolucao'] = str_data_entrega
    novo['estado'] = True   #Emprestimo está a decorrer
    emprestimos.append(novo)
    #atualizar o estado do livro
    novo['livro']['estado'] = 'emprestado'
    novo['livro']['leitor'] = novo['leitor']
    print("Empréstimo registado com sucesso.")
    print(f"Livro emprestado: {novo['livro']}")
    print(f"Leitor: {novo['leitor']}")

def Devolucao():
    #ler o id do livro a devolver
    id_livro = utils.ler_numero_inteiro("Indique o id do livro a devolver:")
    #verifivar se o livro está emprestado
    livro = livros.GetLivro(id_livro)
    if livro == None:
        print("Não existe nenhum livro com o id indicado.")
        if livro['estado'] != 'emprestado':
            print("Esse livro não está emprestado.")
    #verificar se a devolução está dentro do prazo
    emprestimo_devolver = None
    for emprestimo in emprestimos:
        if emprestimo['livro'] == livro and emprestimo['estado'] == True:
            emprestimo_devolver = emprestimo
    if emprestimo_devolver == None:
        print("Empréstimo não encontrado.")
        return
    data_devolucao = emprestimo_devolver['data_devolucao']
    data_atual = datetime.now()
    #comparar como datetime ou como inteiro?
    #Resposta do Afonso foi inteiro
    idata_atual = int(data_atual.strftime("%Y%m%d"))
    idata_devolucao = int(datetime.strptime(data_devolucao,"%Y-%m-%d").strftime("%Y%m%d"))
    if idata_atual > idata_devolucao:
        print("Devolução fora do prazo.")
        #registar se houve infração do leitor
        emprestimo_devolver['leitor']['infracoes'] += "Entrega for de prazo"
    #atualizar o nr de empréstimo do livro
    livro['nr_emprestimos'] += 1
    #mudar o estado do livro
    livro['estado'] = 'disponível'
    livro['leitor'] = None
    #mudar o estado do empréstimo
    emprestimo_devolver['estado'] = False
    print("Devolução concluída com sucesso.")

def Listar():
    #perguntar se pretende ver todos os empréstimos ou só os empréstimos por concluir
    op = utils.ler_string(1,"Listar [T]odos ou só por [C]oncluir")
    for emp in emprestimos:
        if op in 'tT' or (op in 'cC' and emp['estado'] == True):
            print(f"{emp['livro']['titulo']} {emp['leitor']['nome']} {emp['estado']}")

def GuardarDados():
    lista_ficheiro = []
    #criar uma lista sem referências para dicionários de outras listas
    for e in emprestimos:
        novo = {
            #substituir a referência para lista leitores por o id
            'id_leitor'       : e['leitor']['id'],
            #substituir a referência para a lista livros por o id
            'id_livro'        : e['livro']['id'],
            'data_emprestimo' : e['data_emprestimo'],
            'data_devolucao'  : e['data_devolucao'],
            'estado'          : e['estado']
        }
        lista_ficheiro.append(novo)

    with open("emprestimos.dat","wb") as ficheiro:
        pickle.dump(lista_ficheiro,ficheiro)

def LerDados():
    global emprestimos
    emprestimos = []
    lista_ficheiro = []
    if os.path.exists("emprestimos.data") == False:
        return
    with open("emprestimos.dat","rb") as ficheiro:
        lista_ficheiro = pickle.load(ficheiro)
    #criar a lista empréstimos com as referências para livros e leitores
    for e in lista_ficheiro:
        novo = {
            'data_emprestimo' : e['data_emprestimo'],
            'data_devolucao'  : e['data_devolucao'],
            'estado'          : e['estado'],
            'leitor'          : leitores.GetLeitor(e['id_leitor']),
            'livro'           : livros.GetLivro(e['id_livro'])
        }
        emprestimos.append(novo)