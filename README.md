### Project 1: Expense Tracker Application (Intermediate)
#### Project Goal
Build a simple command-line Python application that allows users to track daily expenses.

#### Requirements
- *Input/Output*: The app should accept user inputs to add, view, and delete expenses.
- *Data Management*: Store expenses as objects with attributes like description, amount, and date.
- *CRUD Operations*:
  - Add a new expense.
  - View the list of all expenses.
  - Delete an expense by its ID.
- *Summary*: Calculate the total expenses for the month.
- *File Handling (Optional)*: Save expenses to a file so they persist even when the program is restarted.
- *Error Handling*: Handle invalid inputs gracefully.

#### Skills Covered
- Python Basics: Variables, loops, and conditional statements.
- Object-Oriented Programming: Classes, objects, and methods.
- Data Structures: Lists and dictionaries.
- Input/Output: Reading and writing to files.

#### Example of Expense Structure
python
class Expense:
    def __init__(self, expense_id, description, amount, date):
        self.expense_id = expense_id
        self.description = description
        self.amount = amount
        self.date = date


---

### Project 2: Quiz App (Command Line) (Beginner)
#### Project Goal
Create a console-based quiz application using Python.

#### Requirements
- *Input/Output*: Users should be able to see questions and input answers.
- *Multiple-Choice Questions*: Each question should have 4 possible answers.
- *Score Tracking*: Track the user's score and display it at the end.
- *Question Bank*: Store the questions in a list of objects.
- *Timer (Optional)*: Add a time limit for each question.
- *Error Handling*: Handle incorrect input gracefully.

#### Skills Covered
- Python Basics: Loops, conditionals, and input/output.
- Data Structures: Lists and dictionaries.
- Logic Building: Scoring system and logic for correct answers.

#### Example of Question Structure
python
class Question:
    def __init__(self, question_text, options, correct_answer_index):
        self.question_text = question_text
        self.options = options
        self.correct_answer_index = correct_answer_index


#### Example of the Quiz Flow
1. *Welcome Message*: "Welcome to the Python Quiz! Choose the correct option for each question."
2. *Display Question*:

Q1: What is the keyword to declare a constant variable in Python?
a) const
b) var
c) let
d) There is no specific keyword

3. *User Input*: User enters 'a', 'b', 'c', or 'd'.
4. *Feedback*: Inform the user if they are correct or not.
5. *Final Score*: At the end, show the user's score.

---

### Project 3: To-Do List App (Intermediate)
#### Project Goal
Build a simple console-based to-do list app where users can create, update, view, and delete tasks.

#### Requirements
- *Task Object*: Each task should have id, title, description, and status (completed or not).
- *CRUD Operations*:
  - Create a new task.
  - Read and display all tasks.
  - Update the status of a task.
  - Delete a task.
- *User Input*: Users should be able to type commands like add, view, delete, and update.
- *Data Persistence (Optional)*: Save tasks to a file so they persist when the program is restarted.

#### Skills Covered
- Python Basics: Variables, loops, conditionals, and input/output.
- OOP Concepts: Classes, objects, and methods.
- File Handling: Read and write data to a file.
- Logic Building: CRUD operations for task management.

#### Example of Task Structure
python
class Task:
    def __init__(self, task_id, title, description, is_completed=False):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.is_completed = is_completed


#### Example Flow
User Commands:

add "Buy groceries" "Buy milk, bread, and eggs"
view
update 1 completed
delete 2

Task List:

ID: 1 - Buy groceries - Not Completed  
ID: 2 - Complete Python project - Completed  
