from jogo_dos_8 import print_board, move, check_win, remover_movimentos_invalidos

def resolver_ordenada(board):
    closed_set = set(map(tuple, board))  # Evita estados duplicados
    open_list = [(board, [], 0)]  # Lista de abertos

    while open_list:
        open_list.sort(key=lambda x: x[2])  # Ordena a lista de abertos com base no custo (distância de Manhattan)
        current_board, path, weight = open_list.pop(0)  # Pega o estado com o menor custo

        if check_win(current_board):
            print("Solução encontrada:")
            print_board(current_board)
            print("Caminho percorrido:")
            print(" -> ".join(path))
            print("Profundidade da solução encontrada:", len(path))
            print("Nós expandidos:", len(open_list)+ len(closed_set))
            print("Nós visitados:", len(closed_set))
            print("Custo do caminho: ", weight)
            return True

        moves = ['W', 'S', 'A', 'D']
        movimentos = remover_movimentos_invalidos(moves, current_board)

        for movement in movimentos:
            new_board = [row[:] for row in current_board]
            move(new_board, movement)
            new_board_tuple = tuple(map(tuple, new_board))

            if new_board_tuple not in closed_set:
                closed_set.add(new_board_tuple)
                somatoria  = count_manhattan(new_board)
                open_list.append((new_board, path + [movement], somatoria + weight))

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

def find_goal_position(board, value):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == value:
                return (i, j)

def create_goal_board(tamanho, dimensao):
    num_possiveis_valores = tamanho * dimensao
    valores = list(range(1, num_possiveis_valores)) + [0]
    goal_board = [valores[i:i+dimensao] for i in range(0, num_possiveis_valores, dimensao)]
    return goal_board