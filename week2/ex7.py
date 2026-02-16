# NOTE: This code runs in the browser for practice.
# In your local 'analysis.py', you should call your real load_data("sales_data.csv")
# and then perform similar logic.

def calculate_total_sales(sales_data):
    total = 0
    for line in sales_data:
        total += (int(sales_data["price"]) * int(sales_data["quantity"]))
    return total

# Example data (mocking what your loader returns)
sales = [
    {'product': 'Laptop', 'price': '1200', 'quantity': '1'},
    {'product': 'Mouse', 'price': '25', 'quantity': '2'}
]

print("Total Revenue:", calculate_total_sales(sales))
