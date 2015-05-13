from Resources import Report
from ReportExecutionRequestBuilder import ReportExecutionRequestBuilder
from newReportExecutionRequest import NewReportExecutionRequest

class ReportingService(object):
    
    def __init__(self, js_connect):
        self._connect = js_connect
        self.result = {}
    
    def report(self, path=''):
        return Report(self._connect, path)
    
    def newReportExecutionRequest(self, request):
        return NewReportExecutionRequest(self._connect, request)
    
    def reportExecutionRequest(self, reqId, expId=None):
        return ReportExecutionRequestBuilder(self._connect,reqId, expId)