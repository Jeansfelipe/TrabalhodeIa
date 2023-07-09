import random

# Função para criar o jogo dos 8 embaralhado
def cria_jogo_dos_8(tamanho, dimensao):
    num_possiveis_valores = tamanho * dimensao
    valores = list(range(1, num_possiveis_valores)) + [0]
    board = [valores[i:i+dimensao] for i in range(0, num_possiveis_valores, dimensao)]
    moves = ['W', 'S', 'A', 'D']
    for _ in range(100):
        random_move = random.choice(moves)
        move(board, random_move)
    return board

# Função para trocar as posições das peças
def move(board, move):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                row = i
                col = j

    if move == 'W' and row != 0:
        board[row][col], board[row-1][col] = board[row-1][col], board[row][col]
    elif move == 'S' and row != len(board)-1:
        board[row][col], board[row+1][col] = board[row+1][col], board[row][col]
    elif move == 'A' and col != 0:
        board[row][col], board[row][col-1] = board[row][col-1], board[row][col]
    elif move == 'D' and col != len(board[0])-1:
        board[row][col], board[row][col+1] = board[row][col+1], board[row][col]

# Função para imprimir o tabuleiro
def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=" ")
        print()

# Função para verificar se o jogador venceu
def check_win(board):
    #print(len(board), len(board[0]))
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i == len(board) - 1 and j == len(board[0]) - 1:
                if board[i][j] != 0:
                    return False
            else:
                if board[i][j] != i * len(board[0]) + j + 1:
                    return False

    return True