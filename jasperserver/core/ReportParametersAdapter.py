from resources_mime_type import ResourceFilesMimeType as rmt
from common import setHeader
from ReportParametersUtils import ReportParametersUtils
from ReportParametersValuesAdapter import ReportParametersValuesAdapter


class ReportParametersAdapter(object):
    
    def __init__(self, js_connect, reportUnitUri, idsPathSegment=None):
        self._connect = js_connect
        path = "/reports/%s/inputControls" % (reportUnitUri, )
        self.url = self._connect._rest_url + '_v2' + path
        self.reportUnitUri = reportUnitUri
        self.params = {}
        self.idsPathSegment = idsPathSegment
    
    def parameter(self, name, value):
            if not self.params.get(name):
                self.params[name] = [value]
            else:
                self.params.get[name].append(value)
                
            return self
    
    def prepareRequest(self):
        setHeader('accept',rmt.JSON,self._connect)
        return ReportParametersUtils.toReportParameters(self.params)
        
    #get the list inputcontrol structure
    def get(self):
        reportParams = self.prepareRequest()
        return self._connect.get(self.url)
    
    def values(self):
        return ReportParametersValuesAdapter(self._connect, self.reportUnitUri, self.params, self.idsPathSegment)
    
    def setParameter(self, params):
        self.params = params
        
        return self