import pandas as pd

# 1. Read CSVs
customers = pd.read_csv("lab5_data/customers.csv")
orders = pd.read_csv("lab5_data/orders.csv")

# 2. Join orders with customers
orders_joined = pd.merge(orders, customers, on="customer_id", how="inner")

# 3. Group by country
country_revenue = (
    orders_joined
    .groupby("country", as_index=False)
    .agg(
        total_revenue=("order_value", "sum"),
        avg_order=("order_value", "mean"),
        num_orders=("order_value", "count")
    )
    .sort_values("total_revenue", ascending=False)
)

print("\nRevenue per country:")
print(country_revenue)

# 4. Print required statements
top_country = country_revenue.iloc[0]["country"]
top_revenue = country_revenue.iloc[0]["total_revenue"]

if len(country_revenue) >= 2:
    second_revenue = country_revenue.iloc[1]["total_revenue"]
    diff = top_revenue - second_revenue
    print(f"\nHighest revenue country: {top_country}")
    print(f"It brings in about €{diff:.2f} more than the second country.")
else:
    print(f"\nHighest revenue country: {top_country} (only country in dataset).")