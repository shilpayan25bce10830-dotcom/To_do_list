# Simple To-Do List Manager using Python

tasks = []   # list to store tasks

def add_task():
    task = input("Enter a new task: ").strip()
    tasks.append(task)
    print(f"Task '{task}' added successfully!\n")

def view_tasks():
    if not tasks:
        print("No tasks added yet.\n")
        return
    print("\n----- Your Tasks -----")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print("----------------------\n")

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            print(f"Task '{removed}' deleted successfully!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def mark_task_completed():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to mark completed: "))
        if 1 <= num <= len(tasks):
            tasks[num-1] = tasks[num-1] + " (Completed)"
            print("Task marked as completed!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    while True:
        print("=== TO-DO LIST MENU ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_task_completed()
        elif choice == "5":
            print("Exiting To-Do List...")
            break
        else:
            print("Invalid choice. Try again.\n")


main()