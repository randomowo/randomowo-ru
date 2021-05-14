import asyncio
from .app import Application
from pathlib import Path


def main():
    loop = asyncio.get_event_loop()
    loop.set_exception_handler(exception_handler)
    loop.create_task(start_application())
    loop.run_forever()


async def start_application():
    app = Application(
        config_dir=Path('/etc/randomowo-ru')
    )

    try:
        await app.start()
    except Exception as err:
        asyncio.get_event_loop().stop()
        raise err


def exception_handler(loop, context):
    err = context.get('exception')
    if not isinstance(err, SystemExit):
        loop.default_exception_handler(context)