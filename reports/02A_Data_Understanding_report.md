# Exploratory Data Analysis Report
## Customer Churn Analysis

**Project:** Customer Churn Prediction and Analysis  
**Analysis Stage:** Exploratory Data Analysis (EDA)  
**Notebook:** `02a_Data_Understanding.ipynb`  
**Dataset:** Cleaned Customer Churn Dataset

---

## 1. Executive Summary

The objective of this exploratory data analysis is to understand the
characteristics and behavioral patterns associated with customer churn.

The analysis examines customer demographics, tenure, contract type,
services, billing characteristics, payment methods, and relationships
between multiple variables.

The analysis indicates that customer churn is not associated with a single
factor. Instead, several characteristics appear to interact with churn,
with contract type, customer tenure, monthly charges, internet service,
payment method, and service engagement emerging as important areas for
further investigation.

A particularly important customer profile identified during the analysis
is the combination of:

- Short customer tenure
- Month-to-month contract
- Relatively high monthly charges

This segment shows characteristics associated with elevated churn risk.

The findings from this EDA will be used to guide feature engineering,
model preparation, and subsequent machine-learning analysis.

---

# 2. Business Objective

Customer churn represents the loss of existing customers and can negatively
impact recurring revenue and customer lifetime value.

The primary business objective is to understand:

> **Which customer characteristics and behaviors are associated with
> customer churn, and which customer segments appear to have elevated
> churn risk?**

The analysis is intended to support future retention strategies and
provide a foundation for developing a predictive churn model.

---

# 3. Analytical Objectives

The EDA was designed to answer the following questions:

1. What proportion of customers have churned?
2. Which demographic characteristics are associated with churn?
3. How does customer tenure relate to churn?
4. How does contract type relate to churn?
5. How do services and service engagement relate to churn?
6. How do billing and payment characteristics relate to churn?
7. How do multiple customer characteristics interact with churn?
8. Which customer segments appear to have elevated churn risk?
9. Which variables should be considered during feature engineering and
   predictive modeling?

---

# 4. Dataset Overview

The analysis uses the cleaned customer churn dataset generated during the
data-cleaning stage.

The dataset contains customer-level information covering:

- Customer demographics
- Customer tenure
- Contract information
- Internet and additional services
- Billing information
- Payment methods
- Churn status

The target variable is:

```text
churn_value