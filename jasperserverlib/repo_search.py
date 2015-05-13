import core as jasper
import json

from core.resource_search_param import ResourceSearchParameter as rsp
from core.ResourceLookupDescriptor import ResourceLookupDescriptor


class Search(object):

    paramsMap = {"path": rsp.FOLDER_URI, "text": rsp.Q, "recursive": rsp.RECURSIVE, "type": rsp.TYPE, "accessType": rsp.ACCES_TYPE,\
            "showHiddenItems": rsp.SHOW_HIDDEN_ITEMS, "sortby": rsp.SORT_BY, "limit":rsp.LIMIT, "offset": rsp.OFFSET,\
            "totalPage": rsp.FORCE_TOTAL_COUNT, "resourceUri": rsp.RESOURCE_URI}

    def __init__(self, session):
        self.session = session
        self.resources = self.session.resourcesService().resources()
        self.resourceLookup = None

    def search(self, **params):
        for key, val in params.items():
            paramkey = self.paramsMap.get(key, None)
            if paramkey:
                self.resources.parameter(paramkey, val)
        
        result = self.resources.search().result
        
        try:
            self.resourceLookup = ResourceLookupDescriptor(json.loads(result.content).get('resourceLookup'))
        except:
            self.resourceLookup = None
        
        return self
        
    def getDescriptor(self):
        return self.resourceLookup

