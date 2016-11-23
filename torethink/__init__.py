#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Rethinkdb Mixin For Tornado Framework.
# https://github.com/mehmetkose/torethink

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2016 Mehmet Kose mehmet@linux.com


import asyncio


class Torethink(object):

    @classmethod
    async def init(cls, settings):
        self = Torethink()
        self.settings = settings
        # self.connection = await connect("...")
        return self

    async def hello(self):
        print(self.settings)
        return "hello"
