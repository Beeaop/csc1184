import pandas as pd

data = {
    "id": [1, 2, 3, 4, 5],
    "name": ["Ana", "Bob", "Ciara", "Dan", "Ella"],
    "programme": ["CS", "CS", "DS", "CS", "DS"],
    "exam_score": [55, 62, 71, 48, 83],
    "labs_attended": [6, 7, 5, 2, 8],
}

students = pd.DataFrame(data)

# TODO 1: Add a new boolean column "passed" (True if exam_score >= 60)
students["passed"] = students["exam_score"] >=60

# TODO 2: Compute the maximum exam_score
max_score = max(students["passed"])

# TODO 3: Add a new column "score_normalised" = exam_score / max_score
students["score_normalised"] = students["exam_score"] / max_score

print("Table with new columns:")
print(students)

print("\nAverage normalised score:", students["score_normalised"].mean())
print("Number of students who passed:", students["passed"].sum())