import pandas as pd

orders = pd.DataFrame({
    "order_id":   [1, 2, 3, 4, 5, 6, 7, 8],
    "country":    ["IE", "IE", "UK", "DE", "UK", "IE", "DE", "IE"],
    "status":     ["completed", "cancelled", "completed", "completed", "returned", "completed", "completed", "completed"],
    "order_value":[50.0, 30.0, 80.0, 25.0, 60.0, 120.0, 40.0, 70.0]
})

print(orders)

# TODO 1
completed = orders[orders["status"] == "completed"]

print("\nCompleted orders only:")
print(completed)

# TODO 2
grouped = completed.groupby("country")["order_value"].agg(
    total_revenue="sum",
    num_completed_orders="count"
)

print("\nCompleted orders by country:")
print(grouped)

# TODO 3
grouped_reset = grouped.reset_index()
sorted_revenue = grouped_reset.sort_values("total_revenue", ascending=False)

print("\nSorted by total completed revenue:")
print(sorted_revenue)

# TODO 4
top = sorted_revenue.iloc[0]
print(f"\nTop country by completed revenue: {top['country']} with €{top['total_revenue']:.2f}.")