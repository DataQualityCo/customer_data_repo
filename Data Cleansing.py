import sqlite3
import pander as pander
# Handle missing data
df['email'].fillna('Unknown', inplace=True)
df['Phone'].fillna('Unknown', inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Correct invalid emails and phone numbers by keeping valid ones only
df = df[df['email'].str.contains(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')]
df = df[df['Phone'].str.contains(r'^\+?\d{1,15}$')]

# Handle invalid Date of Birth (assuming valid dates should be before today's date)
df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], errors='coerce')
df = df[df['date_of_birth'] < pd.Timestamp.today()]

# Fix Account Balance: remove negative balances
df['Account_Balance'] = df['Account_Balance'].apply(lambda x: max(x, 0))

# Save the cleaned data back to the database
df.to_sql('customers', conn, if_exists='replace', index=False)
