from jogo_dos_8 import cria_jogo_dos_8, print_board
from backtracking import resolver_backtracking
import time
import sys


sys.setrecursionlimit(1000)

#Inicializando a dimensao da matriz do board
tamanho = int(input("Informe o numero de linhas do jogo que deseja montar: "))
dimensao = int(input("Informe o numero de colunas do jogo que deseja montar: "))
# Criar um jogo dos 8 embaralhado
board = cria_jogo_dos_8(tamanho,dimensao)


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
print_board(board)


match algoritmo:
    case 1:
        inicio = time.time() # Tempo de inicio
        resolver_backtracking(board)
        fim = time.time() # Tempo de fim do algoritmo
        print(str(round((fim-inicio), 3)) + "Segundos")
    case 2:
        inicio = time.time()
        #busca em largura
        print("largura")
        fim = time.time()

    case 3:
         inicio = time.time()
        #busca em profundidade
         print("profundidade")
         fim = time.time()

    case 4:
        inicio = time.time()
        #busca ordenada
        print("ordenada")
        fim = time.time()

    case 5:
        inicio = time.time()
        #busca gulosa
        print("gulosa")
        fim = time.time()

    case 6:
        inicio = time.time()
        #busca A*
        print("A*")
        fim = time.time()

    case 7:
        inicio = time.time()
        #busca IDA*
        print("IDA*")
        fim = time.time()
