# The latest headlines from Reuters
# Copyright (c) Akos Polster. All rights reserved.

import feedparser
from random import randint
import datetime

reuters_last_updated = datetime.datetime.fromtimestamp(0)
reuters_entries = []


def topic_reuters(config):
    global reuters_entries
    global reuters_last_updated

    now = datetime.datetime.now()
    delta = now - reuters_last_updated
    if delta.total_seconds() > 1800:
        reuters_entries = feedparser.parse("http://feeds.reuters.com/reuters/topNews").entries
        reuters_last_updated = now

    count = len(reuters_entries)
    if count == 0:
        return (None, None, None)
    index = randint(0, count - 1)
    return (reuters_entries[index].title, (80, 80, 255), None)
