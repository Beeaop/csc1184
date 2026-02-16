import pandas as pd

data = {
    "id": [1, 2, 3, 4, 5],
    "name": ["Ana", "Bob", "Ciara", "Dan", "Ella"],
    "programme": ["CS", "CS", "DS", "CS", "DS"],
    "exam_score": [55, 62, 71, 48, 83],
    "labs_attended": [6, 7, 5, 2, 8],
}

students = pd.DataFrame(data)

threshold = 60

# TODO 1: Build a boolean mask where exam_score >= threshold
mask = students["exam_score"] >= threshold

print("Mask (exam_score >= 60):")
print(mask)

# TODO 2: Use the mask to filter the table into a new DataFrame called passed
passed = students[mask]

print("\nStudents who passed:")
print(passed)

# TODO 3: Compute how many passed and the pass rate (%)
num_passing = len(passed)
num_total = len(students)
pass_rate = (num_passing / num_total) * 100

print("\nPassing:", num_passing, "out of", num_total)
print("Pass rate (%):", round(pass_rate, 1))