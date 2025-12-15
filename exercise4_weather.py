# Import requests library to make API calls
import requests

# Import csv module to write data into CSV file
import csv

# Import datetime to record date and time
from datetime import datetime


# -------------------------------------------------
# Function to fetch weather data from OpenWeatherMap
# -------------------------------------------------
def fetch_weather(city, api_key):
    try:
        # API URL with city name, API key and metric units
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        # Send GET request to the API
        response = requests.get(url)

        # Raise error if response status is not successful
        response.raise_for_status()

        # Convert JSON response to Python dictionary
        return response.json()

    except requests.exceptions.RequestException as e:
        # Handle network, API and city errors
        print("Error fetching weather data:", e)
        return None


# -----------------------------------------
# Function to analyze fetched weather data
# -----------------------------------------
def analyze_weather(weather_data):
    # Extract temperature, wind speed and humidity
    temperature = weather_data['main']['temp']
    wind_speed = weather_data['wind']['speed']
    humidity = weather_data['main']['humidity']

    # Categorize temperature
    if temperature <= 10:
        summary = "Cold (≤10°C)"
    elif 11 <= temperature <= 24:
        summary = "Mild (11–24°C)"
    else:
        summary = "Hot (≥25°C)"

    # Add warning for high wind speed
    if wind_speed > 10:
        summary += " | High wind alert!"

    # Add warning for high humidity
    if humidity > 80:
        summary += " | Humid conditions!"

    return summary


# -----------------------------------------
# Function to save weather data into CSV
# -----------------------------------------
def log_weather(city, filename, api_key):
    # Fetch weather data
    weather_data = fetch_weather(city, api_key)

    # Proceed only if data is successfully fetched
    if weather_data:
        # Analyze weather conditions
        summary = analyze_weather(weather_data)

        # Open CSV file in append mode using UTF-8 encoding
        with open(filename, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            # Write weather details into CSV
            writer.writerow([
                datetime.now(),                     # Date & Time
                city,                               # City name
                weather_data['main']['temp'],       # Temperature
                weather_data['wind']['speed'],      # Wind speed
                weather_data['main']['humidity'],   # Humidity
                summary                             # Weather summary
            ])

        # Success message
        print("Weather data saved successfully.")


# -------------------------
# Main Program Execution
# -------------------------

# Your OpenWeatherMap API key
API_KEY = "b9fca8492d60ef6e0943658f40757770"

# City name
CITY = "Mumbai"

# Output CSV file
FILENAME = "weather_log.csv"

# Call the function
log_weather(CITY, FILENAME, API_KEY)
