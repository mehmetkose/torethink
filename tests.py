
# Rethinkdb Wrapper For Tornado Framework
# https://github.com/mehmetkose/torethink

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2016 Mehmet Kose mehmet@linux.com

import time
import tornado.ioloop
import tornado.gen

from torethink import Torethink, Database, Table, Row

UserTable = Table(name='user')
UserTable.rows.append(Row('user_name'))
UserTable.rows.append(Row('user_mail', specs=['index']))

ProjectDatabase = Database(db='test', host='127.0.0.1', port=28015)
ProjectDatabase.tables.append(UserTable)

async def test():
    db = await Torethink.init(database=ProjectDatabase, create_structure=True)
    for user in (await db.all("user")):
        print(user)

async def main():
    tornado.ioloop.IOLoop.current().spawn_callback(test)


if __name__ == "__main__":
    tornado.ioloop.IOLoop.current().run_sync(main)
    tornado.ioloop.IOLoop.current().start()

