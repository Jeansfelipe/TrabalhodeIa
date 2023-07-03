from collections import deque
from jogo_dos_8 import print_board, move

# Função para verificar se o jogador venceu
def check_win(board,dimensao):
    count = 1
    for i in range(dimensao):
        for j in range(dimensao):
            if board[i][j] != count % (dimensao * dimensao):
                return False
            count += 1
    return True

from collections import deque

def resolver_backtracking(board, dimensao):
    queue = deque([(board, [])])  # Fila de estados a serem explorados
    visited_states = set()  # Conjunto de estados visitados

    while queue:
        current_board, path = queue.popleft()

        # Verificar se o jogo está resolvido
        if check_win(current_board, dimensao):
            print("Solução encontrada:")
            print_board(current_board, dimensao)
            print("Caminho percorrido:")
            print(" -> ".join(path))
            return True

        # Verificar se o estado atual já foi visitado
        if tuple(map(tuple, current_board)) in visited_states:
            continue

        visited_states.add(tuple(map(tuple, current_board)))

        # Movimentos possíveis: W, S, A, D (cima, baixo, esquerda, direita)
        moves = ['W', 'S', 'A', 'D']

        # Tentar cada movimento
        for movement in moves:
            new_board = [row[:] for row in current_board]  # Fazer uma cópia do tabuleiro

            # Executar o movimento
            move(new_board, movement, dimensao)

            queue.append((new_board, path + [movement]))

    print("Não foi possível encontrar uma solução.")
    return False






