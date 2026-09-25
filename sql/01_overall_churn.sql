-- Customer Churn & Retention Analytics
-- File: 01_overall_churn.sql
-- Purpose: Analyze overall churn and major churn patterns


-- 1. Overall churn rate
SELECT
    COUNT(*) AS total_customers,
    SUM(Churn = 'Yes') AS churned_customers,
    ROUND(SUM(Churn = 'Yes') * 100.0 / COUNT(*), 2) AS churn_rate
FROM customers;


-- 2. Churn by contract type
SELECT
    Contract,
    COUNT(*) AS total_customers,
    SUM(Churn = 'Yes') AS churned_customers,
    ROUND(SUM(Churn = 'Yes') * 100.0 / COUNT(*), 2) AS churn_rate
FROM customers
GROUP BY Contract
ORDER BY churn_rate DESC;


-- 3. Churn by tenure group
SELECT
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
GROUP BY tenure_group
ORDER BY churn_rate DESC;


-- 4. Churn by internet service
SELECT
    InternetService,
    COUNT(*) AS total_customers,
    SUM(Churn = 'Yes') AS churned_customers,
    ROUND(SUM(Churn = 'Yes') * 100.0 / COUNT(*), 2) AS churn_rate
FROM customers
GROUP BY InternetService
ORDER BY churn_rate DESC;


-- 5. Churn by payment method
SELECT
    PaymentMethod,
    COUNT(*) AS total_customers,
    SUM(Churn = 'Yes') AS churned_customers,
    ROUND(SUM(Churn = 'Yes') * 100.0 / COUNT(*), 2) AS churn_rate
FROM customers
GROUP BY PaymentMethod
ORDER BY churn_rate DESC;


-- 6. Churn by senior-citizen status
SELECT
    SeniorCitizen,
    COUNT(*) AS total_customers,
    SUM(Churn = 'Yes') AS churned_customers,
    ROUND(SUM(Churn = 'Yes') * 100.0 / COUNT(*), 2) AS churn_rate
FROM customers
GROUP BY SeniorCitizen
ORDER BY churn_rate DESC;