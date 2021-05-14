import json
from dataclasses import dataclass
from pathlib import Path


def remove_excess_kwargs(cls):
    def init(self, *args, **kwargs):
        for k, v in list(kwargs.items()):
            if hasattr(self, k) and isinstance(self.__annotations__[k], type(v)):
                setattr(self, k, v)
        cls.__init__ = init
        return cls


@dataclass
@remove_excess_kwargs
class EntrypointsSettings:
    server_host: str = '0.0.0.0'
    server_port: int = 8080


@dataclass
@remove_excess_kwargs
class DbSettings:
    pass


@dataclass
@remove_excess_kwargs
class WebSettings:
    pass


class Settings:
    _entrypoints: EntrypointsSettings
    _db: DbSettings
    _web: WebSettings

    def __init__(self, config_dir):
        self._settings = self._parse_settings(config_dir)
        self.entrypoints = EntrypointsSettings(self._settings)
        self.db = DbSettings(self._settings)
        self.web = WebSettings(self._settings)

    def _parse_settings(self, config_dir: Path):
        settings = {}

        for path in config_dir.glob('*'):
            if path.is_file():
                with path.open('r') as f:
                    if path.suffix == '.json':
                        settings |= json.load(f)
                    # TODO: add more types

        return settings
