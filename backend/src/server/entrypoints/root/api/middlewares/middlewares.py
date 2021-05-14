from backend.src.server.entrypoints.root.api.middlewares.redirect_with_auth import RedirectWithAuthMiddleware


class RootMiddlewares:
    def __init__(
        self
    ):
        self.redirect_with_auth = RedirectWithAuthMiddleware()
