from weakref import WeakValueDictionary 

class GameState(object):
    """
    Hold everything about the current game state.
    """
    
    
    def __init__(self):
        
        # Active game objects which can be referred from the client side by their id                
        self.objects = WeakValueDictionary()
        
        