# Loop info, like date, weather etc. on the Unicorn Hat HD
# Copyright (c) Akos Polster. All rights reserved.

import datetime
import signal
import time
import sys
import traceback
from PIL import Image, ImageDraw, ImageFont
import pathlib
import yaml
from astral import sun, LocationInfo

hat_sleep_delay = 0.02

try:
    import unicornhathd as unicorn
    unicorn.rotation(90)
except ImportError:
    # Unicorn Hat HD not available or software not installed -- Use simulator
    from looper.unicorn_hat_sim import unicornhathd as unicorn
    hat_sleep_delay = 0.03

from looper.topic_time import topic_time
from looper.topic_panda import topic_panda
from looper.topic_date import topic_date
from looper.topic_reuters import topic_reuters
from looper.topic_moon import topic_moon
from looper.topic_owm import topic_owm

from looper.tools import get_current_location


hat_width, hat_height = unicorn.get_shape()
font = ImageFont.truetype("looper/Roboto-Regular.ttf", 12)
black = (0, 0, 0)
white = (255, 255, 255)
canvas = Image.new("RGB", (1024, hat_height), black)
draw = ImageDraw.Draw(canvas)
topics = []
topic_index = 0
config = {}


def shutdown(code=None, frame=None):
    unicorn.off()
    sys.exit(0)


def blit(image, offset):
    """Show image pixels on the Unicorn hat"""
    for x in range(hat_width):
        for y in range(hat_height):
            pixel = image.getpixel((x + offset, y))
            r, g, b = [int(n) for n in pixel]
            unicorn.set_pixel(hat_width - 1 - x, y, r, g, b)
    unicorn.show()


def set_brightness():
    """Set the Unicorn hat's brightness according to the current sunrise/sunset time"""
    now = datetime.datetime.now()
    latitude, longitude = get_current_location()
    timezone = datetime.datetime.now(datetime.timezone.utc).astimezone().tzname()
    loc = LocationInfo(latitude=latitude, longitude=longitude)
    sunInfo = sun.sun(loc.observer, date=now.date(), tzinfo=timezone)
    utcNow = datetime.datetime.now(datetime.timezone.utc)
    if utcNow < sunInfo["sunrise"] or utcNow > sunInfo["sunset"]:
        unicorn.brightness(0.10)
    else:
        unicorn.brightness(0.75)


def load_config():
    global config
    global topics

    local_config = {}
    global_config = {}
    try:
        with open("/usr/local/lib/looper/looper.yaml") as f:
            global_config = yaml.safe_load(f)
    except FileNotFoundError:
        try:
            with open("looper/looper.yaml") as f:
                global_config = yaml.safe_load(f)
        except FileNotFoundError:
            pass
    try:
        local_config_file = str(pathlib.Path.home().joinpath(".looper.yaml"))
        with open(local_config_file) as f:
            local_config = yaml.safe_load(f)
    except Exception:
        pass
    config = {**global_config, **local_config}
    topic_map = {
        "time": topic_time,
        "date": topic_date,
        "reuters": topic_reuters,
        "panda": topic_panda,
        "moon": topic_moon,
        "owm": topic_owm,
    }
    for topic in config.get("global", {}).get("topics", []):
        topic_fn = topic_map.get(topic)
        if topic_fn is not None:
            topics.append(topic_fn)


def main():
    global topic_index

    signal.signal(signal.SIGTERM, shutdown)
    load_config()
    unicorn.show()

    while True:
        text, color, image = topics[topic_index](config)
        topic_index += 1
        if topic_index >= len(topics):
            topic_index = 0

        if text is None and color is None and image is None:
            continue

        set_brightness()
        draw.rectangle([0, 0, 1024, hat_height - 1], fill=black)
        topic_width = 0

        if image is not None:
            topic_width, _ = image.size
            canvas.paste(image, (hat_width, 0))

        if color is None:
            color = white

        if text is not None:
            if image is not None:
                text = " " + text
            text_width, _ = font.getsize(text)
            draw.text((hat_width + topic_width, 0), text, color, font=font)
            topic_width += text_width

        for offset in range(topic_width + 2 * hat_width):
            blit(canvas, offset)
            if offset < (hat_width + topic_width):
                time.sleep(hat_sleep_delay)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception:
        traceback.print_exc(file=sys.stdout)
    shutdown()
