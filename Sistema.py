from cadastro.lib.interface import *
from cadastro.lib.Arquivos import *
from time import sleep

arq= "Lista de Pessoas.txt"
if not arqvexiste(arq):
    criararquv(arq)
while True:
    resp=menu(['Cadastrar Pessoas','Listar Pessoas','SAIR'])
    if resp == 1:
        cabeçalho("NOVO CADASTRO")
        nome=str(input("DIGITE SEU NOME: "))
        idade=leiaint("DIGITE SUA IDADE: ")
        cadastrar(arq,nome,idade)

    elif resp == 2:
        # lista de pessoas
        lerarquiv(arq)
    elif resp == 3:
        cabeçalho("Saindo Do Sistema ... Até Logo!")
        break
    else:
        print("\033[31mERRO: Digite uma Opção Valida.\033[m ")
    sleep(1)