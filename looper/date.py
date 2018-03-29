# Get the current date
# Copyright (c) Akos Polster. All rights reserved.

import datetime
from PIL import ImageColor

red = ImageColor.getrgb("red")


def get_date():
    global green
    now = datetime.datetime.now()
    return (now.strftime("%a %-d %b"), red, None)
