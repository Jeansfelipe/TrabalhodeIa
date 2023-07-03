from jogo_dos_8 import cria_jogo_dos_8, print_board
from backtracking import resolver_backtracking

#Inicializando a dimensao da matriz do board
tamanho = int(input("Informe o tamanho do jogo que deseja montar: "))

# Criar um jogo dos 8 embaralhado
board = cria_jogo_dos_8(tamanho)


#Escolhe algoritmo
print("1 - Backtracking")
print("2 - Busca em Largura")
print("3 - Busca em Profundidade")
print("4 - Busca Ordenada")
print("5 - Busca Gulosa")
print("6 - Busca A*")
print("7 - Busca IDA*")
algoritmo = int(input("Escolha o algoritmo que deseja utilizar: "))


# Imprimir o jogo inicial
print("Jogo inicial:")
print_board(board,tamanho)


match algoritmo:
    case 1:
        resolver_backtracking(board, tamanho)
    case 2:
        #busca em largura
        print("largura")
    case 3:
        #busca em profundidade
         print("profundidade")
    case 4:
        #busca ordenada
        print("ordenada")
    case 5:
        #busca gulosa
        print("gulosa")
    case 6:
        #busca A*
        print("A*")
    case 7:
        #busca IDA*
        print("IDA*")