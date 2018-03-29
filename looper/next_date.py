#!/usr/bin/env python

import datetime
from PIL import ImageColor

# sudo apt install fonts-roboto
# sudo pip3 install weather-api


red = ImageColor.getrgb("red")
green = ImageColor.getrgb("green")


def next_date():
    global green
    now = datetime.datetime.now()
    return (now.strftime("%-I:%M"), green, None)
