import requests

"""Get user input for
city name."""

city_name = input("Enter city name: ")

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


    print(f"The temperature in: {city_name} is {current_weather_temperature} degrees Celsius")

if city_name:
    get_weather_data(city_name)
else:
    print("Please enter a city name")
