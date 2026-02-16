import pandas as pd

data = {
    "id": [1, 2, 3, 4, 5],
    "name": ["Ana", "Bob", "Ciara", "Dan", "Ella"],
    "programme": ["CS", "CS", "DS", "CS", "DS"],
    "exam_score": [55, 62, 71, 48, 83],
    "labs_attended": [6, 7, 5, 2, 8],
}

students = pd.DataFrame(data)

# TODO 1: Select the exam_score column as a Series and print it
exam_scores = students["exam_score"]
print("Exam scores (Series):")
print(exam_scores)

# TODO 2: Select a smaller table with only name and exam_score
name_and_score = students[["name", "exam_score"]]
print("\nName and exam_score (DataFrame):")
print(name_and_score)

# TODO 3: Compute and print the average exam score using the Series
avg_score = exam_scores.mean()
print("\nAverage exam score:", avg_score)