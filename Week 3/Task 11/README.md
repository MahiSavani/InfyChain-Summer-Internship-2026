# 🏠 House Price Predictor

End-to-end data science project that trains a machine learning model to predict house
`SalePrice` on the Kaggle **Ames Housing** dataset, then deploys it as an interactive
**Streamlit** web app.

> Internship: Synent Technologies – Data Science Internship Program (InfyChain Tech Solutions)
> Task 8 (Modeling) → Task 9 (Deployment)

---

##  Project Structure

```
.
├── ML_Model_HousePrice.ipynb   # Task 8 — EDA, preprocessing, model training & evaluation
├── train_and_save_model.py     # Retrains the final model and saves deployment artifacts
├── app.py                      # Task 9 — Streamlit web app for live predictions
├── model.pkl                   # Trained RandomForestRegressor
├── encoders.pkl                # LabelEncoders for each categorical column
├── feature_defaults.pkl        # Median/mode value for every feature (auto-fills unentered fields)
├── feature_columns.pkl         # Exact column order the model expects
├── submission.csv              # Final predictions on the Kaggle test set
└── README.md
```

---

##  Workflow

**1. Data Preprocessing**
- Combined `train.csv` and `test.csv` so cleaning/encoding stays consistent across both.
- Filled missing numeric values with the column **median**.
- Filled missing categorical values with `'None'` (many NAs genuinely mean "feature not
  present," e.g. no basement or no garage).
- Encoded all categorical columns with `LabelEncoder`.

**2. Feature Selection**
- Checked correlation with `SalePrice` for interpretability, but kept **all** features since
  tree-based models handle irrelevant ones well.

**3. Model Training & Evaluation**
- Compared **Linear Regression** (baseline), a **Decision Tree**, and a **Random Forest
  Regressor**.
- Evaluated with **RMSE**, **MAE**, and **R²**.
- **Random Forest** won — lowest RMSE, highest R² on the validation set. Top predictors:
  `OverallQual`, `GrLivArea`, and garage/basement size.

**4. Final Model & Predictions**
- Retrained Random Forest on the **full** training set.
- Generated `submission.csv` matching the Kaggle submission format.

**5. Deployment**
- `train_and_save_model.py` saves the final model plus every artifact the app needs
  (`model.pkl`, `encoders.pkl`, `feature_defaults.pkl`, `feature_columns.pkl`).
- `app.py` is a Streamlit UI where a user enters the key house details (quality, size, rooms,
  garage, age, neighborhood, etc.); everything else is auto-filled from `feature_defaults.pkl`
  before the model predicts a price.

---

## 🖥️ Using the App

1. Open the sidebar and fill in the house details:
   - **Size & Quality** — Overall Quality, Living Area, Basement Area, Lot Area
   - **Rooms & Garage** — Total Rooms, Full Bathrooms, Garage Capacity
   - **Age** — Year Built, Year Remodeled
   - **Quality Ratings** — Kitchen Quality, Exterior Quality, Neighborhood
2. Click **🔮 Predict Sale Price**.
3. View the estimated price, plus an expandable table of every feature value sent to the
   model (unfilled fields are auto-populated from the training set's medians/modes).

---

## 🔧 Regenerating the Artifacts

If you retrain or change the model, always regenerate all four `.pkl` files together with
`train_and_save_model.py` — `app.py` expects them to be in sync (same feature order, same
encoders) or predictions will break.

---

## 📊 Model

- **Algorithm:** Random Forest Regressor (`n_estimators=300`, `random_state=42`)
- **Training data:** Kaggle Ames Housing `train.csv` (79 features + target `SalePrice`)
- **Chosen over:** Linear Regression and a single Decision Tree, based on validation RMSE/R²

**Possible next steps:** hyperparameter tuning (`GridSearchCV`), log-transforming the skewed
target, one-hot encoding instead of label encoding, and trying gradient boosting models
(XGBoost/LightGBM) for further improvement.

---

## 🛠️ Tech Stack

- Python, pandas, NumPy
- scikit-learn (RandomForestRegressor, LabelEncoder)
- Streamlit (web app UI)
