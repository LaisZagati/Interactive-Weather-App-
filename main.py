import requests
from rich import print
from datetime import date, datetime

"""Get user input for
city name."""

print("[purple bold]Welcome to the Weather App![/purple bold]")
city_name = input("Enter city name: ")

#GET CURRENT WEATHER DATA

"""Display the weather data 
for the given city name."""
""" Function to get weather data from API"""
def get_weather_data(city):
    api_key = "f093ocaff400a6043tff45112437b840"
    api_url = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}"

    # Make a request to the weather API
    response = requests.get(api_url)
    current_weather_data = response.json()

    # Extract the relevant weather data
    current_weather_city = current_weather_data["city"]
    current_weather_temperature = current_weather_data["temperature"]["current"]

    print(f"[blue bold]The temperature in[/blue bold] {city_name} [blue bold]is [/blue bold]{current_weather_temperature} [blue bold]degrees Celsius[/blue bold]")

#GET FORECAST DATA

def get_forecast_data(city_name):
    api_key = "f093ocaff400a6043tff45112437b840"
    api_url = f"https://api.shecodes.io/weather/v1/forecast?query={city_name}&key={api_key}"

    # Make a request to the weather API
    response = requests.get(api_url)
    forecast_weather_data = response.json()

    for day in forecast_weather_data["daily"]:
        timestamp = day['time']
        date = datetime.fromtimestamp(timestamp)
        formatted_day = date.strftime('%A' )
        temperature = day['temperature']['day']
    
        print(f"{formatted_day}: {round(temperature)}°C")
        


if city_name:
    get_weather_data(city_name)
    print("\n[green bold]Forecast:[/green bold]")
    get_forecast_data(city_name)
    print("\n[magenta bold]This app was built by Lais Zagati![/magenta bold]")

else:
    print("Please enter a city name")


print("\n[yellow bold]Thank you for using Weather App![/yellow bold]")
