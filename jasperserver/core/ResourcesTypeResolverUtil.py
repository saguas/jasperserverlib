from resource_media_types import *
from ClientFile import ClientFile
from ClientFolder import ClientFolder
from queryResource import ClientQuery

class ResourcesTypeResolverUtil(object):
    
    classes = {}
    
    #classes[ClientAdhocDataView.__name__] =  ResourceMediaType.ADHOC_DATA_VIEW_MIME
    #classes[ClientAwsDataSource.__name__] = ResourceMediaType.AWS_DATA_SOURCE_MIME
    #classes[ClientBeanDataSource.__name__] = ResourceMediaType.BEAN_DATA_SOURCE_MIME
    #classes[ClientCustomDataSource.__name__] = ResourceMediaType.CUSTOM_DATA_SOURCE_MIME
    #classes[ClientDataType.__name__] = ResourceMediaType.DATA_TYPE_MIME
    classes[ClientFile.__name__] = TYPE_FILE
    classes[ClientFolder.__name__] = TYPE_FOLDER
    #classes[ClientInputControl.__name__] = ResourceMediaType.INPUT_CONTROL_MIME
    #classes[ClientJdbcDataSource.__name__] = ResourceMediaType.JDBC_DATA_SOURCE_MIME
    #classes[ClientJndiJdbcDataSource.__name__] = ResourceMediaType.JNDI_JDBC_DATA_SOURCE_MIME
    #classes[ClientListOfValues.__name__] = ResourceMediaType.LIST_OF_VALUES_MIME
    #put(ClientMondrianConnection.class, ResourceMediaType.MONDRIAN_CONNECTION_MIME);
    #put(ClientMondrianXmlaDefinition.class, ResourceMediaType.MONDRIAN_XMLA_DEFINITION_MIME);
    #put(ClientOlapUnit.class, ResourceMediaType.OLAP_UNIT_MIME);
    classes[ClientQuery.__name__] = TYPE_QUERY
    #put(ClientReportUnit.class, ResourceMediaType.REPORT_UNIT_MIME);
    #put(ClientSecureMondrianConnection.class, ResourceMediaType.SECURE_MONDRIAN_CONNECTION_MIME);
    #put(ClientSemanticLayerDataSource.class, ResourceMediaType.SEMANTIC_LAYER_DATA_SOURCE_MIME);
    #put(ClientVirtualDataSource.class, ResourceMediaType.VIRTUAL_DATA_SOURCE_MIME);
    #put(ClientXmlaConnection.class, ResourceMediaType.XMLA_CONNECTION_MIME);
    #put(ClientResourceLookup.class, ResourceMediaType.RESOURCE_LOOKUP_MIME);
    #put(ClientDashboard.class, ResourceMediaType.DASHBOARD_MIME);
    #put(ClientDomainTopic.class, ResourceMediaType.DOMAIN_TOPIC_MIME);
    
    @staticmethod
    def getMimeType(resource):
        if isinstance(resource, basestring):
            #return resource as default in the case resource to be of direct type from resource_media_types
            ret = ResourcesTypeResolverUtil.classes.get(resource, resource)
        else:
            ret = ResourcesTypeResolverUtil.classes.get(resource.__class__.__name__, None)
            
        return ret