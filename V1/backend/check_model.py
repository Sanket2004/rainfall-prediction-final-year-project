import joblib
import pandas as pd

# Load trained rainfall model
loaded_model = joblib.load('model/rainfall_model.pkl')

# Sample input data
input_data = pd.DataFrame([[25.0, 85.0, 1005.0, 5.0, 70.0]], columns=[
    'Temperature(C)', 'Humidity(%)', 'Pressure(hPa)', 'WindSpeed(km/h)', 'CloudCover(%)'
])

# Function to generate rule-based risk summary
def summarize_risk_factors(data):
    desc = []
    if data['Humidity(%)'].values[0] > 80:
        desc.append("high humidity")
    if data['Pressure(hPa)'].values[0] < 1005:
        desc.append("low pressure")
    if data['CloudCover(%)'].values[0] > 70:
        desc.append("dense cloud cover")
    if data['WindSpeed(km/h)'].values[0] > 10:
        desc.append("strong wind")
    if data['Temperature(C)'].values[0] > 35:
        desc.append("very high temperature")
    elif data['Temperature(C)'].values[0] < 5:
        desc.append("very low temperature")
    return ", ".join(desc) if desc else "normal conditions"

# Function to generate rule-based precautions
def generate_precautions(summary):
    precautions = []
    if "high humidity" in summary:
        precautions.append("Wear breathable clothes")
    if "low pressure" in summary:
        precautions.append("Carry an umbrella")
    if "dense cloud cover" in summary:
        precautions.append("Be prepared for poor visibility")
    if "strong wind" in summary:
        precautions.append("Secure loose objects outdoors")
    if "very high temperature" in summary:
        precautions.append("Stay hydrated and avoid sun exposure")
    if "very low temperature" in summary:
        precautions.append("Wear warm clothing and stay indoors if possible")
    if not precautions:
        precautions.append("No special precautions needed")
    return precautions

# Predict rainfall
prediction = loaded_model.predict(input_data)[0]
rainfall_status = "Yes" if prediction == 1 else "No"

# Generate risk summary and precautions
risk_summary = summarize_risk_factors(input_data)
precaution_list = generate_precautions(risk_summary)

# Output results
print("RainfallPrediction:", rainfall_status)
print("Risk Summary:", risk_summary)
print("Precautions:")
for i, p in enumerate(precaution_list, 1):
    print(f"{i}. {p}")
