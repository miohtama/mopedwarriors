"""

    Start game engine.
    
    1) Tornado web server


"""

import logging
import json
from weakref import WeakValueDictionary, WeakKeyDictionary

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado.websocket import WebSocketHandler

from client import GameClient
from session import GameSession

logger = logging.getLogger("Server")

class GameServer(object):
    """
    """
    
    def __init__(self):
        """
        
        """
        #: List of available Game sessions object
        self.sessions = {}
        
        self.clients = WeakKeyDictionary()
        
        
    def create_client(self, socket, id):
        """
        Create a new game client.
        """
        client = GameClient(self, socket, id)
        
        self.clients[socket] = client
        
        client.send_message("welcome", None)
        
        logger.info("Client succesfully connected")
        
        return client
    
    def create_session(self, host, name):
        """
        Create a new game session.
        
        :param host: GameClient instance hosting the session
        """
        
        session = GameSession(self, host)
        session.init(name)        
        
        self.sessions[session.id] = session
        
        return session
        
    def join_session(self, session_id, client):
        """
        Join to an existing gaming session.
        
        :return: Session object where we joined or None if failed
        """
        
        session = self.sessions.get(session_id, None)
        if not session:
            return None
        
        session.add_client(client)
      
        self.broadcast_all("clientJoined", client)
        
        self.broadcast_all("sessionStateChanged", session)
        
        return session

    def on_client_message(self, socket, message, payload):
        """
        Handle l
        """
        
        client = self.clients[socket]
        
        client.on_message(message, payload)
        
    def close_client(self, client):
        """
        Clean-up client and make other players aware we lost this one.
        """
        del self.clients[client.socket]
        
    def broadcast_all(self, type, payload):
        """
        Send a message to all client.
        """
        for client in self.clients.values():
            client.send_message(type, payload)
        
        
        
class CommunicationHandler(WebSocketHandler):
    """ Handle communication between the server and the client """
    
    def __init__(self, server, *args):
        WebSocketHandler.__init__(self, *args)
        self.server = server
    
    def open(self):
        logger.info("New connection opened.")

    def on_message(self, message):
        
        logger.debug("Incoming message:" + message)
        
        # Special handling for greeting
        decoded = json.loads(message)
        
        self.on_decoded_message(decoded)
    
    def on_decoded_message(self, data):
        """
        :param message: Python dictionary of de-serialized JSON object
        """
        
        if not "message" in data:
            self.close_bad_connection("Protocol violation: no eventType parameter in the message")
        
        message = data.get("message", None)
        payload = data.get("payload", None)
            
        if message == "greet":
            self.on_greeting(payload)
        else:
            self.server.on_client_message(self, message, payload)
            
    def on_greeting(self, message):
        """
        """
        
        # XXX: Assumes all greetings are valid
        self.server.create_client(self, message["id"])
        
    def on_close(self):
        logger.info("Connection closed")

    def close_bad_connection(self, reason):
        """
        Close the connection as it didn't follow the protocol.
        """
        logger.error("Closing socket because of " + reason)
        self.close()
        
class CommunicationHandlerFactory(object):
    """ Pass initialization parameters through Tornado URL mapping """
    
    def __init__(self, server):
        self.server = server
        
    def __call__(self, *args):
        return CommunicationHandler(self.server, *args)

