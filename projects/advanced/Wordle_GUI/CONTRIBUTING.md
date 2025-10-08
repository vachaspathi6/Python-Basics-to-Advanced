# 🤝 Contributing to Wordle GUI

Thank you for your interest in contributing to the Wordle GUI project! This document provides guidelines for contributing to this specific project.

## 📋 Project Overview

This is an **Advanced** level Python project that implements a fully-featured Wordle game with:

- Graphical user interface using Tkinter
- Complete game logic with proper word evaluation
- Statistics tracking with persistent storage
- Modular code architecture
- Comprehensive documentation and type hints

## 🎯 How to Contribute

### 🔰 For Beginners

- Improve documentation and comments
- Add more words to the word list
- Fix typos in README or code comments
- Add simple features like keyboard shortcuts

### 🎯 For Intermediate Developers

- Enhance the GUI with better styling
- Add sound effects or animations
- Implement themes or color customization
- Add input validation improvements
- Create unit tests

### 🚀 For Advanced Developers

- Implement hard mode constraints
- Add multiplayer functionality
- Create word difficulty levels
- Optimize performance
- Add accessibility features
- Implement custom word lists

## 🛠️ Development Setup

1. **Fork and Clone**:

   ```bash
   git clone https://github.com/mystify7777/Python-Basics-to-Advanced.git
   cd Python-Basics-to-Advanced/projects/advanced/Wordle_GUI
   ```

2. **Test Current Implementation**:

   ```bash
   python test_game.py  # Run basic tests
   python wordle.py     # Test the main game
   ```

3. **Development Requirements**:
   - Python 3.6+
   - Tkinter (usually included)
   - Type checking: `mypy` (optional)
   - Formatting: `black` (optional)

## 📝 Code Standards

### Code Style

- Follow **PEP 8** guidelines
- Use **type hints** for all function parameters and returns
- Add **comprehensive docstrings** for all classes and methods
- Include **inline comments** for complex logic

### Example Code Structure

```python
"""
Title: Feature Description
Author: Your Name  
Difficulty: Beginner/Intermediate/Advanced
"""

def example_function(param: str, optional_param: int = 0) -> bool:
    """
    Brief description of what the function does.
    
    Args:
        param: Description of the parameter
        optional_param: Description with default value
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When input is invalid
    """
    # Implementation with clear comments
    pass
```

### File Organization

- `wordle.py`: All-in-one implementation
- `wordle_logic.py`: Core game logic only
- `wordle_gui.py`: GUI components only  
- `test_game.py`: Unit tests
- `README.md`: Project documentation
- `requirements.txt`: Dependencies

## 🧪 Testing Guidelines

### Before Submitting

- [ ] Run `python test_game.py` - all tests pass
- [ ] Test both `wordle.py` and `wordle_gui.py` 
- [ ] Verify statistics save/load correctly
- [ ] Check input validation works
- [ ] Test win/loss conditions
- [ ] Ensure code follows style guidelines

### Manual Testing Checklist

- [ ] Game starts without errors
- [ ] Can enter 5-letter words
- [ ] Invalid inputs show appropriate warnings
- [ ] Color feedback works correctly (Green/Yellow/Gray)
- [ ] Statistics update after games
- [ ] Game ends properly on win/loss
- [ ] Can play multiple rounds

## 🎨 Feature Ideas

### UI/UX Improvements

- Dark/light theme toggle
- Custom color schemes
- Better fonts and typography
- Animations for tile reveals
- Sound effects
- Keyboard shortcuts

### Gameplay Features

- Hard mode implementation
- Multiple difficulty levels
- Custom word lists
- Hint system
- Timer mode
- Daily challenges

### Technical Enhancements

- Better error handling
- Performance optimization
- Accessibility features
- Internationalization
- Database integration
- Web version

## 🐛 Bug Reports

When reporting bugs, include:

- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error messages (if any)
- Screenshots (if relevant)

## 📚 Resources

- [Python PEP 8 Style Guide](https://pep8.org/)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [Type Hints Guide](https://docs.python.org/3/library/typing.html)
- [Docstring Conventions](https://pep257.readthedocs.io/)

## 🏷️ Pull Request Process

1. **Create a descriptive branch name**: `feature/keyboard-shortcuts` or `fix/statistics-bug`
2. **Write clear commit messages**: `Add: keyboard shortcut support` or `Fix: statistics not saving correctly`
3. **Update documentation** if you add features
4. **Add tests** for new functionality
5. **Ensure all tests pass** before submitting

## 🎃 Hacktoberfest 2025

This project welcomes Hacktoberfest contributions! Valid contributions include:

- Bug fixes
- Feature additions
- Documentation improvements
- Code quality enhancements
- Test coverage improvements

---

**Happy Contributing! 🎯**

For questions, open an issue or start a discussion. We're here to help!
