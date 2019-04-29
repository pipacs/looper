# Get current weather at the current location from OpenWeatherMap
# Copyright (c) Akos Polster. All rights reserved.

import datetime
import json
from PIL import Image, ImageColor
import requests
import sys
import traceback
import pyowm

location_last = (0.0, 0.0)
location_last_updated = datetime.datetime.fromtimestamp(0)

def get_current_location():
    global location_last
    global location_last_updated

    now = datetime.datetime.now()
    delta = now - location_last_updated
    if delta.total_seconds() < 86400:
        return location_last

    try:
        send_url = 'http://gd.geobytes.com/GetCityDetails'
        r = requests.get(send_url)
        j = json.loads(r.text)
        location_last = (float(j["geobyteslatitude"]), float(j["geobyteslongitude"]))
        location_last_updated = now
    except Exception:
        traceback.print_exc(file=sys.stdout)

    return location_last

def get_weather(lat, long, config):
    api_key = config.get("owm", {}).get("key", "")
    if api_key == "":
        return ("", "Missing OWM API key", 0)
    owm = pyowm.OWM(api_key)
    observation = owm.weather_at_coords(lat, long)
    w = observation.get_weather()
    icon_name = w.get_weather_icon_name()
    status = w.get_status()
    temp = w.get_temperature("celsius")["temp"]
    return (icon_name, status, temp)

weather_last = ""
weather_last_updated = datetime.datetime.fromtimestamp(0)
weather_last_image = None

white = ImageColor.getrgb("white")
icon_map = {
    "01d": "sunny",
    # "01n": "starry",
    "03d": "cloudy",
    "03n": "cloudy",
    "04d": "cloudy",
    "04n": "cloudy",
    "02d": "partly-cloudy",
    # "02n": "partly-cloudy-night",
    "09d": "rain",
    "09n": "rain",
    "10d": "rain",
    "10n": "rain",
    "11d": "rain",
    "11n": "rain",
    "13d": "snow",
    "13n": "snow",
    "50d": "mist",
    "50n": "mist",
}

def topic_owm(config):
    global weather_last
    global weather_last_image
    global weather_last_updated
 
    now = datetime.datetime.now()
    delta = now - weather_last_updated
    if delta.total_seconds() < 3600:
        return (weather_last, white, weather_last_image)

    weather_last_updated = now

    try:
        lat, long = get_current_location()
        icon_name, text, temp = get_weather(lat, long, config)
        baseName = icon_map.get(icon_name, None)
        if baseName is not None:
            weather_last_image = Image.open("looper/" + baseName + ".png")
        else:
            weather_last_image = None
        weather_last = ""
        if weather_last_image is None:
            weather_last = text + " "
        weather_last += ("%.0f" % temp) + u"\u2103"
    except Exception:
        traceback.print_exc(file=sys.stdout)

    return (weather_last, white, weather_last_image)
