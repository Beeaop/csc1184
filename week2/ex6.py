def load_data(filename):
    data = []

    with open(filename, "r", encoding="utf-8") as f:
        header = f.readline().strip().split(",")

        for row in f.readlines():
            if not row.strip():
                print("Skipping empty line")
                continue

            values = row.strip().split(",")
            if len(values) != len(header):
                print(f"Skipping malformed line: {row.strip()}")
                continue

            i = 0
            while i < len(values):
                if values[i].isdigit():
                    values[i] = int(values[i])
                i += 1

            data.append(dict(zip(header, values)))
    return data

students = load_data("students_clean.csv")
print(f"Loaded {len(students)} students.")
print(students[0])

