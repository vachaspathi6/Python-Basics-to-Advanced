# 📝 Command-Line Todo Application

A feature-rich command-line todo list manager built with Python. Perfect for beginners to learn file I/O, JSON handling, object-oriented programming, and command-line interfaces.

## ✨ Features

- ✅ Add, remove, and list tasks
- 🎯 Set task priorities (high, medium, low)
- 📅 Set due dates for tasks
- ⚠️ Overdue task detection
- 🔍 Search functionality
- 📊 Statistics and progress tracking
- 💾 Automatic saving to JSON file
- 🎨 Colorful console output with emojis

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

### Installation

1. Download the `todo_app.py` file
2. Make sure you have Python installed
3. Run the application:

```bash
python todo_app.py
```

## 📚 Usage Guide

### Basic Commands

```bash
# Add a simple task
add "Buy groceries"

# Add a task with priority
add "Finish project" high

# Add a task with priority and due date
add "Call dentist" medium 2025-10-15

# List all tasks
list

# List only pending tasks
list pending

# List only completed tasks
list completed

# List high priority tasks
list high

# Mark task as complete/incomplete (toggle)
toggle 1

# Remove a task
remove 2

# Search for tasks
search "groceries"

# Show statistics
stats

# Clear all completed tasks
clear

# Show help
help

# Exit the application
quit
```

### Advanced Features

#### Priority Levels
- `high` 🔴 - Urgent tasks
- `medium` 🟡 - Normal tasks (default)
- `low` 🟢 - Low priority tasks

#### Due Dates
- Format: `YYYY-MM-DD` (e.g., 2025-10-15)
- Overdue tasks are highlighted with ⚠️
- Tasks due today are marked with ⏰
- Tasks due within 3 days show countdown

#### Filtering Options
- `all` - Show all tasks
- `pending` - Show incomplete tasks
- `completed` - Show completed tasks
- `overdue` - Show overdue tasks
- `high/medium/low` - Show tasks by priority

## 📖 Example Session

```
🎯 Welcome to Todo App!
Type 'help' for commands or 'quit' to exit.

📝 todo> add "Learn Python programming" high 2025-10-20
✅ Task added: Learn Python programming

📝 todo> add "Buy groceries" medium 2025-10-02
✅ Task added: Buy groceries

📝 todo> add "Clean room" low
✅ Task added: Clean room

📝 todo> list
📋 ALL TASKS:
------------------------------------------------------------
[ 1] ❌ 🔴 Learn Python programming (📅 Due: 2025-10-20)
[ 2] ❌ 🟡 Buy groceries (⏰ Due in 1 days)
[ 3] ❌ 🟢 Clean room
------------------------------------------------------------

📝 todo> toggle 2
✅ Task marked as complete: Buy groceries

📝 todo> stats
📊 TASK STATISTICS:
----------------------------------------
Total Tasks:     3
Completed:       1
Pending:         2
Overdue:         0
Completion Rate: 33.3%

Pending by Priority:
  🔴 High:       1
  🟡 Medium:     0
  🟢 Low:        1
----------------------------------------
```

## 🏗️ Code Structure

### Classes

#### `Task`
Represents a single todo item with properties:
- `id`: Unique identifier
- `description`: Task description
- `completed`: Completion status
- `priority`: Priority level (high/medium/low)
- `due_date`: Optional due date
- `created_at`: Creation timestamp
- `completed_at`: Completion timestamp

#### `TodoApp`
Main application class that manages:
- Task collection
- File I/O operations
- Command processing
- Data persistence

### Key Methods

- `add_task()`: Add new tasks with optional priority and due date
- `toggle_task()`: Mark tasks as complete/incomplete
- `list_tasks()`: Display tasks with filtering options
- `search_tasks()`: Find tasks by description
- `show_statistics()`: Display progress and statistics
- `load_tasks()` / `save_tasks()`: Data persistence

## 📁 File Storage

Tasks are automatically saved to `todo_list.json` in the same directory as the script. The JSON structure includes:

```json
{
  "tasks": [
    {
      "id": 1,
      "description": "Learn Python",
      "completed": false,
      "created_at": "2025-10-01 10:30:00",
      "completed_at": null,
      "priority": "high",
      "due_date": "2025-10-15"
    }
  ],
  "next_id": 2
}
```

## 🎓 Learning Objectives

This project demonstrates:

### Python Concepts
- **Object-Oriented Programming**: Classes, methods, properties
- **File I/O**: Reading from and writing to files
- **JSON Handling**: Serialization and deserialization
- **Date/Time Operations**: Working with datetime module
- **Exception Handling**: Try/catch blocks for error management
- **List Comprehensions**: Filtering and transforming data
- **Type Hints**: Modern Python type annotations

### Programming Practices
- **Data Persistence**: Saving application state
- **User Interface Design**: Command-line interaction
- **Input Validation**: Checking user input
- **Error Handling**: Graceful error management
- **Code Organization**: Separating concerns into classes/methods

## 🔧 Customization Ideas

Want to extend the application? Try adding:

1. **Categories/Tags**: Group tasks by category
2. **Recurring Tasks**: Tasks that repeat daily/weekly
3. **Time Tracking**: Track time spent on tasks
4. **Export Options**: Export to CSV or other formats
5. **Multiple Lists**: Support for different todo lists
6. **Reminders**: System notifications for due tasks
7. **Collaboration**: Share tasks with others
8. **GUI Version**: Create a graphical interface

## 🐛 Troubleshooting

### Common Issues

**File Permission Error**
- Make sure you have write permissions in the directory
- Try running from a different directory

**JSON Decode Error**
- The todo_list.json file might be corrupted
- Delete the file to start fresh (you'll lose existing tasks)

**Date Format Error**
- Use YYYY-MM-DD format (e.g., 2025-10-15)
- Make sure the date is valid

### Getting Help

If you encounter issues:
1. Check the error message for specific details
2. Ensure you're using Python 3.6+
3. Verify file permissions in your directory
4. Try the `help` command for usage instructions

## 🤝 Contributing

This is a learning project! Feel free to:
- Add new features
- Fix bugs
- Improve documentation
- Add tests
- Enhance the user interface

## 📜 License

This project is part of the Python-Basics-to-Advanced repository and is available under the MIT License.

---

**Happy task managing! 🎯**