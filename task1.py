students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 90
}

name = input("Enter the student's name: ")

if name in students:
    print(f"{name}'s marks are: {students[name]}")
else:
    print(f"Student named '{name}' not found in the record.")
