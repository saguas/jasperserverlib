from resource_media_types import RESOURCE_MEDIA_TYPE_PREFIX

class ResourceFilesMimeType():
    PDF = "application/pdf"
    HTML = "text/html"
    XLS = "application/xls"
    RTF = "application/rtf"
    CSV = "text/csv"
    ODS = "application/vnd.oasis.opendocument.spreadsheet"
    ODT = "application/vnd.oasis.opendocument.text"
    TXT = "text/plain"
    DOCX = "application/vnd.openxmlformatsofficedocument.wordprocessingml.document"
    XLSX = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    FONT = "font/*"
    IMG = "image/*"
    JRXML = "application/jrxml"
    JAR = "application/zip"
    PROP = "application/properties"
    JRTX = "application/jrtx"
    XML = "application/xml"
    CSS = "text/css"
    ACCES_GRANT_SCHEMA = "application/accessGrantSchema"
    OLAP_MONDRIAN_SCHEMA = "application/olapMondrianSchema"
    UNSPECIFIED = "application/octet-stream"
    JSON = 'application/json'
    FORM = 'multipart/form-data'
    REPOSITORYFILEJSON = RESOURCE_MEDIA_TYPE_PREFIX + "file+json"
    REPOSITORYFILEXML = RESOURCE_MEDIA_TYPE_PREFIX + "file+xml"
   
    def getMimeType(self, mimetype):
        return getattr(self, mimetype.upper())
        
    def __getattr__(self, name):
        return None


