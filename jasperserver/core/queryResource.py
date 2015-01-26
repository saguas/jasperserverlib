from ClientResource import ClientResource
from resource_media_types import *
import json


class ClientQuery(ClientResource):
    
    def __init__(self):
        self._resource_type = TYPE_FOLDER
        self.language = 'sql'
        self.value = ''
        #set to None to use the parent dataSource (jrxml datasource)
        self.dataSourceURI = None
        
    def setQuery(self, query):
        self.value = query
        return self
    
    def getQuery(self):
        return self.value
        
    def setLanguage(self, language='sql'):
        self.language = language
        return self
        
    def getLanguage(self):
        return self.language
        
    def setDataSourceURI(self, uri):
        self.dataSourceURI = uri
        return self
        
    def getDataSourceURI(self):
        return self.dataSourceURI
    
    def toString(self):
        return self.__str__()
        
    def toJson(self):
        desc = {"label": self.getLabel(), "description": self.getDescription(), 'value': self.value, 'language': self.language}
        
        if self.dataSourceURI:
            desc['dataSource'] = {'dataSourceReference':{'uri': self.dataSourceURI}}
        #else:
        #    desc['dataSource'] = 'NULL'
        
        return desc
        
    def __str__(self):
        return json.dumps(self.toJson())
        
    def __repr__(self):
        return self.__str__()
