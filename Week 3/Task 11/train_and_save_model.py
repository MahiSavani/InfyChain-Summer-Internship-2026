"""
train_and_save_model.py
Task 9 - End-to-End Data Science Project
Trains the Random Forest model (from Task 8) on the full training data
and saves everything needed for deployment:
  - model.pkl            -> trained RandomForestRegressor
  - encoders.pkl          -> LabelEncoders for each categorical column
  - feature_defaults.pkl  -> median/mode values for every feature (used to
                              fill in fields the user doesn't manually enter)
  - feature_columns.pkl   -> exact column order the model expects
"""

import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# 1. Load data
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

target = 'SalePrice'
y = train[target]
train_features = train.drop(columns=[target])

# 2. Combine train + test so preprocessing/encoding is consistent
combined = pd.concat([train_features, test], axis=0, ignore_index=True)

num_cols = combined.select_dtypes(include=[np.number]).columns.tolist()
cat_cols = combined.select_dtypes(include=['object']).columns.tolist()
if 'Id' in num_cols:
    num_cols.remove('Id')

# 3. Handle missing values
num_medians = {}
for c in num_cols:
    med = combined[c].median()
    num_medians[c] = med
    combined[c] = combined[c].fillna(med)

for c in cat_cols:
    combined[c] = combined[c].fillna('None')

# 4. Encode categorical columns, save encoders
encoders = {}
for c in cat_cols:
    le = LabelEncoder()
    combined[c] = le.fit_transform(combined[c].astype(str))
    encoders[c] = le

# 5. Split back into train features
n_train = train.shape[0]
X_train_full = combined.iloc[:n_train].drop(columns=['Id']).reset_index(drop=True)

feature_columns = X_train_full.columns.tolist()

# 6. Build "defaults" dict: most common / median value for EVERY feature,
#    used later to auto-fill any field the user doesn't type in manually.
feature_defaults = {}
for c in feature_columns:
    if c in cat_cols:
        # store as the ENCODED mode (most frequent encoded value)
        feature_defaults[c] = int(X_train_full[c].mode()[0])
    else:
        feature_defaults[c] = float(X_train_full[c].median())

# 7. Train final Random Forest model on full training data
model = RandomForestRegressor(n_estimators=300, random_state=42, n_jobs=-1)
model.fit(X_train_full, y)

print("Model trained. Train R^2:", model.score(X_train_full, y))

# 8. Save all artifacts
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('encoders.pkl', 'wb') as f:
    pickle.dump(encoders, f)

with open('feature_defaults.pkl', 'wb') as f:
    pickle.dump(feature_defaults, f)

with open('feature_columns.pkl', 'wb') as f:
    pickle.dump(feature_columns, f)

print("Saved: model.pkl, encoders.pkl, feature_defaults.pkl, feature_columns.pkl")
