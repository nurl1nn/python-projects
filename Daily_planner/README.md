# 📝 To-Do List — Python

A simple **command-line To-Do List application** built with Python.
This project allows users to add, view, and remove tasks while assigning a priority and estimated time to each task.

## 🚀 Features

* ➕ Add new tasks
* 🗑️ Remove tasks
* 📋 View all tasks
* ⭐ Assign a priority to each task
* ⏱️ Set an estimated time for each task
* 🔄 Interactive command-line menu

## 🛠️ Technologies

* **Python 3**
* Lists
* Dictionaries
* `while` loops
* `for` loops
* Conditional statements
* User input
* Basic CRUD logic

## 📌 How It Works

When the program starts, the user is presented with a menu:

```text
What do you want to do:
Add task: A
Exit: O
Edit: E
See tasks: S
```

### Add a Task

Select `A` and enter:

* Task name
* Priority
* Estimated time

Example:

```text
Tapsırıq elave et: Python practice
Prioritet teyin et: High
Texmini vaxt teyin et: 1 hour
```

The task is stored as a dictionary:

```python
{
    "Task": "Python practice",
    "Prioritet": "High",
    "Texmini_vaxt": "1 hour"
}
```

### View Tasks

Select `S` to display all added tasks.

### Remove a Task

Select `E` and enter the name of the task you want to remove.

## ▶️ How to Run

Make sure Python is installed on your computer.

Clone the repository:

```bash
git clone https://github.com/your-username/your-repository-name.git
```

Navigate to the project directory:

```bash
cd your-repository-name
```

Run the program:

```bash
python todo.py
```

## 📚 What I Learned

Through this project, I practiced:

* Working with Python lists and dictionaries
* Using loops and conditional statements
* Handling user input
* Adding and removing items from lists
* Creating a simple interactive CLI application
* Structuring data using dictionaries

## 🔮 Future Improvements

Possible improvements for future versions:

* [ ] Add task completion status
* [ ] Add task IDs
* [ ] Improve the Edit feature
* [ ] Save tasks to a file
* [ ] Load tasks when the program starts
* [ ] Add deadlines
* [ ] Sort tasks by priority
* [ ] Create a graphical user interface (GUI)

## 👨‍💻 Author

**Nurlan**

This project was created as part of my Python practice and portfolio development.

