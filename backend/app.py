from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Load the trained model
model = joblib.load("rainfall_model.pkl")

# Define prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    # Parse input JSON data
    data = request.get_json()
    input_data = pd.DataFrame([data])  # Convert JSON to DataFrame

    # Predict using the model
    prediction = model.predict(input_data)
    result = {"rainfall": "Yes" if prediction[0] == 1 else "No"}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
