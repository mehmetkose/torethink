
import tornado.ioloop
import tornado.gen

from torethink import Torethink

async def test():
    db = await Torethink.init(host="127.0.0.1", db="authentication", port=28015)
    hello = await db.hello()
    print(hello)

async def main():
    tornado.ioloop.IOLoop.current().spawn_callback(test)

if __name__ == "__main__":
    tornado.ioloop.IOLoop.current().run_sync(main)
    tornado.ioloop.IOLoop.current().start()
