import numpy as np

students = [
    {"id": "1", "name": "Ana",   "programme": "CS", "exam_score": "55"},
    {"id": "2", "name": "Bob",   "programme": "CS", "exam_score": "62"},
    {"id": "3", "name": "Ciara", "programme": "DS", "exam_score": "71"},
    {"id": "4", "name": "Dan",   "programme": "DS", "exam_score": "48"},
    {"id": "5", "name": "Eli",   "programme": "CS", "exam_score": "90"},
]

# TODO 1: Build a plain Python list of integers
exam_scores_list = []

for student in students:
    exam_scores_list.append(int(student["exam_score"]))

print("Exam scores list:", exam_scores_list)

# TODO 2: Convert exam_scores_list into a NumPy array
exam_scores = np.array(exam_scores_list)

print("Exam scores array:", exam_scores)
print("Mean:", exam_scores.mean())
print("Scores >= 60:", exam_scores[exam_scores >= 60])
