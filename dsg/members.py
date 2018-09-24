from .errors import *

class Members:
    
    def __init__(self, **kwargs):
        pass
    
    @property
    def isgay(self):
        try:
            return False
        except:
            raise dsgException('Finding isgay() property failed')
    
