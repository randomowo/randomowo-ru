from typing import Callable, Awaitable

from aiohttp import web


@web.middleware
class RedirectWithAuthMiddleware:

    @classmethod
    async def __call__(
            cls,
            request: web.Request,
            handler: Callable[[web.Request], Awaitable[web.Response]]
    ) -> web.Response:
        # TODO
        return await handler(request)
