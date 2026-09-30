# Customer Churn & Retention Analytics — Business Insights

## 1. Executive Summary

The analysis of 7,043 telecom customers shows an overall churn rate of 26.54%.

Churn is concentrated among customers with shorter tenure, month-to-month contracts, fiber optic internet service, and electronic check payment methods.

The analysis also identified a high-value, high-risk customer segment consisting of customers with monthly charges of at least 80, month-to-month contracts, and tenure of 12 months or less. This segment contains 468 customers and has a churn rate of 73.29%.

These findings can help prioritize customer retention efforts toward segments where churn is most concentrated.
## 2. Overall Churn

- Total customers: 7,043
- Churned customers: 1,869
- Retained customers: 5,174
- Overall churn rate: 26.54%
- Total monthly charges: 456,116.60
- Monthly charges associated with churned customers: 139,130.85
- Revenue exposure: 30.50%

### Interpretation

Approximately one in four customers in the dataset has churned. Customers who churned account for 30.50% of the total monthly charges in this snapshot.

This indicates that churn is not only a customer-count issue but also represents a meaningful share of the monthly charges associated with the customer base.
## 3. Churn by Contract

| Contract Type | Customers | Churned | Churn Rate |
|---|---:|---:|---:|
| Month-to-month | 3,875 | 1,655 | 42.71% |
| One year | 1,473 | 166 | 11.27% |
| Two year | 1,695 | 48 | 2.83% |

### Interpretation

Month-to-month customers have a substantially higher observed churn rate than customers on one-year or two-year contracts.

The analysis shows a clear association between contract type and churn in this dataset. However, this analysis does not establish that contract type itself causes churn.

### Business Consideration

The company could investigate retention initiatives for month-to-month customers, such as:

- Targeted retention offers before renewal or cancellation.
- Incentives for customers considering longer-term contracts.
- Early engagement programs for newly acquired month-to-month customers.
## 4. Churn by Tenure

| Tenure Group | Customers | Churned | Churn Rate |
|---|---:|---:|---:|
| 0–12 months | 2,186 | 1,037 | 47.44% |
| 13–24 months | 1,024 | 294 | 28.71% |
| 25–48 months | 1,594 | 325 | 20.39% |
| 49+ months | 2,239 | 213 | 9.51% |

### Interpretation

Customers in their first 12 months have the highest observed churn rate at 47.44%. The churn rate decreases across the longer-tenure groups, reaching 9.51% among customers with 49+ months of tenure.

### Business Consideration

The first year represents an important period for retention efforts. The company could consider:

- Stronger onboarding for new customers.
- Early check-ins during the first year.
- Identifying newly acquired customers showing signs of disengagement.
- Retention offers before the first contract renewal.
## 5. Churn by Internet Service

| Internet Service | Customers | Churned | Churn Rate |
|---|---:|---:|---:|
| Fiber optic | 3,096 | 1,297 | 41.89% |
| DSL | 2,421 | 459 | 18.96% |
| No internet | 1,526 | 113 | 7.40% |

### Interpretation

Fiber optic customers have an observed churn rate of 41.89%, which is substantially higher than DSL customers at 18.96% and customers without internet service at 7.40%.

The dataset does not contain enough information to determine why fiber optic customers churn more frequently. Factors such as pricing, service experience, competition, or customer expectations would require additional data to investigate.

### Business Consideration

The company could investigate the fiber optic customer journey in more detail, particularly:

- Pricing and plan competitiveness.
- Service quality and reliability.
- Customer support experience.
- Retention offers for high-risk fiber customers.
## 6. Churn by Payment Method

| Payment Method | Customers | Churned | Churn Rate |
|---|---:|---:|---:|
| Electronic check | 2,365 | 1,071 | 45.29% |
| Mailed check | 1,612 | 308 | 19.11% |
| Bank transfer (automatic) | 1,544 | 258 | 16.71% |
| Credit card (automatic) | 1,522 | 232 | 15.24% |

### Interpretation

Customers using electronic check have the highest observed churn rate at 45.29% among the payment methods analyzed.

The dataset alone does not explain why this group has higher churn. Further investigation would be required before attributing the difference to the payment method itself.

### Business Consideration

The company could examine whether customers using electronic check are more likely to experience payment friction or other differences in their customer journey. It could also evaluate whether customers are willing to use automatic payment options when appropriate.
## 7. High-Value + High-Risk Customer Segment

### Segment Definition

A customer is classified as high-value and high-risk when:

- Monthly charges >= 80
- Contract = Month-to-month
- Tenure <= 12 months

### Results

| Metric | Value |
|---|---:|
| Customers in segment | 468 |
| Churned customers | 343 |
| Churn rate | 73.29% |
| Total monthly charges | 42,119.85 |
| Monthly charges associated with churned customers | 31,005.35 |

### Interpretation

The segment contains 468 customers, of whom 343 are churned, resulting in an observed churn rate of 73.29%.

This segment combines relatively high monthly charges with a month-to-month contract and short tenure, making it a useful group for targeted retention analysis.

### Business Consideration

The company could prioritize this segment for further investigation and targeted retention initiatives, such as:

- Early-tenure engagement programs.
- Personalized retention offers.
- Review of pricing and plan options.
- Proactive customer support.
- Incentives for suitable longer-term contracts.
## 8. Data Limitations

This analysis is based on a cross-sectional telecom customer dataset with a churn label. The dataset does not provide monthly customer snapshots or detailed historical events.

Therefore:

- The analysis identifies associations with churn but does not establish causation.
- The analysis does not predict future churn.
- The dataset does not contain detailed customer complaints, support-ticket history, or service-usage frequency.
- The high-value and high-risk thresholds were defined as analytical segmentation rules for this project.
- Additional operational and customer-interaction data would be required to investigate the reasons behind the observed patterns.
## 9. Conclusion

The analysis shows that customer churn is concentrated in specific customer segments rather than being evenly distributed across the customer base.

The strongest observed patterns are:

- Higher churn among month-to-month customers.
- Higher churn among customers with shorter tenure.
- Higher observed churn among fiber optic customers.
- Higher observed churn among electronic check users.
- A particularly high observed churn rate within the defined high-value + high-risk segment.

These findings can be used as a starting point for targeted retention analysis. The next step for a real business would be to combine these findings with customer behavior, service-quality, pricing, support, and historical interaction data to understand the underlying reasons for churn and evaluate retention actions.
