from aiohttp.web_reqrep import Response
from aiohttp.web_urldispatcher import View

from aio_pybars import render, AIOBarsResponse


class Index(View):
    async def index(request):
        context = {"var": "value"}
        return AIOBarsResponse(request, 'jobs/jobs', context)
