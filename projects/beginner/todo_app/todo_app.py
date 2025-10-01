"""
Title: Command-Line Todo Application
Author: Python-Basics-to-Advanced Contributors
Difficulty: Beginner
Description: A simple yet feature-rich command-line todo list manager
Date: October 2025

Features:
- Add, remove, and list tasks
- Mark tasks as complete/incomplete
- Save tasks to a file for persistence
- Search and filter tasks
- Priority levels and due dates
- Statistics and progress tracking
"""

import json
import os
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class Task:
    """Represents a single todo task."""
    
    def __init__(self, description: str, priority: str = "medium", due_date: Optional[str] = None):
        self.id = None  # Will be set by TodoApp
        self.description = description
        self.completed = False
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.completed_at = None
        self.priority = priority.lower()
        self.due_date = due_date
        
        # Validate priority
        if self.priority not in ["low", "medium", "high"]:
            self.priority = "medium"
    
    def mark_complete(self):
        """Mark the task as completed."""
        self.completed = True
        self.completed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def mark_incomplete(self):
        """Mark the task as incomplete."""
        self.completed = False
        self.completed_at = None
    
    def is_overdue(self) -> bool:
        """Check if the task is overdue."""
        if not self.due_date or self.completed:
            return False
        
        try:
            due = datetime.strptime(self.due_date, "%Y-%m-%d")
            return datetime.now() > due
        except ValueError:
            return False
    
    def days_until_due(self) -> Optional[int]:
        """Calculate days until due date."""
        if not self.due_date:
            return None
        
        try:
            due = datetime.strptime(self.due_date, "%Y-%m-%d")
            delta = due - datetime.now()
            return delta.days
        except ValueError:
            return None
    
    def to_dict(self) -> Dict:
        """Convert task to dictionary for JSON serialization."""
        return {
            "id": self.id,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at,
            "completed_at": self.completed_at,
            "priority": self.priority,
            "due_date": self.due_date
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Task':
        """Create task from dictionary."""
        task = cls(data["description"], data.get("priority", "medium"), data.get("due_date"))
        task.id = data.get("id")
        task.completed = data.get("completed", False)
        task.created_at = data.get("created_at", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        task.completed_at = data.get("completed_at")
        return task
    
    def __str__(self) -> str:
        """String representation of the task."""
        status = "✅" if self.completed else "❌"
        priority_symbols = {"low": "🟢", "medium": "🟡", "high": "🔴"}
        priority_symbol = priority_symbols.get(self.priority, "🟡")
        
        result = f"[{self.id:2}] {status} {priority_symbol} {self.description}"
        
        if self.due_date:
            days = self.days_until_due()
            if days is not None:
                if days < 0:
                    result += f" (⚠️  OVERDUE by {abs(days)} days)"
                elif days == 0:
                    result += f" (⚠️  DUE TODAY)"
                elif days <= 3:
                    result += f" (⏰ Due in {days} days)"
                else:
                    result += f" (📅 Due: {self.due_date})"
        
        return result

class TodoApp:
    """Main Todo Application class."""
    
    def __init__(self, filename: str = "todo_list.json"):
        self.filename = filename
        self.tasks: List[Task] = []
        self.next_id = 1
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    data = json.load(file)
                    self.tasks = [Task.from_dict(task_data) for task_data in data.get("tasks", [])]
                    self.next_id = data.get("next_id", 1)
                print(f"✅ Loaded {len(self.tasks)} tasks from {self.filename}")
            except (json.JSONDecodeError, FileNotFoundError):
                print(f"⚠️  Could not load tasks from {self.filename}. Starting fresh.")
                self.tasks = []
                self.next_id = 1
        else:
            print(f"📝 No existing todo file found. Starting fresh.")
    
    def save_tasks(self):
        """Save tasks to file."""
        try:
            data = {
                "tasks": [task.to_dict() for task in self.tasks],
                "next_id": self.next_id
            }
            with open(self.filename, 'w') as file:
                json.dump(data, file, indent=2)
            print(f"💾 Tasks saved to {self.filename}")
        except Exception as e:
            print(f"❌ Error saving tasks: {e}")
    
    def add_task(self, description: str, priority: str = "medium", due_date: Optional[str] = None):
        """Add a new task."""
        task = Task(description, priority, due_date)
        task.id = self.next_id
        self.tasks.append(task)
        self.next_id += 1
        print(f"✅ Task added: {task.description}")
        self.save_tasks()
    
    def remove_task(self, task_id: int) -> bool:
        """Remove a task by ID."""
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                removed_task = self.tasks.pop(i)
                print(f"🗑️  Task removed: {removed_task.description}")
                self.save_tasks()
                return True
        print(f"❌ Task with ID {task_id} not found.")
        return False
    
    def toggle_task(self, task_id: int) -> bool:
        """Toggle task completion status."""
        for task in self.tasks:
            if task.id == task_id:
                if task.completed:
                    task.mark_incomplete()
                    print(f"⬜ Task marked as incomplete: {task.description}")
                else:
                    task.mark_complete()
                    print(f"✅ Task marked as complete: {task.description}")
                self.save_tasks()
                return True
        print(f"❌ Task with ID {task_id} not found.")
        return False
    
    def list_tasks(self, filter_type: str = "all"):
        """List tasks with optional filtering."""
        if not self.tasks:
            print("📭 No tasks found. Add some tasks to get started!")
            return
        
        filtered_tasks = []
        
        if filter_type == "all":
            filtered_tasks = self.tasks
        elif filter_type == "pending":
            filtered_tasks = [task for task in self.tasks if not task.completed]
        elif filter_type == "completed":
            filtered_tasks = [task for task in self.tasks if task.completed]
        elif filter_type == "overdue":
            filtered_tasks = [task for task in self.tasks if task.is_overdue()]
        elif filter_type in ["high", "medium", "low"]:
            filtered_tasks = [task for task in self.tasks if task.priority == filter_type]
        
        if not filtered_tasks:
            print(f"📭 No {filter_type} tasks found.")
            return
        
        print(f"\n📋 {filter_type.upper()} TASKS:")
        print("-" * 60)
        for task in sorted(filtered_tasks, key=lambda t: (t.completed, t.priority != "high", t.priority != "medium")):
            print(task)
        print("-" * 60)
    
    def search_tasks(self, query: str):
        """Search tasks by description."""
        matching_tasks = [task for task in self.tasks if query.lower() in task.description.lower()]
        
        if not matching_tasks:
            print(f"🔍 No tasks found matching '{query}'")
            return
        
        print(f"\n🔍 SEARCH RESULTS for '{query}':")
        print("-" * 60)
        for task in matching_tasks:
            print(task)
        print("-" * 60)
    
    def show_statistics(self):
        """Show task statistics."""
        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for task in self.tasks if task.completed)
        pending_tasks = total_tasks - completed_tasks
        overdue_tasks = sum(1 for task in self.tasks if task.is_overdue())
        
        high_priority = sum(1 for task in self.tasks if task.priority == "high" and not task.completed)
        medium_priority = sum(1 for task in self.tasks if task.priority == "medium" and not task.completed)
        low_priority = sum(1 for task in self.tasks if task.priority == "low" and not task.completed)
        
        completion_rate = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
        
        print(f"\n📊 TASK STATISTICS:")
        print("-" * 40)
        print(f"Total Tasks:     {total_tasks}")
        print(f"Completed:       {completed_tasks}")
        print(f"Pending:         {pending_tasks}")
        print(f"Overdue:         {overdue_tasks}")
        print(f"Completion Rate: {completion_rate:.1f}%")
        print("\nPending by Priority:")
        print(f"  🔴 High:       {high_priority}")
        print(f"  🟡 Medium:     {medium_priority}")
        print(f"  🟢 Low:        {low_priority}")
        print("-" * 40)
    
    def clear_completed(self):
        """Remove all completed tasks."""
        initial_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task.completed]
        removed_count = initial_count - len(self.tasks)
        
        if removed_count > 0:
            print(f"🧹 Cleared {removed_count} completed tasks.")
            self.save_tasks()
        else:
            print("📭 No completed tasks to clear.")

