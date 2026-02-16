import pandas as pd

# A tiny student table stored as a dict-of-lists
__TODO__ = None

data = {
    "id": [1, 2, 3, 4],
    "name": ["Ana", "Bob", "Ciara", "Dan"],
    "programme": ["CS", "CS", "DS", "DS"],
    "exam_score": [55, 62, 71, 48],
}

# TODO: Build a DataFrame from data and store in a variable named students
students = pd.DataFrame(data)

print("Students table:")
print(students)

# TODO: Print the shape and list of column names
shape = students.shape
cols = students.columns

print("\nShape (rows, columns):", shape)
print("Columns:", cols)