import json
from json import JSONEncoder
import logging

import  utils

logger = logging.getLogger("client")

class GameMessageEncoder(JSONEncoder):
    """
    Support our special callbacks to convert Python objects directly to JSON.
    """
    
    def default(self, o):
        if hasattr(o, "to_json"):
            return o.to_json()
        else:
            JSONEncoder.default(self, o)
            
encoder = GameMessageEncoder()

class GameClient(object):
    """
    Hold game session specific client information.
    """

    def __init__(self, server, connection, id):
        """
        """
        
        self.server = server
        
        self.socket = connection
        
        self.session = None
        
        #: Unguessable number
        self.id = id
        
        # Human readable name
        self.name = u"Dummy"
        
        #: State change events to send
        self.state_change_event_buffer = []

        #: State replace events to send
        self.state_replace_event_buffer = []

        
    def send_message(self, message, payload):
        """

        :param message: Message type as a string
        
        :param payload: Python dict or object having to_json() method
        """
                
        data = {
                "message" : message,
                "payload" : payload
        }
                        
        encoded = encoder.encode(data)

        self.socket.write_message(encoded)
    
    def send_event(self, event):
        """
        Send an event to a client. 
        
        Event class instance is automatically converted to a message.                
        """
        
    def on_create_session(self, message):
        """ This clients wants to host a new session.
        """
        
        name = message["name"]
        session = self.server.create_session(host=self, name=name)                
        self.session = session
        self.send_message("sessioncreated", session)
        
    def on_join_session(self, message):
        """ This client tries to join to existing game session.
        """
        
        id = message["id"]
        session = self.server.join_session(id, self)
        if session:
            self.send_message("joined", session)
        else:
            self.send_message("joinFailed", { "id": id }) 
        
        
    def on_message(self, message, payload):
        """
        :param message: Dictionary of message data        
        """
        
            
        callback_name = "on_" + utils.convert_from_camelcase_to_underscore(message)
        
        if not hasattr(self, callback_name):
            """
            """
            logger.error("Unknown message:" + callback_name)
            self.close()
        else:
            callback = getattr(self, callback_name)
            callback(payload)    
                
    def close(self):
        """
        """
        self.socket.close()
        self.server.close_client(self)
        
        
    def to_json(self):
        """
        Serialize to JSON
        """
        return {
                "id" : self.id,
                "name" : self.name
        }
            