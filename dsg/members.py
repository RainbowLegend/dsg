from .errors import *

class Members:
    
    def __init__(self, **kwargs):
        pass
    
    @classmethod
    def isgay(self, user: str):
        """Returns if the user is gay"""
        if user.lower() == 'rushil':
            return True
        elif user.lower() != 'rushil':
            return False
        else:
            raise dsgException('Finding isgay() method failed')
            
    @classmethod      
    def members(self):
        """Generator that returns all members"""
        membersofDSG = ['rushil', 'nigel', 'matt', 'armen', 'nicolo', 'dan']
        
        for member in membersofDSG:
            yield member.title()
    
