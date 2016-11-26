
# Rethinkdb Wrapper For Tornado Framework
# https://github.com/mehmetkose/torethink

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2016 Mehmet Kose mehmet@linux.com

import rethinkdb as r

async def create_tables(database, connection):
    try:
        await r.db_create(database['db']).run(connection)
        print('Database created: %s' % (database['db']))
    except:
        pass

    for table_name in database['tables'].keys():
        try:
            await r.db(database['db']).table_create(
                table_name, durability='hard').run(connection)
            print('Table created: %s' % (table_name))
        except:
            pass

    for table_name in database['tables'].keys():
        for table_key in database['tables'][table_name].keys():
            if 'specs' in database['tables'][table_name][table_key]:
                specs = database['tables'][table_name][table_key]['specs']
                if 'index' in specs:
                    try:
                        await r.db(database['db']).table(table_name).index_create(table_key).run(connection)
                    except:
                        pass
