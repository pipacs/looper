# Get current weather at the current location
# Copyright (c) Akos Polster. All rights reserved.

import datetime
import json
from PIL import Image, ImageColor
import requests
import sys
import traceback
from weather import Weather, Unit

def get_current_location():
    send_url = 'http://gd.geobytes.com/GetCityDetails'
    r = requests.get(send_url)
    j = json.loads(r.text)
    return j["geobytescity"]


def get_weather(location_name):
    code = 0
    text = ""
    temp = 0
    location = weather.lookup_by_location(location_name)
    try:
        condition = location.condition
        code = int(condition.code)
        text = condition.text
        temp = condition.temp
    except AttributeError:
        condition = location.condition()
        code = int(condition.code())
        text = condition.text()
        temp = condition.temp()
    return (code, text, temp)


white = ImageColor.getrgb("white")
weather = Weather(Unit.CELSIUS)
weather_last = ""
weather_last_updated = datetime.datetime.fromtimestamp(0)
weather_last_image = None
weather_location_name = get_current_location()

def topic_weather(config):
    global weather_last
    global weather_last_image
    global weather_last_updated
 
    now = datetime.datetime.now()
    delta = now - weather_last_updated
    if delta.total_seconds() < 3600:
        return (weather_last, white, weather_last_image)

    weather_last_updated = now

    try:
        code, text, temp = get_weather(weather_location_name)
        if code == 32:
            weather_last_image = Image.open("looper/sunny.png")
        elif code <= 12 or code == 35 or code == 40 or code == 47:
            weather_last_image = Image.open("looper/rain.png")
        elif code == 26 or code == 27:
            weather_last_image = Image.open("looper/cloudy.png")
        elif code == 28 or code == 29 or code == 44:
            weather_last_image = Image.open("looper/partly-cloudy.png")
        elif code == 16 or code == 14 or code == 15 or code == 41 or code == 42 or code == 43 or code == 46:
            weather_last_image = Image.open("looper/snow.png")
        else:
            weather_last_image = None
        weather_last = ""
        if weather_last_image is None:
            weather_last = text + " "
        weather_last += temp + u"\u2103"

    except Exception:
        traceback.print_exc(file=sys.stdout)

    return (weather_last, white, weather_last_image)
