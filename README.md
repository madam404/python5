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

---
task2.py
---

🔹 numbers = list(range(1, 11))

Creates a list of numbers from 1 to 10.

range(1, 11) generates numbers from 1 up to (but not including) 11.

list(...) converts it into a list.


📘 Output:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


---

🔹 first_five = numbers[:5]

This is list slicing.

[:5] means: start from index 0 up to (but not including) index 5.

So it extracts the first 5 elements.


📘 Output:

first_five = [1, 2, 3, 4, 5]


---

🔹 reversed_five = first_five[::-1]

This is reverse slicing.

[::-1] means step backwards through the list.

It reverses the elements in first_five.


📘 Output:

reversed_five = [5, 4, 3, 2, 1]


---

🔹 print(...) Statements

These lines display all three lists:

Output:

Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted first five elements: [1, 2, 3, 4, 5]
Reversed extracted elements: [5, 4, 3, 2, 1]
