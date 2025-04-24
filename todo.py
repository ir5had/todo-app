import json
import os

tasks = []


def load_tasks():
    global tasks
    if os.path.exists("tasks.json"):
        try:
            with open("tasks.json", "r") as file:
                tasks = json.load(file)
        except json.JSONDecodeError:
            print("⚠️ Error: tasks.json is corrupted. Starting with an empty task list.")
            tasks = []
    else:
        tasks = []


def save_tasks():
    try:
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)
    except Exception as e:
        print(f"⚠️ Error saving tasks: {e}")


def add_task():
    description = input("Enter the task description: ").strip()
    if not description:
        print("⚠️ Task description cannot be empty.")
        return

    priority = input("Enter priority (High/Medium/Low): ").strip().capitalize()
    if priority not in ["High", "Medium", "Low"]:
        print("⚠️ Invalid priority. Defaulting to Medium.")
        priority = "Medium"

    task = {
        "description": description,
        "priority": priority,
        "completed": False
    }
    tasks.append(task)
    print(f'✅ Task "{description}" added with {priority} priority.')
    save_tasks()


def view_tasks():
    if not tasks:
        print("📝 No tasks available.")
        return

    print("\n=== Your Tasks ===")
    for index, task in enumerate(tasks, 1):
        status = "✔️ Done" if task["completed"] else "⏳ Pending"
        print(f"{index}. {task['description']} | Priority: {task['priority']} | Status: {status}")


def delete_task():
    view_tasks()
    if not tasks:
        return

    try:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"🗑️ Task '{removed_task['description']}' deleted.")
            save_tasks()
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")


def mark_complete():
    view_tasks()
    if not tasks:
        return

    try:
        index = int(input("Enter the task number to mark as complete: ")) - 1
        if 0 <= index < len(tasks):
            if tasks[index]["completed"]:
                print("⚠️ Task is already marked as complete.")
            else:
                tasks[index]["completed"] = True
                print(f"✔️ Task '{tasks[index]['description']}' marked as complete.")
                save_tasks()
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")


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
                print("⚠️ Invalid priority. Keeping current priority.")

            print(f"✅ Task updated: {tasks[index]['description']} | Priority: {tasks[index]['priority']}")
            save_tasks()
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")


def sort_tasks():
    priority_order = {"High": 1, "Medium": 2, "Low": 3}
    global tasks
    tasks.sort(key=lambda task: priority_order[task["priority"]])
    print("✅ Tasks sorted by priority (High > Medium > Low).")
    save_tasks()


load_tasks()