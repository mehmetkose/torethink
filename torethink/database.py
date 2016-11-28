
# Rethinkdb Wrapper For Tornado Framework
# https://github.com/mehmetkose/torethink

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2016 Mehmet Kose mehmet@linux.com


import time


class Database(object):

    def __init__(self, db=None, host='127.0.0.1', port=28015, tables=[]):
        self.db = db
        self.host = host
        self.port = port
        self.tables = tables

    def __str__(self):
        return "Database Name: %s, Host: %s, Port: %s, \
                Tables: %s" % (self.db, self.host, self.port, self.tables)

    def get_table(self, table_name):
        for table in self.tables:
            if table.name == table_name:
                return table
        return False


class Row(object):

    def __init__(self, name=None, value=None, default=None, specs=[]):
        self.name = name
        self.default = default
        self.specs = specs
        self.value = value
        if not self.value:
            self.value = self.default

    def __str__(self):
        return "Row Name: %s, Value: %s, Default: %s, \
                Specs: %s" % (self.name, self.value, self.default, self.specs)


class Table(object):

    def __init__(self, name=None, rows=[]):
        self.name = name
        self.rows = rows

        self.rows.append(Row(name='add_date', default=int(
            time.time()), specs=['noedit', 'index']))
        self.rows.append(Row(name='update_date', default=int(
            time.time()), specs=['noedit', 'index']))

    def __str__(self):
        return "Table Name: %s, Rows: %s" % (self.name, self.rows)

    def get_row(self, row_name):
        for row in self.rows:
            if row.name == row_name:
                return row
        return False


class Record(object):

    def __init__(self, target_dict):
        for key, value in target_dict.items():
            if isinstance(value, (list, tuple)):
                setattr(self, key, [Record(key) if isinstance(
                    key, dict) else key for key in value])
            else:
                setattr(self, key, Record(value)
                        if isinstance(value, dict) else value)
