# Get the current date
# Copyright (c) Akos Polster. All rights reserved.

import datetime

red = (255, 0, 0)


def topic_date():
    now = datetime.datetime.now()
    return (now.strftime("%a %-d %b"), red, None)
