import pandas as pd

data = {
    "id": [1, 2, 3, 4, 5],
    "name": ["Ana", "Bob", "Ciara", "Dan", "Ella"],
    "programme": ["CS", "CS", "DS", "CS", "DS"],
    "exam_score": [55, 62, 71, 48, 83],
    "labs_attended": [6, 7, 5, 2, 8],
}

students = pd.DataFrame(data)

print("HEAD (first rows):")
# TODO: print the first few rows using head()
print(students.head)

print("\nShape (rows, columns):")
# TODO: print shape
print(students.shape)

print("\nINFO:")
# TODO: show info()
print(students.info)

print("\nDESCRIBE (numeric columns):")
# TODO: show describe()
print(students.describe)