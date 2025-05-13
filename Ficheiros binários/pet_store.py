"""
Programa para gerir uma loja de pets:
    Pets.dat
    Raça - string   30 30
    Peso - float       4
    Género - string 1  1
    Preço - float      4
                     39 bytes
Funções:1. Adicionar 2. Listar todos 3. Apagar 4. Editar 5. Sair
"""
import struct,os

NOME_FICHEIRO = "pets.bin"
TAMANHO_REGISTO = 39

def Adicionar():
    """Lê os dados do utilizador e adiciona ao ficheiro"""
    raca = input("Introduza a raça do pet:")
    peso = float(input("Introduza o peso do pet:"))
    genero = input("Introduza o genero do pet:")
    preco = float(input("Introduza o preço do pet:"))
    with open(NOME_FICHEIRO,"ab") as ficheiro:
        #gravar um campo de cada vez
        ficheiro.write(struct.pack("30s",raca.encode("utf-8")))
        ficheiro.write(struct.pack("f",peso))
        ficheiro.write(struct.pack("1s",genero.encode("utf-8")))
        ficheiro.write(struct.pack("f",preco))
        #gravar o registo de uma vez
        #dados_binario = struct("30sf1sf",raca.encode("utf-8"),peso,genero.encode("utf-8"),preco)
        #ficheiro.write(dados_binario)
    print("Dados registados com sucesso.")

def Listar():
    """Lista todos os pets do ficheiro - opcionalmente perguntar a raça e só listar os pets da raça indicada"""
    #testar se ficheiro existe
    if os.path.exists(NOME_FICHEIRO) == False:
        print("Ainda não tem dados")
        return
    with open(NOME_FICHEIRO,"rb") as ficheiro:
        while True:
            #raça
            dados_binario = ficheiro.read(30)
            if not dados_binario:
                break
            dados = struct.unpack("30s",dados_binario)
            print("Raça ",dados[0].decode("utf-8").rstrip("\x00"))
            #peso
            dados_binario = ficheiro.read(4)
            dados = struct.unpack("f",dados_binario)
            print("Peso ",dados[0])
            #genero
            dados_binario = ficheiro.read(1)
            dados = struct.unpack("1s",dados_binario)
            print("Género ",dados[0].decode("utf-8").rstrip("\x00"))
            #peso
            dados_binario = ficheiro.read(4)
            dados = struct.unpack("f",dados_binario)
            print("Preço ",dados[0])

def Apagar():
    """Lista os pets e pergunta se é o pet a apagar"""
    with open(NOME_FICHEIRO,"rb") as f_ler:
        #criar um ficheiro temporário
        with open("temp.bin","wb") as f_escrever:
            while True:
                    raca_binario = f_ler.read(30)
                    if not raca_binario:
                        break
                    #ler um registo
                    peso_binario = f_ler.read(4)
                    genero_binario = f_ler.read(1)
                    preco_binario = f_ler.read(4)
                    raça = struct.unpack("30s",raca_binario)
                    #mostrar ao utlizar
                    print("raça: ",raça[0].decode('utf-8').rstrip("\x00"))
                    #se NÃO é para agravar no ficheiro temp
                    op = input("Pretende apagar este animal? ")
                    if op not in "sS":
                        f_escrever.write(raca_binario)
                        f_escrever.write(peso_binario)
                        f_escrever.write(genero_binario)
                        f_escrever.write(preco_binario)
    #apagar o ficheiro de dados
    os.remove(NOME_FICHEIRO)
    #mudar o nome do ficheiro temporário
    os.rename("temp.bin",NOME_FICHEIRO)
    print("Animal removido com sucesso")

def Editar():
    """Lista os pets e pergunta se pretende editar"""
    #Abrir o ficheiro para leitura e escrita rb+
    with open(NOME_FICHEIRO,"rb+") as ficheiro:
        while True:
            #ler um registo
            raca_binario = ficheiro.read(30)
            if not raca_binario:
                break   #terminar o ciclo chegou ao fim do ficheiro
            peso_binario = ficheiro.read(4)
            genero_binario = ficheiro.read(1)
            preco_binario = ficheiro.read(4)
            #mostrar ao utilizador
            raca = struct.unpack("30s",raca_binario)[0]
            raca = raca.decode("utf-8").rstrip("\x00")
            peso = struct.unpack("f",peso_binario)[0]
            genero = struct.unpack("1s",genero_binario)[0]
            genero = genero.decode("utf-8").rstrip("\x00")
            preco = struct.unpack("f",preco_binario)[0]
            print("Pretende editar este animal?")
            print(f"{raca} - {peso} - {genero} - {preco}")
            op = input("op? ")
            #perguntar se quer alterar
            if op in "sS":
                raca = input("Nova raça? ")
                peso = float(input("Novo peso? "))
                genero = input("Novo género? ")
                preco = float(input("Novo preço? "))
                #se alterar gravar novamente o mesmo registo
                ficheiro.seek(-39,os.SEEK_CUR)
                ficheiro.write(struct.pack("30s",raca.encode("utf-8")))
                ficheiro.write(struct.pack("f",peso))
                ficheiro.write(struct.pack("1s",genero.encode("utf-8")))
                ficheiro.write(struct.pack("f",preco))

def Menu():
    """Menu principal da aplicação"""
    op = 0
    while op != 5:
        op = int(input("1.Adicionar\n2.Listar\n3.Apagar\n4.Editar\n5.Sair"))
        if op == 1:
            Adicionar()
        if op == 2:
            Listar()
        if op == 3:
            Apagar()
        if op == 4:
            Editar()

if __name__=="__main__":
    Menu()