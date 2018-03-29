# Copyright (c) Akos Polster. All rights reserved.

from PIL import Image

def next_image():
    image = Image.open("looper/panda.png")
    return (None, None, image)
