"""


"""


class GameLoop(object):
    """
    Master game loop for one session.
    
    One server can run several sessions.
    """
    
    def __init__(self):
        
        self.state = None
    
        self.event_id = 0
        
        self.current_tick = 0
        
        
    def tick(self):        
        """
        Do game calculations for one step.
        """
        
    def start(self):
        """
        """
        
    def attach_client(self, client):
        """
        Attach a client session which will start folloing this game.
        """
        

    def create_event(self, type):
        """
        Create a game event.
        
        Associate a running counter on each event.
        """