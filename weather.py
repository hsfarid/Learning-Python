import requests
import datetime as dt

apiKey = "6e855adb181d00a009ab8a5c19e99326"
baseURL = "https://api.openweathermap.org/data/2.5/weather?q="
cityName = input("Enter city name: ")

completeURL = baseURL  + cityName + "&appid=" + apiKey
response = requests.get(completeURL)
data = response.json()
print("Current temperature: ", data["main"]["temp"])
        