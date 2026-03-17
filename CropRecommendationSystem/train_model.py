import pandas as pd
import numpy as np
import joblib
import os
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, 'data', 'Crop_recommendation.csv')
    model_dir = os.path.join(base_dir, 'model')
    notebooks_dir = os.path.join(base_dir, 'notebooks')

    if not os.path.exists(data_path):
        print(f"Error: Dataset not found at {data_path}. Please download it first.")
        return

    # Load data
    df = pd.read_csv(data_path)
    print("Dataset shape:", df.shape)
    
    # Missing values check
    if df.isnull().sum().sum() > 0:
        print("Handling missing values...")
        df = df.dropna()

    # Features and Target
    X = df.drop('label', axis=1)
    y = df['label']

    # --- EDA: Correlation Heatmap ---
    plt.figure(figsize=(10, 8))
    sns.heatmap(X.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Feature Correlation Heatmap')
    plt.savefig(os.path.join(notebooks_dir, 'correlation_heatmap.png'))
    plt.close()
    print("Saved correlation heatmap to notebooks/correlation_heatmap.png")

    # Encode labels
    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(y)
    
    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Train Test Split
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.2, random_state=42)

    # 1. Decision Tree
    # ----------------
    dt_clf = DecisionTreeClassifier(random_state=42)
    dt_clf.fit(X_train, y_train)
    dt_pred = dt_clf.predict(X_test)
    dt_acc = accuracy_score(y_test, dt_pred)
    print(f"\nDecision Tree Accuracy: {dt_acc * 100:.2f}%")

    # 2. Random Forest
    # ----------------
    rf_clf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_clf.fit(X_train, y_train)
    rf_pred = rf_clf.predict(X_test)
    rf_acc = accuracy_score(y_test, rf_pred)
    print(f"Random Forest Accuracy: {rf_acc * 100:.2f}%")

    # Choose Best Model
    best_model = rf_clf if rf_acc >= dt_acc else dt_clf
    best_name = "Random Forest" if rf_acc >= dt_acc else "Decision Tree"
    print(f"\nBest Model: {best_name} (Accuracy: {max(rf_acc, dt_acc) * 100:.2f}%)")

    # Feature Importance (for Random Forest)
    if best_name == "Random Forest":
        importances = best_model.feature_importances_
        indices = np.argsort(importances)[::-1]
        plt.figure(figsize=(10, 6))
        plt.title("Feature Importances")
        plt.bar(range(X.shape[1]), importances[indices], align="center")
        plt.xticks(range(X.shape[1]), X.columns[indices], rotation=45)
        plt.xlim([-1, X.shape[1]])
        plt.tight_layout()
        plt.savefig(os.path.join(notebooks_dir, 'feature_importance.png'))
        plt.close()
        print("Saved feature importance chart to notebooks/feature_importance.png")

    # Save artifacts
    print("\nSaving artifacts...")
    joblib.dump(best_model, os.path.join(model_dir, 'model.pkl'))
    joblib.dump(scaler, os.path.join(model_dir, 'scaler.pkl'))
    joblib.dump(encoder, os.path.join(model_dir, 'encoder.pkl'))
    print(f"All artifacts saved successfully in {model_dir}/")

    # Detailed Evaluation for Best Model
    print("\nClassification Report (Best Model):")
    print(classification_report(y_test, best_model.predict(X_test), target_names=encoder.classes_))

if __name__ == "__main__":
    main()
