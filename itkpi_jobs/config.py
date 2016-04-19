import trafaret as t

from aio_yamlconfig.trafarets import ExistingDirectory


CONFIG_TRAFARET = t.Dict({
    t.Key('ASSETS_DIR'): ExistingDirectory,
    t.Key('TEMPLATES_DIR'): ExistingDirectory,
    t.Key('DEBUG'): t.Bool
})
