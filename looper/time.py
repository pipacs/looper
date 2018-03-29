# Get the current time
# Copyright (c) Akos Polster. All rights reserved.

import datetime
from PIL import ImageColor

red = ImageColor.getrgb("red")
green = ImageColor.getrgb("green")


def get_time():
    global green
    now = datetime.datetime.now()
    return (now.strftime("%-I:%M"), green, None)
