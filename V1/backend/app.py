from flask import Flask, request, jsonify
import joblib
import pandas as pd
import flask_cors

app = Flask(__name__)
flask_cors.CORS(app)

# Load the model once when server starts
model = joblib.load('model/rainfall_model.pkl')

# Rule-based risk summarizer
def summarize_risk_factors(data):
    desc = []
    if data['Humidity(%)'] > 80:
        desc.append("high humidity")
    if data['Pressure(hPa)'] < 1005:
        desc.append("low pressure")
    if data['CloudCover(%)'] > 70:
        desc.append("dense cloud cover")
    if data['WindSpeed(km/h)'] > 10:
        desc.append("strong wind")
    if data['Temperature(C)'] > 35:
        desc.append("very high temperature")
    elif data['Temperature(C)'] < 5:
        desc.append("very low temperature")
    return ", ".join(desc) if desc else "normal conditions"

# Rule-based precaution generator
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




# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        input_df = pd.DataFrame([data])
        prediction = model.predict(input_df)[0]
        rainfall = "Yes" if prediction == 1 else "No"
        summary = summarize_risk_factors(data)
        precautions = generate_precautions(summary)

        if data is None or not all(key in data for key in ['Temperature(C)', 'Humidity(%)', 'Pressure(hPa)', 'WindSpeed(km/h)', 'CloudCover(%)']):
            return jsonify({"error": "Invalid input data"}), 400

        return jsonify({
            "RainfallPrediction": rainfall,
            "RiskSummary": summary,
            "Precautions": precautions
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    



# Load historical data for trends
df = pd.read_csv('data/historical_weather_data.csv')

@app.route('/historical-trends/<area>', methods=['GET'])
def get_historical_trends(area):
    start_date = request.args.get('start_date')  # e.g. '2025-05-01'
    end_date = request.args.get('end_date')      # e.g. '2025-05-15'

    if not area:
        return jsonify({'error': 'Area parameter is required'}), 400

    area_df = df[df['Area'].str.lower() == area.lower()]

    if area_df.empty:
        return jsonify({'error': 'This area is not available'}), 404

    if start_date:
        area_df = area_df[area_df['Date'] >= start_date]
    if end_date:
        area_df = area_df[area_df['Date'] <= end_date]

    # Convert to rainfall trend instead of temperature
    trend = area_df.sort_values('Date')[['Date', 'Rainfall(mm)']].to_dict(orient='records')

    return jsonify({'area': area, 'rainfall_trend': trend})


@app.route("/areas", methods=["GET"])
def get_areas():
    return jsonify(df["Area"].unique().tolist())



    
# Home route for API documentation
@app.route('/', methods=['GET'])
def home():
    return '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rainfall Prediction API Documentation</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,100..1000;1,9..40,100..1000&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {
            font-family: 'DM Sans', sans-serif;
        }
        pre {
            white-space: pre-wrap;
            word-wrap: break-word;
        }
    </style>
</head>
<body class="bg-gray-100 text-gray-900">
    <header class="bg-white shadow-sm text-center">
        <div class="container mx-auto max-w-5xl px-6 py-4">
            <h1 class="text-2xl font-semibold text-gray-900">Rainfall Prediction API Documentation</h1>
            <p class="mt-2 text-sm text-gray-600">Official documentation for the Rainfall Prediction API</p>
        </div>
    </header>

    <main class="container mx-auto max-w-5xl px-6 py-8">
        <!-- Introduction -->
        <section class="bg-white rounded-lg shadow-sm p-6 mb-8">
            <h2 class="text-xl font-semibold text-gray-900 mb-4">Introduction</h2>
            <p class="text-gray-600">
                The Rainfall Prediction API provides accurate rainfall predictions based on meteorological inputs such as temperature, humidity, pressure, wind speed, and cloud cover. Use the <code class="bg-gray-200 text-gray-800 px-1 py-0.5 rounded">/predict</code> endpoint to access predictions.
            </p>
        </section>

        <!-- API Endpoint -->
        <section class="bg-white rounded-lg shadow-sm p-6 mb-8">
            <h2 class="text-xl font-semibold text-gray-900 mb-4">API Endpoint</h2>
            <div class="overflow-x-auto">
                <table class="w-full text-left border border-gray-200">
                    <thead class="bg-gray-50">
                        <tr>
                            <th class="px-4 py-2 text-sm font-medium text-gray-900">Method</th>
                            <th class="px-4 py-2 text-sm font-medium text-gray-900">Endpoint</th>
                            <th class="px-4 py-2 text-sm font-medium text-gray-900">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-t">
                            <td class="px-4 py-2 text-sm text-gray-600">POST</td>
                            <td class="px-4 py-2 text-sm text-gray-600"><code>/predict</code></td>
                            <td class="px-4 py-2 text-sm text-gray-600">Returns a rainfall prediction based on provided weather parameters.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>

        <!-- Request Format -->
        <section class="bg-white rounded-lg shadow-sm p-6 mb-8">
            <h2 class="text-xl font-semibold text-gray-900 mb-4">Request Format</h2>
            <p class="text-gray-600 mb-4">Send a POST request to <code class="bg-gray-200 text-gray-800 px-1 py-0.5 rounded">/predict</code> with the following JSON payload:</p>
            <div class="bg-gray-50 p-4 rounded-lg border border-gray-200">
                <pre class="text-sm text-gray-800">
{
    "Temperature(C)": 30,
    "Humidity(%)": 85,
    "Pressure(hPa)": 1000,
    "WindSpeed(km/h)": 15,
    "CloudCover(%)": 75
}
                </pre>
            </div>
            <h3 class="text-lg font-medium text-gray-900 mt-4 mb-2">Parameters</h3>
            <ul class="list-disc pl-5 text-gray-600 text-sm">
                <li><strong>Temperature(C)</strong>: Temperature in Celsius (integer or float)</li>
                <li><strong>Humidity(%)</strong>: Relative humidity percentage (integer)</li>
                <li><strong>Pressure(hPa)</strong>: Atmospheric pressure in hectopascals (integer or float)</li>
                <li><strong>WindSpeed(km/h)</strong>: Wind speed in kilometers per hour (integer or float)</li>
                <li><strong>CloudCover(%)</strong>: Cloud cover percentage (integer)</li>
            </ul>
        </section>

        <!-- Response Format -->
        <section class="bg-white rounded-lg shadow-sm p-6 mb-8">
            <h2 class="text-xl font-semibold text-gray-900 mb-4">Response Format</h2>
            <p class="text-gray-600 mb-4">The API returns a JSON object with the following structure:</p>
            <div class="bg-gray-50 p-4 rounded-lg border border-gray-200">
                <pre class="text-sm text-gray-800">
{
    "RainfallPrediction": "No",
    "RiskSummary": "normal conditions",
    "Precautions": "No special precautions needed"
}
                </pre>
            </div>
            <h3 class="text-lg font-medium text-gray-900 mt-4 mb-2">Fields</h3>
            <ul class="list-disc pl-5 text-gray-600 text-sm">
                <li><strong>RainfallPrediction</strong>: Prediction result ("Yes" or "No")</li>
                <li><strong>RiskSummary</strong>: Brief summary of weather conditions</li>
                <li><strong>Precautions</strong>: Recommended actions based on prediction</li>
            </ul>
        </section>

        <!-- Example Usage -->
        <section class="bg-white rounded-lg shadow-sm p-6">
            <h2 class="text-xl font-semibold text-gray-900 mb-4">Example Usage</h2>
            <h3 class="text-lg font-medium text-gray-900 mb-2">cURL</h3>
            <div class="bg-gray-50 p-4 rounded-lg border border-gray-200 mb-4">
                <pre class="text-sm text-gray-800">
curl -X POST http://your-api-url/predict \
-H "Content-Type: application/json" \
-d '{
    "Temperature(C)": 30,
    "Humidity(%)": 85,
    "Pressure(hPa)": 1000,
    "WindSpeed(km/h)": 15,
    "CloudCover(%)": 75
}'
                </pre>
            </div>
            <h3 class="text-lg font-medium text-gray-900 mb-2">Python</h3>
            <div class="bg-gray-50 p-4 rounded-lg border border-gray-200">
                <pre class="text-sm text-gray-800">
import requests

url = "http://your-api-url/predict"
data = {
    "Temperature(C)": 30,
    "Humidity(%)": 85,
    "Pressure(hPa)": 1000,
    "WindSpeed(km/h)": 15,
    "CloudCover(%)": 75
}
response = requests.post(url, json=data)
print(response.json())
                </pre>
            </div>
        </section>
    </main>

    <footer class="bg-white shadow-sm mt-8">
        <div class="container mx-auto max-w-5xl px-6 py-4 text-center text-sm text-gray-600">
            &copy; 2025 Rainfall Prediction API. All rights reserved.
        </div>
    </footer>
</body>
</html>
    '''



if __name__ == '__main__':
    app.run(debug=True)
