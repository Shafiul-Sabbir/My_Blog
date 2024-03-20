import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    # print(data)
    
    direction = data['wind']['deg']
    if direction > 337.5 or direction <= 22.5:
        direction = 'N'
    elif direction > 22.5 and direction <= 67.5:
        direction = 'NE'
    elif direction > 67.5 and direction <= 112.5:
        direction = 'E'
    elif direction > 112.5 and direction <= 157.5:
        direction = 'SE'
    elif direction > 157.5 and direction <= 202.5:
        direction = 'S'
    elif direction > 202.5 and direction <= 247.5:
        direction = 'SW'
    elif direction > 247.5 and direction <= 292.5:
        direction = 'W'
    elif direction > 292.5 and direction <= 337.5:
        direction = 'NW'
    else:
        pass
    
    if response.status_code == 200:
        weather_info = {
            'temperature': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'air_pressure': data['main']['pressure'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'visibility': data['visibility'] / 1000,
            'wind_speed': data['wind']['speed'],
            'wind_deg': data['wind']['deg'],
            'wind_dir': direction,
            'coord' : data['coord'],
            'lat' : data['coord']['lat'],
            'lon' : data['coord']['lon'],
            'sunrise' : data['sys']['sunrise'],
            'sunset' : data['sys']['sunset'],
            'city' : data['name'],
            'country' : data['sys']['country']
        }
        return weather_info
    else:
        return None

# Replace 'YOUR_API_KEY' with your actual API key from OpenWeatherMap
api_key = '30d4741c779ba94c470ca1f63045390a'
city = 'London,uk'

weather_data = get_weather(api_key, city)
if weather_data:
    print("Weather Information:")
    print(f"Temperature: {weather_data['temperature']}°C")
    print(f"Description: {weather_data['description']}")
    print(f"Humidity: {weather_data['humidity']}%")
    print(f"visibility : {weather_data['visibility']} km")
    print(f"Wind Speed:  {weather_data['wind_speed'] * 3.6} km/h")
    print(f"Wind Direction: {weather_data['wind_deg']}° {weather_data['wind_dir']}")
    print(f"Air Pressure: {weather_data['air_pressure']} hPa")
    print(f"Coord: lat = {weather_data['lat']}, lon = {weather_data['lon']}")
    print(f"Sunrise: {weather_data['sunrise']}")
    print(f"Sunset: {weather_data['sunset']}")
    print(f"City: {weather_data['city']}, {weather_data['country']}")
else:
    print("Failed to fetch weather data.")
