from todo import add_task, view_tasks, delete_task, mark_complete, edit_task, sort_tasks

def show_menu():
    print('\n=== TO-DO APP ===')
    print('1. View Tasks')
    print('2. Add Task')
    print('3. Delete Task')
    print('4. Mark Task as complete')
    print('5. Edit Task')
    print('6. Sort Tasks by Priority')
    print('7. Exit')

def main():
    while True:
        show_menu()
        choice = input('Enter your choice (1-7): ')

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            mark_complete()
        elif choice == '5':
            edit_task()
        elif choice == '6':
            sort_tasks()
        elif choice == '7':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 5.')

if __name__ == "__main__":
    main()