def print_help():
    """Print help information."""
    print("""
📚 TODO APP COMMANDS:
    
Basic Commands:
    add <description> [priority] [due_date]  - Add a new task
    list [filter]                           - List tasks (all/pending/completed/overdue/high/medium/low)
    toggle <id>                            - Toggle task completion
    remove <id>                            - Remove a task
    search <query>                         - Search tasks
    
Management:
    stats                                  - Show statistics
    clear                                  - Clear completed tasks
    help                                   - Show this help
    quit/exit                              - Exit the application
    
Examples:
    add "Buy groceries" high 2025-10-15
    add "Write report" medium
    add "Call mom"
    list pending
    toggle 1
    remove 3
    search "groceries"
    
Priority levels: high, medium, low (default: medium)
Date format: YYYY-MM-DD
""")

def parse_add_command(args: List[str]) -> tuple:
    """Parse the add command arguments."""
    if not args:
        return None, None, None
    
    description = args[0]
    priority = "medium"
    due_date = None
    
    # Check for priority
    if len(args) > 1 and args[1].lower() in ["high", "medium", "low"]:
        priority = args[1].lower()
        
        # Check for due date
        if len(args) > 2:
            try:
                # Validate date format
                datetime.strptime(args[2], "%Y-%m-%d")
                due_date = args[2]
            except ValueError:
                print("⚠️  Invalid date format. Use YYYY-MM-DD")
                return None, None, None
    
    # Check if second argument is a date (no priority specified)
    elif len(args) > 1:
        try:
            datetime.strptime(args[1], "%Y-%m-%d")
            due_date = args[1]
        except ValueError:
            print("⚠️  Invalid priority or date format.")
            return None, None, None
    
    return description, priority, due_date

