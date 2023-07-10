from jogo_dos_8 import cria_jogo_dos_8, print_board
from backtracking import resolver_backtracking
from largura import resolver_largura
from profundidade import resolver_profundidade
from ordenada import resolver_ordenada
from gulosa import resolver_gulosa
from aestrela import resolver_a_estrela
from idaestrela import resolver_ida_estrela
import time
import sys


sys.setrecursionlimit(1000)

# Inicializando a dimensao da matriz do board
tamanho = int(input("Informe o numero de linhas do jogo que deseja montar: "))
dimensao = int(
    input("Informe o numero de colunas do jogo que deseja montar: "))
# Criar um jogo dos 8 embaralhado
board = cria_jogo_dos_8(tamanho, dimensao)


# Escolhe algoritmo
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
        inicio = time.time()  # Tempo de inicio
        resolver_backtracking(board)
        fim = time.time()  # Tempo de fim do algoritmo
        print(str(round((fim-inicio), 3)) + "s")
    case 2:
        inicio = time.time()
        resolver_largura(board)
        fim = time.time()
        print(str(round((fim-inicio), 3)) + "s")

    case 3:
        max_depth = int(input("Digite qual a profundidade maxima que o codigo pode chegar: "))
        inicio = time.time()  # Tempo de inicio
        solucao = resolver_profundidade(board, max_depth)
        fim = time.time()  # Tempo de fim do algoritmo
        if not solucao:
            print("Nao foi encontrada uma solucao com a profundidade maxima de " + str(max_depth))
            print("Tente com uma profundidade de "+ (str(max_depth + 5 )))
        else:
            print(str(round((fim-inicio), 3)) + "s")

    case 4:
        inicio = time.time()
        resolver_ordenada(board)
        fim = time.time()
        print(str(round((fim-inicio), 3)) + "s")

    case 5:
        inicio = time.time()
        resolver_greed_search(board)
        fim = time.time()
        print(str(round((fim-inicio), 3)) + "s")

    case 6:
        inicio = time.time()
        resolver_a_estrela(board)
        fim = time.time()
        print(str(round((fim-inicio), 3)) + "s")

    case 7:
        inicio = time.time()
        resolver_ida_estrela(board)
        fim = time.time()
        print(str(round((fim-inicio), 3)) + "s")