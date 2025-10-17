#scikit classification example - golixco
"""
Advanced Example: Scikit-learn Classification

This script demonstrates using scikit-learn to perform a classification task.
It loads a built-in dataset (breast cancer), preprocesses features,
trains a logistic regression model, and evaluates performance on a test set.
"""
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset: features (X) and binary target (y)
data = load_breast_cancer()
X, y = data.data, data.target  # Features and labels

# Split into training and testing sets (70% train, 30% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)

# Preprocess features by standardizing (mean=0, variance=1)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # fit on train, transform train
X_test_scaled = scaler.transform(X_test)        # use same transform on test

# Train a logistic regression classifier
clf = LogisticRegression()
clf.fit(X_train_scaled, y_train)  # fit model to training data

# Predict on the test set
y_pred = clf.predict(X_test_scaled)

# Evaluate the classifier: accuracy and detailed report
accuracy = accuracy_score(y_test, y_pred)
print(f"Test Accuracy: {accuracy:.2f}")
print(classification_report(y_test, y_pred, target_names=data.target_names))

