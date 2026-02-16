import pandas as pd

data = {
    "id": [1, 2, 3, 4, 5, 6],
    "name": ["Ana", "Bob", "Ciara", "Dan", "Ella", "Farah"],
    "programme": ["CS", "CS", "DS", "CS", "DS", "CS"],
    "exam_score": [55, 62, 71, 48, 83, 66],
    "labs_attended": [6, 7, 5, 2, 8, 4],
}

students = pd.DataFrame(data)

# Condition 1: programme is CS
cs_mask = students["programme"] == "CS"

# Condition 2: exam_score >= 60
pass_mask = students["exam_score"] >= 60

# TODO: Combine both masks with & to get CS students who passed
cs_and_pass = cs_mask & pass_mask

cs_passed = students[cs_and_pass]

print("CS students who passed:")
print(cs_passed)

print("\nCount:", len(cs_passed))
print("Average exam score (CS & passed):", cs_passed["exam_score"].mean())