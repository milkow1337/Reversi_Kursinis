import tkinter as tk
from othello_game import OthelloGame
from othello_gui import OthelloGUI

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Othello")
    othello_game = OthelloGame()
    othello_gui = OthelloGUI(root, othello_game)
    root.mainloop()