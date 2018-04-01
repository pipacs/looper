# Get the current date
# Copyright (c) Akos Polster. All rights reserved.

import datetime

def topic_date():
    now = datetime.datetime.now()
    return (now.strftime("%a %-d %b"), (255, 255, 255), None)
