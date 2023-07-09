from jogo_dos_8 import print_board, move, check_win


def resolver_profundidade(board, max_depth):
    closed_set = set(map(tuple, board))  # Evita estados duplicados
    stack = [(board, [])]

    while stack:
        current_board, path = stack.pop()

        if check_win(current_board):
            print("Solução encontrada:")
            print_board(current_board)
            print("Caminho percorrido:")
            print(" -> ".join(path))
            print("Profundidade da solução encontrada:", len(path))
            print("Nós visitados:", len(closed_set))
            return True

        if len(path) >= max_depth:
            continue  # Limite de profundidade atingido, pular para a próxima iteração

        moves = ['W', 'S', 'A', 'D']

        for movement in moves:
            new_board = [row[:] for row in current_board]
            move(new_board, movement)
            new_board_tuple = tuple(map(tuple, new_board))

            if new_board_tuple not in closed_set:
                closed_set.add(new_board_tuple)
                stack.append((new_board, path + [movement]))
    return False
