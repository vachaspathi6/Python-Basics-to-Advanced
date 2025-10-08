"""
Title: Wordle Game Logic Module
Author: Contributor
Difficulty: Advanced
Description: Core game logic for Wordle implementation including word evaluation,
             statistics tracking, and game state management.
"""

import random
import json
import os
from typing import List, Tuple, Dict, Any

# Game constants
WORD_LEN: int = 5
MAX_ATTEMPTS: int = 6
STATS_FILE: str = "stats.json"


class WordleGame:
    """
    Core Wordle game logic and statistics management.
    
    This class implements the standard Wordle gameplay mechanics:
    - Random word selection from predefined list
    - Guess evaluation with color-coded feedback
    - Persistent statistics tracking
    - Hard mode support (future enhancement)
    
    Attributes:
        words (List[str]): Available words for the game
        target (str): The secret word to guess
        hard_mode (bool): Whether hard mode is enabled
        board (List[Tuple[str, List[str]]]): Game history of guesses and feedback
        stats (Dict[str, int]): Game statistics
    """
    
    def __init__(self, hard_mode: bool = True) -> None:
        """
        Initialize a new Wordle game.
        
        Args:
            hard_mode: Enable hard mode constraints (currently not implemented)
        """
        self.words: List[str] = [
            "apple", "river", "storm", "plane", "bring",
            "table", "crane", "peace", "light", "sound",
            "brave", "flame", "sword", "track", "sharp"
        ]
        self.target: str = random.choice(self.words)
        self.hard_mode: bool = hard_mode
        self.board: List[Tuple[str, List[str]]] = []  # list of (guess, feedback)
        self.stats: Dict[str, int] = self.load_stats()

    def evaluate(self, guess: str) -> List[str]:
        """
        Evaluate a guess against the target word and return color feedback.
        
        Uses standard Wordle rules:
        - 'G' (Green): Correct letter in correct position
        - 'Y' (Yellow): Correct letter in wrong position
        - ' ' (Gray): Letter not in the word
        
        Args:
            guess: The 5-letter word guess (should be lowercase)
            
        Returns:
            List of feedback characters for each letter position
        """
        feedback: List[str] = [" "] * WORD_LEN
        used: List[bool] = [False] * WORD_LEN

        # First pass: Mark exact position matches (green)
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

    def load_stats(self) -> Dict[str, int]:
        """
        Load game statistics from JSON file.
        
        Returns:
            Dictionary with game statistics or default values if file doesn't exist
        """
        if os.path.exists(STATS_FILE):
            try:
                with open(STATS_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                # Return defaults if file is corrupted or missing
                pass
        return {"played": 0, "won": 0, "streak": 0, "best": 0}

    def save_stats(self) -> None:
        """
        Save current statistics to JSON file.
        """
        try:
            with open(STATS_FILE, 'w', encoding='utf-8') as f:
                json.dump(self.stats, f, indent=2)
        except IOError as e:
            print(f"Warning: Could not save statistics: {e}")

    def update_stats(self, won: bool) -> None:
        """
        Update game statistics after a game ends.
        
        Args:
            won: True if the player won, False if they lost
        """
        self.stats["played"] += 1
        if won:
            self.stats["won"] += 1
            self.stats["streak"] += 1
            self.stats["best"] = max(self.stats["best"], self.stats["streak"])
        else:
            self.stats["streak"] = 0
        self.save_stats()
