# Loop info, like date, weather etc. on the Unicorn Hat HD
# Copyright (c) Akos Polster. All rights reserved.

import signal
import time
import sys
import traceback
from PIL import Image, ImageDraw, ImageFont
from random import randint

hat_sleep_delay = 0.02

try:
    import unicornhathd as unicorn
    unicorn.rotation(90)
except ImportError:
    # Unicorn Hat HD not available or software not installed -- Use simulator
    from unicorn_hat_sim import unicornhathd as unicorn
    hat_sleep_delay = 0.03

from looper.topic_time import topic_time
from looper.topic_weather import topic_weather
from looper.topic_panda import topic_panda
from looper.topic_date import topic_date
from looper.topic_holiday import topic_holiday
from looper.topic_reuters import topic_reuters


hat_width, hat_height = unicorn.get_shape()
font_file = "looper/Roboto-Regular.ttf"
font_size = 12
font = ImageFont.truetype(font_file, font_size)
black = (0, 0, 0)
white = (255, 255, 255)
canvas = Image.new("RGB", (1024, hat_height), black)
draw = ImageDraw.Draw(canvas)
topics = [
    topic_time,
    topic_date,
    topic_holiday,
    topic_time,
    topic_weather,
    topic_time,
    topic_panda,
    topic_time,
    topic_reuters
]
topic_index = 0


def shutdown(code=None, frame=None):
    unicorn.off()
    sys.exit(0)


def blit(image, offset):
    for x in range(hat_width):
        for y in range(hat_height):
            pixel = image.getpixel((x + offset, y))
            r, g, b = [int(n) for n in pixel]
            unicorn.set_pixel(hat_width - 1 - x, y, r, g, b)
    unicorn.show()


def main():
    global topic_index

    signal.signal(signal.SIGTERM, shutdown)
    unicorn.brightness(1.0)
    unicorn.show()

    while True:
        text, color, image = topics[topic_index]()
        topic_index += 1
        if topic_index >= len(topics):
            topic_index = 0

        if text is None and color is None and image is None:
            continue

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
