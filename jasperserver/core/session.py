

class Session(object):
    
    def __init__(self):
        self.ids = {}
        pass
    
    def setSessionId(self, sessionId):
        self.sessionId = sessionId
        return self
    
    def getSessionId(self):
        return self.sessionId
    
    def setResquestId(self, reqId, value=None):
        self.ids[reqId] = value
        return self
        
    def getExportId(self, reqId):
        return self.ids.get(reqId, None)
        
    def setExportId(self, reqId, id):
        self.ids[reqId] = id
        return self