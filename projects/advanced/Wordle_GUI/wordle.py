"""
Title: Wordle GUI Game - Complete Implementation
Author: Contributor
Difficulty: Advanced
Description: A fully-featured Wordle game with graphical interface using Tkinter.
             Includes game logic, statistics tracking, and interactive GUI components.
"""

import tkinter as tk
from tkinter import messagebox
import random
import json
import os

# --- Settings ---
WORD_LEN = 5
MAX_ATTEMPTS = 6
WORD_LIST = [
    "apple","river","storm","plane","bring",
    "table","crane","peace","light","sound",
    "brave","flame","sword","track","sharp"
]

COLOR_MAP = {"G": "#6aaa64", "Y": "#c9b458", " ": "#787c7e"}
HARD_MODE = True
STATS_FILE = "stats.json"

# --- Wordle Logic ---
class WordleGame:
    """
    Core Wordle game logic and statistics management.
    
    This class handles word selection, guess evaluation, and persistent
    statistics tracking. It implements the standard Wordle rules:
    - 5-letter words
    - 6 maximum attempts
    - Color-coded feedback (Green=correct, Yellow=wrong position, Gray=not in word)
    
    Attributes:
        target (str): The secret word to guess
        board (list): List of (guess, feedback) tuples
        stats (dict): Game statistics (played, won, streak, best)
    """
    
    def __init__(self):
        self.target = random.choice(WORD_LIST)
        self.board = []
        self.stats = self.load_stats()

    def evaluate(self, guess):
        """
        Evaluate a guess against the target word and return color feedback.
        
        Args:
            guess (str): The 5-letter word guess
            
        Returns:
            list: Feedback list with 'G' (green), 'Y' (yellow), or ' ' (gray)
                 for each letter position
        """
        feedback = [" "] * WORD_LEN
        used = [False] * WORD_LEN

        # First pass: Mark exact matches (green)
        for i in range(WORD_LEN):
            if guess[i] == self.target[i]:
                feedback[i] = "G"
                used[i] = True

        # Second pass: Mark wrong position matches (yellow)
        for i in range(WORD_LEN):
            if feedback[i] == "G": 
                continue
            for j in range(WORD_LEN):
                if not used[j] and guess[i] == self.target[j]:
                    feedback[i] = "Y"
                    used[j] = True
                    break

        self.board.append((guess, feedback))
        return feedback

    def load_stats(self):
        """
        Load game statistics from JSON file.
        
        Returns:
            dict: Statistics dictionary with default values if file doesn't exist
        """
        if os.path.exists(STATS_FILE):
            with open(STATS_FILE) as f:
                return json.load(f)
        return {"played": 0, "won": 0, "streak": 0, "best": 0}

    def save_stats(self):
        """
        Save current statistics to JSON file.
        """
        with open(STATS_FILE, "w") as f:
            json.dump(self.stats, f)

    def update_stats(self, won):
        """
        Update game statistics after a game ends.
        
        Args:
            won (bool): True if the player won, False if they lost
        """
        self.stats["played"] += 1
        if won:
            self.stats["won"] += 1
            self.stats["streak"] += 1
            self.stats["best"] = max(self.stats["best"], self.stats["streak"])
        else:
            self.stats["streak"] = 0
        self.save_stats()

