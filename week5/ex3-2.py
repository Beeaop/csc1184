import pandas as pd

data = {
    "student_id": [1, 2, 3, 4, 5, 6, 7],
    "programme":  ["CS", "CS", "DS", "CS", "DS", "IT", "IT"],
    "exam_score": [60, 72, 80, 55, 68, 49, 90],
}
students = pd.DataFrame(data)

# Group by programme and compute mean and count
stats = (
    students
    .groupby("programme")["exam_score"]
    .agg(["mean", "count"])
    .reset_index()
)

print("Stats per programme (unsorted):")
print(stats)

# sort_values: order rows by the 'mean' column (descending)
sorted_stats = stats.sort_values("mean", ascending=False)
print("\nStats per programme sorted by mean score (highest first):")
print(sorted_stats)