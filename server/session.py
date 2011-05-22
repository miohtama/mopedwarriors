"""


"""

import random

class GameSession(object):
    """
    One game session where players may start join.
    """
    
    def __init__(self, server, host):
        self.server = server
        self.host = host
        self.id = None
        self.clients = []
        
        
    def init(self, name):
        """
        Initialize the game state.
        """
        
        # Unique id for this session
        self.id = random.random()
        
        # Human readable name for this session (unicode)
        assert type(name) == unicode
        
        self.name = name
        
    def add_client(self, client):
        """
        A new client joins to an existing session.
        
        :param client: GameClient instance
        """
        if not client in self.clients:
            self.clients.append(client)
        
    def to_json(self):
        """
        :return: JSON data to be transfered to clients
        """
        return {
                "id" : self.id,
                "host" : self.host.id,
                "name" : self.name,
                "clients" : self.clients
        }
        
        
        