# --- GUI ---
class WordleApp:
    """
    Graphical user interface for the Wordle game using Tkinter.
    
    This class manages the visual components of the game including:
    - 6x5 grid of letter tiles
    - Input field for guesses
    - On-screen keyboard with color feedback
    - Game state management and user interactions
    
    Attributes:
        root: Main Tkinter window
        game: WordleGame instance for game logic
        current_row: Current row index for displaying guesses
        tiles: 2D list of label widgets for the game board
        keyboard_buttons: Dictionary mapping letters to keyboard buttons
    """
    
    def __init__(self, root):
        """Initialize the Wordle GUI application."""
        self.root = root
        self.root.title("Wordle++")
        self.game = WordleGame()
        self.current_row = 0

        # Create 6x5 grid of tiles for game board
        self.tiles = []
        for r in range(MAX_ATTEMPTS):
            row = []
            for c in range(WORD_LEN):
                lbl = tk.Label(root, text="", width=4, height=2,
                               font=("Helvetica", 24, "bold"),
                               bg="#121213", fg="white", relief="solid", bd=1)
                lbl.grid(row=r, column=c, padx=4, pady=4)
                row.append(lbl)
            self.tiles.append(row)

        # Create input field for typing guesses
        self.entry = tk.Entry(root, font=("Helvetica", 16))
        self.entry.grid(row=MAX_ATTEMPTS+1, column=0, columnspan=WORD_LEN, pady=10)
        self.entry.bind("<Return>", self.submit_guess)

        # Create on-screen keyboard
        self.keyboard_frame = tk.Frame(root)
        self.keyboard_frame.grid(row=MAX_ATTEMPTS+2, column=0, columnspan=WORD_LEN)
        self.keyboard_buttons = {}
        
        # Standard QWERTY keyboard layout
        for i, row_keys in enumerate(["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]):
            row_frame = tk.Frame(self.keyboard_frame)
            row_frame.pack()
            for k in row_keys:
                btn = tk.Button(row_frame, text=k, width=4, height=2,
                                command=lambda c=k: self.press_key(c))
                btn.pack(side="left", padx=1, pady=1)
                self.keyboard_buttons[k] = btn

    def press_key(self, char):
        """
        Handle on-screen keyboard button presses.
        
        Args:
            char (str): The character from the pressed keyboard button
        """
        current = self.entry.get()
        if len(current) < WORD_LEN:
            self.entry.insert(tk.END, char)

    def submit_guess(self, event=None):
        """
        Process a word guess when Enter is pressed or Submit is clicked.
        
        Args:
            event: Optional Tkinter event object (from key binding)
        """
        guess = self.entry.get().lower().strip()
        
        # Validate guess length
        if len(guess) != WORD_LEN:
            messagebox.showwarning("Invalid", f"Word must be {WORD_LEN} letters.")
            return
            
        # Validate guess is in word list
        if guess not in WORD_LIST:
            messagebox.showwarning("Invalid", "Word not in list.")
            return

        # Process the guess
        feedback = self.game.evaluate(guess)
        self.display_guess(guess, feedback)
        self.update_keyboard(guess, feedback)
        self.entry.delete(0, tk.END)
        self.current_row += 1

        # Check win condition
        if guess == self.game.target:
            messagebox.showinfo("🎉 Congrats!", f"You guessed it! ({self.game.target.upper()})")
            self.game.update_stats(True)
            self.show_stats()
            self.root.destroy()
        # Check loss condition
        elif self.current_row == MAX_ATTEMPTS:
            messagebox.showinfo("Game Over", f"The word was {self.game.target.upper()}")
            self.game.update_stats(False)
            self.show_stats()
            self.root.destroy()

    def display_guess(self, guess, feedback):
        """
        Update the game board to show the latest guess with color feedback.
        
        Args:
            guess (str): The guessed word
            feedback (list): List of feedback characters ('G', 'Y', or ' ')
        """
        for c in range(WORD_LEN):
            lbl = self.tiles[self.current_row][c]
            lbl.config(text=guess[c].upper(), bg=COLOR_MAP[feedback[c]])

    def update_keyboard(self, guess, feedback):
        """
        Update the on-screen keyboard colors based on letter feedback.
        
        Args:
            guess (str): The guessed word
            feedback (list): List of feedback characters ('G', 'Y', or ' ')
        """
        for i in range(WORD_LEN):
            c = guess[i].upper()
            btn = self.keyboard_buttons.get(c)
            if btn:
                # Green takes priority over other colors
                if feedback[i] == "G":
                    btn.config(bg=COLOR_MAP["G"])
                # Yellow only if not already green
                elif feedback[i] == "Y" and btn.cget("bg") != COLOR_MAP["G"]:
                    btn.config(bg=COLOR_MAP["Y"])
                # Gray only if not already green or yellow
                elif feedback[i] == " " and btn.cget("bg") not in (COLOR_MAP["G"], COLOR_MAP["Y"]):
                    btn.config(bg=COLOR_MAP[" "])

    def show_stats(self):
        """
        Display game statistics in the console.
        """
        s = self.game.stats
        msg = f"Played: {s['played']} | Won: {s['won']} | Streak: {s['streak']} | Best: {s['best']}"
        print(msg)


if __name__ == "__main__":
    root = tk.Tk()
    app = WordleApp(root)
    root.mainloop()
