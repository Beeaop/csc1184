names = ["Alice", "Bob", "Charlie", "David"]
scores = [85, 42, 90, 30]

# TODO 1: Use zip() and dict() to create a dictionary 
# named 'gradebook' mapping names to scores.
gradebook = dict(zip(names, scores))

# TODO 2: Loop through the dictionary items.
# Print "{Name} passed" if score >= 40
# Print "{Name} failed" if score < 40

for name, score in gradebook.items():
  if score >= 40:
    print(f"{name} passed")
  else:
    print(f"{name} failed")

print("--- Results ---")
