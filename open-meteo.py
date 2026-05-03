import requests
import pandas as pd

url = "https://archive-api.open-meteo.com/v1/archive"
params = {
    "latitude": 50.45,
    "longitude": 30.52,
    "start_date": "1940-01-01",
    "end_date": "2025-12-31",
    "daily": "temperature_2m_mean,temperature_2m_max,temperature_2m_min",
    "timezone": "Europe/Kyiv"
}

response = requests.get(url, params=params)
data = response.json()

df = pd.DataFrame(data["daily"])
df.to_csv("kyiv_temperature_1940_2025.csv", index=False)
print(df.head())