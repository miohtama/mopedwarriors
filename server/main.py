"""

    Start game engine.
    
    1) Tornado web server


"""

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado.websocket import WebSocketHandler

class GameServer(object):
    """
    """
    
    def __init__(self):
        """
        
        """
        #: List of available Game sessions object
        sessions = []
        
class WebHandler(WebSocketHandler):
    
    def open(self):
        print "New connection opened."

    def on_message(self, message):
        print "Message"
        print message

    def on_close(self):
        print "Connection closed."

