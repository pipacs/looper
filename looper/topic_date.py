# Get the current date and today's holiday
# Copyright (c) Akos Polster. All rights reserved.

from datetime import datetime
import holidays
import json
import requests
import sys
import traceback
import urllib
from ip2geotools.databases.noncommercial import DbIpCity
from chest import Chest

settings = Chest()

def get_country_code():
    country_last = "US"
    if "country_last" in settings:
        country_last = settings["country_last"]
    country_last_updated = datetime.fromtimestamp(0)
    if "country_last_updated" in settings:
        country_last_updated = settings["country_last_updated"]

    now = datetime.now()
    delta = now - country_last_updated
    if delta.total_seconds() < 86400:
        return country_last

    try:
        myIp = urllib.request.urlopen('http://icanhazip.com/', timeout=2).read().strip()
        response = DbIpCity.get(myIp, api_key='free')
        country_last = response.country
    except:
        pass

    settings["country_last_updated"] = now
    settings["country_last"] = country_last
    settings.flush()
    return country_last

country_holidays = {
    "CA": holidays.CA(),
    "CO": holidays.CO(),
    "MX": holidays.MX(),
    "US": holidays.US(),
    "NZ": holidays.NZ(),
    "AU": holidays.AU(),
    "DE": holidays.DE(),
    "AT": holidays.AT(),
    "DK": holidays.DK(),
    "UK": holidays.UK(),
    "IE": holidays.IE(),
    "ES": holidays.ES(),
    "CZ": holidays.CZ(),
    "SK": holidays.SK(),
    "PL": holidays.PL(),
    "PT": holidays.PT(),
    "NL": holidays.NL(),
    "NO": holidays.NO(),
    "IT": holidays.IT(),
    "SE": holidays.SE(),
    "JP": holidays.JP(),
    "BE": holidays.BE(),
    "ZA": holidays.ZA(),
    "SI": holidays.SI(),
    "FI": holidays.FI(),
    "CH": holidays.CH()
}

def get_holiday():
    country = get_country_code()
    if not country in country_holidays.keys():
        return None
    return country_holidays[country].get(datetime.now().date())

def topic_date(config):
    now = datetime.now()
    date = now.strftime("%a %-d %b")
    holiday = get_holiday()
    if holiday is not None:
        date += " " + holiday
    return (date, (255, 255, 255), None)
