import requests
import datetime as dt

def getObserverDarkSkyHours(latitude, longitude):
    observer_params = {
        "lat": latitude,
        "lng": longitude
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=observer_params)
    response.raise_for_status()

    data = response.json()
    observer_sunset = data["results"]["sunset"]

    tomorrow_date = (dt.datetime.now() + dt.timedelta(days=1))
    observer_params = {
        "lat": latitude,
        "lng": longitude,
        "date": tomorrow_date.strftime("%Y-%m-%d")
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=observer_params)
    response.raise_for_status()

    data = response.json()
    observer_sunrise = data["results"]["sunrise"]

    return (observer_sunset, observer_sunrise)



# ISS location
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()

# print(data["iss_position"])
# iss_lat = data["iss_position"]["latitude"]
# iss_long = data["iss_position"]["longitude"]

# iss_position = (float(iss_lat), float(iss_long))
# print(iss_position)

# Sunset/sunrise
visibility_time_window = getObserverDarkSkyHours(latitude=51.507351, longitude=-0.127758)
print(visibility_time_window)