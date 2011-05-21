"""


"""

from server import event

class PlayerJoin(event.Command):
    
    name = ""


class PlayerJoined(event.StateChangingEvent):
    """
    Broadcast to all clients who has joined the game.
    """ 
    
class PlayerStart(event.Command):
    """
    Someone wants start playing.
    """
    
class PlayerCreated(event.StateChangingEvent):
    """
    Broadcast to all clients who has joined the game.
    """ 
    
    player_data = None