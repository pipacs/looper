# Copyright (c) Akos Polster. All rights reserved.

from PIL import Image

def topic_panda():
    image = Image.open("looper/panda.png")
    return (None, None, image)
