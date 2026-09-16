# Customer Churn Prediction

An end-to-end Machine Learning project that predicts whether a customer is likely to churn based on their demographic, service, account, and billing information.

## 🚀 Live Application

**Try the deployed application:**
[Customer Churn Prediction App](https://customerchurnproject-ykhp92gnqncpmrklxtvogy.streamlit.app/)

---

## 📌 Project Overview

Customer churn is an important business problem for subscription-based companies. Identifying customers who are likely to leave can help businesses take proactive retention measures.

This project follows the **CRISP-DM (Cross-Industry Standard Process for Data Mining)** methodology to structure the complete Machine Learning workflow, from understanding the business problem to deploying the final model.

### CRISP-DM Workflow

```text
Business Understanding
        ↓
Data Understanding
        ↓
Data Preparation
        ↓
Modeling
        ↓
Evaluation
        ↓
Deployment
```

### How CRISP-DM Was Applied

| CRISP-DM Phase             | Project Implementation                                                                                                       |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **Business Understanding** | Defined customer churn as the primary business problem and identified the objective of predicting customers likely to churn. |
| **Data Understanding**     | Explored customer demographics, services, tenure, contracts, billing information, and churn patterns through EDA.            |
| **Data Preparation**       | Cleaned the dataset, performed feature engineering, encoded categorical variables, and scaled numerical features.            |
| **Modeling**               | Trained and evaluated multiple classification approaches and selected a Random Forest classifier for the final pipeline.     |
| **Evaluation**             | Evaluated the model using classification metrics, confusion matrix, and feature importance analysis.                         |
| **Deployment**             | Serialized the complete ML pipeline and deployed a Streamlit application for real-time customer churn predictions.           |

---

## 🎯 Objective

The primary objective is to build a machine learning model that can predict whether a customer will:

* **Churn**
* **Not Churn**

The model can serve as a foundation for identifying customers who may require targeted retention strategies.

---

## 🔎 1. Business Understanding

The project begins by defining the business problem:

> **Can we predict whether a customer is likely to churn based on their available customer information?**

The analysis focuses on understanding the factors associated with customer churn and translating those findings into useful features for a predictive model.

---

## 📊 2. Data Understanding

The dataset contains information related to:

* Customer demographics
* Tenure
* Internet and phone services
* Additional services
* Contract information
* Billing information
* Payment methods
* Monthly charges
* Total charges
* Customer churn status

The target variable is:

```text
Churn
```

Exploratory Data Analysis was structured around business-oriented questions to understand how different customer characteristics relate to churn.

---

## 🛠️ 3. Data Preparation

The data preparation stage included:

* Data cleaning
* Exploratory analysis
* Deep-dive analysis
* Feature engineering
* Numerical feature scaling
* Categorical feature encoding
* Construction of a unified preprocessing pipeline

Feature engineering was guided by observations from the EDA and deep-dive analysis.

For example, customers were classified based on tenure to distinguish relatively established customers from newer customers.

```text
tenure_months > 13 → Established Customer
```

The preprocessing transformations and model were combined into a single Scikit-learn pipeline to ensure consistent processing during deployment.

---

## 🤖 4. Modeling

Different classification approaches were considered during model development.

The final solution uses a:

```text
Random Forest Classifier
```

The model was selected after evaluating the candidate models using appropriate classification metrics and considering its ability to capture non-linear relationships between customer characteristics and churn.

### Final ML Pipeline

```text
Customer Input
      ↓
Preprocessing Pipeline
      ├── Numerical Scaling
      └── Categorical Encoding
      ↓
Random Forest Classifier
      ↓
Churn Prediction
```

---

## 📈 5. Evaluation

The model was evaluated using multiple classification metrics, including:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix
* Feature Importance

Feature importance analysis was also performed to understand which customer characteristics contributed most to the model's predictions.

The evaluation stage ensured that the final model was suitable for integration into the prediction application.

---

## 🌐 6. Deployment

The final preprocessing and model pipeline was serialized using `joblib`.

```text
models/
└── customer_churn_pipeline.joblib
```

A Streamlit application was then developed to provide an interactive interface for making customer churn predictions.

### Deployment Workflow

```text
User Input
    ↓
Streamlit Application
    ↓
Saved ML Pipeline
    ↓
Preprocessing
    ↓
Random Forest
    ↓
Prediction
    ↓
Churn Result
```

### 🔗 Live Application

👉 **[Launch Customer Churn Prediction App](https://customerchurnproject-ykhp92gnqncpmrklxtvogy.streamlit.app/)**


---

## 🧰 Technologies Used

| Technology   | Purpose                          |
| ------------ | -------------------------------- |
| Python       | Programming language             |
| Pandas       | Data manipulation                |
| NumPy        | Numerical operations             |
| Matplotlib   | Data visualization               |
| Seaborn      | Exploratory data visualization   |
| Scikit-learn | Machine Learning & preprocessing |
| Joblib       | Model serialization              |
| PostgreSQL   | Data storage                     |
| Streamlit    | Web application                  |
| Git & GitHub | Version control                  |

---

## 💡 Project Takeaways

This project demonstrates the complete **CRISP-DM-based Machine Learning lifecycle**:

1. **Business Understanding** — Define the churn prediction problem
2. **Data Understanding** — Explore customer behavior and churn patterns
3. **Data Preparation** — Clean, transform, and engineer features
4. **Modeling** — Train and evaluate classification models
5. **Evaluation** — Assess model performance and interpret feature importance
6. **Deployment** — Integrate the final pipeline into a Streamlit application

The project therefore goes beyond model training and demonstrates how a Machine Learning solution can be taken from **business problem → data → model → deployed application**.
