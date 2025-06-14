from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import joblib

df = pd.read_csv('data/weather_data.csv')

X = df.drop(columns=['Rainfall'])
Y = df['Rainfall']

# Train-Test Split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Model: Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, Y_train)

# Predictions
Y_pred = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(Y_test, Y_pred)
report = classification_report(Y_test, Y_pred)

print(f"Accuracy: {accuracy:.2f}")
print("Classification Report: \n", report)

# Save Model
joblib.dump(model, 'model/rainfall_model.pkl')