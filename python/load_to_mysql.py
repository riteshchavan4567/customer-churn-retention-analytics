import os

import pandas as pd
import pymysql
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load cleaned dataset
df = pd.read_csv("data/cleaned/Telco-Customer-Churn-Cleaned.csv")

# Connect to MySQL
connection = pymysql.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)

print("Connected to MySQL successfully!")

cursor = connection.cursor()

# Generate placeholders for all columns
placeholders = ", ".join(["%s"] * len(df.columns))

query = f"""
INSERT IGNORE INTO customers
VALUES ({placeholders})
"""

# Convert dataframe rows to tuples
data = list(df.itertuples(index=False, name=None))

print("Columns:", len(df.columns))
print("Rows:", len(data))

# Insert records
cursor.executemany(query, data)

connection.commit()

print(f"{len(data)} customers loaded successfully!")

cursor.close()
connection.close()