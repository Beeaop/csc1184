header = ["id", "name", "exam_score", "labs_attended"]
row1 = ["101", "Amal", "72", "7"]
row2 = ["102", "Grace", "64", "5"]

# TODO: Use zip() + dict() to convert each row into a dictionary.
# Cast exam_score and labs_attended to int inside the dict construction.
rows = [row1, row2]

students = []

for row in rows:
  student_dict = dict(zip(header, [row[0], row[1], int(row[2]), int(row[3])]))
  students.append(student_dict)

print(students)
