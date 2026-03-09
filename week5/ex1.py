import pandas as pd

# Tiny student table: each row = one student
data = {
    "student_id": [1, 2, 3, 4, 5, 6, 7],
    "programme":  ["CS", "CS", "DS", "CS", "DS", "IT", "IT"],
    "exam_score": [60, 72, 80, 55, 68, 49, 90],
}
students = pd.DataFrame(data)

print("Students table:")
print(students)

print("\nHow many students per programme?")
counts = students["programme"].value_counts()
print(counts)

print("\nWhat proportion per programme?")
proportions = students["programme"].value_counts(normalize=True)
print(proportions)

# Turn proportions into percentages
print("\nAs percentages:")
print((proportions * 100).round(1))