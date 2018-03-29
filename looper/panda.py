# Copyright (c) Akos Polster. All rights reserved.

from PIL import Image

def get_panda():
    image = Image.open("looper/panda.png")
    return (None, None, image)
