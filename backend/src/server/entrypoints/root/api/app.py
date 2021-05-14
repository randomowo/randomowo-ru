from aiohttp import web

from . import WishlistView


def make_app() -> web.Application:
    app = web.Application(
        middlewares=[

        ]
    )


    app.add_routes([
        web.view('/wishlist', WishlistView),
        #web.view('/filmlist', FilmListView)
    ])

    return app