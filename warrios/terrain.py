import pygame

class Terrain(object):
    """
    2D map presenting the game arena.
    
    Default size is 824 x 768 (iPad screen optimized with one side panel)
    """
    
    def __init__(self):
        #: Raw pixel data of game mask 
        self.mask = None 
        
        #: Raw pixel data of background image layer
        self.background = None
        
        #: Raw pixel data of foreground layer   - can be destroyed
        self.foreground = None
        
        
    def load(self, folder):
        """
        :param folder: Absolute path to folder from where to load fg, bg and mask files
        """
        