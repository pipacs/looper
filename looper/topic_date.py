# Get the current date and today's holiday
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


def get_holiday():
    if not country in country_holidays.keys():
        return None
    return country_holidays[country].get(datetime.datetime.now().date())


def topic_date():
    now = datetime.datetime.now()
    date = now.strftime("%a %-d %b")
    holiday = get_holiday()
    if holiday is not None:
        date += " " + holiday
    return (date, (255, 255, 255), None)
