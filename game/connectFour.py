import random

def inputPlayer(letter):
    # define qual letra para cada jogador retorna [w, b] or [b, w]
    if letter == 'w':
        return ['w', 'b']
    else:
        return ['b', 'w']

def askForFirstPlayer():
    #perguntar ao jogador quem é que deve jogar primeiro, as opções
    #podem ser por exemplo "white", "black" ou "random" e retorna o valor relacionado
    valid = False
    while not valid:
        piece = input("Queres ser w, b or r? ")
        if piece == "w" or piece == "b":
            return piece
        elif piece == "r":
            m = random.randint(0, 1)
            return "w" if m == 0 else "b"

def testMoveValidity(board, col):
    # testa se a jogada é válida se a casa esta vazia e qual a posição esta vazia
    # retorna a posição que esta vazia ou false
    for i in range(6):
        if board[5 - i][col] == "-":
            return 5 - i
    return False

def testMove(board, col):

    if col > 6 or col < 0:
        print("Fora das margens")
        return False

    position = testMoveValidity(board, col)

    if not isinstance(position, int):
        print("Coluna não disponível")
        return False

    return position

def move(board, turn, col, line):
    board[line][col] = turn

def askForNextMove(board, turn):
    while True:
        try:
            move_col = int(input("Em qual coluna? "))
        except ValueError:
            print("Tente inteiros.")
            continue

        move = testMove(board, move_col)
        if isinstance(move, bool):
            print("A jogada não é válida. Tente novamente.")
        else:
            return (turn, move_col, move)

def winner(board):

    for row in range(6):
        for col in range(7):

            #horizontal
            if col <= 3:
                if (board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] and board[row][col] != '-'):
                    return board[row][col]

            #vertical
            if row <= 2:
                if (board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] and board[row][col] != '-'):
                    return board[row][col]

            #diagonal
            if (col <= 3 and row <= 2):
                if (board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3] and board[row][col] != '-'):
                    return board[row][col]

            #diagonal
            if (col <= 3 and row >= 3):
                if (board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3] and board[row][col] != '-'):
                    return board[row][col]

    return False

def availableMoveAi(board):
    # retorna uma lista com movimentos possiveis para a IA
    acc = []
    for i in range(7):
        position = testMoveValidity(board, i)
        if isinstance(position, int):
            acc.append((i, position))
    return acc