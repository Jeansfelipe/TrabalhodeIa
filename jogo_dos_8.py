import random
import sys

sys.setrecursionlimit(10**6)

# Função para criar o jogo dos 8 embaralhado
def cria_jogo_dos_8(tamanho, dimensao):
    num_possiveis_valores = tamanho * dimensao
    valores = list(range(1, num_possiveis_valores)) + [0]
    board = [valores[i:i+dimensao] for i in range(0, num_possiveis_valores, dimensao)]
    moves = ['W', 'S', 'A', 'D']
    for _ in range(50):
        random_move = random.choice(moves)
        move(board, random_move)
    return board

# Função para trocar as posições das peças
def move(board, move):
    # Encontra a posição do elemento vazio
    row, col = next((i, j) for i, row in enumerate(board) for j, val in enumerate(row) if val == 0)

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
    n_rows = len(board)
    n_cols = len(board[0])

    if board[n_rows - 1][n_cols - 1] != 0:
        return False

    expected_value = 1
    for i in range(n_rows):
        for j in range(n_cols):
            if i == n_rows - 1 and j == n_cols - 1:
                continue
            if board[i][j] != expected_value:
                return False
            expected_value += 1

    return True