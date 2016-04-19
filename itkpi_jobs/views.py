from aiohttp.web_urldispatcher import View

from aio_pybars import AIOBarsResponse


class Index(View):
    async def index(request):
        context = {"var": "value"}
        return AIOBarsResponse(request, 'jobs/jobs', context)
