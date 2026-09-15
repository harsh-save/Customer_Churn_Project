# Final Summary: Deep-Dive Customer Churn Analysis

The deep-dive exploratory analysis identified several important patterns and associations related to customer churn.

## 1. Customer Demographics

Gender showed relatively little difference in churn rates between male and female customers, suggesting that it may have a limited association with customer churn.

However, **senior-citizen status, partner status, and dependent status** showed more noticeable differences. Senior citizens generally had higher churn rates than non-senior customers, while customers without partners or dependents were more likely to churn.

The combined demographic analysis revealed particularly high churn among **senior citizens without partners (48.9%)** and **senior citizens without dependents (43.4%)**. In contrast, **non-senior customers with partners (16.6%)** and **non-senior customers with dependents (6.0%)** showed substantially lower churn rates.

These findings suggest that certain demographic characteristics and their combinations may be useful for identifying higher-risk customer segments.

## 2. Contract Type

Contract type demonstrated one of the strongest relationships with customer churn.

Customers on **month-to-month contracts had the highest churn rate (42.7%)**, compared with **11.3% for one-year contracts** and only **2.8% for two-year contracts**.

This indicates a strong association between longer contract durations and lower customer churn, making **contract type a potentially important feature for churn prediction and customer retention strategies**.

## 3. Monthly Charges

Churned customers had slightly higher monthly charges on average than retained customers.

This suggests that customers with higher monthly charges may have a greater tendency to churn. However, the difference between the groups appeared relatively small, indicating that **monthly charges alone may not be a strong predictor of churn**.

Monthly charges may provide more meaningful insights when analyzed alongside other variables such as contract type, tenure, and internet service.

## 4. Geographic Location

City-level churn analysis was restricted to cities with more than **100 customers** to reduce the influence of small sample sizes and produce more meaningful comparisons.

The analysis identified differences in churn rates across cities, suggesting that **geographic location may be associated with customer churn patterns**. Cities with higher churn rates may require further investigation to identify the customer, service, or market-related factors contributing to increased churn.

## 5. Internet Service

Customers using **fiber optic internet service** showed a noticeably higher churn rate than customers using other internet service types.

This indicates a potential association between internet service type and churn. However, this relationship should not be interpreted as causal because other factors—including **contract type, tenure, and monthly charges**—may also influence the observed churn pattern.

Overall, **internet service type appears to be a potentially important feature for predicting customer churn**.

## 6. Additional Services

The analysis of additional services—including online security, online backup, device protection, tech support, streaming TV, and streaming movies—showed variations in churn across service categories.

However, these differences were generally less substantial than those observed for major factors such as **contract type and internet service**.

Additional service subscriptions may still provide useful predictive information when combined with other customer characteristics, even if they are not strong standalone indicators of churn.

## 7. High-CLTV Customers

Customers in the **high and very high CLTV quartiles** were classified as high-CLTV customers for this analysis.

Approximately **77.56% of high-CLTV customers were retained**, while **22.43% had churned**.

Although most high-value customers remained with the company, the loss of more than one-fifth of high-CLTV customers represents a meaningful business concern because losing high-value customers can have a greater financial impact than losing lower-value customers.

## 8. Customer Tenure

The tenure analysis showed that customers with **very short tenure (0–9 months)** had the highest churn rate at **49.38%**.

This means that nearly **1 in every 2 customers** in this early stage of the customer lifecycle had churned.

The finding suggests that the risk of churn is particularly high among newer customers, making the **early customer lifecycle a critical period for retention efforts**.

Customer tenure therefore appears to be an important factor associated with churn and may be a valuable feature for machine learning models.

# Overall Conclusion

The deep-dive analysis indicates that customer churn is most strongly associated with several key factors, particularly:

* **Contract type**
* **Customer tenure**
* **Senior-citizen status**
* **Partner and dependent status**
* **Internet service type**
* **Monthly charges**
* **Customer Lifetime Value (CLTV)**

Among these factors, **month-to-month contracts, short customer tenure, senior-citizen status, and fiber optic internet service** emerged as important characteristics associated with higher customer churn.

These findings provide valuable business insights and establish a strong foundation for the next stage of the project: **feature engineering, machine learning model development, and identifying the most important predictors of customer churn**.

It is important to note that the relationships identified during this exploratory analysis represent **associations rather than causal relationships**. Further statistical analysis and machine learning techniques are required to evaluate the relative importance and predictive power of these features.
