"""
Programa para criar um ficheiro com produtos e preços
"""
import os

NOME_FICHEIRO = "Produtos.txt"

def FicheiroExiste():
    if os.path.exists(NOME_FICHEIRO) == False:
        print("Ainda não tem produtos.")
        return False
    return True

def AdicionarProdutos():
    with open(NOME_FICHEIRO,"a",encoding="UTF-8") as ficheiro:
        nome = input("Produto:")
        preco = float(input("Preço:"))
        linha = f"{nome} - {preco}\n"
        ficheiro.write(linha)

def LerProdutos():
    #verificar se existe o ficheiro
    if FicheiroExiste() == False:
        return
    with open(NOME_FICHEIRO,"r",encoding="UTF-8") as ficheiro:
        while True:
            linha = ficheiro.readline()
            #EOF
            if not linha:
                break
            partes = linha.split("-")
            nome = partes[0].strip()
            preco = float(partes[1].strip())
            print(f"Produto: {nome} Preço {preco}€")

def EditarProdutos():
    #verificar se existe o ficheiro
    if FicheiroExiste() == False:
        return
    #ler o nome do produto a editar
    nome = input("Qual o produto que pretende editar?")
    #abrir ficheiro dos produtos para ler
    ficheiro_ler = open(NOME_FICHEIRO,"r",encoding="UTF-8")
    #abrir ficheiro temporário para escrever
    ficheiro_escrever = open("temp.txt","w",encoding="UTF-8")
    while True:
        #ler um produto
        linha = ficheiro_ler.readline()
        if not linha:
            break
        #verificar se é o produto a editar
        partes = linha.split("-")
        if nome == partes[0].strip():
            #se sim ler os novos dados
            novo_nome = input("Novo nome para o produto:")
            novo_preco = float(input("Novo preço para o produto:"))
            linha = f"{novo_nome} - {novo_preco}\n"
        #gravar no ficheiro temporário
        ficheiro_escrever.write(linha)
    #fechar os dois ficheiros
    ficheiro_escrever.close()
    ficheiro_ler.close()
    #apagar o ficheiro produtos
    os.remove(NOME_FICHEIRO)
    #mudar o nome do ficheiro temporário para produtos
    os.rename("temp.txt",NOME_FICHEIRO)
    print("Produto editado com sucessso.")

def ApagarProdutos():
    #verificar se existe o ficheiro
    if FicheiroExiste() == False:
        return
    #ler o nome do produto a apagar
    nome = input("Qual o produto que pretende apagar?")
    #abrir ficheiro dos produtos para ler
    ficheiro_ler = open(NOME_FICHEIRO,"r",encoding="UTF-8")
    #abrir ficheiro temporário para escrever
    ficheiro_escrever = open("temp.txt","w",encoding="UTF-8")
    while True:
        #ler um produto
        linha = ficheiro_ler.readline()
        #EOF
        if not linha:
            break
        #verificar se é o produto a editar
        partes = linha.split("-")
        if nome == partes[0].strip():
            continue
        #gravar no ficheiro temporário
        ficheiro_escrever.write(linha)
    #fechar os dois ficheiros
    ficheiro_escrever.close()
    ficheiro_ler.close()
    #apagar o ficheiro produtos
    os.remove(NOME_FICHEIRO)
    #mudar o nome do ficheiro temporário para produtos
    os.rename("temp.txt",NOME_FICHEIRO)
    print("Produto apagado com sucessso.")

def Menu():
    op = 0
    while op != 5:
        print("1.Adicionar\n2.Ler\n3.Editar\n4.Apagar\n5.Sair")
        op = int(input())
        if op == 1:
            AdicionarProdutos()
        if op == 2:
            LerProdutos()
        if op == 3:
            EditarProdutos()
        if op == 4:
            ApagarProdutos()

if __name__=="__main__":
    Menu()