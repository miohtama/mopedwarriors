

class Terrain(object):
    """
    2D map presenting the game arena.
    """
    
    def __init__(self):
        #: Raw pixel data of game mask 
        self.mask = None 
        
        #: Raw pixel data of background layer 
        self.background = None
        
        #: Raw pixel data of foreground layer 
        self.background = None
        
        
    def load(self, folder):
        """
        :param folder: Absolute path to folder from where to load fg, bg and mask files
        """