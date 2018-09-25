from .errors import *

class Members:
    
    def __init__(self, **kwargs):
        pass

    def isgay(user: str):
        """Returns if the user is gay"""
        if user == 'rushil':
            return True
        elif user != 'rushil':
            return False
        else:
            raise dsgException('Finding isgay() method failed')
            
    def members():
        """Method that returns a list of members"""
        membersofDSG = ['rushil', 'nigel', 'matt', 'armen', 'nicolo', 'dan']
        gen = []
        for member in membersofDSG:
            gen.append(member.title())
        return gen
