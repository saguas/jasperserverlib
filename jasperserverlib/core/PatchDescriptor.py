import json
from PatchItem import PatchItem

class PatchDescriptor(object):
    
    def __init__(self):
        self.items = []
        self.version = 2
        
    def getVersion(self):
        return self.version
    
    def setVersion(self, version=0):
        self.version = version
        return self
    
    def getItems(self):
        return self.items
    
    def setItems(self, items):
        self.items = items
        return self
    
    def field(self, name, value):
        
        item = PatchItem()
        item.setField(name)
        item.setValue(value)
        self.items.append(item)
        return self
        
    def expression(self, expression):
        
        item = PatchItem()
        item.setExpression(expression)
        self.items.append(item)
        return self;
        
    def toString(self):
        return self.__str__()
    
    def __str__(self):
        rd = {'version': self.getVersion(), "patch":[]}
        for item in self.items:
            if item.expression:
                rd.get("patch").append({"expression": item.getExpression()})
            elif item.field:
                rd.get("patch").append({"field": item.getField(), "value":item.getValue()})
        
        return json.dumps(rd)
    
    def __repr__(self):
        return self.__str__()
    
    def __getattr__( self, name):
        return None