import requests

api_key = "638ed4342efacd2a72117c3cc1bc01ed"
city = "Jerusalem"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("City:", data["name"])
    print("Weather:", data["weather"][0]["description"])
    print("Temperature:", data["main"]["temp"])
else:
    print("Failed to fetch data. Status code:", response.status_code, response.text)


    