# Final Model Evaluation and Selection

## 1. Model Selection Approach

Multiple classification algorithms were evaluated to identify the most suitable model for predicting customer churn.

The following models were initially considered:

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting

The models were evaluated using **Accuracy, Precision, Recall, F1-score, and ROC-AUC**.

Since the primary objective of this project is to identify customers who are likely to churn, particular importance was given to **Recall and F1-score for the Churn class**.

---

## 2. Baseline Model Evaluation

The initial evaluation showed that Decision Tree consistently underperformed compared with the other models and was therefore removed from further consideration.

Logistic Regression, Random Forest, and Gradient Boosting demonstrated stronger overall performance and were retained for cross-validation and hyperparameter tuning.

---

## 3. Cross-Validation

Five-fold stratified cross-validation was performed on the retained models to evaluate the consistency of their performance across different subsets of the training data.

The results showed that:

- **Logistic Regression** achieved the strongest overall cross-validation performance.
- **Gradient Boosting** achieved the highest ROC-AUC by a small margin.
- **Random Forest** performed slightly below Logistic Regression and Gradient Boosting.

Because the differences were relatively small, Logistic Regression, Random Forest, and Gradient Boosting were retained for hyperparameter tuning rather than selecting a final model based solely on baseline performance.

---

## 4. Hyperparameter Tuning

`RandomizedSearchCV` was used to tune the retained models.

**F1-score** was selected as the primary optimization metric because it provides a balance between Precision and Recall and is particularly useful for the churn prediction problem.

The best cross-validated F1-scores were:

| Model | Best F1-score |
|---|---:|
| Logistic Regression | 0.6326 |
| Random Forest | **0.6365** |
| Gradient Boosting | 0.5882 |

Random Forest achieved the highest F1-score after tuning, while Gradient Boosting showed a significant decline in performance.

Therefore, **Logistic Regression and Random Forest** were selected for final evaluation on the untouched test set.

---

## 5. Final Test Set Evaluation

The tuned Logistic Regression and Random Forest models were evaluated using the previously untouched test set.

| Model | Accuracy | Precision | Recall | F1-score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 76.15% | 53.52% | 77.27% | 63.24% | 85.63% |
| **Random Forest** | **76.79%** | **54.23%** | **80.48%** | **64.80%** | **85.89%** |

Random Forest achieved better performance than Logistic Regression across **all five evaluation metrics**.

The most significant advantage was its higher Recall and F1-score for churn prediction.

---

## 6. Classification Report

The final Random Forest model produced the following results:

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| No Churn | 0.91 | 0.75 | 0.83 | 1035 |
| Churn | 0.54 | **0.80** | **0.65** | 374 |
| **Accuracy** | | | **0.77** | **1409** |

The model achieves approximately **80% recall for the Churn class**, meaning it correctly identifies the majority of customers who actually churn.

The churn precision of approximately **54%** indicates that some customers predicted as churners will not actually churn. This represents a reasonable trade-off because the project prioritizes identifying potential churners and reducing the number of actual churners missed by the model.

---

## 7. Feature Importance

Feature importance was examined to understand which variables contribute most to the Random Forest's predictions.

The most influential features were:

| Rank | Feature | Importance |
|---:|---|---:|
| 1 | Tenure Months | 21.92% |
| 2 | Internet Service – Fiber Optic | 15.04% |
| 3 | Total Charges | 12.76% |
| 4 | Dependents | 10.67% |
| 5 | Payment Method – Electronic Check | 9.67% |
| 6 | Monthly Charges | 8.37% |
| 7 | Internet Service – No | 6.75% |
| 8 | Protection/Support Count | 5.66% |
| 9 | Internet Service – DSL | 3.39% |
| 10 | CLTV | 1.58% |

**Tenure** was the most influential feature, accounting for approximately **21.9%** of the model's impurity-based feature importance.

The importance of tenure, internet service, and customer charges is broadly consistent with the patterns identified during the exploratory data analysis and feature engineering stages.

Feature importance indicates how useful a feature is to the model's predictions and should not be interpreted as evidence of causation.

---

# 8. Final Model Selection

Based on the complete modelling process, **Random Forest was selected as the final model**.

The selection was based on the following factors:

- It achieved the highest F1-score during hyperparameter tuning.
- It achieved the best performance among the final candidates on the untouched test set.
- It achieved the highest Recall for the Churn class.
- It achieved the highest F1-score on the Churn class.
- It achieved the highest ROC-AUC among the final candidates.
- Its performance remained reasonably consistent between cross-validation and final test evaluation.

The final Random Forest model achieved:

- **Accuracy:** 76.79%
- **Precision:** 54.23%
- **Recall:** 80.48%
- **F1-score:** 64.80%
- **ROC-AUC:** 85.89%

The model's **80.48% churn recall** is particularly valuable for the business objective because it allows the company to identify a large proportion of customers who are at risk of leaving.

Although the model has moderate precision, this trade-off is acceptable for a retention-focused use case where missing an actual churner may represent a greater business cost than contacting some customers who ultimately remain.

---

## 9. Final Model Configuration

The selected Random Forest model uses the following hyperparameters:

```python
{
    'n_estimators': 200,
    'max_depth': 5,
    'min_samples_split': 10,
    'min_samples_leaf': 2,
    'max_features': 'sqrt',
    'class_weight': 'balanced',
    'random_state': 42
}