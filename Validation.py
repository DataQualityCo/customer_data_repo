import sqlite3
import pander as pander
# Validate Customer ID (should be unique)
if df['customer_ID'].duplicated().sum() > 0:
    print("Warning: Duplicate Customer IDs found!")

# Validate Email, Phone, Account Balance, and Date of Birth
valid_email = df['email'].str.contains(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$').all()
valid_phone = df['Phone'].str.contains(r'^\+?\d{1,15}$').all()
valid_balance = (df['Account_Balance'] >= 0).all()
valid_dob = (df['date_of_birth'] < pd.Timestamp.today()).all()

if valid_email and valid_phone and valid_balance and valid_dob:
    print("Data Validation Passed")
else:
    print("Some data failed validation checks.")
