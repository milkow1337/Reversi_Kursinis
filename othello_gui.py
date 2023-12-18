import tkinter as tk
from tkinter import messagebox


class OthelloGUI:
    def __init__(self, master, othello):
        self.master = master
        self.othello = othello
        self.buttons = [[None] * 8 for _ in range(8)]
        self.create_board()
        self.create_score_display()

    def create_board(self):
        for i in range(8):
            for j in range(8):
                self.buttons[i][j] = tk.Button(self.master, text='', width=4, height=2,
                                               command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)
        self.update_board()

    def create_score_display(self):
        score_label = tk.Label(self.master, text="Scores:")
        score_label.grid(row=8, column=0, columnspan=8)

        for player in ['X', 'O']:
            score_value = tk.StringVar()
            score_value.set(f"{player}: {self.othello.get_score(player)}")
            score_label = tk.Label(self.master, textvariable=score_value)
            score_label.grid(row=9, column=['X', 'O'].index(player), sticky='nsew')

    def update_board(self):
        for i in range(8):
            for j in range(8):
                if self.othello.is_valid_move(i, j):
                    self.buttons[i][j].config(text='', bg='light green')
                else:
                    self.buttons[i][j].config(text=self.othello.board[i][j],
                                              bg='white' if (i + j) % 2 == 0 else 'light gray')

    def make_move(self, row, col):
        self.othello.make_move(row, col)
        self.update_board()
        self.update_scores_display()
        if self.othello.is_game_over():
            self.show_game_over_message()

    def update_scores_display(self):
        for player in ['X', 'O']:
            score_value = tk.StringVar()
            score_value.set(f"{player}: {self.othello.get_score(player)}")
            score_label = tk.Label(self.master, textvariable=score_value)
            score_label.grid(row=9, column=['X', 'O'].index(player), sticky='nsew')

    def show_game_over_message(self):
        winner = self.othello.get_winner()
        result = f"Game Over! {'Tie' if winner == 'Tie' else f'{winner} wins'}."
        messagebox.showinfo("Game Over", result)
        self.master.destroy()
