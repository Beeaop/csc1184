print("HEAD:")
# TODO 1: Show the first few rows
print(students.head())

# TODO 2: Add a pass flag (exam_score >= 60)
students["passed"] = students["exam_score"] >= 60

# TODO 3: Filter to DS students only
ds_students = students[students["programme"] == "DS"]

print("\nDS students:")
print(ds_students)

# TODO 4: For DS students, compute:
# - average exam_score
# - pass rate (%)
avg_ds_score = ds_students["exam_score"].mean()
ds_pass_rate = ds_students["passed"].mean() * 100

print("\nAverage DS exam score:", round(avg_ds_score, 1))
print("DS pass rate (%):", round(ds_pass_rate, 1))
