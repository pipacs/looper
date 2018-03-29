#!/usr/bin/env python

import datetime
import json
from PIL import Image, ImageColor
import requests
import sys
import traceback
from weather import Weather, Unit

def get_current_location():
    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    j = json.loads(r.text)
    return j['city']


red = ImageColor.getrgb("red")
white = ImageColor.getrgb("white")
weather = Weather(Unit.CELSIUS)
weather_last = ""
weather_last_updated = datetime.datetime.fromtimestamp(0)
weather_last_image = None
weather_location_name = get_current_location()

def next_weather():
    global weather_last
    global weather_last_image
    global weather_last_updated
    global red

    now = datetime.datetime.now()
    delta = now - weather_last_updated
    if delta.total_seconds() < 3600:
        return (weather_last, white, weather_last_image)

    weather_last_updated = now

    try:
        location = weather.lookup_by_location(weather_location_name)
        condition = location.condition()
        weather_last = condition.text() + " " + condition.temp() + u"\u2103"
        code = int(condition.code())
        if code == 32:
            weather_last_image = Image.open("looper/sunny.png")
        elif code < 12 or code == 35 or code == 40 or code == 47:
            weather_last_image = Image.open("looper/rain.png")
        elif code == 26 or code == 27 or code == 28:
            weather_last_image = Image.open("looper/cloudy.png")
        else:
            weather_last_image = None
    except Exception:
        traceback.print_exc(file=sys.stdout)

    return (weather_last, white, weather_last_image)
