# 📊 Data Science Summer Internship — 2026

**Intern:** Mahi Savani (24AIML059)
**Program:** InfyChain Tech Solutions Pvt. Ltd.
**Role:** AIML, Data Analyst Intern

A complete, task-based data science internship covering the full pipeline — data cleaning,
visualization, EDA, dashboarding, feature engineering, machine learning, unsupervised
learning, time series forecasting, and end-to-end model deployment — applied to real,
Kaggle-sourced datasets and delivered as version-controlled, documented GitHub projects.

---

## Repository Structure

```
├── Week-1/
│   ├── Task-1/   # Titanic — Data Cleaning & Preprocessing
│   ├── Task-2/   # Iris — Data Visualization
│   ├── Task-3/   # Netflix — Exploratory Data Analysis
│   └── Task-4/   # Sales Dataset — Cleaning & Basic EDA
├── Week-2/
│   ├── Task-5/   # Power BI — Interactive Dashboard
│   ├── Task-6/   # Web Scraping — Data Collection
│   └── Task-7/   # Insights & Trends Analysis on Scraped Data
├── Week 3/
│   ├── Task 8/    # Feature Engineering on Real-World Datasets
│   ├── Task 9/    # Supervised ML Algorithms (Linear Regression, Decision Tree, KNN)
│   ├── Task 10/   # Unsupervised ML Algorithms (K-Means, Hierarchical Clustering)
│   └── Task 11/   # Building & Evaluating Prediction Models
└── Week 4/Task 12/
    ├── Backend/    # Flask REST API serving the trained model
    ├── Dataset/    # Ames House Price dataset
    ├── Frontend/   # Deployment UI
    └── README.md   # Task 12–15: End-to-end ML project, GitHub workflow, Flask deployment
```
---

## 📅 Week 1 — Data Cleaning & Visualization

**Project:** Data Cleaning and Visualization using various datasets

| Task | Dataset | Description |
|------|---------|-------------|
| **Task 1** | Titanic | Handled missing values (`Age`, `Cabin`, `Embarked`), removed duplicates and irrelevant features, encoded categorical variables (`Sex`, `Embarked`) using Label Encoding |
| **Task 2** | Iris | Built bar charts, histograms, and scatter plots (Matplotlib/Seaborn); visualized feature distributions and species-wise comparisons; used pair plots for inter-feature relationships |
| **Task 3** | Netflix | Analyzed content type distribution (Movies vs. TV Shows), country-, genre-, and rating-wise trends; visualized release year and duration trends; identified top contributing countries and genres |
| **Task 4** | Sales Dataset | Cleaned sales data (nulls, data types, outliers); explored trends across categories, regions, and time periods; generated summary statistics and visualizations |

**Tools:** Python, Pandas, NumPy, Matplotlib, Seaborn, Jupyter/Google Colab

---

## 📅 Week 2 — Dashboards & Web Scraping

**Project:** Dashboard Making using Power BI & Dataset making using Web Scraping

| Task | Description |
|------|-------------|
| **Task 5** | Introduction to Power BI — imported and modeled datasets; built an interactive dashboard with slicers and filters |
| **Task 6** | Web Scraping — collected structured data from online sources using BeautifulSoup and Requests; stored results as CSV |
| **Task 7** | Insights & Trends Analysis on the scraped dataset — identified key patterns, trends, and outliers; presented findings through charts |

**Tools:** Power BI, Python, BeautifulSoup, Requests, Pandas, Matplotlib, Seaborn

---

## 📅 Week 3 — Machine Learning Fundamentals

**Project:** Machine Learning Fundamentals: Feature Engineering, Algorithm Exploration & Predictive Modelling

| Task | Description |
|------|-------------|
| **Task 8** | Feature Engineering on real-world datasets — encoding, scaling, feature selection, and derived features |
| **Task 9** | Exploring Supervised ML Algorithms — implemented Linear Regression, Decision Tree, and KNN classifiers |
| **Task 10** | Exploring Unsupervised ML Algorithms — K-Means and hierarchical clustering; compared model outputs |
| **Task 11** | Building & Evaluating Prediction Models — trained models on Kaggle datasets; evaluated using accuracy, precision, and RMSE |

**Tools:** Scikit-learn, Pandas, NumPy, Matplotlib, Seaborn

---

## 📅 Week 4 — End-to-End Project, GitHub & Deployment

**Project:** End-to-End Data Science Project Development, GitHub Collaboration & Flask-Based Model Deployment

