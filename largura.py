from collections import deque
from jogo_dos_8 import print_board, move, check_win

from collections import deque

def resolver_largura(board):
    opened_list = [(board, [])]
    closed_list = []
    path = []

    while len(opened_list) > 0:
        current_board, path = opened_list.pop(0) # Pega o primeiro elemento da lista e coloca nos vertices abertos
        closed_list.append(current_board) #Pega o ultimo elemento da lista e coloca nos vertices fechados

        if check_win(current_board):
            print("Solução encontrada:")
            print_board(current_board)
            print("Caminho percorrido:")
            print(" ->".join(path))

            print("Profundidade da solução encontrada:", len(path))

            print("Nós expandidos: ", len(opened_list)+ len(closed_list))
            print("Nós visitados: ", len(closed_list))

            return True

        moves = ['W', 'S', 'A', 'D']

        for movement in moves:
            new_board = [row[:] for row in current_board]

            move(new_board, movement)

            if new_board not in closed_list and [new_board, path + [movement]] not in opened_list:
                opened_list.append([new_board, path + [movement]])
        

