import tkinter as tk

class TicTacToeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text="", width=10, height=5, command=lambda row=i, col=j: self.clicked(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def clicked(self, row, col):
        button = self.buttons[row][col]
        if button["text"] == "":
            button["text"] = "X"
        else:
            button["text"] = ""

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = TicTacToeGUI()
    app.run()
