import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Load dataset
data = pd.read_csv("weather_data.csv")  # Replace with your dataset file

data.columns = data.columns.str.strip()  # Removes leading/trailing spaces

# Preprocessing
X = data[['pressure', 'maxtemp', 'temparature', 'mintemp', 'dewpoint', 'humidity', 'cloud', 'sunshine', 'winddirection', 'windspeed']]
y = data['rainfall'].apply(lambda x: 1 if x == 'yes' else 0)  # Convert 'yes'/'no' to 1/0

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "rainfall_model.pkl")
print("Model saved as 'rainfall_model.pkl'")