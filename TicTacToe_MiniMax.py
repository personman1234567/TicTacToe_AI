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

def make_move(board, player, x, y):
    if board[x][y] != ' ':
        return False
    board[x][y] = player
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

def evaluate(board, player, otherPlayer):
    winner = has_winner(board)
    if winner == player:
        return 1
    elif winner == otherPlayer:
        return -1
    else:
        return 0

def minimax(board, depth, is_maximizing, player):
    if player == 'X':
        otherPlayer = 'O'
    else:
        otherPlayer = 'X'

    if has_winner(board):
        return evaluate(board, player, otherPlayer)
    
    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = player
                    score = minimax(board, depth + 1, False, player)    #Calls recursivly
                    board[i][j] = ' '
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = otherPlayer
                    score = minimax(board, depth + 1, True, player)     #Calls recursivly
                    board[i][j] = ' '
                    best_score = min(best_score, score)
        return best_score

def get_best_move_minimax(board, player):
    best_score = -float('inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = player
                score = minimax(board, 0, False, player)    #Use minimax function to determine best move
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

def main():
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

        if player == 'X':               #If its x players turn, find best move first, then display best move. Then take the inputs
            x, y = get_best_move_minimax(board)
            print("The most optimal move for X is: (Column:{}, Row:{})".format(y+1, x+1))

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

        if not make_move(board, player, x, y):
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