
# Rethinkdb Wrapper For Tornado Framework
# https://github.com/mehmetkose/torethink

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2016 Mehmet Kose mehmet@linux.com


import asyncio
import rethinkdb as r
r.set_loop_type("tornado")

from torethink import initiator


class Torethink(object):

    @classmethod
    async def init(cls, database, create_scheme=True):
        self = Torethink()
        self.db = await r.connect(host=database['host'], db=database['db'], port=database['port'])
        if create_scheme:
            await initiator.create_tables(database=database, connection=self.db)
        return self

    async def iterate_cursor(self, cursor):
        items = []
        while (await cursor.fetch_next()):
            item = await cursor.next()
            items.append(item)
        return items

    async def get(self, table, record_id):
        return (await r.table(table).get(record_id).run(self.db))

    async def insert(self, table, insert_dict):
        return (await r.table(table).insert(insert_dict).run(self.db))

    async def remove(self, table, record_id):
        return (await r.table(table).get(id=record_id).delete().run(self.db))

    async def update(self, table, id, data):
        return (await r.table(table).get(id).update(data).run(self.db))

    async def filter(self, table, criterion):
        cursor = await r.table(table).filter(criterion).run(self.db)
        return (await self.iterate_cursor(cursor))

    async def list(self, table, key='get', value='all', index='update_date', order='desc', create_index=False):
        if create_index:
            await self.index(table, index)

        if order == "desc":
            direction = r.desc(index)
        else:
            direction = r.asc(index)

        if key == 'get' and value == 'all':
            items = await self.all(table)
        else:
            items = await self.filter(table, {key: value})
        return items

    async def all(self, table):
        cursor = await r.table(table).run(self.db)
        return (await self.iterate_cursor(cursor))

    async def insert_unique(self, table, check_dict, insert_dict):
        cursor = await r.table(table).filter(check_dict).run(self.db)
        items = await self.iterate_cursor(cursor)
        if len(items) == 0:
            results = await r.table(table).insert(insert_dict).run(self.db)
            return results
        return False

    async def remove_all_with_key(self, table, key, value):
        result = await r.table(table).filter({key: value}).delete().run(self.db)
        return (result)

    async def remove_one_with_key(self, table, key, value):
        items = await self.list(table, key, value)
        if len(items) > 0:
            item_id = items[0]
            await self.remove(table, item_id)
            return True
        return False

    async def update_all_with_key(self, table, key, value, data):
        return (await r.table(table).filter({key: value}).update(data).run(self.db))

    async def update_one_with_key(self, table, key, value, data):
        items = await self.list(table, key, value)
        if len(items) > 0:
            item_id = items[0]['id']
            return (await self.update(table, item_id, data))
        return False

    async def list_contains_with_key(self, table, key, value, limit=200):
        cursor = await r.table(table).filter(
            lambda record: record[key].contains(value)
        ).limit(limit).run(self.db)
        return (await self.iterate_cursor(cursor))

    async def flush(self, table):
        return(await r.table(table).delete().run(self.db))

    async def index(self, table, key):
        try:
            return (await r.table(table).index_create(key).run(self.db))
        except r.errors.ReqlOpFailedError as e:
            return False
