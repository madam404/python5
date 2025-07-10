# python5
task1.py 
---

🔹 students = {...}

A dictionary named students is created.

It stores student names as keys and their marks as values.


📘 Example:

"Alice": 85

means Alice has 85 marks.


---

🔹 name = input("Enter the student's name: ")

The program asks the user to enter a student’s name.

This input is stored in the variable name.


👤 Example:

Enter the student's name: Bob

Now name = "Bob"


---

🔹 if name in students:

Checks whether the entered name exists as a key in the students dictionary.


✔️ If found:

print(f"{name}'s marks are: {students[name]}")

This will print the marks associated with that student.


Example output:

Bob's marks are: 92

❌ If not found:

print(f"Student named '{name}' not found in the record.")

Displays an error-like message.


Example:

Student named 'John' not found in the record.
