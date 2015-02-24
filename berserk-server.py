"""The server side of the I/O-bound Berserk benchmark"""

# import tornado.ioloop
# import tornado.web
from flask import Flask
from flask import request

import conf
import berserk
from log import log_server as log
import json

# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("Hello, world")

# application = tornado.web.Application([
#     (r"/", MainHandler),
# ])


app = Flask(__name__)

@app.route("/")
def hello():
    n = int(request.args.get('task_size'))
    run_num = int(request.args.get('tasks'))
    berserk.cpu(run_num, n)
    result_json = json.dumps({'result': True})
    return result_json


if __name__ == "__main__":
    log('Berserk I/O-bound benchmark server listening on: {}'.format(
        conf.berserk_server_url)
    )
    # application.listen(conf.berserk_server_port)
    # tornado.ioloop.IOLoop.instance().start()
    #app.debug = True
    app.run(port=conf.berserk_server_port)
