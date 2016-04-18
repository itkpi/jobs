from aiohttp.multidict import CIMultiDict
from aiohttp.web_reqrep import Response


def render(request, template_name, context):
    loader = request.app['loader']
    template = loader.get_template(template_name)
    return template(context, helpers=loader.get_helpers(), partials=loader.get_partials())


class AIOBarsResponse(Response):
    def __init__(self, request, template_name, context, headers=None, **kwargs):
        if not headers:
            headers = {}
        headers = CIMultiDict(headers)
        if 'Content-type' not in headers:
            headers.update({'Content-type': 'text/html; charset=utf-8'})

        body = render(request, template_name, context)
        super().__init__(body=body.encode(), headers=headers, **kwargs)
