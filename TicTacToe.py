from gui import TicTacToeGUI

def print_board(board):
    print("\n\n----------------------------------------------\n\n")
    print("   1   2   3")
    for i in range(3):
        print(i+1, ' ' + board[i][0] + ' | ' + board[i][1] + ' | ' + board[i][2])
        if i != 2:
            print('  ---+---+---')

def print_board_initial(board):
    print("   1   2   3")
    for i in range(3):
        print(i+1, ' ' + board[i][0] + ' | ' + board[i][1] + ' | ' + board[i][2])
        if i != 2:
            print('  ---+---+---')

def make_move(board, player, x, y, gui):
    if board[x][y] != ' ':
        return False
    board[x][y] = player
    gui.setPlayer(player)
    gui.clicked(x, y, player)
    if player == "X":
        gui.setLabelOne("Turn: O")
    else:
        gui.setLabelOne("Turn: X")
    return True

def has_winner(board):
    # check rows for winner
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    # check columns for winner
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    # check diagonals for winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    # If no winner yet, then main loop continues
    return None

def has_empty(board):
    for row in board:
        for col in range(3):
            if row[col] == "":
                return True
            
    return False

def main():
    gui = TicTacToeGUI()
    # gui.run()

    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

    player = 'X'
    print_board_initial(board)
    gameStarted = False
    placementCount = 0
    loop = True

    while loop == True:
        if gameStarted:
            print_board(board)
            print("\n")
            print("Player", player+"'s Turn")

        if not gameStarted:
            gameStarted = True
            print("\nPlayer X's Turn")

        columnInput = False
        while not columnInput:  
            y = int(input('\nEnter Column Number: '))
            if(y == 1 or y == 2 or y == 3):
                y = y - 1
                columnInput = True
            else:
                print("\nInvalid Input: Select a valid column")

        rowInput = False
        while not rowInput:
            x = int(input('Enter Row Number: '))
            if(x == 1 or x == 2 or x == 3):
                x = x - 1
                rowInput = True
            else:
                print("\nInvalid Input: Select a valid row")

        if not make_move(board, player, x, y, gui):
            print('Invalid move!')
            continue

        winner = has_winner(board)

        if winner:
            print_board(board)
            print("\n")
            print(winner, 'is the winner!!!\n')
            break
        player = 'X' if player == 'O' else 'O'  #Switches the player symbol if move was valid, and there is no winner
        placementCount += 1
        if placementCount == 9:
            print("\nIt's a Draw!\n")
            loop = False

# main()