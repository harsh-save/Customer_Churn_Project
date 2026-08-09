# Data Cleaning Report

## Objective
Data cleaning is the process of identifying and correcting data quality issues before performing exploratory analysis and machine learning.

### Cleaning activities performed

- Loaded the raw dataset without modifying the original source.
- Created a working copy for preprocessing.
- Standardized column names.
- Checked for duplicate records.
- Checked for duplicate customer IDs.
- Identified missing values.
- Converted `total_charges` to a numeric data type.
- Investigated missing values in `churn_reason`.
- Checked categorical values for inconsistencies.
- Validated numerical ranges.
- Applied business-rule checks.
- Performed an initial outlier investigation.
- Validated the final dataset.
- Saved the cleaned dataset to the processed data directory and Postgresql database.

The cleaned dataset will be used as the input for the Exploratory Data Analysis phase.