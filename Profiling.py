import sqlite3
import pandas as pd

# Load the customer data from your SQLite database
conn = sqlite3.connect('customer_data.db')  # Ensure the path is correct
query = "SELECT * FROM customers;"
df = pd.read_sql(query, conn)

# Check for missing values (nulls)
missing_data = df.isnull().sum()

# Check data types
data_types = df.dtypes

# Summary statistics for numerical columns (like Account_Balance)
summary_stats = df.describe()

# Check for duplicates
duplicates = df.duplicated().sum()

# Check the format of critical columns (e.g., email, phone, date_of_birth)
email_format = df['email'].str.contains(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$').sum()
phone_format = df['Phone'].str.contains(r'^\+?\d{1,15}$').sum()
dob_format = pd.to_datetime(df['date_of_birth'], errors='coerce').isna().sum()

# Print summary reports
print(f"Missing Data:\n{missing_data}")
print(f"\nData Types:\n{data_types}")
print(f"\nSummary Statistics:\n{summary_stats}")
print(f"\nDuplicates: {duplicates}")
print(f"\nValid Emails: {email_format} / {len(df)}")
print(f"Valid Phone Numbers: {phone_format} / {len(df)}")
print(f"Invalid Date of Birth Entries: {dob_format}")
