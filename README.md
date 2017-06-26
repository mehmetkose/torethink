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

class BaseHandler(tornado.web.RequestHandler):

    async def prepare(self):
        self.db = await Torethink.init(host="127.0.0.1", db="authentication", port=28015)

    def write_json(self, obj):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.finish(tornado.escape.json_encode(obj))

class DemoHandler(BaseHandler):

    async def get(self):
        list = await self.db.list("user")
        self.write_json({'users': list})

```
