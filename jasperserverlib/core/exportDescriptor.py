import json

class ExportDescriptor(object):
    def __init__(self, resourceDescriptor={}):
        self.outputFormat = None
        self.pages = None
        self.attachmentsPrefix = None
        
        
        
    def getOutputFormat(self):
        return self.outputFormat
    
    def setOutputFormat(self, outputFormat):
        self.outputFormat = outputFormat
        return self
        
    def toJson(self):
           report = {'outputFormat': self.getOutputFormat()}
        
           if self.pages:
               report['pages'] = self.getPages()
        
           if self.attachmentsPrefix:
               report['attachmentsPrefix'] = self.getAttachmentsPrefix()

           return report
        
    def toString(self):
        return json.dumps(self.toJson)