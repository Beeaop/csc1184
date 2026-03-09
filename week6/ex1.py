import pandas as pd

data = {
    "student_id": [101, 102, 103, 104, 105, 106, 107],
    "programme":  ["CS", "CS", "DS", "IT", "DS", "CS", "IT"]
}

df = pd.DataFrame(data)
print(df)

# TODO 1
prog_counts = df["programme"].value_counts()

print("\nCounts per programme:")
print(prog_counts)

# TODO 2
prog_props = df["programme"].value_counts(normalize=True)

print("\nProportions per programme (fraction):")
print(prog_props)

# TODO 3
prog_percent = (prog_props * 100).round(1)

print("\nProportions per programme (%):")
print(prog_percent)

# TODO 4
print(f"\nObservation: The most common programme is {prog_counts.idxmax()} with {prog_counts.max()} students.")