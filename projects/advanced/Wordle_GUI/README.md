# 🎮 Wordle GUI - Python Implementation

A fully-featured graphical Wordle game built with Python's Tkinter. Experience the popular word-guessing game with an intuitive interface, statistics tracking, and authentic gameplay mechanics.

## 📋 Table of Contents

- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [Game Rules](#-game-rules)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)

## ✨ Features

### Core Gameplay

- **Classic Wordle Experience**: 6 attempts to guess a 5-letter word
- **Visual Feedback**: Color-coded tiles (Green = correct, Yellow = wrong position, Gray = not in word)
- **Interactive GUI**: Clean, modern interface built with Tkinter
- **On-screen Keyboard**: Visual keyboard with color feedback
- **Statistics Tracking**: Persistent game statistics (games played, win rate, streaks)

### Technical Features

- **Modular Design**: Separated game logic from GUI components
- **Data Persistence**: JSON-based statistics storage
- **Input Validation**: Robust word length and dictionary checking
- **Cross-platform**: Works on Windows, macOS, and Linux

## 🔧 Prerequisites

- Python 3.6 or higher
- Tkinter (included with most Python installations)

## 💻 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/username/Python-Basics-to-Advanced.git
   cd Python-Basics-to-Advanced/projects/advanced/Wordle_GUI
   ```

2. **Verify Python installation**:

   ```bash
   python --version
   ```

3. **Install dependencies** (if needed):

   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

### Quick Start

```bash
python wordle.py
```

### Alternative (Modular Version)

```bash
python wordle_gui.py
```

### Game Instructions

1. Enter a 5-letter word in the text field
2. Press Enter or click Submit
3. Watch the tile colors for feedback:
   - 🟩 **Green**: Correct letter in correct position
   - 🟨 **Yellow**: Correct letter in wrong position  
   - ⬜ **Gray**: Letter not in the word
4. Use the feedback to make your next guess
5. Win by guessing the word in 6 attempts or fewer!

## 🎯 Game Rules

- **Word Length**: All guesses must be exactly 5 letters
- **Attempts**: You have 6 chances to guess the correct word
- **Valid Words**: Only words from the built-in dictionary are accepted
- **Feedback System**: 
  - Each letter is evaluated independently
  - If a word contains duplicate letters, feedback prioritizes exact matches first
- **Win Condition**: Guess the exact word within 6 attempts
- **Statistics**: Games played, wins, current streak, and best streak are tracked

## 📁 Project Structure

```bash
Wordle_GUI/
├── wordle.py          # Main game file (all-in-one version)
├── wordle_gui.py      # GUI components (modular version)
├── wordle_logic.py    # Game logic (modular version)
├── stats.json         # Persistent statistics storage
├── requirements.txt   # Python dependencies
└── README.md         # Project documentation
```

### File Descriptions

- **`wordle.py`**: Complete game implementation in a single file
- **`wordle_gui.py`**: GUI interface and user interaction handling
- **`wordle_logic.py`**: Core game mechanics and word evaluation
- **`stats.json`**: JSON file storing player statistics
- **`requirements.txt`**: List of required Python packages

## 🎮 Screenshots

When you run the game, you'll see:

- A 6x5 grid of letter tiles
- An input field for typing guesses
- An on-screen keyboard with color feedback
- Win/loss message boxes with statistics

## 🛠️ Development

### Code Structure

```python
"""
Title: Wordle GUI Game
Author: [Your Name]
Difficulty: Advanced
Description: A complete Wordle implementation with GUI interface
"""
```

### Key Components

- **WordleGame Class**: Handles game logic, word evaluation, and statistics
- **WordleApp Class**: Manages GUI components and user interactions
- **Color System**: Visual feedback using hex color codes
- **Statistics System**: JSON-based persistent data storage

## 🧪 Testing

Run the game and test:

- Valid 5-letter word inputs
- Invalid inputs (too short/long, not in dictionary)
- Win conditions (correct guess)
- Loss conditions (6 incorrect guesses)
- Statistics persistence across games

## 🤝 Contributing

Contributions are welcome! Please read the [contributing guidelines](../../../CONTRIBUTING.md) before submitting pull requests.

### Ideas for Enhancement

- Expanded word dictionary
- Difficulty levels
- Hint system
- Sound effects
- Theme customization
- Multiplayer mode

## 📝 License

This project is part of the Python-Basics-to-Advanced repository and follows the same license terms.

## 🎃 Hacktoberfest 2025

This project is participating in Hacktoberfest 2025! Feel free to contribute improvements, bug fixes, or new features.

---

**Happy Word Guessing! 🎯**
