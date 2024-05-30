# Get current weather at the current location from OpenWeatherMap
# Copyright (c) Akos Polster. All rights reserved.

import datetime
from PIL import Image, ImageColor
import sys
import traceback
from pyowm.owm import OWM

from looper.tools import get_current_location


def get_weather(lat, long, config):
    now = datetime.datetime.now()
    delta = now - weather_last_updated
    if delta.total_seconds() < 3600:
        return weather_last

    api_key = config.get("owm", {}).get("key", "")
    if api_key == "":
        return ("", "Missing OWM API key", 0)

    owm = OWM(api_key)
    weather_manager = owm.weather_manager()
    observation = weather_manager.weather_at_coords(lat, long)
    w = observation.weather
    icon_name = w.weather_icon_name
    status = w.status
    temp = w.temperature("celsius")["temp"]
    result = (icon_name, status, temp)
    print(result)
    return result


weather_last = ""
weather_last_updated = datetime.datetime.fromtimestamp(0)
weather_last_image = None

white = ImageColor.getrgb("white")
icon_map = {
    "01d": "sunny",
    "01n": "starry",
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

    try:
        lat, long = get_current_location()
        icon_name, text, temp = get_weather(lat, long, config)
        baseName = icon_map.get(icon_name, None)
        if baseName is not None:
            weather_last_image = Image.open("looper/" + baseName + ".png")
        else:
            print("No weather icon for", icon_name)
            weather_last_image = None
        weather_last = ""
        if weather_last_image is None:
            weather_last = text + " "
        weather_last += ("%.0f" % temp) + u"\u2103"
        weather_last_updated = now
    except Exception:
        traceback.print_exc(file=sys.stdout)

    return (weather_last, white, weather_last_image)
