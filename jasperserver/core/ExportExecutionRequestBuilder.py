from time import sleep
from resources_mime_type import ResourceFilesMimeType as rmt

class ExportExecutionRequestBuilder(object):
    
    def __init__(self, ReportExecutionRequestBuilder,js_connect, requestId, exportId):
        self.rerb = ReportExecutionRequestBuilder
        self.requestId = requestId
        self.exportId = exportId
        self._connect = js_connect
        self.result = {}
        #self.opresult = opresult
        path = "/reportExecutions"
        self.url = self._connect._rest_url + '_v2' + path
    
    #for each id. Get one file each time
    def outputResource(self):
            #exports = self.opresult.get('exports', [])
            path = "/%s/exports/%s/outputResource" % (self.requestId, self.exportId)
            content = None
            while True:
                response = self._connect.get(self.url + path).response
                print "output-final {}".format(response.headers['output-final'])
                if response.headers['output-final'] == "true":
                    break
        
            #result = response.content
            self.result["content"] = response.content
        
            return self
        
    def attachment(self, attachmentId):
        if not attachmentId or attachmentId == "/":
            raise Exception("attachmentId mustn't be an empty string!")
            
        path = "/%s/exports/%s/attachments/%s" % (self.requestId, self.exportId, attachmentId)
        
        while True:
            result = self.rerb.status().content
            status = json.loads(result)
            print "status {}".format(result)
            if  status.get('value') == "ready":
                break
            sleep(1)
        
        response = self._connect.get(self.url + path)
        
        return response
        
    def status(self):
        path = "/%s/exports/%s/status" % (self.requestId, self.exportId)
        #setHeader('Content-type',rmt.JSON,self._connect)
        setHeader('accept','application/json',self._connect)
        return self._connect.get(self.url + path)
        
    def getResult(self, rtype=None):
        return self.result.get(rtype.lower()) if rtype else self.result
    
    '''def outputResource(self):
        result = []
        exports = self.opresult.get('exports', [])
        for file in exports:
            path = "/%s/exports/%s/outputResource" % (self.requestId, file.get("id"))
            content = None
            while True:
                response = self._connect.get(self.url + path).response
                print "output-final {}".format(response.headers['output-final'])
                if response.headers['output-final'] == "true":
                    content = response.content
                    break
            
            result.append(content)
        
        return result'''
    
    