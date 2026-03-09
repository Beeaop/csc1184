import pandas as pd

order_items = pd.DataFrame({
    "order_id":   [101, 101, 102, 103, 104],
    "product_id": [10, 11, 10, 12, 11],
    "quantity":   [1, 2, 1, 3, 1]
})

products = pd.DataFrame({
    "product_id":   [10, 11, 12],
    "product_name": ["Laptop", "Mouse", "Keyboard"],
    "price":        [1200.0, 25.0, 45.0]
})

print("Order items:")
print(order_items)
print("\nProducts:")
print(products)

# TODO 1
items_with_price = pd.merge(order_items, products, on="product_id", how="left")

print("\nOrder items with price:")
print(items_with_price)

# TODO 2
items_with_price["line_total"] = items_with_price["price"] * items_with_price["quantity"]

print("\nWith line_total:")
print(items_with_price)

# TODO 3
product_revenue = (
    items_with_price
    .groupby("product_name")["line_total"]
    .sum()
    .reset_index(name="total_revenue")
    .sort_values("total_revenue", ascending=False)
)

print("\nTotal revenue by product:")
print(product_revenue)

# TODO 4
top = product_revenue.iloc[0]
print(f"\nTop product by revenue: {top['product_name']} with €{top['total_revenue']:.2f}.")