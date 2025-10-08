"""
Title: Wordle GUI Module
Author: Contributor
Difficulty: Advanced
Description: Graphical user interface for Wordle game using Tkinter.
             Provides interactive game board, input handling, and visual feedback.
"""

import tkinter as tk
from tkinter import messagebox
from typing import List, Optional
from wordle_logic import WordleGame

# Color mapping for game feedback
COLOR_MAP = {"G": "#6aaa64", "Y": "#c9b458", " ": "#787c7e"}


class WordleApp:
    """
    Graphical user interface for the Wordle game.
    
    This class creates and manages a Tkinter-based GUI for playing Wordle,
    including a visual game board, input field, and interactive feedback.
    
    Attributes:
        root: Main Tkinter window
        game: WordleGame instance for game logic
        current_row: Current row index for displaying guesses (0-5)
        tiles: 2D list of label widgets representing the game board
    """
    
    def __init__(self, root: tk.Tk) -> None:
        """
        Initialize the Wordle GUI application.
        
        Args:
            root: The main Tkinter window
        """
        self.root = root
        self.root.title("Wordle++ (Python GUI)")
        self.game = WordleGame()
        self.current_row: int = 0

        # Create 6x5 grid of tiles for the game board
        self.tiles: List[List[tk.Label]] = []
        for r in range(6):  # 6 attempts maximum
            row = []
            for c in range(5):  # 5 letters per word
                lbl = tk.Label(
                    root, 
                    text="", 
                    width=4, 
                    height=2,
                    font=("Helvetica", 24, "bold"),
                    bg="#121213", 
                    fg="white", 
                    relief="solid", 
                    bd=1
                )
                lbl.grid(row=r, column=c, padx=4, pady=4)
                row.append(lbl)
            self.tiles.append(row)

        # Create input field for typing guesses
        self.entry = tk.Entry(root, font=("Helvetica", 16))
        self.entry.grid(row=7, column=0, columnspan=5, pady=10)
        self.entry.bind("<Return>", self.submit_guess)
        self.entry.focus()  # Set focus to input field

    def submit_guess(self, event: Optional[tk.Event] = None) -> None:
        """
        Process a word guess when Enter is pressed.
        
        Validates the input, updates the game state, and checks for win/loss conditions.
        
        Args:
            event: Optional Tkinter event object (from key binding)
        """
        guess = self.entry.get().lower().strip()
        
        # Validate guess length
        if len(guess) != 5:
            messagebox.showwarning("Invalid Input", "Word must be exactly 5 letters.")
            return
            
        # Validate guess contains only letters
        if not guess.isalpha():
            messagebox.showwarning("Invalid Input", "Word must contain only letters.")
            return
            
        # Check if word is in the valid word list
        if guess not in self.game.words:
            messagebox.showwarning("Invalid Word", "Word not found in dictionary.")
            return

        # Process the guess
        feedback = self.game.evaluate(guess)
        self.display_guess(guess, feedback)
        self.entry.delete(0, tk.END)

        # Check win condition
        if guess == self.game.target:
            messagebox.showinfo(
                "🎉 Congratulations!", 
                f"You guessed it! The word was '{self.game.target.upper()}'\n"
                f"You solved it in {len(self.game.board)} attempt(s)!"
            )
            self.game.update_stats(True)
            self._show_play_again_dialog()
        # Check loss condition
        elif len(self.game.board) == 6:
            messagebox.showinfo(
                "Game Over", 
                f"The word was '{self.game.target.upper()}'\n"
                "Better luck next time!"
            )
            self.game.update_stats(False)
            self._show_play_again_dialog()

    def display_guess(self, guess: str, feedback: List[str]) -> None:
        """
        Update the game board to show the latest guess with color feedback.
        
        Args:
            guess: The guessed word
            feedback: List of feedback characters ('G', 'Y', or ' ')
        """
        for c in range(5):
            lbl = self.tiles[self.current_row][c]
            lbl.config(text=guess[c].upper(), bg=COLOR_MAP[feedback[c]])
        self.current_row += 1
    
    def _show_play_again_dialog(self) -> None:
        """
        Show statistics and ask if the player wants to play again.
        """
        stats = self.game.stats
        stats_msg = (
            f"Game Statistics:\n"
            f"Games Played: {stats['played']}\n"
            f"Games Won: {stats['won']}\n"
            f"Win Rate: {(stats['won']/stats['played']*100):.1f}%\n"
            f"Current Streak: {stats['streak']}\n"
            f"Best Streak: {stats['best']}"
        )
        
        play_again = messagebox.askyesno(
            "Game Statistics", 
            f"{stats_msg}\n\nWould you like to play again?"
        )
        
        if play_again:
            self._reset_game()
        else:
            self.root.destroy()
    
    def _reset_game(self) -> None:
        """
        Reset the game for a new round.
        """
        # Reset game state
        self.game = WordleGame()
        self.current_row = 0
        
        # Clear all tiles
        for row in self.tiles:
            for tile in row:
                tile.config(text="", bg="#121213")
        
        # Clear and focus input field
        self.entry.delete(0, tk.END)
        self.entry.focus()


if __name__ == "__main__":
    root = tk.Tk()
    app = WordleApp(root)
    root.mainloop()
