import pandas as pd

data = {
    "id": [1, 2, 3, 4, 5],
    "name": ["Ana", "Bob", "Ciara", "Dan", "Ella"],
    "programme": ["CS", "CS", "DS", "CS", "DS"],
    "exam_score": [55, 62, 71, 48, 83],
    "labs_attended": [6, 7, 5, 2, 8],
}

students = pd.DataFrame(data)

print("Full table:")
print(students)

# TODO 1: Use iloc to select the first 2 rows
print("\nFirst two rows (iloc):")
first_two = students.iloc[0:2]
print(first_two)

# TODO 2: Use loc to select rows with labels 2..4 (inclusive)
print("\nRows with labels 2..4 (loc):")
two_to_four = students.loc[2:4]
print(two_to_four)

# TODO 3: Use loc to select rows with labels 1..3 and only the columns name and exam_score
print("\nRows 1..3, columns name & exam_score (loc):")
subset = students.loc[1:3, ["name", "exam_score"]]
print(subset)