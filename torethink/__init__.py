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

    async def hello(self):
        #await self.db
        return "hello"
