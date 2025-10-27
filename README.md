# TO_DO_LIST# 🧩 Task 1 – To-Do List Application

### 🎯 Objective
The goal of this project is to create a simple **To-Do List Application** using Python that allows users to efficiently **add, view, and remove tasks** through a command-line interface.

---

### 📝 Description
A To-Do List helps users **organize their daily tasks** and keep track of pending work.  
This project is a beginner-friendly console-based app written in **Python**.  
It uses **lists** and basic control structures to manage tasks interactively.

---

### ⚙️ Features
✅ Add new tasks  
✅ View all tasks  
✅ Remove completed tasks  
✅ Exit the application safely  

---

### 🧠 Concepts Used
- Python Lists  
- Loops (`while`, `for`)  
- Conditional Statements (`if-elif-else`)  
- User Input Handling  

---

### 💻 Code Example
```python
tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks yet.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter new task: ")
        tasks.append(task)
        print("✅ Task added successfully.")
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        show_tasks()
        num = int(input("Enter task number to remove: "))
        if 0 < num <= len(tasks):
            tasks.pop(num - 1)
            print("🗑 Task removed.")
        else:
            print("Invalid number.")
    elif choice == '4':
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice, try again.")
