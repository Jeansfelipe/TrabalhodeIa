from collections import deque
from jogo_dos_8 import print_board, move, check_win, remover_movimentos_invalidos

def resolver_backtracking(board):
    queue = deque([(board, [])])  # Fila de estados a serem explorados
    visited_states = set()  # Conjunto de estados visitados

    while queue:
        current_board, path = queue.popleft()

        # Verificar se o jogo está resolvido
        if check_win(current_board):
            print("Solução encontrada:")
            print_board(current_board)
            print("Caminho percorrido:")
            print(" -> ".join(path))
            print("Profundidade da solução encontrada:", len(path))
            print("Nós expandidos: ", len(queue)+ len(visited_states))
            print("Nós visitados: ", len(visited_states))
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

            queue.append((new_board, path + [movement]))

    print("Não foi possível encontrar uma solução.")
    return False