def main():
    """Main application loop."""
    print("🎯 Welcome to Todo App!")
    print("Type 'help' for commands or 'quit' to exit.")
    
    app = TodoApp()
    
    while True:
        try:
            command = input("\n📝 todo> ").strip().split()
            
            if not command:
                continue
            
            action = command[0].lower()
            args = command[1:] if len(command) > 1 else []
            
            if action in ["quit", "exit"]:
                print("👋 Goodbye! Your tasks have been saved.")
                break
            
            elif action == "help":
                print_help()
            
            elif action == "add":
                if not args:
                    print("❌ Please provide a task description.")
                    print("Usage: add <description> [priority] [due_date]")
                    continue
                
                description, priority, due_date = parse_add_command(args)
                if description:
                    app.add_task(description, priority, due_date)
            
            elif action == "list":
                filter_type = args[0] if args else "all"
                app.list_tasks(filter_type)
            
            elif action == "toggle":
                if not args:
                    print("❌ Please provide a task ID.")
                    print("Usage: toggle <id>")
                    continue
                
                try:
                    task_id = int(args[0])
                    app.toggle_task(task_id)
                except ValueError:
                    print("❌ Invalid task ID. Please provide a number.")
            
            elif action == "remove":
                if not args:
                    print("❌ Please provide a task ID.")
                    print("Usage: remove <id>")
                    continue
                
                try:
                    task_id = int(args[0])
                    app.remove_task(task_id)
                except ValueError:
                    print("❌ Invalid task ID. Please provide a number.")
            
            elif action == "search":
                if not args:
                    print("❌ Please provide a search query.")
                    print("Usage: search <query>")
                    continue
                
                query = " ".join(args)
                app.search_tasks(query)
            
            elif action == "stats":
                app.show_statistics()
            
            elif action == "clear":
                app.clear_completed()
            
            else:
                print(f"❌ Unknown command: {action}")
                print("Type 'help' for available commands.")
        
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Your tasks have been saved.")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()