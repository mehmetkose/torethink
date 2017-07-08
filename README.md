# torethink

Rethinkdb Mixin For Tornado Framework

**only Python 3.5 projects**

# Installation

**pip install torethink**


# Usage

```python
import tornado.web
import tornado.escape

from torethink import Torethink

scheme = {
    'db': 'awesome_project',
    'host': '127.0.0.1',
    'port': 28015,
    'tables': {
        'user': {
            'user_email': {'default': None, 'specs': []},
            'user_username': {'default': None, 'specs': []},
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
        list = await self.db.list("user")
        self.write_json({'users': list})

```
