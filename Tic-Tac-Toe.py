"""
Tic-Tac-Toe: Pavani vs Computer
Author: Pavani Naidu

A simple GUI Tic-Tac-Toe game using Python's Tkinter library.
Play as 'X' against the computer ('O'). The game highlights the winning combination,
handles draws, and allows restarting the game.
"""

import tkinter as tk
from tkinter import messagebox
import random

def check_winner():
    """
    Checks for a winner or a tie.
    Highlights the winning combination and displays a message.
    """
    global winner
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in win_combos:
        if (buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != ""):
            for idx in combo:
                buttons[idx].config(bg="yellow")
            winner_name = "Pavani" if buttons[combo[0]]["text"] == "X" else "Computer"
            messagebox.showinfo("Tic-Tac-Toe", f"Congratulations, {winner_name} wins the game!")
            winner = True
            return
    # Check for tie
    if all(btn["text"] != "" for btn in buttons) and not winner:
        messagebox.showinfo("Tic-Tac-Toe", "No winners this time—it's a draw!")
        winner = True

def user_move(index):
    """
    Handles the user's move.
    """
    global winner
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = "X"
        buttons[index].config(bg="pink")
        check_winner()
        if not winner:
            label.config(text="Computer's turn")
            root.after(500, computer_move)

def computer_move():
    """
    Handles the computer's move.
    """
    global winner
    empty_indices = [i for i, btn in enumerate(buttons) if btn["text"] == ""]
    if empty_indices and not winner:
        comp_choice = random.choice(empty_indices)
        buttons[comp_choice]["text"] = "O"
        buttons[comp_choice].config(bg="light green")
        check_winner()
        if not winner:
            label.config(text="Pavani's turn")

def reset_game():
    """
    Resets the game board for a new game.
    """
    global winner
    for btn in buttons:
        btn.config(text="", bg="light blue")
    winner = False
    label.config(text="Pavani's turn")

# --- Main Application Window ---
root = tk.Tk()
root.title("Tic-Tac-Toe: Pavani vs Computer")
root.resizable(False, False)

# --- Create Buttons for the Game Board ---
buttons = [
    tk.Button(
        root, text="", font=("Arial", 25, "bold"), width=7, height=2,
        bg="light blue", command=lambda i=i: user_move(i)
    ) for i in range(9)
]
for i, btn in enumerate(buttons):
    btn.grid(row=i // 3, column=i % 3, padx=2, pady=2)

# --- Game State Variables and Labels ---
winner = False
label = tk.Label(root, text="Pavani's turn", font=("Arial", 16, "bold"))
label.grid(row=3, column=0, columnspan=3, pady=(10, 0))

reset_btn = tk.Button(root, text="Restart", font=("Arial", 20), command=reset_game)
reset_btn.grid(row=4, column=0, columnspan=3, pady=10)

# --- Start the Application ---
if __name__ == "__main__":
    root.mainloop()
