# TODO: Write a function 'greet(name, title="Student")'
# If title is not passed, it defaults to "Student".
# Example: greet("Alice") -> "Hello Student Alice"
# Example: greet("Dr. Bob", "Professor") -> "Hello Professor Dr. Bob"


def greet(name, title="Student"):
  print(f"Hello {title} {name}")


greet("Alice")
greet("Dr. Bob", "Professor")

