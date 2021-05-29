# Get current weather at the current location from OpenWeatherMap
# Copyright (c) Akos Polster. All rights reserved.

import datetime
import json
from PIL import Image, ImageColor
import requests
import sys
import traceback
from pyowm.owm import OWM
from ip2geotools.databases.noncommercial import DbIpCity
import urllib

from chest import Chest
settings = Chest()


def get_current_location():
    location_last = (55.667, 12.583)
    if "location_last" in settings:
        location_last = settings["location_last"]
    location_last_updated = datetime.datetime.fromtimestamp(0)
    if "location_last_updated" in settings:
        location_last_updated = settings["location_last_updated"]

    now = datetime.datetime.now()
    delta = now - location_last_updated
    if delta.total_seconds() < 86400:
        return location_last

    try:
        myIp = urllib.request.urlopen('http://icanhazip.com/', timeout=5).read().strip()
        response = DbIpCity.get(myIp, api_key='free')
        location_last = (response.latitude, response.longitude)
        settings["location_last"] = location_last
        settings["location_last_updated"] = now
        settings.flush
        return location_last
    except:
        return location_last

def get_weather(lat, long, config):
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
        weather_last_updated = now
    except Exception:
        traceback.print_exc(file=sys.stdout)

    return (weather_last, white, weather_last_image)
