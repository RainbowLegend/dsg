from .errors import *

class Members:
    
    def __init__(self, **kwargs):
        pass
    
    @property
    def isgay(member):
        if member.lower() == 'rushil':
            return True
        elif member.lower() != 'rushil':
            return False
        else:
            raise dsgException(Exception)
    
