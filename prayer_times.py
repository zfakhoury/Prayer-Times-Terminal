import requests
from datetime import datetime
from tabulate import tabulate

country = str(input("Country: "))
city = str(input("City: "))

api_url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}"
response = requests.get(api_url)

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

    print(f'\n{datetime.now().strftime("%d-%m-%Y")} | {country.upper()} - {city.upper()}\n')
    print(tabulate(required_timings, headers=["Prayer", "Time"]))

else:
    print("Error: ", response.status_code)
