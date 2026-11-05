
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

board = [['-'] * 3 for i in range(3)]

winner = '-'
tie = False 

while winner == '-' and not tie:
    # display the board 
    for row in range(3):
        for col in range(3): 
            print(board[row][col], end=' ')
        print()

    # Ask user to play - row and col (1 to 3)
    print(f"{current_palyer} PLAYS")
    row = int(input("Row: "))
    col = int(input("Col: "))

    # Check if valid and if cell is available
    if 1 <= row <= 3 and 1 <= col <= 3:
        # row = row - 1
        # col = col - 1
        row -= 1
        col -= 1
        if board[row][col] == '-': 
            board[row][col] = current_palyer

            # Check for winner
            # Check rows and columns
            for i in range(3):
                # Assume i indicates Row
                if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '-':
                    winner = board[i][0]
                    break
                # Assume i indicates Column
                if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '-':
                    winner = board[0][i]
                    break
            # Check diagonals
            if board[0][0] == board[1][1] == board[2][2] and board[1][1] != '-':
                winner = board[1][1]
                break
            if board[0][2] == board[1][1] == board[2][0] and board[1][1] != '-':
                winner = board[1][1]
                break

            # Check for tie
            if winner == '-':
                tie = True
                for r in range(3):
                    for c in range(3):
                        if board[r][c] == '-':
                            tie = False
                            break

            if winner != '-' or tie:
                continue 

            # Change player
            # if current_palyer == player_x:
            #     current_palyer = player_o
            # else: 
            #     current_palyer = player_x
            current_palyer = player_x if current_palyer == player_o else player_o
        else:
            print(f"Cell at {row},{col} is not empty")
    else:
        print(f"Invalid cell {row},{col}")


# display the board 
for row in range(3):
    for col in range(3): 
        print(board[row][col], end=' ')
    print()

if winner != '-':
    print(f"{winner} Wins!")
else: 
    print("It's a Tie.")