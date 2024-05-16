"""
Name: Janielle Jackson
UID: 117595598
Due Date: May 15 2024
Title: Final Project - TerpTu-Do
"""

import pytest
from todo import ToDoList, Task

class TestToDoList():
    def setUp(self):
        self.todo = ToDoList()

    def test_add_task(self):
        self.todo.add_task("Finish INST326 homework")
        self.todo.add_task("Read INST327 chapter")
        tasks = self.todo.list_tasks()
        self.assertIn("[✗] Finish INST326 homework", tasks)
        self.assertIn("[✗] Read INST327 chapter", tasks)

    def test_remove_task(self):
        self.todo.add_task("Finish INST326 homework")
        self.todo.remove_task(0)
        self.assertEqual(self.todo.list_tasks(), [])

    def test_mark_task_completed(self):
        self.todo.add_task("Finish INST326 homework")
        self.todo.mark_task_completed(0)
        tasks = self.todo.list_tasks()
        self.assertIn("[✓] Finish INST326 homework", tasks)
    
    def test_update_task(self):
        self.todo.add_task("Finish INST326 homework")
        self.todo.update_task(0, "Complete INST326 homework")
        tasks = self.todo.list_tasks()
        self.assertIn("[✗] Complete INST326 homework", tasks)

    def test_list_tasks(self):
        self.todo.add_task("Finish INST326 homework")
        self.todo.add_task("Read INST327 chapter")
        tasks = self.todo.list_tasks()
        self.assertEqual(len(tasks), 2)

    def test_clear_tasks(self):
        self.todo.add_task("Finish INST326 homework")
        self.todo.add_task("Read INST327 chapter")
        self.todo.clear_tasks()
        self.assertEqual(self.todo.list_tasks(), [])


