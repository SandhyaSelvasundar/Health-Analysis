import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
# from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, 'dataset1.xlsx')

# Load and clean data
data = pd.read_excel(data_path)
data['PULSE'] = data['PULSE'].fillna(data['PULSE'].median())
data['SpO2'] = data['SpO2'].fillna(data['SpO2'].median())

# Features and labels
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# Train model
classifier = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=0)
classifier.fit(X_train, y_train)

# Predict on test set
# y_pred = classifier.predict(X_test)

# # Calculate accuracy
# accuracy = accuracy_score(y_test, y_pred)
# print("Model Accuracy:", accuracy)
# print(data.iloc[:, -1].value_counts())
# print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
# print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save model
model_path = os.path.join(BASE_DIR, 'model.pkl')
joblib.dump(classifier, model_path)
