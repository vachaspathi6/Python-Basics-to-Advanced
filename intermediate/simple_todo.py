#!/usr/bin/env python3
"""
Simple CLI Todo app for Hacktoberfest contribution.
Stores tasks in a JSON file with features: add, list, done, remove, clear.
"""
import json
import argparse
from pathlib import Path
from datetime import datetime

DATA_FILE = Path("tasks.json")


def load_tasks() -> list:
    """
    Load and return the list of tasks from the JSON file.
    Returns an empty list if the file does not exist or is invalid.
    """
    if not DATA_FILE.exists():
        return []
    try:
        return json.loads(DATA_FILE.read_text())
    except json.JSONDecodeError:
        # Warn the user and reset tasks if JSON is invalid.
        print("Warning: tasks.json is corrupted or not valid JSON. Resetting tasks list.")
        return []


def save_tasks(tasks: list) -> None:
    """
    Save the list of tasks to the JSON file with pretty formatting.
    """
    DATA_FILE.write_text(json.dumps(tasks, indent=2, sort_keys=False))


def add_task(text: str) -> None:
    """
    Add a new task with the given text to the list.
    """
    tasks = load_tasks()
    tasks.append({
        "id": int(datetime.now().timestamp()),
        "text": text,
        "done": False,
        "created": datetime.now().isoformat()
    })
    save_tasks(tasks)
    print("Added:", text)


def list_tasks() -> None:
    """
    List all tasks with their status. Uncompleted tasks show [ ] and done tasks show [✓].
    """
    tasks = load_tasks()
    if not tasks:
        print('No tasks. Add one using: todo.py add "Buy milk"')
        return
    for i, t in enumerate(tasks, 1):
        status = "✓" if t.get("done") else " "
        print(f"{i}. [{status}] {t.get('text')} (id:{t.get('id')})")


def mark_done(index: int) -> None:
    """
    Mark the task at the given 1-based index as done.
    """
    tasks = load_tasks()
    if index < 1 or index > len(tasks):
        print("Invalid task number.")
        return
    tasks[index - 1]["done"] = True
    save_tasks(tasks)
    print("Marked done:", tasks[index - 1]["text"])


def remove_task(index: int) -> None:
    """
    Remove the task at the given 1-based index.
    """
    tasks = load_tasks()
    if index < 1 or index > len(tasks):
        print("Invalid task number.")
        return
    removed = tasks.pop(index - 1)
    save_tasks(tasks)
    print("Removed:", removed["text"])


def clear_tasks() -> None:
    """
    Clear all tasks.
    """
    save_tasks([])
    print("All tasks cleared.")


def parse_args() -> argparse.Namespace:
    """
    Parse command-line arguments and return the parsed namespace.
    """
    parser = argparse.ArgumentParser(prog="todo.py", description="Simple CLI todo app")
    subparsers = parser.add_subparsers(dest="cmd")

    # Add command
    sp_add = subparsers.add_parser("add", help="Add a new task")
    sp_add.add_argument("text", nargs="+", help="Task text")
    # List command
    sp_list = subparsers.add_parser("list", help="List all tasks")
    # Done command
    sp_done = subparsers.add_parser("done", help="Mark a task as done")
    sp_done.add_argument("number", type=int, help="Task index to mark as done (from list)")
    # Remove command
    sp_rm = subparsers.add_parser("remove", help="Remove a task")
    sp_rm.add_argument("number", type=int, help="Task index to remove (from list)")
    # Clear command
    sp_clear = subparsers.add_parser("clear", help="Remove all tasks")

    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.cmd == "add":
        add_task(" ".join(args.text))
    elif args.cmd == "list" or args.cmd is None:
        list_tasks()
    elif args.cmd == "done":
        mark_done(args.number)
    elif args.cmd == "remove":
        remove_task(args.number)
    elif args.cmd == "clear":
        clear_tasks()
    else:
        print("Unknown command. Use add/list/done/remove/clear")


if __name__ == "__main__":
    main()
