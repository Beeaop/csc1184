import pandas as pd

data = {
    "id": [1, 2, 3, 4, 5, 6],
    "name": ["Ana", "Bob", "Ciara", "Dan", "Ella", "Farah"],
    "programme": ["CS", "CS", "DS", "CS", "DS", "CS"],
    "exam_score": [55, 62, 71, 48, 83, 66],
    "labs_attended": [6, 7, 5, 2, 8, 4],
}

students = pd.DataFrame(data)

print("Full table:")
print(students)

# TODO: Compute the average exam_score per programme using groupby
avg_by_programme = students.groupby("programme")["exam_score"].mean()

print("\nAverage exam score by programme:")
print(avg_by_programme)
