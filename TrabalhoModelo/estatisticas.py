import utils
from datetime import datetime
import emprestimos

def MenuEstatisticas():
    op = 0
    while op != 5:
        op = utils.Menu(["Livro mais requisitado","Leitor com mais requesições","Empréstimos fora do prazo","Top dos meses","Voltar"],"Menu de estatísticas")
        if op == 5:
            return
        if op == 1:
            LivroMais()
        if op == 2:
            LeitorMais()
        if op == 3:
            EmprestimoForaPrazo()
        if op == 4:
            MesMais()

def LivroMais():
    """Função para encontrar o livro mais requisitado no último mês (mês anterior ao mês atual)"""
    if len(emprestimos.emprestimos) == 0:
        print("Não tem empréstimos")
        return
    #mês e ano a pesquisar
    data_atual = datetime.now()
    data_atual = data_atual.strftime("%Y-%m-%d")
    partes = data_atual.split("-")
    ano = int(partes[0])
    mes = int(partes[1])
    mes = mes - 1
    if mes == 0:
        mes = 12
        ano = ano - 1
   
    #criar um dicionário { titulo: contagem}
    dicionario_livros={}
    #percorrer empréstimos
    for emprestimo in emprestimos.emprestimos:
        #verificar se é do mês anterior (comparar mês e ano)
        data_emprestimo = emprestimo['data_emprestimo'].split("-")
        ano_emprestimo = int(data_emprestimo[0])
        mes_emprestimo = int(data_emprestimo[1])
        if ano_emprestimo == ano and mes_emprestimo == mes:
            #contar se sim
            if emprestimo['livro']['titulo'] in dicionario_livros:
                dicionario_livros[emprestimo['livro']['titulo']] += 1
            else:
                dicionario_livros[emprestimo['livro']['titulo']] = 1
    #percorrer o dicionário e encontrar o maior
    maior = 0
    titulo_maior =""
    for livro in dicionario_livros:
        if dicionario_livros[livro]>maior:
            titulo_maior = livro
            maior = dicionario_livros[livro]
    print(f"O livro mais emprestado no mês anterior ({mes}/{ano}) foi {titulo_maior} com {maior} empréstimos.")

def LeitorMais():
    """Função para mostrar o leitor com mais empréstimos"""
    if len(emprestimos.emprestimos) == 0:
        print("Não tem empréstimos.")
        return
    dicionario_leitores= {}
    for emprestimo in emprestimos.emprestimos:
        nome = emprestimo['leitor']['nome']
        if nome in dicionario_leitores:
            dicionario_leitores[nome] += 1
        else:
            dicionario_leitores[nome] = 1

    nome_maior = ""
    maior = 0
    for leitor in dicionario_leitores:
        if dicionario_leitores[leitor] > maior:
            maior = dicionario_leitores[leitor]
            nome_maior = leitor
    print(f"O leitor com mais empréstimos é {nome_maior}")

def EmprestimoForaPrazo():
    """Função para listar os empréstimos que ainda não acabaram e estão fora do prazo de entrega"""
    if len(emprestimos.emprestimos) == 0:
        print("Não tem empréstimos.")
        return
    #criar uma variável para a data atual
    data_atual = datetime.now()
    #converter para inteiro
    idata_atual = int(data_atual.strftime("%Y%m%d"))
    #contar nº de mepréstimos fora do prazo
    contar = 0
    #percorrer a lista de empréstimos
    for emprestimo in emprestimos.emprestimos:
        #converter a data do empréstimo em inteiro
        data_devolucao = emprestimo['data_devolucao']
        idata_devolucao = int(datetime.strptime(data_devolucao,"%Y-%m-%d").strftime("%Y%m%d"))
        #comparar com a data atual
        if idata_atual > idata_devolucao and emprestimo['estado'] == True:
            dias_atraso = idata_atual - idata_devolucao
            print(f"O leitor {emprestimo['leitor']['nome']} tem o livro {emprestimo['livro']['titulo']} por entregar fora do prazo à {dias_atraso} dias.")
            contar += 1
    percentagem = (contar / len(emprestimos.emprestimos)) * 100
    print(f"{percentagem}% de empréstimos fora do prazo")

def MesMais():
    """Mostra o mês em que existem mais requisições, independentemente do ano"""
    if len(emprestimos.emprestimos) == 0:
        print("Não tem empréstimos.")
        return
    #criar uma lista com 12 posições (1 por mês)
    meses = []
    for i in range(12):
        meses.append(0)
    #percorrer os empréstimos
    for emprestimo in emprestimos.emprestimos:
        #extrair o mês da data do empréstimo
        partes = emprestimo['data_emprestimo'].split("-")
        mes_emprestimo = int(partes[1])
    #somar 1 na lista dos meses na posição do mês do empréstimos
        meses[mes_emprestimo-1] += 1
    
    #percorrer a lista dos meses e encontrar o maior
    posicao_maior = 0
    for i in range(len(meses)):
        if meses[i] > meses[posicao_maior]:
            posicao_maior = i

    #mostrar a posição do maior +1
    print(f"O mês que tem mais empréstimos é {posicao_maior+1} com {meses[posicao_maior]} empréstimos.")