eimport json
import os

# File to store tasks persistently
TASKS_FILE = 'tasks.json'

def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, task_desc):
    """Add a new task to the list."""
    tasks.append({'task': task_desc, 'done': False})
    save_tasks(tasks)

def delete_task(tasks, index):
    """Delete a task by its index."""
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
    else:
        print("Invalid task number.")

def mark_done(tasks, index):
    """Mark a task as done by its index."""
    if 0 <= index < len(tasks):
        tasks[index]['done'] = True
        save_tasks(tasks)
    else:
        print("Invalid task number.")

def list_tasks(tasks):
    """Display all tasks with their status."""
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks):
        status = "Done" if task['done'] else "Pending"
        print(f"{i + 1}. [{status}] {task['task']}")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application - Codeveda Technology")
        print("1. List tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Mark task as done")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            list_tasks(tasks)
        elif choice == '2':
            task_desc = input("Enter task description: ")
            add_task(tasks, task_desc)
        elif choice == '3':
            list_tasks(tasks)
            try:
                index = int(input("Enter task number to delete: ")) - 1
                delete_task(tasks, index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            list_tasks(tasks)
            try:
                index = int(input("Enter task number to mark as done: ")) - 1
                mark_done(tasks, index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

