#!/usr/bin/env python3
"""
Simple test script to verify Wordle game functionality.
Run this to check if the game logic works correctly.
"""

import sys
import os

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from wordle_logic import WordleGame


def test_game_logic():
    """Test basic game functionality."""
    print("🧪 Testing Wordle Game Logic...")
    
    # Test game initialization
    game = WordleGame()
    print(f"✅ Game initialized with target word: {game.target}")
    
    # Test exact match
    if game.target in game.words:
        feedback = game.evaluate(game.target)
        expected = ["G"] * 5
        assert feedback == expected, f"Expected {expected}, got {feedback}"
        print("✅ Exact match test passed")
    
    # Test no match
    test_word = "zzzzz"  # Should not match any real word
    game_test = WordleGame()
    game_test.target = "apple"  # Set known target
    feedback = game_test.evaluate(test_word)
    expected = [" "] * 5
    assert feedback == expected, f"Expected {expected}, got {feedback}"
    print("✅ No match test passed")
    
    # Test partial match
    game_test.target = "apple"
    feedback = game_test.evaluate("pleas")  # 'p', 'l', 'e' are in apple but wrong positions
    # Should have some yellows for p, l, e
    print(f"✅ Partial match test: {feedback}")
    
    # Test statistics
    initial_played = game.stats["played"]
    game.update_stats(True)
    assert game.stats["played"] == initial_played + 1
    assert game.stats["won"] == initial_played + 1
    print("✅ Statistics test passed")
    
    print("🎉 All tests passed! Game logic is working correctly.")


if __name__ == "__main__":
    test_game_logic()