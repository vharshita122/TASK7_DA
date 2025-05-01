import sqlite3

# Connect to SQLite database (it will create one if it doesn't exist)
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create a sales table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL,
    sale_date TEXT NOT NULL
)
""")

# Optional: Insert some sample data
cursor.executemany("""
INSERT INTO sales (product_name, quantity, price, sale_date) VALUES (?, ?, ?, ?)
""", [
    ("Pen", 10, 1.5, "2025-04-25"),
    ("Notebook", 5, 3.2, "2025-04-26"),
    ("Eraser", 20, 0.5, "2025-04-27")
])

# Save changes and close connection
conn.commit()
conn.close()

print("Database and table created successfully with sample data.")
