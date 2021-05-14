from aiohttp import web

import api
from backend.src.server.settings.settings import WebSettings


def make_app(
    settings: WebSettings,
    services,
    domains
) -> web.Application:
    app = web.Application(
        middlewares=[]
    )

    app.add_subapp('/api', api.make_app())

    return app
