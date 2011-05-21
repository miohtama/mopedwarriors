import sys
import os

import tornado.ioloop
import tornado.web
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado.websocket import WebSocketHandler

PORT = 9999

sys.path.append("..")

from server.main import GameServer, WebHandler


class MainHandler(tornado.web.RequestHandler):
    """ """
    def get(self):
        self.write("Hello, world")


static_path = os.path.join(os.path.dirname(__file__), "..", "client", "html")
static_path = os.path.abspath(static_path)

app = Application([
   ("/websocket", WebSocketHandler),
   (r"/(.*)", tornado.web.StaticFileHandler, {"path": static_path}),               
   ])

# For Adobe security policy file serving
crossdomain_xml_server = Application([
   (r"/(.*)", tornado.web.StaticFileHandler, {"path": static_path}),               
   ])

app.listen(PORT)

crossdomain_xml_server.listen(843)

print "Server started at port " + str(PORT)

#from tornado.ioloop import _Select 
#loop = IOLoop(_Select())
#loop.start()

IOLoop.instance().start()