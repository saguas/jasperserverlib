from ClientResource import ClientResource
from resource_media_types import *
import json


class ClientFolder(ClientResource):
    
    def __init__(self):
        self._resource_type = TYPE_FOLDER
    
    def toString(self):
        return self.__str__()
        
    def toJson(self):
        return {"label": self.getLabel(), "description": self.getDescription()}
        
    def __str__(self):
        #return '{"version":' + str(self.getVersion()) + ', "permissionMask":' + str(self.getPermissionMask()) + ', "uri":"' + self.getUri() + '", "label":"' + self.getLabel()+'"}'
        #return '{"version": %d,"permissionMask":%d, "uri": "%s", "label":"%s"}' % (self.getVersion(), self.getPermissionMask(), self.getUri(), self.getLabel())
        #return '{"label": "%s", "description": "%s"}' % (self.getLabel(), self.getDescription())
        return json.dumps(self.toJson())
        
    def __repr__(self):
        return self.__str__()