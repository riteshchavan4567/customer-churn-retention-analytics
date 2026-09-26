import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("data/cleaned/Telco-Customer-Churn-Cleaned.csv")

# Display basic information
print("Dataset shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nData types:")
print(df.dtypes)


# 1. Overall churn distribution
churn_counts = df["Churn"].value_counts()

total_customers = len(df)
churned_customers = churn_counts.get("Yes", 0)
churn_rate = churned_customers * 100 / total_customers

plt.figure(figsize=(6, 5))
bars = plt.bar(churn_counts.index, churn_counts.values)

plt.title(f"Customer Churn Distribution (Churn Rate: {churn_rate:.2f}%)")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")

# Add values on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        int(height),
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.show()
# 2. Churn rate by contract
contract_churn = (
    df.groupby("Contract")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .sort_values(ascending=False)
)

plt.figure(figsize=(7, 5))
bars = plt.bar(contract_churn.index, contract_churn.values)

plt.title("Churn Rate by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Churn Rate (%)")

# Add percentages on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}%",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.show()
# 3. Churn rate by tenure group
df["TenureGroup"] = pd.cut(
    df["tenure"],
    bins=[-1, 12, 24, 48, float("inf")],
    labels=["0-12 months", "13-24 months", "25-48 months", "49+ months"]
)

tenure_churn = (
    df.groupby("TenureGroup", observed=False)["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
)

plt.figure(figsize=(8, 5))
bars = plt.bar(tenure_churn.index, tenure_churn.values)

plt.title("Churn Rate by Customer Tenure")
plt.xlabel("Tenure Group")
plt.ylabel("Churn Rate (%)")

# Add percentages on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}%",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.show()
# 4. Churn rate by internet service
internet_churn = (
    df.groupby("InternetService")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .sort_values(ascending=False)
)

plt.figure(figsize=(7, 5))
bars = plt.bar(internet_churn.index, internet_churn.values)

plt.title("Churn Rate by Internet Service")
plt.xlabel("Internet Service")
plt.ylabel("Churn Rate (%)")

# Add percentages on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}%",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.show()
# 5. Churn rate by payment method
payment_churn = (
    df.groupby("PaymentMethod")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 5))
bars = plt.bar(payment_churn.index, payment_churn.values)

plt.title("Churn Rate by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=20, ha="right")

# Add percentages on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}%",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.show()
# 6. Average monthly charges by churn status
avg_charges = df.groupby("Churn")["MonthlyCharges"].mean()

plt.figure(figsize=(6, 5))
bars = plt.bar(avg_charges.index, avg_charges.values)

plt.title("Average Monthly Charges by Churn Status")
plt.xlabel("Churn")
plt.ylabel("Average Monthly Charges")

# Add values on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.show()
# 7. High-value + high-risk customer segment

high_value_high_risk = df[
    (df["MonthlyCharges"] >= 80)
    & (df["Contract"] == "Month-to-month")
    & (df["tenure"] <= 12)
]

total_high_risk = len(high_value_high_risk)
churned_high_risk = (high_value_high_risk["Churn"] == "Yes").sum()

high_risk_churn_rate = (
    churned_high_risk / total_high_risk * 100
)

monthly_charges = high_value_high_risk["MonthlyCharges"].sum()
churned_monthly_charges = high_value_high_risk.loc[
    high_value_high_risk["Churn"] == "Yes",
    "MonthlyCharges"
].sum()

print("\n--- High-Value + High-Risk Segment ---")
print("Customers:", total_high_risk)
print("Churned customers:", churned_high_risk)
print(f"Churn rate: {high_risk_churn_rate:.2f}%")
print(f"Total monthly charges: {monthly_charges:.2f}")
print(f"Churned monthly charges: {churned_monthly_charges:.2f}")
# 8. Key project KPIs

total_customers = len(df)
churned_customers = (df["Churn"] == "Yes").sum()
retained_customers = (df["Churn"] == "No").sum()

overall_churn_rate = churned_customers / total_customers * 100

total_monthly_charges = df["MonthlyCharges"].sum()

churned_monthly_charges = df.loc[
    df["Churn"] == "Yes",
    "MonthlyCharges"
].sum()

revenue_at_risk = (
    churned_monthly_charges / total_monthly_charges * 100
)

print("\n--- Key Project KPIs ---")
print("Total customers:", total_customers)
print("Churned customers:", churned_customers)
print("Retained customers:", retained_customers)
print(f"Overall churn rate: {overall_churn_rate:.2f}%")
print(f"Total monthly charges: {total_monthly_charges:.2f}")
print(f"Churned monthly charges: {churned_monthly_charges:.2f}")
print(f"Revenue exposure: {revenue_at_risk:.2f}%")
# 9. Export key analysis results for Power BI

kpi_data = {
    "Metric": [
        "Total Customers",
        "Churned Customers",
        "Retained Customers",
        "Overall Churn Rate",
        "Total Monthly Charges",
        "Churned Monthly Charges",
        "Revenue Exposure",
        "High-Value High-Risk Customers",
        "High-Value High-Risk Churned Customers",
        "High-Value High-Risk Churn Rate"
    ],
    "Value": [
        total_customers,
        churned_customers,
        retained_customers,
        overall_churn_rate,
        total_monthly_charges,
        churned_monthly_charges,
        revenue_at_risk,
        total_high_risk,
        churned_high_risk,
        high_risk_churn_rate
    ]
}

kpi_df = pd.DataFrame(kpi_data)

kpi_df.to_csv(
    "data/cleaned/project_kpis.csv",
    index=False
)

print("\nProject KPI file exported successfully.")
# 10. Create Power BI analysis dataset

powerbi_df = df.copy()

# Tenure groups
powerbi_df["TenureGroup"] = pd.cut(
    powerbi_df["tenure"],
    bins=[-1, 12, 24, 48, float("inf")],
    labels=["0-12 months", "13-24 months", "25-48 months", "49+ months"]
)

# Monthly charge segments
powerbi_df["ChargeSegment"] = pd.cut(
    powerbi_df["MonthlyCharges"],
    bins=[-float("inf"), 40, 80, float("inf")],
    labels=["Low", "Medium", "High"]
)

# Convert churn into numeric flag
powerbi_df["ChurnFlag"] = (
    powerbi_df["Churn"] == "Yes"
).astype(int)

# Identify high-value + high-risk customers
powerbi_df["HighValueHighRisk"] = (
    (powerbi_df["MonthlyCharges"] >= 80)
    & (powerbi_df["Contract"] == "Month-to-month")
    & (powerbi_df["tenure"] <= 12)
).astype(int)

# Export dataset
powerbi_df.to_csv(
    "data/cleaned/powerbi_customer_analysis.csv",
    index=False
)

print("Power BI analysis dataset exported successfully.")