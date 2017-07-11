# torethink

Rethinkdb Mixin For Tornado Framework

**only Python 3.5 projects**

# Installation

**pip install torethink**


# Usage

```python
import time
import tornado.web
import tornado.escape

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

class BaseHandler(tornado.web.RequestHandler):

    async def prepare(self):
        self.db = await Torethink.init(database=scheme, create_scheme=True)

    def write_json(self, obj):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.finish(tornado.escape.json_encode(obj))

class DemoHandler(BaseHandler):

    async def get(self):
        for i in range(20):
            email = "%s@%s.com" % (int(time.time()), int(time.time()))
            email_record = scheme['tables'].get('user', {})
            email_record['email'] = email

            check = {'email': email}
            result = await self.db.insert_unique('user', check, email_record)
            print(result)

        for user in (await self.db.list("user")):
            print("user email: %s, user id: %s" % (user['email'], user['id']))

        self.write('done. check console')

```
