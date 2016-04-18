from aiohttp.web_reqrep import Response
from aiohttp.web_urldispatcher import View


class Index(View):
    async def index(request):

        return Response(body=b"Hello world from aiohttp app", headers={'Content-type': 'text/html; charset=utf-8'})
