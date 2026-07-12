#!/usr/bin/env python3
"""
Train a Decision Tree Classifier for Kyphosis prediction.

This script loads the kyphosis dataset, trains a model, evaluates it,
and saves the trained model for use by the web application.
"""

import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import os

def load_and_prepare_data():
    """Load the kyphosis dataset and prepare features and target."""
    # Load the dataset
    data_path = os.path.join('..', 'Dataset', 'kyphosis.csv')
    df = pd.read_csv(data_path)
    
    print(f"Dataset loaded successfully!")
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print(f"\nTarget distribution:")
    print(df['Kyphosis'].value_counts())
    
    # Prepare features and target
    X = df[['Age', 'Number', 'Start']]
    y = df['Kyphosis'].map({'present': 1, 'absent': 0})
    
    print(f"\nFeatures shape: {X.shape}")
    print(f"Target shape: {y.shape}")
    
    return X, y

def train_model(X, y):
    """Train a Decision Tree classifier."""
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"\nTraining set size: {X_train.shape[0]}")
    print(f"Test set size: {X_test.shape[0]}")
    
    # Train the model
    model = DecisionTreeClassifier(
        random_state=42,
        max_depth=10,
        min_samples_split=5,
        min_samples_leaf=2
    )
    
    print(f"\nTraining the Decision Tree model...")
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\nModel Performance:")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"\nDetailed Classification Report:")
    print(classification_report(y_test, y_pred, target_names=['absent', 'present']))
    
    print(f"\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    
    # Feature importance
    feature_names = ['Age', 'Number', 'Start']
    feature_importance = pd.DataFrame({
        'feature': feature_names,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    print(f"\nFeature Importance:")
    print(feature_importance)
    
    return model

def save_model(model, filename='model.pkl'):
    """Save the trained model to disk."""
    joblib.dump(model, filename)
    print(f"\nModel saved as '{filename}'")

def main():
    """Main function to train and save the model."""
    print("=" * 50)
    print("KYPHOSIS PREDICTION MODEL TRAINING")
    print("=" * 50)
    
    try:
        # Load and prepare data
        X, y = load_and_prepare_data()
        
        # Train model
        model = train_model(X, y)
        
        # Save model
        save_model(model)
        
        print(f"\n" + "=" * 50)
        print("MODEL TRAINING COMPLETED SUCCESSFULLY!")
        print("=" * 50)
        print(f"The model is ready to be used by the web application.")
        
    except Exception as e:
        print(f"Error during training: {e}")
        raise

if __name__ == "__main__":
    main()