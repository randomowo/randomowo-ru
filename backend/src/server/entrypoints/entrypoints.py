from aiohttp import web

from .root.app import make_app
from ..settings.settings import Settings, EntrypointsSettings


class Entrypoits:
    _runner: web.AppRunner

    def __init__(
            self,
            settings: Settings,
            services,
            domains
    ):
        self._app = make_app(
            settings.web,
            services,
            domains
        )
        self._settings: EntrypointsSettings = settings.entrypoints

    async def start(self):
        self._runner = web.AppRunner(
            self._app,
            # add logging things
        )

        await self._runner.setup()

        host = self._settings.server_host
        port = self._settings.server_port
        site = web.TCPSite(
            self._runner,
            host,
            port
        )
        await site.start()

        # log service started

    async def stop(self):
        await self._runner.cleanup()
