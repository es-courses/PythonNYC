

def initialize_board() -> list[list[str]]:
    """ Initialize a 3x3 array with the dash caracter ('-') """
    board = [['-'] * 3 for i in range(3)]
    return board

def display_board(board):
    for row in range(3):
        for col in range(3): 
            print(board[row][col], end=' ')
        print()

def user_plays():
    print(f"{current_palyer} PLAYS")
    r = int(input("Row: "))
    c = int(input("Col: "))
    return r, c

def row_col_valid(row, col):
    if 1 <= row <= 3 and 1 <= col <= 3:
        return True
    else:
        return False

def user_to_bord_convert(row, col):
    return row-1, col-1


def is_empty_cell(cell):
    if cell == '-':
        return True
    else:
        return False

def change_player(current, px, po):
    return px if current == po else po
            


def get_winner(board):
    for i in range(3):
        # Assume i indicates Row
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '-':
            winner = board[i][0]
            return winner
        # Assume i indicates Column
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '-':
            winner = board[0][i]
            return winner
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[1][1] != '-':
        winner = board[1][1]
        return winner
    if board[0][2] == board[1][1] == board[2][0] and board[1][1] != '-':
        winner = board[1][1]
        return winner
    return None

def is_tie(board, winner):
    # Check for tie
    if winner is None:
        tie = True
        for r in range(3):
            for c in range(3):
                if board[r][c] == '-':
                    tie = False
                    return False
        return True
    else:
        return False

player_x = 'X'
player_o = 'O'
current_palyer = player_x

# Simple way to initialize 2D list, but there is a better one, see below
# board = [
#     ['-','-','-'],
#     ['-','-','-'],
#     ['-','-','-'],
# ]

# Next has an error ... 
# board = [['-'] * 3] * 3

board = initialize_board()

winner = None
tie = False 

while winner is None and not tie: 
    display_board(board)
    row, col = user_plays()

    if row_col_valid(row, col):
        row, col = user_to_bord_convert(row, col)

        if is_empty_cell(board[row][col]): 
            board[row][col] = current_palyer

            winner = get_winner(board)
            if winner is not None:
                break

            tie = is_tie(board, winner)
            if tie:
                break

            if winner is not None or tie:
                continue 

            current_palyer = change_player(current_palyer, player_x, player_o)
        else:
            print(f"Cell at {row},{col} is not empty")
    else:
        print(f"Invalid cell {row},{col}")

display_board(board)

if winner is not None:
    print(f"{winner} Wins!")
else: 
    print("It's a Tie.")