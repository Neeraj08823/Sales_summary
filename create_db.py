import sqlite3

# Connect (this will create the database file if it doesn't exist)
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create sales table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL
)
""")

# Insert some sample data
sample_data = [
    ("Laptop", 5, 50000),
    ("Laptop", 3, 52000),
    ("Mobile", 10, 15000),
    ("Mobile", 15, 14500),
    ("Tablet", 7, 25000),
    ("Tablet", 4, 27000),
]

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)

conn.commit()
conn.close()

print("✅ Database created successfully with sample data!")
