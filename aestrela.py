from collections import deque
from jogo_dos_8 import print_board, move, check_win, remover_movimentos_invalidos


def resolver_a_estrela(board):
    goal_board = create_goal_board(len(board), len(board[0]))
    queue = [(board, [], out_of_place(board, goal_board))] # Fila de estados a serem explorados
    visited_states = set()  # Conjunto de estados visitados

    while queue:
        queue.sort(key=lambda x: x[2])
        current_board, path, weight = queue.pop(0)

        # Verificar se o jogo está resolvido
        if check_win(current_board):
            print("Solução encontrada:")
            print_board(current_board)
            print("Caminho percorrido:")
            print(" -> ".join(path))
            print("Nós expandidos:", len(queue)+ len(visited_states))
            print("Nós visitados:", len(visited_states))
            print("Custo do caminho: ", weight)
            return True

        # Verificar se o estado atual já foi visitado
        if tuple(map(tuple, current_board)) in visited_states:
            continue

        visited_states.add(tuple(map(tuple, current_board)))

        # Movimentos possíveis: W, S, A, D (cima, baixo, esquerda, direita)
        moves = ['W', 'S', 'A', 'D']
        movimentos = remover_movimentos_invalidos(moves, current_board)


        # Tentar cada movimento
        for movement in movimentos:
            new_board = [row[:] for row in current_board]  # Fazer uma cópia do tabuleiro

            # Executar o movimento
            move(new_board, movement)

            custo = count_manhattan(new_board) + out_of_place(new_board, goal_board)
            queue.append((new_board, path + [movement], custo))

    print("Não foi possível encontrar uma solução.")
    return False

def count_manhattan(board):
    size = len(board)
    dimensao = len(board[0])
    goal_board = create_goal_board(size,dimensao)  # Tabuleiro objetivo
    manhattan = 0

    for i in range(size):
        for j in range(len(board[i])):
            if board[i][j] != goal_board[i][j] and board[i][j] != 0:  # Verifica se a peça está fora do lugar
                value = board[i][j]
                goal_pos = find_goal_position(goal_board, value)
                manhattan += abs(i - goal_pos[0]) + abs(j - goal_pos[1])

    return manhattan

def out_of_place(board, value):
    count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != value:
                count = count+1
    return count

def create_goal_board(tamanho, dimensao):
    num_possiveis_valores = tamanho * dimensao
    valores = list(range(1, num_possiveis_valores)) + [0]
    goal_board = [valores[i:i+dimensao] for i in range(0, num_possiveis_valores, dimensao)]
    return goal_board

def find_goal_position(board, value):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == value:
                return (i, j)
