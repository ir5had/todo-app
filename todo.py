import json
import os
from colorama import init, Fore, Style

# Initialize colorama for Windows
init()

tasks = []


def load_tasks():
    global tasks
    if os.path.exists("tasks.json"):
        try:
            with open("tasks.json", "r") as file:
                tasks = json.load(file)
        except json.JSONDecodeError:
            print(f"{Fore.RED}⚠️ Error: tasks.json is corrupted. Starting with an empty task list.{Style.RESET_ALL}")
            tasks = []
    else:
        tasks = []


def save_tasks():
    try:
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)
    except Exception as e:
        print(f"{Fore.RED}⚠️ Error saving tasks: {e}{Style.RESET_ALL}")


def add_task():
    description = input("Enter the task description: ").strip()
    if not description:
        print(f"{Fore.YELLOW}⚠️ Task description cannot be empty.{Style.RESET_ALL}")
        return

    priority = input("Enter priority (High/Medium/Low): ").strip().capitalize()
    if priority not in ["High", "Medium", "Low"]:
        print(f"{Fore.YELLOW}⚠️ Invalid priority. Defaulting to Medium.{Style.RESET_ALL}")
        priority = "Medium"

    task = {
        "description": description,
        "priority": priority,
        "completed": False
    }
    tasks.append(task)
    print(f"{Fore.GREEN}✅ Task \"{description}\" added with {priority} priority.{Style.RESET_ALL}")
    save_tasks()


def view_tasks():
    if not tasks:
        print(f"{Fore.YELLOW}📝 No tasks available.{Style.RESET_ALL}")
        return

    print(f"\n{Fore.CYAN}=== Your Tasks ==={Style.RESET_ALL}")
    print(f"{'No.':<4} {'Description':<30} {'Priority':<10} {'Status':<10}")
    print("-" * 60)
    for index, task in enumerate(tasks, 1):
        status = "✔️ Done" if task["completed"] else "⏳ Pending"
        print(f"{index:<4} {task['description'][:28]:<30} {task['priority']:<10} {status:<10}")


def delete_task():
    view_tasks()
    if not tasks:
        return

    try:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"{Fore.GREEN}🗑️ Task '{removed_task['description']}' deleted.{Style.RESET_ALL}")
            save_tasks()
        else:
            print(f"{Fore.YELLOW}⚠️ Invalid task number.{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.YELLOW}⚠️ Please enter a valid number.{Style.RESET_ALL}")


def mark_complete():
    view_tasks()
    if not tasks:
        return

    try:
        index = int(input("Enter the task number to mark as complete: ")) - 1
        if 0 <= index < len(tasks):
            if tasks[index]["completed"]:
                print(f"{Fore.YELLOW}⚠️ Task is already marked as complete.{Style.RESET_ALL}")
            else:
                tasks[index]["completed"] = True
                print(f"{Fore.GREEN}✔️ Task '{tasks[index]['description']}' marked as complete.{Style.RESET_ALL}")
                save_tasks()
        else:
            print(f"{Fore.YELLOW}⚠️ Invalid task number.{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.YELLOW}⚠️ Please enter a valid number.{Style.RESET_ALL}")


def edit_task():
    view_tasks()
    if not tasks:
        return

    try:
        index = int(input("Enter the task number to edit: ")) - 1
        if 0 <= index < len(tasks):
            print(f"Editing Task: {tasks[index]['description']} | Priority: {tasks[index]['priority']}")
            new_description = input("Enter new description (or press Enter to keep current): ").strip()
            if new_description:
                tasks[index]["description"] = new_description

            new_priority = input(
                "Enter new priority (High/Medium/Low, or press Enter to keep current): ").strip().capitalize()
            if new_priority and new_priority in ["High", "Medium", "Low"]:
                tasks[index]["priority"] = new_priority
            elif new_priority:
                print(f"{Fore.YELLOW}⚠️ Invalid priority. Keeping current priority.{Style.RESET_ALL}")

            print(
                f"{Fore.GREEN}✅ Task updated: {tasks[index]['description']} | Priority: {tasks[index]['priority']}{Style.RESET_ALL}")
            save_tasks()
        else:
            print(f"{Fore.YELLOW}⚠️ Invalid task number.{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.YELLOW}⚠️ Please enter a valid number.{Style.RESET_ALL}")


def sort_tasks():
    priority_order = {"High": 1, "Medium": 2, "Low": 3}
    global tasks
    tasks.sort(key=lambda task: priority_order[task["priority"]])
    print(f"{Fore.GREEN}✅ Tasks sorted by priority (High > Medium > Low).{Style.RESET_ALL}")
    save_tasks()


def filter_tasks():
    if not tasks:
        print(f"{Fore.YELLOW}📝 No tasks available.{Style.RESET_ALL}")
        return

    print(f"\n{Fore.CYAN}Filter Tasks:{Style.RESET_ALL}")
    print("1. Show Completed Tasks")
    print("2. Show Pending Tasks")
    print("3. Show All Tasks")
    choice = input("Enter your choice (1-3): ").strip()

    filtered_tasks = tasks
    if choice == "1":
        filtered_tasks = [task for task in tasks if task["completed"]]
    elif choice == "2":
        filtered_tasks = [task for task in tasks if not task["completed"]]
    elif choice == "3":
        pass  # Show all tasks
    else:
        print(f"{Fore.YELLOW}⚠️ Invalid choice. Showing all tasks.{Style.RESET_ALL}")

    if not filtered_tasks:
        print(f"{Fore.YELLOW}📝 No tasks match the filter.{Style.RESET_ALL}")
        return

    print(f"\n{Fore.CYAN}=== Filtered Tasks ==={Style.RESET_ALL}")
    print(f"{'No.':<4} {'Description':<30} {'Priority':<10} {'Status':<10}")
    print("-" * 60)
    for index, task in enumerate(filtered_tasks, 1):
        status = "✔️ Done" if task["completed"] else "⏳ Pending"
        print(f"{index:<4} {task['description'][:28]:<30} {task['priority']:<10} {status:<10}")


load_tasks()