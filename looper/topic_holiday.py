# Get today's holiday, if any
# Copyright (c) Akos Polster. All rights reserved.

import datetime
import json
import holidays
import requests


def get_country_code():
    send_url = "http://gd.geobytes.com/GetCityDetails"
    r = requests.get(send_url)
    j = json.loads(r.text)
    return j["geobytesinternet"]


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
country = get_country_code()
red = (255, 0, 0)


def topic_holiday():
    if not country in country_holidays.keys():
        return (None, None, None)
    holiday = country_holidays[country].get(datetime.datetime.now().date())
    return (holiday, red, None)
