import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect("sales_data.db")

# SQL query
query = """
SELECT product_name AS product,
       SUM(quantity) AS total_qty,
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""

# Load into pandas DataFrame
df = pd.read_sql_query(query, conn)

# Print DataFrame
print("Sales Summary:\n")
print(df)

# Plot revenue per product
df.plot(kind='bar', x='product', y='revenue', legend=False, color='orange')
plt.ylabel("Revenue ($)")
plt.title("Revenue by Product")
plt.tight_layout()

# Show the plot
plt.show()

# Optional: Save the chart as a PNG file
plt.savefig("sales_chart.png")

# Close DB connection
conn.close()
