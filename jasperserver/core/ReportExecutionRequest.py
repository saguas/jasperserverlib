import json

class ReportExecutionRequest(object):
    
    def __init__(self):
        self.freshData = "false"
        self.saveDataSnapshot = "false"
        self.interactive = "false"
        self.ignorePagination = None
        self.pages = None
        self.async = "false"
        self.transformerKey = None
        self.attachmentsPrefix = None
        self.parameters = None
        self.outputFormat = 'pdf'
        
    
    def getReportUnitUri(self):
        return self.reportUnitUri
    
    def setReportUnitUri(self, reportUnitUri):
        self.reportUnitUri = reportUnitUri
        return self
    
    def getFreshData(self):
        return self.freshData
    
    def setFreshData(self, freshData):
        self.freshData = freshData
        return self
        
    def getSaveDataSnapshot(self):
        return self.saveDataSnapshot
    
    def setSaveDataSnapshot(self, saveDataSnapshot):
        self.saveDataSnapshot = saveDataSnapshot
        return self
    
    def getInteractive(self):
        return self.interactive
    
    def setInteractive(self, interactive):
        self.interactive = interactive
        return self
    
    def getIgnorePagination(self):
        return self.ignorePagination
    
    def setIgnorePagination(self, ignorePagination):
        self.ignorePagination = ignorePagination
        return self
        
    def getAsync(self):
        return self.async
        
    def setAsync(self, async):
        self.async = async
        return self
    
    def getTransformerKey(self):
        return self.transformerKey
    
    def setTransformerKey(self, transformerKey):
        self.transformerKey = transformerKey
        return self
        
    def getOutputFormat(self):
        return self.outputFormat
    
    def setOutputFormat(self, outputFormat):
        self.outputFormat = outputFormat
        return self
        
    def getAttachmentsPrefix(self):
        return self.attachmentsPrefix
    
    def setAttachmentsPrefix(self, attachmentsPrefix):
        self.attachmentsPrefix = attachmentsPrefix
        return self
        
    def getPages(self):
        return self.pages
        
    def setPages(self, pages):
        self.pages = pages;
        return self
        
    def getParameters(self):
        return self.parameters
    
    def setParameters(self, parameters):
        self.parameters = parameters
        return self
        
    def toJson(self):
        report = {'reportUnitUri': self.getReportUnitUri(), 'freshData': self.getFreshData(),\
        'saveDataSnapshot': self.getSaveDataSnapshot(), 'interactive': self.getInteractive(),\
        'async': self.getAsync(), 'outputFormat': self.getOutputFormat()}
        
        if self.pages:
            report['pages'] = self.getPages()
        
        if self.ignorePagination:
            report['ignorePagination'] = self.getIgnorePagination()
        
        if self.transformerKey:
            report['transformerKey'] = self.getTransformerKey()
        
        if self.attachmentsPrefix:
            report['attachmentsPrefix'] = self.getAttachmentsPrefix()
        
        if self.parameters:
            report['parameters'] = {'reportParameter':self.getParameters()}
            
        return report
        
    def toString(self):
        return json.dumps(self.toJson)
    
    
    
    
    
    
        