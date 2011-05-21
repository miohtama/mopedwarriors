

class Client(object):
    """
    Hold game session specific client information.
    """
    
    
    def __init__(self, magic_token):
        """
        """
        
        #: Unguessable number
        self.magic_token = magic_token
        
        #: State change events to send
        self.state_change_event_buffer = []

        #: State replace events to send
        self.state_replace_event_buffer = []

        
    def send_upate(self):
        pass