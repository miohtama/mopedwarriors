

class GameObject(object):
    """
    Stateful game object on the screen. E.g. bullet, player sprite, etc.
    """

    def tick(self, loop, state):
        """
        Perform thinking for this object
        
        :param loop: Game loop
        
        :param state: Game state
        """
    
    def serialize_state(self):
        """
        
        """