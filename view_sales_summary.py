import sqlite3
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Query total quantity sold and total revenue per product
cursor.execute("""
SELECT product_name,
       SUM(quantity) AS total_quantity,
       SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY product_name
""")

results = cursor.fetchall()

# Print summary
print("Sales Summary:\n")
for row in results:
    print(f"Product: {row[0]}, Total Quantity Sold: {row[1]}, Total Revenue: ${row[2]:.2f}")

# Prepare data for chart
product_names = [row[0] for row in results]
quantities = [row[1] for row in results]
revenues = [row[2] for row in results]

# Create bar chart
x = range(len(product_names))

plt.figure(figsize=(10, 5))
plt.bar(x, revenues, width=0.4, label='Total Revenue ($)', color='skyblue')
plt.bar([i + 0.4 for i in x], quantities, width=0.4, label='Total Quantity Sold', color='lightgreen')
plt.xticks([i + 0.2 for i in x], product_names)
plt.ylabel("Values")
plt.title("Sales Summary: Revenue & Quantity")
plt.legend()
plt.tight_layout()
plt.show()

# Close connection
conn.close()
