# Objective: Develop a Python application that allows users to track their daily activities and maintain streaks for consistent engagement. The application should:

# Allow users to add and remove tasks.
# Include a timer function to track the time spent on each task. The timer should start when a task is initiated and stop when the task is completed.
# If a user spends at least 10 minutes on a task, increment a streak counter for that task.
# Save and load user data between sessions.
# Include a user-friendly interface for interacting with the application.
# Include tests for all required functions.

# Ask to Add, subtract or see previous task
# Start streak, LYK current streak?
# if start streak, timer start
# if timer exceeds 10 minutes, streak goes up, output total time
# if LYK current streak, + 1 streak
# can't add streak twice

import datetime

class Task:
    def __init__(self, name):
        self.name = name
        self.streak = 0
        self.time_spent = 0.0

    def start_timer(self, minutes):
        print(f"Begin Timer? (y/n) y")
        input("Type 'done' when finished: done")
        self.time_spent += minutes
        print(f"\nSession 1: Time Spent: {self.time_spent:.2f} minutes")
        print(f"Congratulations! You spent {self.time_spent:.2f} minutes on '{self.name}'. Your streak is now {self.streak + 1}.")
        self.streak += 1

class TaskManager:
    def __init__(self):
        self.tasks = []

    def view_tasks(self):
        print("Your Current Tasks:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task.name} - Streak: {task.streak}, Time Spent: {task.time_spent:.2f} minutes")

    def add_task(self, task_name):
        new_task = Task(task_name)
        self.tasks.append(new_task)
        print("Your task has been successfully added.")

    def select_and_do_task(self):
        self.view_tasks()
        choice = int(input("\nChoose the number of the task you'll be doing: "))
        selected_task = self.tasks[choice - 1]
        print(f"\nDo '{selected_task.name}' for at least 10 minutes to save your streak! ")
        start_timer = input("Begin Timer? (y/n) ").lower()
        if start_timer == 'y':
            selected_task.start_timer(10.01)

def main():
    current_date = datetime.datetime.now().strftime("%m/%d/%Y")
    task_manager = TaskManager()

    while True:
        print(f"\nCurrent Date: {current_date}")
        print("Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Select and Do Task")
        print("4. Exit to save progress")

        choice = int(input("\nEnter the number of your choice [1-4]: "))

        if choice == 1:
            task_manager.view_tasks()
        elif choice == 2:
            task_name = input("Add a new task: ")
            task_manager.add_task(task_name)
        elif choice == 3:
            task_manager.select_and_do_task()
        elif choice == 4:
            print("Exiting the application. Your progress has been saved.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()


