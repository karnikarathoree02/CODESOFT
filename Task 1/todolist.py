tasks = []

def show_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks):
            status = "✓" if task["done"] else "✗"
            print(f"{i+1}. {task['task']} [{status}]")

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task_name = input("Enter task: ")
        tasks.append({"task": task_name, "done": False})

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()
        task_no = int(input("Enter task number: "))
        tasks[task_no - 1]["done"] = True

    elif choice == "4":
        show_tasks()
        task_no = int(input("Enter task number: "))
        tasks.pop(task_no - 1)

    elif choice == "5":
        break

    else:
        print("Invalid choice!")