| Task | Description |
|------|-------------|
| **Task 12** | End-to-End ML Project on the **Ames House Price** dataset — completed full pipeline: data cleaning, EDA, feature engineering, model training and evaluation |
| **Task 13** | GitHub Collaboration & Version Control — branching, pull requests, merge conflict resolution, collaborative workflows |
| **Task 14** | Model Deployment using Flask — built a REST API to serve the trained ML model; tested via browser and Postman |
| **Task 15** | Project Documentation & Final Submission — wrote a detailed README, documented model results, deployed the project on GitHub |

**Tools:** Scikit-learn, Flask, Git/GitHub, Streamlit (dashboarding variant), Postman

### Task 12 — House Price Prediction (Highlight Project)
- **Dataset:** Ames House Price (1,460 train / 1,459 test records, 79 features)
- **Preprocessing:** Median imputation for numeric columns, `'None'` category for categoricals, Label Encoding
- **Models compared:**

  | Model | RMSE | R² |
  |---|---|---|
  | Linear Regression | ≈34,900 | ≈0.84 |
  | Decision Tree | ≈39,600 | ≈0.79 |
  | **Random Forest** | **≈28,500** | **≈0.89** |

- **Result:** Random Forest selected as the final model, retrained on the full training set, and served through a Flask API / Streamlit app for real-time predictions.
- **Top predictors:** `OverallQual`, `GrLivArea`, `TotalBsmtSF`, `GarageCars`, `GarageArea`

---

## 🛠️ Overall Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.x |
| Data Manipulation | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Dashboarding | Power BI, Streamlit |
| Machine Learning | Scikit-learn (Linear Regression, Decision Tree, KNN, Random Forest, K-Means) |
| Time Series | Statsmodels, Facebook Prophet |
| Web Scraping | BeautifulSoup, Requests |
| Deployment | Flask, Streamlit Community Cloud |
| Dataset Sourcing | Kaggle API |
| Dev Environment | VS Code, Jupyter Notebook, Google Colab |
| Version Control | Git, GitHub |

---

## 🔁 Standard Workflow (per task)

```
Kaggle API → Local CSV Dataset
      ↓
Data Cleaning & Preprocessing (Pandas)
      ↓
Exploratory Analysis / Modeling (Pandas, Scikit-learn, Statsmodels)
      ↓
Visualization (Matplotlib, Seaborn, Plotly)
      ↓
Interactive Dashboard (Streamlit / Power BI, where applicable)
      ↓
GitHub Repository (Documentation & Version Control)
```

---

## 📈 Results Summary

| Task | Key Result |
|---|---|
| Task 1 | Clean dataset with zero missing values in key columns |
| Task 2 | Five visualizations clearly separating Iris species by petal measurements |
| Task 3 | Identified peak content-adding year and top content-producing country (Netflix) |
| Task 4 | Fully interactive, filterable dashboard deployed live via Streamlit Cloud |
| Task 5 | Interactive Power BI dashboard with slicers/filters |
| Task 6–7 | Web-scraped dataset with identified trends, patterns, and outliers |
| Task 8–11 | Feature-engineered pipeline; supervised & unsupervised models trained and evaluated |
| Task 12 | Random Forest achieved best performance (RMSE ≈ 28,500, R² ≈ 0.89) on house price prediction |
| Task 13 | Collaborative Git workflow with branches and pull requests |
| Task 14 | Flask REST API serving live model predictions |
| Task 15 | Fully documented, deployed, and submitted project |

---

## 📜 Certification

Internship completion certified by **InfyChain Tech Solutions Pvt. Ltd.** (Pratham Kapopara,
CEO), confirming successful completion of the Data Analyst Intern role covering Data Science,
Machine Learning, Web Scraping, Data Preprocessing, and Power BI Business Intelligence.

A detailed academic **Summer Internship Report (AIML306)**, supervised by Dr. Jalpesh Vasa
and Mr. Renish Kanpariya, was submitted to Charotar University of Science & Technology
(CHARUSAT) in fulfillment of the B.Tech program requirements.

---

## 📚 References

1. Kaggle Datasets — Titanic, Iris, Netflix Titles, Superstore, Mall Customers, Stock Exchange Data, Ames House Price
2. [Pandas Documentation](https://pandas.pydata.org/docs/)
3. [Scikit-learn Documentation](https://scikit-learn.org/stable/)
4. [Statsmodels Documentation](https://www.statsmodels.org/stable/)
5. [Streamlit Documentation](https://docs.streamlit.io/)
6. [Flask Documentation](https://flask.palletsprojects.com/)
7. GitHub Docs — Collaboration & Pull Requests
