import pandas as pd

# 1. Read CSVs
customers = pd.read_csv("lab5_data/customers.csv")
orders = pd.read_csv("lab5_data/orders.csv")

print(customers.head())
print(orders.head())

# 2. Join orders with customers
orders_joined = pd.merge(orders, customers, on="customer_id", how="inner")

# 3. Group and calculate total spend + number of orders
customer_spend = (
    orders_joined
    .groupby(["customer_id", "name"], as_index=False)
    .agg(
        total_spend=("order_value", "sum"),
        num_orders=("order_id", "count")
    )
)

# 4. Sort by total spend
customer_spend_sorted = customer_spend.sort_values("total_spend", ascending=False)

print("\nTop 5 customers by total spend:")
print(customer_spend_sorted.head(5))