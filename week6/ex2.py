import pandas as pd

orders = pd.DataFrame({
    "order_id":   [1, 2, 3, 4, 5, 6, 7],
    "country":    ["IE", "IE", "UK", "DE", "UK", "IE", "DE"],
    "order_value":[50.0, 30.0, 80.0, 25.0, 60.0, 120.0, 40.0]
})

print(orders)

# TODO 1
grouped = orders.groupby("country")["order_value"].agg(["mean", "count"])

print("\nGrouped result (index is country):")
print(grouped)

# TODO 2
grouped_reset = grouped.reset_index()

print("\nAfter reset_index:")
print(grouped_reset)

# TODO 3
sorted_by_mean = grouped_reset.sort_values("mean", ascending=False)

print("\nSorted by mean order value (descending):")
print(sorted_by_mean)

# TODO 4
top_country_ex2 = sorted_by_mean.iloc[0]["country"]
print(f"\nObservation: {top_country_ex2} has the highest average order value.")