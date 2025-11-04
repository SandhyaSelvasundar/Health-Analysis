import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, 'dataset1.xlsx')

data = pd.read_excel(data_path)
data['PULSE'] = data['PULSE'].fillna(data['PULSE'].median())
data['SpO2'] = data['SpO2'].fillna(data['SpO2'].median())

X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

classifier = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=0)
classifier.fit(X_train, y_train)

model_path = os.path.join(BASE_DIR, 'model.pkl')
joblib.dump(classifier, model_path)
