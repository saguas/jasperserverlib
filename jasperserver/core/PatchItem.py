

class PatchItem(object):
    
    def getField(self):
        return self.field
    
    def setField(self, field):
        self.field = field
        return self
        
    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value
        return self
    
    def getExpression(self):
        return self.expression
    
    def setExpression(self, expression):
        self.expression = expression
        return self
    
    def __getattr__( self, name):
        return None