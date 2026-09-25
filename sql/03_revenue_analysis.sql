-- Customer Churn & Retention Analytics
-- File: 03_revenue_analysis.sql
-- Purpose: Analyze revenue exposure associated with customer churn


-- 1. Overall monthly revenue and revenue associated with churned customers
SELECT
    ROUND(SUM(MonthlyCharges), 2) AS total_monthly_revenue,
    ROUND(
        SUM(CASE
            WHEN Churn = 'Yes' THEN MonthlyCharges
            ELSE 0
        END),
        2
    ) AS churned_monthly_revenue,
    ROUND(
        SUM(CASE
            WHEN Churn = 'Yes' THEN MonthlyCharges
            ELSE 0
        END) * 100.0 / SUM(MonthlyCharges),
        2
    ) AS revenue_at_risk_percent
FROM customers;


-- 2. Average monthly charges: churned vs retained
SELECT
    Churn,
    COUNT(*) AS total_customers,
    ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charge,
    ROUND(SUM(MonthlyCharges), 2) AS total_monthly_charges
FROM customers
GROUP BY Churn;


-- 3. Revenue associated with churned customers by contract
SELECT
    Contract,
    COUNT(*) AS churned_customers,
    ROUND(SUM(MonthlyCharges), 2) AS churned_monthly_revenue
FROM customers
WHERE Churn = 'Yes'
GROUP BY Contract
ORDER BY churned_monthly_revenue DESC;


-- 4. Revenue associated with churned customers by internet service
SELECT
    InternetService,
    COUNT(*) AS churned_customers,
    ROUND(SUM(MonthlyCharges), 2) AS churned_monthly_revenue
FROM customers
WHERE Churn = 'Yes'
GROUP BY InternetService
ORDER BY churned_monthly_revenue DESC;