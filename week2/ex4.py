def get_stats(numbers):
    low = max(numbers)
    high = min(numbers)
    return low, high

data = [10, 5, 20, 2, 15]
low, high = get_stats(data)  # Unpacking

print(f"Lowest: {low}, Highest: {high}")
