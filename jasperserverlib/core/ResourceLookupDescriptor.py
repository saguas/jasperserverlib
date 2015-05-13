import json
import copy

#import jasperserverlib.core

def descriptor(f):
    def new_f(self, name=None):
        #print "f name ", f.__name__
        if self.getLength() == 1 and not name:
            name = self.getLabels()[0]
        elif self.getLength() > 1 and not name:
            name = self.getLabels()[0]
        elif self.getLength() < 1:
            raise IndexError()
        
        return f(self, name)
    
    return new_f
    

class ResourceLookupDescriptor(object):
    
    def __init__(self, resourceDescriptor={}):
        self._resourceDescriptor = resourceDescriptor#.get('resourceLookup')
    
    @descriptor 
    def getUri(self, name=None):
        uri = None
        desc = self._search("label", name)
        if desc:
            uri = desc.get('uri')
        return uri
    
    def getLabels(self):
        return [desc.get("label") for desc in self._resourceDescriptor]
    
    @descriptor
    def getLabel(self, uri):
        label = None
        
        desc = self._search("uri", uri)
        
        if desc:
            label = desc.get('label')
        
        return label

    @descriptor
    def getDescription(self, name=None):
        
        description = None
        
        desc = self._search("label", name)
        
        if desc:
            description = desc.get('description')
        
        return description
    
    @descriptor
    def getType(self, name=None):
        
        descType = None
        
        desc = self._search("label", name)
        
        if desc:
            descType = desc.get('type')
        
        return descType
    
    @descriptor
    def getPermissionMask(self, name=None):
        
        perm = None
        
        desc = self._search("label", name)
        
        if desc:
            perm = desc.get('permissionMask')
        
        return perm
    
    @descriptor
    def getVersion(self, name=None):
        print "inside version ", name
        version = None
        
        desc = self._search("label", name)
        
        if desc:
            version = desc.get('version')
        
        return version
    
    @descriptor
    def getUpdateDate(self, name=None):
        
        udate = None
        
        desc = self._search("label", name)
        
        if desc:
            udate = desc.get('updateDate')
        
        return udate
    
    @descriptor
    def getCreationDate(self, name=None):
        
        cdate = None
        
        desc = self._search("label", name)
        
        if desc:
            cdate = desc.get('creationDate')
        
        return cdate
    
    def getLength(self):
        return len(self._resourceDescriptor)
        
    def json_descriptor(self):
        return self._resourceDescriptor
        
    def _search(self, what, name):
        result = None
        for desc in self._resourceDescriptor:
            if desc.get(what) == name:
                result = desc
                break
        
        return result
    
    def __getattr__(self, attr):
        def find(*args, **kwargs):
            name = args[0] if len(args) > 0 else None
            if not name and self.getLength() == 1:
                name = self.getLabels()[0]
            elif self.getLength() > 1 and not name:
                name = self.getLabels()[0]
            elif self.getLength() < 1:
                raise IndexError()
                
            ret = None
            desc = self._search("label", name)
            if desc:
                ret = desc.get(attr[3].lower() + attr[4:])
                #if ret is of type dict return another ResourceDescriptor
                if isinstance(ret,dict):
                    ret = ResourceDescriptor(ret)
                    
            return ret
            
        return find
    
    def __str__(self, ):
        new_list = copy.deepcopy(self._resourceDescriptor)
        for desc in new_list:
            if 'content' in desc:
                desc['content'] = "get content from getContent() method"
        #return json.dumps(self._resourceDescriptor)
        return json.dumps(new_list)
        
    def __repr__(self):
        return self.__str__()
        
    #__repr__ = __str__
    
    
    