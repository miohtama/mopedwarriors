

class GameEvent(object):
    """
    """
    
class StateChangingEvent(GameEvent):
    """
    The client must receive and process all state changing events in order.
    """
    
    
class StateReplacingEvent(GameEvent):
    """
    The state replacing events can be skipped by client, as new events are expected to flow in steadily. 
    """
    
class Command(GameEvent):
    """
    Client issued a command on the server.
    """