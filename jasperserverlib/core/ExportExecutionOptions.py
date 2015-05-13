import json

class ExportExecutionOptions(object):
    
    def __init__(self):
        self.attachmentsPrefix = None
    
    def setPages(self, pages):
        self.pages = pages
        return self
    
    def getAttachmentsPrefix(self):
        return self.attachmentsPrefix
    
    def setAttachmentsPrefix(self, attachmentsPrefix):
        self.attachmentsPrefix = attachmentsPrefix
        return self
    
    def getPages(self):
        return self.pages
    
    def getOutputFormat(self):
        return self.outputFormat
    
    def setOutputFormat(self, outputFormat):
        self.outputFormat = outputFormat
        return self
    
    def getBaseUrl(self):
        return self.baseUrl
    
    def setBaseUrl(self, baseUrl):
        self.baseUrl = baseUrl
    
    def isAllowInlineScripts(self):
        return self.allowInlineScripts
    
    def setAllowInlineScripts(self, allowInlineScripts):
        self.allowInlineScripts = allowInlineScripts
    
    def toJson(self):
        report = {"outputFormat": self.getOutputFormat(), "pages": self.getPages()}
        
        if self.attachmentsPrefix:
            report['attachmentsPrefix'] = self.attachmentsPrefix
        
        return report