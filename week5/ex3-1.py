import pandas as pd

data = {
    "programme":  ["CS", "CS", "DS", "IT"],
    "exam_score": [60, 72, 80, 49],
}

# Option A: Provide an index at creation time
students_a = pd.DataFrame(data, index=[101, 102, 103, 104])
students_a.index.name = "student_id"  # (optional) give the index a label

print("A) DataFrame created with index= ...")
print(students_a)
print("\nLookup by index using .loc[103]:")
print(students_a.loc[103])

# Option B: Start with a normal column, then set it as the index
students_b = pd.DataFrame({
    "student_id": [101, 102, 103, 104],
    "programme":  ["CS", "CS", "DS", "IT"],
    "exam_score": [60, 72, 80, 49],
})

print("\nB) Original DataFrame (default 0..N index):")
print(students_b)

students_b_indexed = students_b.set_index("student_id")
print("\nAfter set_index('student_id'):")
print(students_b_indexed)

print("\nLookup by index using .loc[104]:")
print(students_b_indexed.loc[104])

# If you need student_id back as a normal column:
students_b_reset = students_b_indexed.reset_index()
print("\nAfter reset_index() (student_id back as a column):")
print(students_b_reset)