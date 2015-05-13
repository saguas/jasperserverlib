import core as jasper
import json

from core.ResourceDescriptor import ResourceDescriptor
from resource_details import Details
from core.exceptions import JsException, StatusException
from core.common import setHeader, removeHeader

class DownloadBinary(object):
    
    def __init__(self, session, path=''):
        self.session = session
        self.path = path
        self.resource = self.session.resourcesService().resource(path)
        self.resourceDescriptor = None
        
    def _download(self, file=True):
        
        return self.resource.downloadBinary(file)
        
    def downloadBinary(self, descriptor=False, file=False):
        
        #if True get just the file no need for type file, already known
        if not file:
            #setHeader('accept','application/repository.file+json',self.session)
            fileDesc = self._download(False)
            self._checkFileDescriptor(fileDesc.result.content)
        else:
            self.resourceDescriptor = ResourceDescriptor()
        
        #just descriptor file
        if descriptor:
            return
        
        file = self._download()
        #print "file content {}".format(file.content)
        try:
            self.resourceDescriptor._resourceDescriptor[0]['content'] = file.result.content
        except:
            self.resourceDescriptor._resourceDescriptor[0]['content'] = ''
        
        return self
        
    def _checkFileDescriptor(self, fileDesc):
        
        #removeHeader('accept', self.session)
        
        if not fileDesc:
            raise StatusException[404]()
            
        self.resourceDescriptor = ResourceDescriptor(json.loads(fileDesc))
        #print "mimetype: {}".format(self.getDescriptor().getType())
        
        return self
        
    def getDescriptor(self):
        return self.resourceDescriptor
    
    def getFileContent(self):
        return self.resourceDescriptor._resourceDescriptor[0]['content']
        
        