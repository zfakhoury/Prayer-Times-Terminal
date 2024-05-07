import requests
import datetime
import json
from tabulate import tabulate

current_date = datetime.datetime.now()
year = current_date.year
month = current_date.month
country = str(input("Country: "))
city = str(input("City: "))

api_url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}"
response = requests.get(api_url)

print("")

if response.status_code == 200:
    data = response.json()
    
    required_timings = [
        ["Fajr",    data["data"]["timings"]["Fajr"]],
        ["Sunrise", data["data"]["timings"]["Sunrise"]],
        ["Dhuhr",   data["data"]["timings"]["Dhuhr"]],
        ["Asr",     data["data"]["timings"]["Asr"]],
        ["Maghrib", data["data"]["timings"]["Maghrib"]],
        ["Isha",    data["data"]["timings"]["Isha"]]
    ]

    print(tabulate(required_timings, headers=["Prayer", "Time"]))

else:
    print("Error: ", response.status_code)
