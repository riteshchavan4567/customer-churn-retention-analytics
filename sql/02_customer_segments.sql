-- Customer Churn & Retention Analytics
-- File: 02_customer_segments.sql
-- Purpose: Identify high-risk and high-value customer segments


-- 1. Churn by contract and tenure
SELECT
    Contract,
    CASE
        WHEN tenure <= 12 THEN '0-12 months'
        WHEN tenure <= 24 THEN '13-24 months'
        WHEN tenure <= 48 THEN '25-48 months'
        ELSE '49+ months'
    END AS tenure_group,
    COUNT(*) AS total_customers,
    SUM(Churn = 'Yes') AS churned_customers,
    ROUND(SUM(Churn = 'Yes') * 100.0 / COUNT(*), 2) AS churn_rate
FROM customers
GROUP BY
    Contract,
    tenure_group
ORDER BY churn_rate DESC;


-- 2. Customer segments based on monthly charges
SELECT
    CASE
        WHEN MonthlyCharges < 40 THEN 'Low'
        WHEN MonthlyCharges < 80 THEN 'Medium'
        ELSE 'High'
    END AS charge_segment,
    COUNT(*) AS total_customers,
    SUM(Churn = 'Yes') AS churned_customers,
    ROUND(SUM(Churn = 'Yes') * 100.0 / COUNT(*), 2) AS churn_rate,
    ROUND(SUM(MonthlyCharges), 2) AS monthly_charges
FROM customers
GROUP BY charge_segment
ORDER BY churn_rate DESC;


-- 3. High-value + high-risk customer segment
SELECT
    COUNT(*) AS high_value_high_risk_customers,
    SUM(Churn = 'Yes') AS churned_customers,
    ROUND(SUM(MonthlyCharges), 2) AS monthly_charges,
    ROUND(
        SUM(Churn = 'Yes') * 100.0 / COUNT(*),
        2
    ) AS churn_rate
FROM customers
WHERE MonthlyCharges >= 80
  AND Contract = 'Month-to-month'
  AND tenure <= 12;


-- 4. Churned customers within the high-value + high-risk segment
SELECT
    COUNT(*) AS churned_high_value_high_risk,
    ROUND(SUM(MonthlyCharges), 2) AS churned_monthly_charges
FROM customers
WHERE MonthlyCharges >= 80
  AND Contract = 'Month-to-month'
  AND tenure <= 12
  AND Churn = 'Yes';