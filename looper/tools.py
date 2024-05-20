# Various utilities for Looper
# Copyright (c) Akos Polster. All rights reserved.

from ip2geotools.databases.noncommercial import DbIpCity
import urllib
import datetime

settings = {}


def get_current_location():
    location_last = (55.667, 12.583)
    if "location_last" in settings:
        location_last = settings["location_last"]
    location_last_updated = datetime.datetime.fromtimestamp(0)
    if "location_last_updated" in settings:
        location_last_updated = settings["location_last_updated"]

    now = datetime.datetime.now()
    delta = now - location_last_updated
    if delta.total_seconds() < 86400:
        return location_last

    try:
        myIp = urllib.request.urlopen('http://icanhazip.com/', timeout=5).read().strip()
        response = DbIpCity.get(myIp, api_key='free')
        location_last = (response.latitude, response.longitude)
        settings["location_last"] = location_last
        settings["location_last_updated"] = now
    except:
        pass

    return location_last
