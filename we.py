
import pandas as pd
import requests

API_KEY = "ba1a98bb25ee33333b49830388aeab9e"
cities = ["London", "New York", "Delhi", "Tokyo"]
weather_alerts = []

for city in cities:
    print(f"\nFetching forecast for {city}...")

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if "list" not in data:
            print(f"No forecast data available for {city}.")
            continue

        forecast_entries = data["list"]
        processed_data = []

        for entry in forecast_entries:
            date = entry["dt_txt"]
            temp = entry["main"]["temp"]
            humidity = entry["main"]["humidity"]
            condition = entry["weather"][0]["main"].lower()

            processed_data.append({
                "Date": date,
                "Temperature": temp,
                "Humidity": humidity,
                "Condition": condition.capitalize()
            })

            # Generate alerts
            if temp > 35:
                weather_alerts.append(f"High Temperature Alert in {city} on {date}")
            elif temp < 5:
                weather_alerts.append(f"Cold Weather Alert in {city} on {date}")
            if "rain" in condition or "storm" in condition:
                weather_alerts.append(f"Storm/Rain Alert in {city} on {date}")

        # Save forecast to CSV
        df = pd.DataFrame(processed_data)
        file_name = f"{city.replace(' ', '_')}_forecast.csv"
        df.to_csv(file_name, index=False)
        print(f" Forecast saved to {file_name}")

    except requests.exceptions.RequestException as err:
        print(f"Error fetching data for {city}: {err}")

# Save alerts to file
if weather_alerts:
    with open("weather_alerts.txt", "w") as f:
        for alert in weather_alerts:
            f.write(alert + "\n")
    print(" Weather alerts saved to weather_alerts.txt")
else:
    print(" No extreme weather alerts generated.")
         