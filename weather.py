import requests 
api_key = "eb48725f884ad46a054b1fc0178c10c4"
city = ""
weather_data = []
while True:
    city = input("Enter a city name: ")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_data.append(f"Temperature: {data['main']['temp']}°C")
        weather_data.append(f"Country: {data['sys']['country']}")
        weather_data.append(f"Humidity: {data['main']['humidity']}%")
        weather_data.append(f"Description: {data['weather'][0]['description']}")
        break
    else:
        print("City not found. Try again.")
for item in weather_data:
    print(item)