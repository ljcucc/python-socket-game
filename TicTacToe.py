import tkinter as tk
import tkinter.messagebox
import time
from PIL import Image, ImageTk

WIDTH = 400
HEIGHT = 500
POSITION_X = (1920-WIDTH)//2
POSITION_Y = (1080-HEIGHT)//2
COLOR1 = "skyblue"
COLOR2 = "white"
COLOR3 = "darkblue"
COLOR4 = "red"
COLOR5 = "purple"
FONT1 = ("Arial", 40)
FONT2 = ("Arial", 20)
FONT3 = ("Arial", 16)
IMAGE_FOLDER_PATH = "C:\\TicTacToe\\image\\"

class TicTacToe:
    def __init__(self, master):
        self.root = master
        self.root.title("Manager")
        self.root.geometry(f"{WIDTH}x{HEIGHT}+{POSITION_X}+{POSITION_Y}")

        self.page = tk.Frame(self.root)
        self.page.place(width=WIDTH, height=HEIGHT)
        self.page['bg'] = COLOR1

        self.lbPlayer1 = tk.Label(self.page, font=FONT2, fg=COLOR3, text="Player1")
        self.lbPlayer1.place(x=10, y=10, width=120, height=40)

        self.lbP1Score = tk.Label(self.page, font=FONT3, fg=COLOR3, text="Score: 0")
        self.lbP1Score.place(x=10, y=60, width=120, height=40)

        self.lbPlayer2 = tk.Label(self.page, font=FONT2, fg=COLOR4, text="Player2")
        self.lbPlayer2.place(x=270, y=10, width=120, height=40)

        self.lbP2Score = tk.Label(self.page, font=FONT3, fg=COLOR4, text="Score: 0")
        self.lbP2Score.place(x=270, y=60, width=120, height=40)

        self.lbTurn = tk.Label(self.page, font=FONT3, fg=COLOR5, text="P1's turn")
        self.lbTurn.place(x=140, y=10, width=120, height=40)

        self.lbRound = tk.Label(self.page, font=FONT3, fg=COLOR5, text="Round 1")
        self.lbRound.place(x=140, y=60, width=120, height=40)
        
        self.bt1 = tk.Button(self.page, font=FONT1, command= lambda: self.press(1))
        self.bt2 = tk.Button(self.page, font=FONT1, command= lambda: self.press(2))
        self.bt3 = tk.Button(self.page, font=FONT1, command= lambda: self.press(3))
        self.bt4 = tk.Button(self.page, font=FONT1, command= lambda: self.press(4))
        self.bt5 = tk.Button(self.page, font=FONT1, command= lambda: self.press(5))
        self.bt6 = tk.Button(self.page, font=FONT1, command= lambda: self.press(6))
        self.bt7 = tk.Button(self.page, font=FONT1, command= lambda: self.press(7))
        self.bt8 = tk.Button(self.page, font=FONT1, command= lambda: self.press(8))
        self.bt9 = tk.Button(self.page, font=FONT1, command= lambda: self.press(9))
        self.buttons = {1:self.bt1, 2:self.bt2, 3:self.bt3, 4:self.bt4, 5:self.bt5, 6:self.bt6, 7:self.bt7, 8:self.bt8, 9:self.bt9}

        i = 0
        for btNum in self.buttons:
            x = i%3
            y = i//3
            self.buttons[btNum].place(x=10+x*130, y=110+y*130, width=120, height=120)
            i += 1

        self.board = [[0,0,0],[0,0,0],[0,0,0]]
        self.turn = 1
        self.round = 1

        self.p1Score = 0
        self.p2Score = 0

        self.root.bind("<Escape>", self.close_window)
    
    def press(self, btNum):

        if self.board[(btNum-1)//3][(btNum-1)%3] != 0:
            return
        if self.turn == 1:
            self.board[(btNum-1)//3][(btNum-1)%3] = 1
            self.buttons[btNum]['text'] = "O"
            self.buttons[btNum]['fg'] = COLOR3
        else:
            self.board[(btNum-1)//3][(btNum-1)%3] = 2
            self.buttons[btNum]['text'] = "X"
            self.buttons[btNum]['fg'] = COLOR4

        self.turn = self.turn % 2 + 1
        self.lbTurn['text'] = f"P{self.turn}'s turn"

        winner = self.check_win()
        if winner != 0:
            self.win(winner)
            self.restart()
            self.update_info()

        elif self.check_draw():
            self.draw()
            self.restart()
            self.update_info()

    def check_win(self):
        for i in range(3):
            if self.board[i][0] != 0 and self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
                return self.board[i][0]
            if self.board[0][i] != 0 and self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
                return self.board[0][i]
        if self.board[1][1] != 0:
            if (self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]) or (self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]):
                return self.board[1][1]
        return 0
        
    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return False
        return True

    def win(self, winner):
        tkinter.messagebox.showinfo("Game over", f"Game over!\nWinner: <Player{winner}>")
        if winner == 1:
            self.p1Score += 1
        else:
            self.p2Score += 1

    def draw(self):
        tkinter.messagebox.showinfo("Game over", f"Game over!\nIt's a draw!")
        self.p1Score += 1
        self.p2Score += 1

    def update_info(self):
        self.lbP1Score['text'] = f"Score: {self.p1Score}"
        self.lbP2Score['text'] = f"Score: {self.p2Score}"
        self.lbRound['text'] = f"Round {self.round}"

    def restart(self):
        self.board = [[0,0,0],[0,0,0],[0,0,0]]
        self.turn = self.round % 2 + 1
        self.lbTurn['text'] = f"P{self.turn}'s turn"
        for btNum in self.buttons:
            self.buttons[btNum]['text'] = ""
        self.round += 1

    def close_window(self, event):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    TicTacToe(root)
    root.mainloop()