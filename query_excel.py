import sqlite3
import pandas as pd

# Step 1: Load Excel Data
excel_file = "data/customer_data.xlsx"  # Path to your Excel file
df = pd.read_excel(excel_file)  # Read Excel file into DataFrame

# Step 2: Connect to SQLite (or create the database)
conn = sqlite3.connect("data/customer_database.db")  # Create database file
cursor = conn.cursor()

# Step 3: Create a table in SQLite
table_name = "customers"
df.to_sql(table_name, conn, if_exists="replace", index=False)  # Store DataFrame in SQLite

# Step 4: Query the database
query = "SELECT * FROM customers WHERE age > 30"  # Example: Get customers older than 30
query_results = pd.read_sql(query, conn)

# Step 5: Display and save results
print(query_results)  # Print results in console
query_results.to_csv("data/query_results.csv", index=False)  # Save to CSV

# Step 6: Close the connection
conn.close()
