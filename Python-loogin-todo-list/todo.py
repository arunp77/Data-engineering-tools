# todo.py

from logger import logger

class ToDoApp:
    def __init__(self):
        self.tasks = []
        logger.info("To-Do application started")

    def add_task(self, task):
        if task:
            self.tasks.append(task)
            logger.info(f"Task added: {task}")
        else:
            logger.warning("Empty task cannot be added")

    def complete_task(self, task_index):
        try:
            completed_task = self.tasks.pop(task_index)
            logger.info(f"Task completed: {completed_task}")
        except IndexError:
            logger.error(f"Task index {task_index} is out of range")

    def show_tasks(self):
        if not self.tasks:
            logger.info("No tasks to show")
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for idx, task in enumerate(self.tasks):
                print(f"{idx + 1}. {task}")
            logger.info(f"{len(self.tasks)} tasks shown")

def main():
    app = ToDoApp() 

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Show Tasks")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            app.add_task(task)
        elif choice == '2':
            task_index = int(input("Enter the task number to complete: ")) - 1
            app.complete_task(task_index)
        elif choice == '3':
            app.show_tasks()
        elif choice == '4':
            logger.info("Exiting the To-Do application")
            print("Goodbye!")
            break
        else:
            logger.warning(f"Invalid option selected: {choice}")
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
