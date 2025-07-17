

As a developer, I want to fetch weather data from a public API, extract and store the daily forecast, and generate alerts when extreme weather conditions are detected, so that users can be informed in advance for planning and safety.

API Endpoint:
Use the OpenWeatherMap API (Free Tier):
https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric

(Sign up at https://openweathermap.org/api for a free API key.)

Logic:

    Accept a list of city names (e.g., ["London", "New York", "Delhi", "Tokyo"]).

    For each city:

    Call the weather forecast API.
    Extract the next 5 days of forecasted data (date, temperature, humidity, weather condition).

    Store the data for each city in a CSV file named: {city}_forecast.csv

    If any forecasted temperature:

     is above 35°C → generate an alert "High Temperature Alert in {city} on {date}"

     is below 5°C → generate an alert "Cold Weather Alert in {city} on {date}"

     includes "rain" or "storm" → generate "Storm/Rain Alert in {city} on {date}"

     Save all alerts to a text file named weather_alerts.txt.

Sample Forecast Record

{
  "dt_txt": "2025-07-03 15:00:00",
  "main": {
    "temp": 36.1,
    "humidity": 48
  },
  "weather": [
    {
      "main": "Clear",
      "description": "clear sky"
    }
  ]
}

Acceptance Criteria:

    Weather data is fetched for all input cities without failure.
    Each city has a forecast file ({city}_forecast.csv) with structured columns: Date, Temperature, Humidity,
    Condition.
    Weather alerts are correctly identified and written into weather_alerts.txt.
    Code includes error handling (e.g., invalid city, API failure).
    Screenshot or sample of generated files is submitted.
