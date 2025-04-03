import sqlite3

# Connect to SQLite database (it will create a new database file if it doesn't exist)
conn = sqlite3.connect('customer_data.db')
cursor = conn.cursor()

# Create the customer table
cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    customer_ID INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT,
    date_of_birth TEXT,
    account_balance REAL,
    join_date TEXT
)
''')

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully!")

