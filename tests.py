
# Rethinkdb Wrapper For Tornado Framework
# https://github.com/mehmetkose/torethink

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2016 Mehmet Kose mehmet@linux.com

import time
import tornado.ioloop
import tornado.gen

from torethink import Torethink

scheme = {
    'db': 'awesome_project',
    'host': '127.0.0.1',
    'port': 28015,
    'tables': {
        'user': {
            'email': {'default': None, 'specs': []},
            'add_date': {'default': int(time.time()), 'specs': ['noedit']},
            'update_date': {'default': int(time.time()), 'specs': ['noedit', 'index']},
            'is_deleted': {'default': False, 'specs': ['index']},
        },
    }
}

async def test():
    db = await Torethink.init(database=scheme, create_scheme=True)

    for i in range(20):
        email = "%s@%s.com" % (int(time.time()), int(time.time()))
        email_record = scheme['tables'].get('user', {})
        email_record['email'] = email

        check = {'email': email}
        result = await db.insert_unique('user', check, email_record)
        print(result)

    for user in (await db.list("user")):
        print("user email: %s, user id: %s" % (user['email'], user['id']))

async def main():
    tornado.ioloop.IOLoop.current().spawn_callback(test)


if __name__ == "__main__":
    tornado.ioloop.IOLoop.current().run_sync(main)
    tornado.ioloop.IOLoop.current().start()
