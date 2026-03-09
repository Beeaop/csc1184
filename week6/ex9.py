import pandas as pd

# Read CSVs
customers = pd.read_csv("lab5_data/customers.csv")
orders = pd.read_csv("lab5_data/orders.csv")

# Join
orders_joined = pd.merge(orders, customers, on="customer_id", how="inner")

# Customer summary
customer_spend = (
    orders_joined
    .groupby(["customer_id", "name"], as_index=False)
    .agg(
        total_spend=("order_value", "sum"),
        num_orders=("order_id", "count")
    )
    .sort_values("total_spend", ascending=False)
)

# Country summary
country_revenue = (
    orders_joined
    .groupby("country", as_index=False)
    .agg(
        total_revenue=("order_value", "sum")
    )
    .sort_values("total_revenue", ascending=False)
)

# Extract top values
top_customer = customer_spend.iloc[0]
top_country = country_revenue.iloc[0]
total_dataset_revenue = country_revenue["total_revenue"].sum()

country_share = (top_country["total_revenue"] / total_dataset_revenue) * 100 if total_dataset_revenue else 0

# Report
print("=== MINI REPORT ===\n")

print(f"Top customer: {top_customer['name']} (ID {top_customer['customer_id']})")
print(f"They placed {int(top_customer['num_orders'])} orders with total spend of €{top_customer['total_spend']:.2f}.\n")

print(f"Top country: {top_country['country']}")
print(f"It accounts for about {country_share:.1f}% of total revenue in this dataset.")