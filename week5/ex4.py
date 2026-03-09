import pandas as pd

data = {
    "student_id":    [1, 2, 3, 4, 5, 6, 7],
    "programme":     ["CS", "CS", "DS", "CS", "DS", "IT", "IT"],
    "exam_score":    [60, 72, 80, 55, 68, 49, 90],
    "labs_attended": [6,   5,   7,  2,  4,  3,  6],
}
students = pd.DataFrame(data)

print("All students:")
print(students)

# 1. Filter: only students with at least 4 labs
mask = students["labs_attended"] >= 4
engaged = students[mask]

print("\nStudents with labs_attended >= 4:")
print(engaged)

# 2. Group by programme, 3. Summarise, 4. Sort
summary = (
    engaged
    .groupby("programme")["exam_score"]
    .agg(["mean", "count"])
    .reset_index()
    .sort_values("mean", ascending=False)
)

print("\nAverage exam_score per programme (among engaged students):")
print(summary)
