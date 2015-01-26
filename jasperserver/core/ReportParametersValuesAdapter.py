from common import setHeader
from resources_mime_type import ResourceFilesMimeType as rmt
from ReportParametersUtils import ReportParametersUtils

class ReportParametersValuesAdapter(object):
    
    def __init__(self, js_connect, reportUnitUri, params, idsPathSegment=None):
        self._connect = js_connect
        path = "/reports/%s/inputControls" % (reportUnitUri, )
        self.url = self._connect._rest_url + '_v2' + path
        self.reportUnitUri = reportUnitUri
        self.params = params
        self.idsPathSegment = idsPathSegment
        self.path = ''
        
    def prepareRequest(self):
        setHeader('Content-type',rmt.JSON,self._connect)
        setHeader('accept',rmt.JSON,self._connect)
        
        path = ''
        if self.idsPathSegment:
            path = ReportParametersUtils.toPathSegment(self.idsPathSegment)
            
        params = ReportParametersUtils.toReportParameters(self.params)
        
        return params, path
    
    #get the list of inputcontrol values
    def get(self):
        self.prepareRequest()
        path = "/values"
        return self._connect.get(self.url + path)
        
    #set inputcontrol values
    def update(self):
        params, path = self.prepareRequest()
        if path:
            path = "/%s/values" % (path,)
        else:
            path = "/values"
            
        #params = ReportParametersUtils.toReportParameters(self.params)
        print "update params: {0} path {1}".format(params, self.url + path)
        return self._connect.post(self.url + path, data=params)
        
    def parameter(self, name, value):
        if not self.params.get(name):
            self.params[name] = [value]
        else:
            self.params.get[name].append(value)
                
        return self
        
    def setParameter(self, params):
        self.params = params
        
        return self
    
    