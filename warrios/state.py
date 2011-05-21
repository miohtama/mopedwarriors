from server.state import GameState

class WarriorState(GameState):
    """
    The Moped Warriors game state.
    """
    
    def __init__(self):
        GameState.__init__(self)
        self.terrain = None
        self.players = []
        