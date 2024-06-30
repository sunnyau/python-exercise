# In tic tac toe board, "" means empty, x means x and o means o

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def check_mate():
    # horizontal
    for i in range(3):
        if board[i][0] != " " and board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            return True
    # verital
    for j in range(3):
        if board[0][j] != " " and board[0][j] == board[1][j] and board[0][j] == board[2][j]:
            return True
    # diagonal
    if board[0][0] != " " and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return True
    if board[2][0] != " " and board[2][0] == board[1][1] and board[2][0] == board[0][2]:
        return True
    return False


def print_board():
    for i in range(3):
        print(board[i])
    print()


def check_end():
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True



def put( xo, i, j ):
    if i < 0 or i > 2 or j < 0 or j > 2 or ( xo != "o" and xo != "x" ):
        return False
    elif board[i][j] != " ":
        return False
    board[i][j] = xo
    return True

def switch( data ):
    if data == "x":
        return "o"
    else:
        return "x"


def play():
    chess = "x"
    while not check_mate() and not check_end():
        row_column = input(chess + " turns. Please enter row and column (e.g. 1 1 ): ").split()
        if len(row_column) == 2:
            if row_column[0].isdigit() and row_column[1].isdigit():
                if put( chess, int(row_column[0]), int(row_column[1])):
                    print_board()
                    if not check_mate():
                        chess = switch(chess)
    return chess

# main
print_board()
chess = play()
if check_end():
    print("draw")
else:
    print( chess + " win")
