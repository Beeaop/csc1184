import pandas as pd

orders = pd.DataFrame({
    "order_id":   [1, 2, 3, 4, 5, 6, 7, 8],
    "country":    ["IE", "IE", "UK", "DE", "UK", "IE", "DE", "IE"],
    "channel":    ["online", "store", "online", "store", "online", "online", "store", "store"],
    "order_value":[50.0, 30.0, 80.0, 25.0, 60.0, 120.0, 40.0, 70.0]
})

print(orders)

# TODO 1
grouped_ex3 = orders.groupby(["country", "channel"])["order_value"].agg(["mean", "count"])

print("\nGrouped by country + channel:")
print(grouped_ex3)

# TODO 2
grouped_reset = grouped_ex3.reset_index()

print("\nAfter reset_index:")
print(grouped_reset)

# TODO 3
sorted_result = grouped_reset.sort_values(["country", "channel"])

print("\nSorted by country, channel:")
print(sorted_result)

# TODO 4
# Example: If IE + online has mean=85 and count=2,
# it means Ireland had 2 online orders with average value €85.