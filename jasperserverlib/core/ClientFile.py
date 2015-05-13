from ClientResource import ClientResource
from resources_mime_type import ResourceFilesMimeType as ft
from resource_media_types import *
from resources_mime_type import ResourceFilesMimeType
import json

class ClientFile(ClientResource):
    
    FileType = ResourceFilesMimeType
    
    def __init__(self):
        self._resource_type = TYPE_FILE
    
    def getType(self):
        return self.filetype
    
    def setType(self, mimetype):
        self.filetype = mimetype
        mtype = ft().getMimeType(mimetype.upper())
        self.setMimeType(mtype)
        return self
        
    def getContent(self):
        return self.content
    
    def setContent(self, content):
        self.content = content
        return self
        
    def setMimeType(self, mimetype):
        self.mimetype = mimetype
        
    def getMimeType(self):
        return self.mimetype
        
    def toJson(self):
        return {"label": self.getLabel(), "description": self.getDescription(), "content": self.getContent(), "type": self.getType()}
    
    def toString(self):
        return self.__str__()
        
    def __str__(self):
        return json.dumps(self.toJson())
        
    def __repr__(self):
        return self.__str__()
