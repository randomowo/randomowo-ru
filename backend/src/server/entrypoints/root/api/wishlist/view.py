from aiohttp import web

__all__ = ['WishlistView']


class WishlistView(web.View):

    def __init__(self):
        # add db controller
        pass

    async def get(self, request) -> web.Response:
        # get list from db with pagination
        pass

    async def post(self, request) -> web.Response:
        # get element from request
        # put to db
        # return 200
        pass

    async def put(self, request) -> web.Response:
        # for admin
        # update field
        pass
