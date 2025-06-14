import pandas as pd
import numpy as np


np.random.seed(42)


n_samples = 1000

temperature = np.round(np.random.normal(loc=25, scale=5, size=n_samples), 1)  # in Celsius
humidity = np.round(np.random.uniform(40, 100, size=n_samples), 1)             # in %
pressure = np.round(np.random.normal(loc=1013, scale=10, size=n_samples), 1)   # in hPa
wind_speed = np.round(np.random.uniform(0, 15, size=n_samples), 1)             # in km/h
cloud_cover = np.round(np.random.uniform(0, 100, size=n_samples), 1)           # in %
rainfall = []

# Rule to determine rainfall: high humidity, low pressure, high cloud cover
for i in range(n_samples):
    if humidity[i] > 70 and pressure[i] < 1010 and cloud_cover[i] > 60:
        rainfall.append(1)  # Rain
    else:
        rainfall.append(0)  # No Rain

# Create DataFrame
df = pd.DataFrame({
    'Temperature(C)': temperature,
    'Humidity(%)': humidity,
    'Pressure(hPa)': pressure,
    'WindSpeed(km/h)': wind_speed,
    'CloudCover(%)': cloud_cover,
    'Rainfall': rainfall
})

df.head()
df.to_csv('weather_data.csv', index=False)
