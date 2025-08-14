import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 1. Connect to the database
conn = sqlite3.connect("sales_data.db")

# 2. SQL query to get total quantity and revenue per product
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""

# 3. Load result into a pandas DataFrame
df = pd.read_sql_query(query, conn)

# 4. Print results
print("\n📊 Sales Summary:")
print(df)

# 5. Plot a bar chart for Revenue per product
plt.figure(figsize=(6,4))
df.plot(kind='bar', x='product', y='revenue', color='skyblue')
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=45)
plt.tight_layout()

# 6. Save and Show the chart
plt.savefig("sales_chart.png")
plt.show()

# 7. Close connection
conn.close()
