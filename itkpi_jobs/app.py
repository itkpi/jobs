import asyncio
import os

from aiohttp.web import Application

import aio_pybars
import aio_yamlconfig
from itkpi_jobs.config import CONFIG_TRAFARET
from itkpi_jobs.template_utils import AppFSTemplateLoader
from itkpi_jobs.views import Index

CONFIG_FILE = os.path.join(os.path.dirname(__file__), "config.yaml")


def build_application():
    loop = asyncio.get_event_loop()
    app = Application(loop=loop)

    loop.run_until_complete(aio_yamlconfig.setup(app,
                                                 config_files=[CONFIG_FILE],
                                                 trafaret_validator=CONFIG_TRAFARET,
                                                 base_dir=os.path.dirname(__file__)))

    loop.run_until_complete(aio_pybars.setup(app,
                                             templates_dir=app.config['TEMPLATES_DIR'],
                                             Loader=AppFSTemplateLoader))

    app.router.add_route('*', r'/', Index.index)
    app.router.add_static(r'/static/',  os.path.join(os.path.dirname(__file__), app.config['ASSETS_DIR']))
    return app
