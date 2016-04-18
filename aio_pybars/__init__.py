from aio_pybars.loader import FSTemplateLoader


async def setup(app):
    app['loader'] = FSTemplateLoader(app['config']['TEMPLATES_DIR'])
