# Copyright (c) Akos Polster. All rights reserved.

import ephem
import datetime
from PIL import Image


def get_lunation(day=datetime.datetime.now().date()):
    """
    Returns a floating-point number from 0-1, that roughly corresponds 
    to the phase of the moon: 0=new, 0.5=full, 1=new.
    """
    
    date = ephem.Date(day)
    nnm = ephem.next_new_moon(date)
    pnm = ephem.previous_new_moon(date)
    lunation = (date - pnm) / (nnm - pnm)
    return lunation


def get_moon(lunation):
    moon_map = {
        0: "moon-5.png",
        1: "moon-6.png",
        2: "moon-7.png",
        3: "moon-8.png",
        4: "moon-1.png",
        5: "moon-2.png",
        6: "moon-3.png",
        7: "moon-4.png",
        8: "moon-5.png"
    }
    return moon_map.get(int(lunation * 8))
    

def topic_moon():
    moon = get_moon(get_lunation())
    if moon is None:
        return (None, None, None)
    else:
        return (None, None, Image.open("looper/" + moon))


if __name__ == "__main__":
    today = datetime.datetime.now().date()
    print(get_moon(get_lunation(today)))
    print(get_moon(get_lunation(today + datetime.timedelta(days=1))))
    print(get_moon(get_lunation(today + datetime.timedelta(days=3))))
    print(get_moon(get_lunation(today + datetime.timedelta(days=5))))
    print(get_moon(get_lunation(today + datetime.timedelta(days=7))))
    print(get_moon(get_lunation(today + datetime.timedelta(days=9))))
    print(get_moon(get_lunation(today + datetime.timedelta(days=11))))
    print(get_moon(get_lunation(today + datetime.timedelta(days=13))))
    print(get_moon(get_lunation(today + datetime.timedelta(days=15))))
    print(get_moon(get_lunation(today + datetime.timedelta(days=17))))
    print(get_moon(get_lunation(today + datetime.timedelta(days=19))))
    print(get_moon(get_lunation(today + datetime.timedelta(days=21))))
    print(get_moon(get_lunation(today + datetime.timedelta(days=23))))
    print(get_moon(get_lunation(today + datetime.timedelta(days=25))))
    print(get_moon(get_lunation(today + datetime.timedelta(days=27))))
    print(get_moon(get_lunation(today + datetime.timedelta(days=29))))
    print(topic_moon())
