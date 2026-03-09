import pandas as pd

customers = pd.DataFrame({
    "customer_id": [1, 2, 3, 4],
    "name":        ["Alice", "Bob", "Ciara", "Dan"],
    "country":     ["IE", "UK", "IE", "DE"]
})

orders = pd.DataFrame({
    "order_id":    [101, 102, 103, 104, 105],
    "customer_id": [1, 1, 2, 4, 5],
    "order_value": [50.0, 80.0, 25.0, 40.0, 60.0]
})

print("Customers:")
print(customers)
print("\nOrders:")
print(orders)

# TODO 1
inner_join = pd.merge(orders, customers, on="customer_id", how="inner")

print("\nInner join result:")
print(inner_join)

# TODO 2
left_join = pd.merge(orders, customers, on="customer_id", how="left")

print("\nLeft join result:")
print(left_join)

# TODO 3
# The inner join removes the order with customer_id 5.
# The left join keeps it but fills name and country with NaN.