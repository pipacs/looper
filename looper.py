# Loop info, like date, weather etc. on the Unicorn Hat HD
# Copyright (c) Akos Polster. All rights reserved.

import signal
import time
import sys
import traceback
from PIL import Image, ImageDraw, ImageFont, ImageColor
from random import randint

hat_sleep_delay = 0.02

try:
    import unicornhathd as unicorn
    unicorn.rotation(90)
except ImportError:
    # Unicorn Hat HD not available or software not installed -- Use simulator
    from unicorn_hat_sim import unicornhathd as unicorn
    hat_sleep_delay = 0.03

from looper.time import get_time
from looper.weather import get_weather
from looper.panda import get_panda
from looper.date import get_date


def shutdown(code = None, frame = None):
    unicorn.off()
    sys.exit(0)

signal.signal(signal.SIGTERM, shutdown)
unicorn.brightness(1.0)
unicorn.show()

hat_width, hat_height = unicorn.get_shape()
font_file = "looper/Roboto-Regular.ttf"
font_size = 12
font = ImageFont.truetype(font_file, font_size)

black = ImageColor.getrgb("black")
red = ImageColor.getrgb("red")
green = ImageColor.getrgb("green")
canvas = Image.new("RGB", (1024, hat_height), black)
draw = ImageDraw.Draw(canvas)

topics = \
        [get_weather] * 2 + \
        [get_panda] * 1 + \
        [get_time] * 5 + \
        [get_date] * 1


def blit(image, offset):
    for x in range(hat_width):
        for y in range(hat_height):
            pixel = image.getpixel((x + offset, y))
            r, g, b = [int(n) for n in pixel]
            unicorn.set_pixel(hat_width - 1 - x, y, r, g, b)
    unicorn.show()


def next_topic():
    return topics[randint(0, len(topics) - 1)]()


def main():
    while True:
        draw.rectangle([0, 0, 1024, hat_height - 1], fill=black)
        text, color, image = next_topic()
        topic_width = 0

        if image is not None:
            topic_width, _ = image.size
            canvas.paste(image, (hat_width, 0))

        if text is not None and color is not None:
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
