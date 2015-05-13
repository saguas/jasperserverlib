from common import setHeader
from resources_mime_type import ResourceFilesMimeType as rmt
from ExportExecutionRequestBuilder import ExportExecutionRequestBuilder
import json

class ReportExecutionRequestBuilder(object):
    
    def __init__(self, js_connect, reqId, expId=None):
        self._connect = js_connect
        self.session = self._connect.session
        path = "/reportExecutions"
        self.url = self._connect._rest_url + '_v2' + path
        self.requestId = reqId
        self.exportId = expId
        self.opresult = None
    
    def status(self):
        path = "/%s/status" % (self.requestId, )
        #setHeader('Content-type',rmt.JSON,self._connect)
        setHeader('accept','application/json',self._connect)
        return self._connect.get(self.url + path)
    
    def executionDetails(self):
        path = "/%s" % (self.requestId, )
        setHeader('accept','application/json',self._connect)
        result = self._connect.get(self.url + path).content
        self.opresult = json.loads(result)
        return self.opresult
    
    #for each id create one ExportExecutionRequestBuilder
    def export(self):
        #return ExportExecutionRequestBuilder(self, self._connect, self.opresult, self.requestId, fileformat)
        return ExportExecutionRequestBuilder(self, self._connect, self.requestId, self.exportId)
    
    def runExport(self, exportExecutionOptions):
        setHeader('accept','application/json',self._connect)
        setHeader('Content-type',rmt.JSON,self._connect)
        path = "/%s/exports/" % (self.requestId,)
        
        rd = exportExecutionOptions.toJson()
        
        result = self._connect.post(self.url + path, data=json.dumps(rd))
        
        return result
    
    def modifyParameters(self, params):
        setHeader('accept','application/json',self._connect)
        setHeader('Content-Type',rmt.JSON,self._connect)
        path = "/%s/parameters" % (self.requestId,)
        print "modifyParameters path {0} params {1} headers {2}".format(self.url + path, json.dumps(params), self._connect.headers)
        result = self._connect.get(self.url + path, params=json.dumps(params))
        
        return result
    
    def cancelExecution(self):
        path = "/%s/status/" % (self.requestId, )
        setHeader('Content-type',rmt.JSON,self._connect)
        setHeader('accept',rmt.JSON,self._connect)
        cancelled = { "value": "cancelled" }
        return self._connect.put(self.url + path, data=json.dumps(cancelled))
        
        
        
        
        