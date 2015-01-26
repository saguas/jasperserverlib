import json

class ReportParametersUtils(object):
    
    def __init__(self):
        pass
    
    @classmethod
    def toReportParameters(self, params):
        #new_params = {}
        for key, value in params.items():
            if not isinstance(value, list):
                params[key]=[value]
            #else:
             #   new_params[key]=params
                
        return json.dumps(params)
    
    @classmethod
    def toPathSegment(self, ids):
        if not ids:
            return ''
        
        return ''.join(ids)