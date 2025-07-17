import json
import os
from datetime import datetime

TASK_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def create_task():
    task = {
        "name": input("Task name: "),
        "description": input("Description: "),
        "due_date": input("Due date (YYYY-MM-DD): "),
        "priority": input("Priority (Low/Medium/High): "),
        "category": input("Category (e.g., Work, Personal): "),
        "status": "To Do",
        "notes": input("Additional notes (optional): ")
    }
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task created successfully.")

def list_tasks(filter_by=None, value=None):
    tasks = load_tasks()
    if filter_by:
        tasks = [t for t in tasks if t[filter_by] == value]
    tasks = sorted(tasks, key=lambda x: x["priority"], reverse=True)
    for idx, task in enumerate(tasks, 1):
        print(f"\n[{idx}] {task['name']} - {task['status']} (Due: {task['due_date']})")
        print(f"    Priority: {task['priority']}, Category: {task['category']}")
        print(f"    Description: {task['description']}")
        if task.get("notes"):
            print(f"    Notes: {task['notes']}")

def update_task():
    tasks = load_tasks()
    list_tasks()
    index = int(input("Enter task number to update: ")) - 1
    if 0 <= index < len(tasks):
        task = tasks[index]
        task['status'] = input(f"New status (To Do/In Progress/Completed): ")
        save_tasks(tasks)
        print("Task updated.")
    else:
        print("Invalid task number.")

def delete_task():
    tasks = load_tasks()
    list_tasks()
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        del tasks[index]
        save_tasks(tasks)
        print("Task deleted.")
    else:
        print("Invalid task number.")

def menu():
    while True:
        print("\n--- Task Manager ---")
        print("1. Create Task")
        print("2. List All Tasks")
        print("3. List Tasks by Category")
        print("4. List Tasks by Status")
        print("5. Update Task Status")
        print("6. Delete Task")
        print("7. Exit")
        choice = input("Select option: ")
        if choice == "1":
            create_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            category = input("Enter category: ")
            list_tasks(filter_by="category", value=category)
        elif choice == "4":
            status = input("Enter status (To Do/In Progress/Completed): ")
            list_tasks(filter_by="status", value=status)
        elif choice == "5":
            update_task()
        elif choice == "6":
            delete_task()
        elif choice == "7":
            print("Exiting.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    menu()
