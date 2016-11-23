#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Rethinkdb Mixin For Tornado Framework.
# https://github.com/mehmetkose/torethink

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2016 Mehmet Kose mehmet@linux.com


import asyncio
import rethinkdb as r
r.set_loop_type("tornado")


class Torethink(object):

    @classmethod
    async def init(cls, host="localhost", db="test", port=28015):
        self = Torethink()
        self.db = await r.connect(host=host, db=db, port=port)
        return self

    async def iterate_cursor(self, cursor):
        items = []
        while (await cursor.fetch_next()):
            item = await cursor.next()
            items.append(item)
        return items

    async def insert(self, table, insert_dict):
        results = await r.table(table).insert(insert_dict).run(self.db)
        return results

    async def remove(self, table, record_id):
        results = await r.table(table).get(id=record_id).delete().run(self.db)
        return results

    async def update(self, table, id, data):
        results = await r.table(table).get(id).update(data).run(self.db)
        return results

    async def filter(self, table, criterion):
        cursor = await r.table(table).filter(criterion).run(self.db)
        items = await self.iterate_cursor(cursor)
        return items

    async def list(self, table, key='get', value='all', index='update_date', order='desc', create_index=True):
        if create_index:
            await self.index(table, index)

        if order == "desc":
            direction = r.desc(index)
        else:
            direction = r.asc(index)

        if key == 'get' and value == 'all':
            cursor = await r.table(table).order_by(index=direction).run(self.db)
        else:
            cursor = await r.table(table).order_by(index=direction).filter(r.row[key] == value).run(self.db)

        items = await self.iterate_cursor(cursor)
        return items

    async def insert_unique(self, table, check_dict, insert_dict):
        cursor = await r.table(table).filter(check_dict).run(self.db)
        items = await self.iterate_cursor(cursor)
        if len(items) == 0:
            results = await r.table(table).insert(insert_dict).run(self.db)
            return results
        return False

    async def remove_all_with_key(self, table, key, value):
        results = await r.table(table).filter({key: value}).delete().run(self.db)
        return results

    async def remove_one_with_key(self, table, key, value):
        items = await self.list(table, key, value)
        if len(items) > 0:
            item_id = items[0]
            await self.remove(table, item_id)
            return True
        return False

    async def update_all_with_key(self, table, key, value, data):
        results = await r.table(table).filter({key: value}).update(data).run(self.db)
        return(results)

    async def update_one_with_key(self, table, key, value, data):
        items = await self.list(table, key, value)
        if len(get_list) > 0:
            item_id = items[0]
            results = await self.update(table, item_id, data)
            return results
        return False

    async def flush(self, table):
        results = await r.table(table).delete().run(self.db)
        return results

    async def index(self, table, key):
        try:
            result = await r.table(table).index_create(key).run(self.db)
            return True
        except r.errors.ReqlOpFailedError as e:
            return False
