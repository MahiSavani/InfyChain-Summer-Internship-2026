# Task 1 — Titanic Dataset: Data Cleaning & Preprocessing

**Week:** 1
**Dataset:** [Titanic Dataset](https://www.kaggle.com/datasets/yasserh/titanic-dataset) (891 passenger records, Kaggle)
**Category:** Data Cleaning & Preprocessing

## 🎯 Objective
Clean and preprocess the raw Titanic passenger dataset to prepare it for downstream
analysis and modeling.

## 🛠️ Work Done
- Imputed missing **Age** values with the column **median**
- Filled missing **Embarked** values with the column **mode**
- Dropped the **Cabin** column due to a high proportion of missing data
- Removed duplicate entries and irrelevant features
- Converted key columns (`Survived`, `Pclass`, `Sex`) to categorical types
- Encoded categorical variables (`Sex`, `Embarked`) using Label Encoding
- Renamed all columns to a consistent `snake_case` format for downstream usability

## ✅ Result
A clean dataset with zero missing values in key columns, ready for exploratory analysis
and modeling.

## 🧰 Tools & Libraries
Python, Pandas, NumPy

## 📚 References
- Pandas Documentation
- Kaggle — Titanic Dataset
