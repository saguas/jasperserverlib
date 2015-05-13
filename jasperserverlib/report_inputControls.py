import core as jasper
import json


from resource_details import Details
from core.exceptions import PathError


class InputControls(object):
    
    def __init__(self, session, path):
        self.session = session
        self.path = path
        self.icDescriptor = None
        self.d = Details(self.session, self.path)
    
    def getDescriptor(self, expanded=True):
        if not self.icDescriptor:
            self.icDescriptor = self.d.details(expanded=expanded).getDescriptor()
        return self.icDescriptor