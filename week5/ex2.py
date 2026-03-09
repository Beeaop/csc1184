import pandas as pd

data = {
    "student_id": [1, 2, 3, 4, 5, 6, 7],
    "programme":  ["CS", "CS", "DS", "CS", "DS", "IT", "IT"],
    "exam_score": [60, 72, 80, 55, 68, 49, 90],
}
students = pd.DataFrame(data)

print("Students table:")
print(students)

# Average exam_score per programme
grouped_mean = students.groupby("programme")["exam_score"].mean()
print("\nAverage score per programme:")
print(grouped_mean)

# Mean and count together
grouped_stats = students.groupby("programme")["exam_score"].agg(["mean", "count"])
print("\nMean and count per programme:")
print(grouped_stats)

# Reset index to turn 'programme' back into a normal column
print("\nAs a normal DataFrame (after reset_index):")
grouped_stats_reset = grouped_stats.reset_index()
print(grouped_stats_reset)
