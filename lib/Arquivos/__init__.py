from cadastro.lib.interface import*
def arqvexiste(nome):
    try:
        a=open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return  True

def criararquv(nome):
    try:
        a=open(nome, "wt+")
        a.close()
    except:
        print("\033[31mHouve um Problema ao Criar o Arquivo\033[m ")
    else:
        print(f"\033[32mArquivo {nome} Criado Com Sucesso\033[m")


def lerarquiv(nome):
    try:
        a= open(nome, "rt")
    except:
        print("\033[31mHouve um Problema ao ler o Arquivo\033[m ")
    else:
        cabeçalho("\033[32m PESSOAS CADASTRADAS\033[m")
        print(a.read())

    finally:
        a.close()


def cadastrar(arq, nome="Desconhecido", idade=0):
    try:
        a = open(arq, "at")
    except:
        print("\033[31mHouve um Problema ao abrir o Arquivo\033[m ")
    else:
        try:
            dado = [nome, idade]
            a.writelines(f"{dado[0].title():<4}{dado[1]:>30} anos\n")
            dadogeral = []
            dadogeral.append(dado[:])

        except:
            print("\033[31mHouve um ERRO ao Escrever os dados \033[m ")
        else:
            print("\033[32m Novo Registro adicionado\033[m")
            a.close()
