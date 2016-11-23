import unittest

import asyncio

from torethink import Torethink

async def main(settings):
    db = await Torethink.init(settings)
    hello = await db.hello()
    print(hello)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main({}))
