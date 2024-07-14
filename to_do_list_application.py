#Introduction
#In this project, you will apply your Python programming skills to create a functional To-Do List Application 
#from scratch. The objective of this project is to reinforce your understanding of Python syntax, data types, 
#control structures, functions, and error handling while building a practical and interactive application.

#Project Requirements

#User Interface (UI):
#Create a command-line interface (CLI) for the To-Do List Application.
#Display a welcoming message and a menu with the following options:
#        Welcome to the To-Do List App!

#        Menu:
#        1. Add a task
#        2. View tasks
#        3. Mark a task as complete
#        4. Delete a task
#        5. Quit

#To-Do List Features:
#Implement the following features for the To-Do List:
#Adding a task with a title (by default “Incomplete”).
#Viewing the list of tasks with their titles and statuses (e.g., "Incomplete" or "Complete").
#Marking a task as complete.
#Deleting a task.
#Quitting the application.

#User Interaction:
#Allow users to interact with the application by selecting menu options using input().
#Implement input validation to handle unexpected user input gracefully.


#Error Handling:
#Implement error handling using try, except, else, and finally blocks to handle potential issues.

#Code Organization:
#Organize your code into functions to promote modularity and readability.
#Use meaningful function names with appropriate comments and docstrings for clarity.

#Testing and Debugging:
#Thoroughly test your application to identify and fix any bugs.
#Consider edge cases, such as empty task lists or incorrect user input.

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

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to display.")
            return
        for i, task in enumerate(self.tasks, 1):
            status = "Completed" if task["completed"] else "Incomplete"
            print(f"{i}. {task['task']} - {status}")

    def mark_task_complete(self):
        self.view_tasks()
        try:
            task_num = int(input("Enter the number of the task to mark as complete: "))
            if 1 <= task_num <= len(self.tasks):
                self.tasks[task_num - 1]["completed"] = True
                print(f'Task "{self.tasks[task_num - 1]["task"]}" marked as complete.')
            else:
                print("Empty task number.")
        except ValueError:
            print("Please enter a valid number.")

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
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    app = ToDoListApp()
    app.run()



#Documentation:
#Include a README file that explains how to run the application and provides a brief overview of its features.
#Optional Features (Bonus):
#If you feel adventurous, you can add extra features like task priorities, due dates, or color-coding tasks based on their status.
#GitHub Repository:
#Create a GitHub repository for your project.
#Commit your code to the repository regularly.
#Include a link to your GitHub repository in your project documentation.
#Submission

#Submit your project, including all source code files and the README, to your instructor or designated platform.
#Project Tips

#Start by designing a simple user interface and plan the program's structure.
#Test your code frequently as you build each feature to ensure everything works as expected.
#Collaborate with fellow learners and seek help when needed. Remember, learning is a communal effort!
#By completing this project, you'll gain practical experience in Python programming and have a useful 
# To-Do List Application to help you stay organized in your own life.




