import pandas as pd

students = pd.DataFrame({
    "student_id": [1, 2, 3, 4],
    "programme_id": ["CS", "CS", "DS", "UNK"],  # UNK = unknown / invalid code
    "exam_score": [60, 72, 80, 55],
})

programmes = pd.DataFrame({
    "programme_id": ["CS", "DS", "IT"],
    "programme_name": ["Computer Science", "Data Science", "Information Technology"],
})

print("Students:")
print(students)
print("\nProgrammes:")
print(programmes)

# Inner join: only rows with matching programme_id in both tables
inner_join = pd.merge(students, programmes, on="programme_id", how="inner")
print("\nInner join on programme_id:")
print(inner_join)

# Left join: keep all students, even if programme_id is unknown
left_join = pd.merge(students, programmes, on="programme_id", how="left")
print("\nLeft join on programme_id (all students kept):")
print(left_join)
