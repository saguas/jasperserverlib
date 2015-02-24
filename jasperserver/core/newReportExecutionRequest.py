from common import setHeader
from resources_mime_type import ResourceFilesMimeType as rmt
import json



class NewReportExecutionRequest(object):
    
    def __init__(self, js_connect, request):
        self._connect = js_connect
        self.request = request
        self.session = self._connect.session
        self.path = "/reportExecutions"
        self.url = self._connect._rest_url + '_v2' + self.path
        self.result = {}
        
    
    def run(self):
        rd = self.request.toJson()
        setHeader('Content-type',rmt.JSON,self._connect)
        setHeader('accept','application/json',self._connect)
        print "url async request: {0}".format(rd)
        rest = self._connect.post(self.url, data=json.dumps(rd))
        self.result["content"] = rest.content
        return self

    #get report in another format
    def run_exports(self, requestId):
        rd = self.request.toJson()
        path = "/%s/exports" % (requestId)
        setHeader('Content-type',rmt.JSON,self._connect)
        setHeader('accept','application/json',self._connect)
        rest = self._connect.post(self.url + path, data=json.dumps(rd))
        self.result["content"] = rest.content
        return self
        
    def getResult(self, rtype=None):
        return self.result.get(rtype.lower()) if rtype else self.result