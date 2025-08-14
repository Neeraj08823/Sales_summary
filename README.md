# 🛒 Basic Sales Summary Using SQLite in Python — Task 7

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=yellow)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-4062BB?style=for-the-badge)

---

## 📑 Table of Contents

- [📌 Overview](#-overview)
- [📂 Dataset](#-dataset)
- [🎯 Objective](#-objective)
- [🛠 Tools Used](#-tools-used)
- [⚙️ Steps Implemented](#️-steps-implemented)
- [📊 Output & Insights](#-output--insights)
- [📁 Repository Contents](#-repository-contents)

---

## 📌 Overview

This project is part of my **Data Analyst Internship (Task 7)** focusing on **Basic Sales Summary from a Tiny SQLite Database using Python**.

The goal is to:

- Connect to a local SQLite database in Python.
- Run SQL queries to calculate **total quantity sold** and **total revenue** per product.
- Display the output in the terminal.
- Create and save a **bar chart** visualization of revenue by product.

---

## 📂 Dataset

- **Name**: `sales_data.db` (created locally for this task)
- **Table**: `sales`
- **Columns**:
  - `product` — Name of the product
  - `quantity` — Units sold
  - `price` — Price per unit

The database is generated using `create_db.py` with sample sales records for three products — Laptop, Mobile, Tablet.

---

## 🎯 Objective

**Main Goals:**

1. Calculate and display:
   - Total Quantity sold per product
   - Total Revenue per product
2. Visualize:
   - Bar chart showing product-wise revenue

---

## 🛠 Tools Used

- **Python** — Main programming language
- **SQLite3** — Lightweight built-in database engine
- **Pandas** — For loading SQL results and data processing
- **Matplotlib** — For creating bar charts

---

## ⚙️ Steps Implemented

1. Created a SQLite database `sales_data.db` and inserted sample sales data (`create_db.py`).
2. Connected to the database using `sqlite3`.
3. Ran SQL query with `GROUP BY` to calculate **total quantity** and **revenue** per product.
4. Loaded results into pandas DataFrame.
5. Printed summary in tabular format.
6. Created and saved a bar chart (`sales_chart.png`) using Matplotlib.

---

## 📊 Output & Insights

**Sales Summary Sample Output:**

| product | total_qty | revenue  |
| ------- | --------- | -------- |
| Laptop  | 8         | 406000.0 |
| Mobile  | 25        | 367500.0 |
| Tablet  | 11        | 283000.0 |

**Insights:**

- **Laptop** generated the maximum revenue.
- **Mobile** had the highest units sold but slightly lower revenue than Laptop.
- Clear product sales trend can be visualized via the bar chart.

**Sample Visualization:**

📈 **Bar Chart — Revenue by Product**  
(Output image saved as `sales_chart.png`)

---

## 📁 Repository Contents

| File / Folder Name  | Description                                                  |
| ------------------- | ------------------------------------------------------------ |
| `create_db.py`      | Creates `sales_data.db` and inserts sample records           |
| `sales_summary.py`  | Connects to DB, runs SQL query, prints results & saves chart |
| `sales_data.db`     | SQLite database file (generated)                             |
| `sales_chart.png`   | Bar chart visualization of revenue per product               |
| `sales_summary.png` | Sales Summary Sample Output                                  |
| `README.md`         | Project documentation (this file)                            |

---
