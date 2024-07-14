class ToDoListApp:
    def __init__(self):
        self.tasks = []

    def display_menu(self):
        print("\nWelcome to the To-do List app")
        print("\nMenu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as complete")
        print("4. Delete a task")
        print("5. Quit")

    def add_task(self):
        task = input("Enter the task: ")
        self.tasks.append({"task": task, "completed": False})
        print(f'Task "{task}" added.')
# Add a task. This feature allows you to add a new task to your to-do list. 
# When you select this option, you will be prompted to enter the task description.
    def view_tasks(self):
        if not self.tasks:
            print("No tasks to display.")
            return
        for i, task in enumerate(self.tasks, 1):
            status = "Completed" if task["completed"] else "Not completed"
            print(f"{i}. {task['task']} - {status}")
# View tasks. This option displays all the tasks in your to-do list with their status (completed or incomplete).
    def mark_task_complete(self):
        self.view_tasks()
        try:
            task_num = int(input("Enter the number of the task to mark as complete: "))
            if 1 <= task_num <= len(self.tasks):
                self.tasks[task_num - 1]["completed"] = True
                print(f'Task "{self.tasks[task_num - 1]["task"]}" marked as complete.')
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
# Mark a task as complete. This feature lets you mark a specific task as completed. You will need to enter the task number to mark it as complete.
    def delete_task(self):
        self.view_tasks()
        try:
            task_num = int(input("Enter the number of the task to delete: "))
            if 1 <= task_num <= len(self.tasks):
                deleted_task = self.tasks.pop(task_num - 1)
                print(f'Task "{deleted_task["task"]}" deleted.')
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
# Delete a task. This option allows you to delete a specific task from your to-do list. You will need to enter the task number to delete it.
    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.mark_task_complete()
            elif choice == '4':
                self.delete_task()
            elif choice == '5':
                print("Goodbye!")
                break
# Quit (Option). This option allows you to exit the application.
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    app = ToDoListApp()
    app.run()
