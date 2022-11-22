import datetime


def unixToDatetime(unixTimestamp):
    return datetime.datetime.fromtimestamp(unixTimestamp)
