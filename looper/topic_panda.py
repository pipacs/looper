# Copyright (c) Akos Polster. All rights reserved.

import random
from PIL import Image

image_names = ["easter.png", "panda.png"]

def topic_panda(config):
    image_name = "looper/" + random.SystemRandom().choice(image_names)
    image = Image.open(image_name)
    return (None, None, image)
