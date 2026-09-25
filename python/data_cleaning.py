import pandas as pd

# Load raw dataset
df = pd.read_csv("data/raw/Telco-Customer-Churn.csv")

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# Replace missing TotalCharges for new customers with 0
df["TotalCharges"] = df["TotalCharges"].fillna(0)

print(df.head())
print("\nData types:")
print(df.dtypes)

# Save cleaned dataset
df.to_csv("data/cleaned/Telco-Customer-Churn-Cleaned.csv", index=False)

print("\nCleaned dataset saved successfully.")