

class RunReportAdapter(object):
    
    def __init__(self, js_connect, reportUnitUri, output_format, pages):
        self._connect = js_connect
        self.reportUnitUri = reportUnitUri
        self.output_format = output_format
        self.pages = pages
        self.url = js_connect._rest_url + '_v2/reports/'
        self.params = {}
    
    def parameter(self, rsp_type, rsp_value):
        
        self.params[rsp_type] = rsp_value
        
        return self
    
    def run(self):
        url = self.url + self.reportUnitUri + '.' + self.output_format
        return self._connect.get(url, params=self.params)
    