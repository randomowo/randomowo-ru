from pathlib import Path

from .entrypoints.entrypoints import Entrypoits
from .settings.settings import Settings

class Application:
    _config_dir: Path

    def __init__(self, config_dir):
        self._config_dir = config_dir

    async def start(self):
        settings = Settings(self._config_dir)

        services = None
        settings = None
        domains = None
        entrypoints = Entrypoits(
            settings,
            services,
            domains,
        )

        await entrypoints.start()

    async def stop(self):
        pass
