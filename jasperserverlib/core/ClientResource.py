

class ClientResource(object):
    
    def getVersion(self):
        return self.version
    
    def setVersion(self, version):
        self.version = version
        return self
    
    def getPermissionMask(self):
        return self.permissionMask
    
    def setPermissionMask(self, permissionMask):
        self.permissionMask = permissionMask
        return self
        
    def getCreationDate(self):
        return self.creationDate
    
    def setCreationDate(self, dt):
        self.creationDate = dt
        return self
    
    def getUpdateDate(self):
        return self.updateDate
    
    def setUpdateDate(self, updateDate):
        self.updateDate = updateDate
        return self
    
    def getLabel(self):
        return self.label
            
    def setLabel(self, label):
        self.label = label
        return self
    
    def getDescription(self):
        return self.description
    
    def setDescription(self, dc):
        self.description = dc
        return self
    
    def getUri(self):
        return self.uri
        
    def setUri(self, uri):
        self.uri = uri
        return self
    
    def __getattr__(self, name):
        return None
    
    