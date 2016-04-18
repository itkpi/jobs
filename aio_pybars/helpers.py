import datetime
import dateutil.parser
import re


def _asset(options, val, *args, **kwargs):
    prefix = r'/events'
    return prefix + "/assets/{}".format(val)


def _date(options, format, *args, **kwargs):
    if options['when_start']:
        dt = dateutil.parser.parse(options['when_start'])
    else:
        dt = datetime.datetime.now()

    date = format.replace("YYYY", str(dt.year))
    date = date.replace("DD", str(dt.day))
    date = date.replace("MMMM", str(dt.month))
    date = date.replace("MM", str(dt.month))
    return date


def _strftime(options, source, format, *args, **kwargs):
    dt = dateutil.parser.parse(options[source])
    return datetime.datetime.strftime(dt, format)


def _excerpt(options, words, *args, **kwargs):
    text = options["agenda"]
    text = re.sub('<[^<]+?>', ' ', text)
    if text:
        text = ' '.join(text.split()[:int(words)])
    return text
