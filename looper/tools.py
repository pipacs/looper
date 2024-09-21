# Various utilities for Looper
# Copyright (c) Akos Polster. All rights reserved.

import urllib
import datetime
import sys
import traceback
import json


settings = {}


def get_current_location():
    location_last = (55.667, 12.583)
    location_last_updated = datetime.datetime.fromtimestamp(0)

    if "location_last" in settings:
        location_last = settings["location_last"]
        if "location_last_updated" in settings:
            location_last_updated = settings["location_last_updated"]

    now = datetime.datetime.now()
    delta = now - location_last_updated
    if delta.total_seconds() < 86400:
        return location_last

    try:
        location_json = urllib.request.urlopen('http://ipinfo.io/json', timeout=5).read()
        location = json.loads(location_json)
        lat_lng = location["loc"].split(",")
        lat = float(lat_lng[0])
        lng = float(lat_lng[1])
        # print("Location: " + str(location))
        location_last = (lat, lng)
        settings["location_last"] = location_last
        settings["location_last_updated"] = now
    except:
        traceback.print_exc(file=sys.stdout)

    return location_last
