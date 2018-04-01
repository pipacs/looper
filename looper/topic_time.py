# Get the current time
# Copyright (c) Akos Polster. All rights reserved.

import datetime

green = (0, 255, 0)


def topic_time():
    now = datetime.datetime.now()
    return (now.strftime("%-I:%M"), green, None)
