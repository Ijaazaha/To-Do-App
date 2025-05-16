import sys

todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"Added task: {task}")

def list_tasks():
    if not todo_list:
        print("No tasks found.")
    else:
        print("To-Do List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def delete_task(index):
    try:
        removed = todo_list.pop(index - 1)
        print(f"Deleted task: {removed}")
    except IndexError:
        print("Invalid task number.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python todo.py [add <task> | list | delete <task_number>]")
    elif sys.argv[1] == "add":
        add_task(" ".join(sys.argv[2:]))
    elif sys.argv[1] == "list":
        list_tasks()
    elif sys.argv[1] == "delete":
        if len(sys.argv) == 3 and sys.argv[2].isdigit():
            delete_task(int(sys.argv[2]))
        else:
            print("Please provide a valid task number to delete.")
    else:
        print("Unknown command.")
        print("Unknown command.")

