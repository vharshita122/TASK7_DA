# 🧾 Sales Summary Project

This project uses Python, SQLite, and Pandas to analyze basic sales data stored in a SQLite database and visualize total revenue per product.

## 📂 Files Included
- `create_sales_db.py` – Creates a sample `sales_data.db` with a `sales` table and sample entries.
- `sales_summary_pandas.py` – Runs SQL to get total quantity and revenue per product, displays results, and shows a bar chart.
- `sales_data.db` – SQLite database file (auto-created by the script).
- `sales_chart.png` – Chart showing revenue by product (auto-generated).

## ▶️ How to Run
1. Clone or download this repo.
2. Make sure Python is installed.
3. Install required libraries:
   ```bash
   pip install pandas matplotlib

Run the scripts:
python create_sales_db.py
python sales_summary_pandas.py
