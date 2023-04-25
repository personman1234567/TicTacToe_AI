import tkinter as tk
from TicTacToe import *
from minRiskClassifier import *

class TicTacToeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.player = "X"
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

        self.buttons = [[" " for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text="", width=10, height=5, command=lambda row=i, col=j: self.clicked(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

        self.nextTurnVal = tk.Label(self.root, text="X")
        self.nextTurnVal.grid(row=0, column=4)
        self.nextTurnLabel = tk.Label(self.root, text="Next Turn:")
        self.nextTurnLabel.grid(row=0, column=3)

        self.xRecVal = tk.Label(self.root, text="-")
        self.xRecVal.grid(row=1, column=4)
        self.xRecLabel = tk.Label(self.root, text="Recommended X:")
        self.xRecLabel.grid(row=1, column=3)


    def setPlayer(self, player):
        self.player = player

    def clicked(self, row, col):

        button = self.buttons[row][col]

        if self.board[row][col] != " ":
            self.player = " "

        self.board[row][col] = self.player

        if self.player == "X":
            button["text"] = "X"
            self.setTurnLabel("O")
            self.setPlayer("O")
        elif self.player == "O":
            button["text"] = "O"
            self.setTurnLabel("X")
            self.setPlayer("X")
        else:
            button["text"] = ""
            self.setPlayer(" ")

        self.updateXRec()

        winner = self.has_winner()
        if winner != None:
            self.setTurnLabel("Winner: " + winner)

        # Check if the board is full
        empty = self.has_empty()
        if empty == False:
            self.setTurnLabel("Draw!")

    def setTurnLabel(self, content):
        self.nextTurnVal["text"] = content

    def setXRecLabel(self, content):
        self.xRecVal["text"] = content

    def has_winner(self):
        # check rows for winner
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                return row[0]

        # check columns for winner
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != ' ':
                return self.board[0][col]

        # check diagonals for winner
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != ' ':
            return self.board[0][2]
        
    def has_empty(self):
        for row in self.board:
            for col in range(3):
                if row[col] == ' ':
                    return True
        return False
    
    def transformBoard(self):
        transformedBoard = list()

        for row in self.board:
            for col in range(3):
                if row[col] == "X":
                    transformedBoard.append(1)
                elif row[col] == "O":
                    transformedBoard.append(-1)
                else:
                    transformedBoard.append(0)
        return transformedBoard
    
    def updateXRec(self):
        board = self.transformBoard()
        if self.player == "X":
            player = 1
        elif self.player == "O":
            player = -1
        else:
            player = 0

        if self.player == "X":
            nextMove = getNextBestMove(board, player)

            move = nextMove[0]
            self.setXRecLabel(str(move))


    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = TicTacToeGUI()
    gui.run()
    # board = [
    #     [' ', ' ', ' '],
    #     [' ', ' ', ' '],
    #     [' ', ' ', ' ']
    # ]

    # player = 'X'
    # print_board_initial(board)
    # gameStarted = False
    # placementCount = 0
    # loop = True

    # while loop == True:
        # if gameStarted:
        #     print_board(board)
        #     print("\n")
        #     print("Player", player+"'s Turn")

        # if not gameStarted:
        #     gameStarted = True
        #     print("\nPlayer X's Turn")

        

        # columnInput = False
        # while not columnInput:  
        #     y = int(input('\nEnter Column Number: '))
        #     if(y == 1 or y == 2 or y == 3):
        #         y = y - 1
        #         columnInput = True
        #     else:
        #         print("\nInvalid Input: Select a valid column")

        # rowInput = False
        # while not rowInput:
        #     x = int(input('Enter Row Number: '))
        #     if(x == 1 or x == 2 or x == 3):
        #         x = x - 1
        #         rowInput = True
        #     else:
        #         print("\nInvalid Input: Select a valid row")

        # if not make_move(board, player, x, y, gui):
        #     print('Invalid move!')
        #     continue

        # winner = has_winner(board)

        # if winner:
        #     print_board(board)
        #     print("\n")
        #     print(winner, 'is the winner!!!\n')
        #     break
        # player = 'X' if player == 'O' else 'O'  #Switches the player symbol if move was valid, and there is no winner
        # placementCount += 1
        # if placementCount == 9:
        #     print("\nIt's a Draw!\n")
        #     loop = False
