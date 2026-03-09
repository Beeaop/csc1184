import pandas as pd

# Table 1: students
students = pd.DataFrame({
    "student_id":    [1, 2, 3, 4, 5, 6, 7],
    "programme_id":  ["CS", "CS", "DS", "CS", "DS", "IT", "IT"],
    "exam_score":    [60, 72, 80, 55, 68, 49, 90],
})

# Table 2: programme info
programmes = pd.DataFrame({
    "programme_id":   ["CS", "DS", "IT"],
    "programme_name": ["Computer Science", "Data Science", "Information Technology"],
    "school":         ["Computing", "Computing", "Computing"],
})

print("Students:")
print(students)
print("\nProgrammes:")
print(programmes)

# 1. Join students with programmes to get names
joined = pd.merge(students, programmes, on="programme_id", how="inner")

print("\nAfter join (students with programme_name and school):")
print(joined)

# 2. Group by programme_name and summarise exam_score
summary = (
    joined
    .groupby("programme_name")["exam_score"]
    .agg(["mean", "count"])
    .reset_index()
    .sort_values("mean", ascending=False)
)

print("\nAverage exam_score per programme:")
print(summary)
