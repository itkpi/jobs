import os

import datetime

import dateutil.parser
import re

from aio_pybars import FSTemplateLoader


class AppFSTemplateLoader(FSTemplateLoader):
    def __init__(self, app, base_dir):
        super().__init__(app, base_dir)

    def get_partials(self):
        partials = super().get_partials()
        base_partials = os.path.join(self.app.config['TEMPLATES_DIR'], 'partials')
        for name in os.listdir(base_partials):
            filename = os.path.splitext(name)[0]
            template_source = open(os.path.join(base_partials, name), 'r', encoding='utf8').read()
            template = self.compiler.compile(template_source)
            partials[filename] = template
        return partials

    def get_helpers(self):
        helpers = super().get_helpers()
        helpers.update({"asset": _asset,
                        "date": _date,
                        "strftime": _strftime,
                        })
        return helpers


def _asset(options, val, *args, **kwargs):
    return "/static/{}".format(val)


def _date(options, format, *args, **kwargs):
    dt = datetime.datetime.now()

    date = format.replace("YYYY", str(dt.year))
    date = date.replace("DD", str(dt.day))
    date = date.replace("MMMM", str(dt.month))
    date = date.replace("MM", str(dt.month))
    return date


def _strftime(options, source, format, *args, **kwargs):
    dt = dateutil.parser.parse(options[source])
    return datetime.datetime.strftime(dt, format)
