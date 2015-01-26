from Resources import Report
from common import setHeader
from resources_mime_type import ResourceFilesMimeType as rmt
import json
from ReportExecutionRequestBuilder import ReportExecutionRequestBuilder
from newReportExecutionRequest import NewReportExecutionRequest

class ReportingService(object):
    
    def __init__(self, js_connect):
        self._connect = js_connect
        self.result = {}
        pass
    
    def report(self, path=''):
        return Report(self._connect, path)
    
    def newReportExecutionRequest(self, request):
        return NewReportExecutionRequest(self._connect, request)
        """path = "/reportExecutions"
        rd = request.toJson()
        url = self._connect._rest_url + '_v2' + path
        setHeader('Content-type',rmt.JSON,self._connect)
        setHeader('accept','application/json',self._connect)
        print "url async request: {0}".format(rd)
        rest = self._connect.post(url, data=json.dumps(rd))
        self.result["content"] = rest.content
        return self"""
    
    def reportExecutionRequest(self, reqId, expId=None):
        return ReportExecutionRequestBuilder(self._connect,reqId, expId)