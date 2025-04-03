import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('customer_data.db')

# Load data from CSV into a pandas DataFrame
df = pd.read_excel('customer_data.xlsx')  # Replace with your CSV file path

# Insert the data into the customers table
df.to_sql('customers', conn, if_exists='replace', index=False)

# Commit and close the connection
conn.commit()
conn.close()

print("Data from CSV loaded into database!")

