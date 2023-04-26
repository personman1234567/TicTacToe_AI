import tkinter as tk
from TicTacToe import *
from minRiskClassifier import *
import tkinter.font as tkFont

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
        self.round = 1

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

        nextMove = getNextBestMove([0,0,0,0,0,0,0,0,0], 1)
        move = nextMove[0]

        # Label and Value for Minimum Risk Classifier for X
        self.xRecVal = tk.Label(self.root, text=str(move))
        self.xRecVal.grid(row=1, column=4)
        self.xRecLabel = tk.Label(self.root, text="MinRisk Classifier for X:")
        self.xRecLabel.grid(row=1, column=3)

        # Label and Value for Game Status
        self.statusLabel = tk.Label(self.root, text="Round")
        self.statusLabel.grid(row=2, column=3)
        self.statusVal = tk.Label(self.root, text=self.round)
        self.statusVal.grid(row=2, column=4)


        self.mapLabel = tk.Label(self.root, text="Map: ")
        self.mapLabel.grid(row=3, column=0)
        self.mapVal = tk.Label(self.root, text="1|2|3\n4|5|6\n7|8|9")
        f = tkFont.Font(self.mapVal, self.mapVal.cget("font"))
        f.configure(underline = True)
        self.mapVal.configure(font=f)
        self.mapVal.grid(row=3, column=1)


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
            self.updateRoundDisplay()
        elif self.player == "O":
            button["text"] = "O"
            self.setTurnLabel("X")
            self.setPlayer("X")
            self.updateRoundDisplay()
        else:
            button["text"] = ""
            self.setPlayer(" ")

        self.updateXRec()

        winner = self.has_winner()
        if winner != None:
            self.updateWinnerDisplay(winner)
            # self.setTurnLabel("Winner: " + winner)

        # Check if the board is full
        empty = self.has_empty()
        if empty == False:
            self.setStatusLabel("Draw!")
            self.setStatusVal("")

    def setTurnLabel(self, content):
        self.nextTurnVal["text"] = content

    def setXRecLabel(self, content):
        self.xRecVal["text"] = content

    def setStatusLabel(self, content):
        self.statusLabel["text"] = content

    def setStatusVal(self, content):
        self.statusVal["text"] = content

    def setRound(self, round):
        self.round = round

    def updateRoundDisplay(self):
        self.setRound(self.round + 1)
        self.setStatusVal(self.round)

    def updateWinnerDisplay(self, winner):
        self.setStatusLabel("Winner: ")
        self.setStatusVal(str(winner))

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
