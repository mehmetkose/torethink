
# Rethinkdb Wrapper For Tornado Framework
# https://github.com/mehmetkose/torethink

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2016 Mehmet Kose mehmet@linux.com

import time
import tornado.ioloop
import tornado.gen

from torethink import Torethink

database = {
    'db': 'test',
    'host': '127.0.0.1',
    'port': 28015,
    'tables': {
        'user': {
            'user_name': {'default': None, 'specs': []},
            'user_mail': {'default': None, 'specs': []},
            'add_date': {'default': int(time.time()), 'specs': ['noedit', 'index']},
            'update_date': {'default': int(time.time()), 'specs': ['noedit', 'index']},
        }
    }
}

async def test():
    db = await Torethink.init(database=database, create_scheme=True)
    list = await db.all("user")
    print(list)

async def main():
    tornado.ioloop.IOLoop.current().spawn_callback(test)


if __name__ == "__main__":
    tornado.ioloop.IOLoop.current().run_sync(main)
    tornado.ioloop.IOLoop.current().start()
