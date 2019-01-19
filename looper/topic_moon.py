# Copyright (c) Akos Polster. All rights reserved.

import datetime
from PIL import Image


def get_moon_phase(month, day, year):
    ages = [18, 0, 11, 22, 3, 14, 25, 6, 17, 28, 9, 20, 1, 12, 23, 4, 15, 26, 7]
    offsets = [-1, 1, 0, 1, 2, 3, 4, 5, 7, 7, 9, 9]
    description = [
        ("moon-5.png", "New"),
        ("moon-6.png", "Crescent"),
        ("moon-7.png", "First Q"),
        ("moon-8.png", "Gibbous"),
        ("moon-1.png", "Full"),
        ("moon-2.png", "Gibbous"),
        ("moon-3.png", "Third Q"),
        ("moon-4.png", "Crescent"),
        ("moon-5.png", "New")
    ]
    if day == 31:
        day = 1
    days_into_phase = ((ages[(year + 1) % 19] +
                        ((day + offsets[month - 1]) % 30) +
                        (year < 1900)) % 30)
    index = int((days_into_phase + 2) * 16 / 59.0)
    if index > 7:
        index = 7
    return description[index]


def topic_moon(config):
    now = datetime.datetime.now().date()
    moon, _ = get_moon_phase(now.month, now.day, now.year)
    if moon is None:
        return (None, None, None)
    else:
        return ("", (255, 255, 255), Image.open("looper/" + moon))
