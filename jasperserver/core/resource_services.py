from Resources import Resources, Resource

class ResourcesServices(object):
    
    def __init__(self, js_connect):
        self._connect = js_connect
        pass
    
    def resources(self):
        return Resources(self._connect)
        
    def resource(self, path=''):
        return Resource(self._connect, path)