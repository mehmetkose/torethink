# torethink

Rethinkdb Mixin For Tornado Framework 
**only Python 3.5 projects**

# Installation

**pip install torethink**


# Usage

```python
...
from torethink import Torethink
...

class BaseHandler(tornado.web.RequestHandler):

    @tornado.gen.coroutine
    def prepare(self):
        self.db = yield Torethink.init(host="127.0.0.1", db="authentication", port=28015)

    def write_json(self, obj):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.finish(json.dumps(obj))

class DemoHandler(BaseHandler):

    @tornado.gen.coroutine
    def get(self):
    	list = yield self.db.list("user")
    	self.write_json({'users': list})

    ...
```