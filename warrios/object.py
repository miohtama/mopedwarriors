from server.object import GameObject


class PlayerState(object):
    """
    
    """
    
    def __init__(self):
        self.name = None    
        self.alive = True
        # Cotrolled moped id
        self.moped = None
        

class MopedState(object):
    """
    
    """
    
    def __init__(self):
        
        # 2D coordinates where         
        self.desired_direction = None
        
        # 2D coordinates where we are now
        self.position = None
        
    
    def tick(self, loop, state):
        """
        """