import sys
"""
Name: Janielle Jackson
UID: 117595598
Due Date: May 15 2024
Title: Final Project - TerpTu-Do
"""

class ToDoList:
    """
    ToDoList class that takes care of the application itself. Includes different functions that allows the user to
    add/remove a task, update, mark a task completed, return a list of the tasks inputted by the user, and clearing the list.
    """
    def __init__(self):
        """
        An initialized empty list
        """
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def remove_task(self, index):
        """
        Function works to remove tasks in the application. 
        Pop() method is used to remove an element if the amount of tasks is less than or equal to.
        """
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            raise IndexError("Task index out of range")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
        else:
            raise IndexError("Task index out of range")

    def update_task(self, index, description):
        if 0 <= index < len(self.tasks):
            self.tasks[index].description = description
        else:
            raise IndexError("Task index out of range")

    def list_tasks(self):
        return [str(task) for task in self.tasks]

    def clear_tasks(self):
        self.tasks.clear()

class Task:
    """
    Task class has several functions that assists the functionality of the task typed by the User. 
    Consist of the user being able to mark complete and the status of the task if it is completed or uncompleted.
    """
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        """
        Function sets the default value of True to allow the user to Mark Completed to their task.
        """
        self.completed = True

    def __str__(self):
        """
        Function works to either put a "✓" if completed or "✗" not completed. 
        """
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description}"


def main():
    """
    Main function that puts everything together. 
    """
    todo = ToDoList()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Update Task")
        print("4. Mark Task Completed")
        print("5. List Tasks")
        print("6. Clear Tasks")
        print("0. Exit")
        chosen_option = input("Enter your choice: ")

        try:
            if chosen_option == "1":
                description = input("Enter description of task: ")
                todo.add_task(description)
            elif chosen_option == "2":
                index = int(input("Enter task number to remove: ")) - 1
                todo.remove_task(index)
            elif chosen_option == "3":
                index = int(input("Enter task number to update: ")) - 1
                description = input("Enter new task description: ")
                todo.update_task(index, description)
            elif chosen_option == "4":
                index = int(input("Enter task number to mark as completed: ")) - 1
                todo.mark_task_completed(index)
            elif chosen_option == "5":
                print("\nTo-Do List:")
                for i, task in enumerate(todo.list_tasks(), start=1):
                    print(f"{i}. {task}")
            elif chosen_option == "6":
                todo.clear_tasks()
                print("All tasks have been cleared.")
            elif chosen_option == "0":
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

    
        


    


