import core as jasper
import json
import xmltodict
import io

from jasperserver.resource_details import Details
from jasperserver.resource_download import DownloadBinary
from core.PatchDescriptor import PatchDescriptor
from core.exceptions import ReportNotFoundError, ReportRunError, ReportJRXMLError, PathError, NoContent, InputControlUpdateError
#from report_inputControls import InputControls
from core.ResourceDescriptor import ResourceDescriptor
from core.InputControlsDescriptor import InputControlDescriptor
from core.queryResource import ClientQuery


class Report(object):
    
    def __init__(self, session, path):
        self.session = session
        self.path = path
        self._report = None
        self.resource = None
        self.d = None #details
        if session:
            self.reporting = self.session.reportingService()
        self.reportDescriptor = None
        self.dlb = None
        self.jrxmlDescriptor = None
        self.attachDescriptor = {}
        self.patchDescriptor = None
        self.reportParameterAdapter = None
        self.jrxml = {}
        self.params = {}
        self.ics = []
        self.icsValues = []
        
        
    def report(self):
        if not self.path:
            raise PathError()
            
        if not self._report:    
            self._report = self.reporting.report(self.path)
            
        return self
        
    def parameter(self, rsp_type, rsp_value):
        
        self.params[rsp_type] = rsp_value
        
        return self
        
    def run(self, reportFormat="pdf", pages='', use_params=True):
        if not self._report:
            self.report()
            
        self._runadapter = self._report.prepareForRun(reportFormat, pages)
        
        if use_params:
            for key, value in self.params.items():
                self._runadapter.parameter(key, value)
        #try:
        self._runreport = self._runadapter.run().content
            #fo = open("foo.pdf", "wb")
            #fo.write(self._runreport)
            #fo.close()
        #except:
         #   raise ReportRunError()
            
        return self
        
    def getReportContent(self):
        return self._runreport
        
    
    def details(self, expanded=True):
        if not self.path:
            raise PathError()
        
        if not self.d:
            self.d = Details(self.session, self.path)
        
        if not self.reportDescriptor:
            self.reportDescriptor = self.d.details(expanded=expanded).getDescriptor()
        
        return self
        
    #em teste
    '''def inputControlsRef(self):
        if not self.d:
            self.details()
            
        #print "repor d {}".format(self.reportDescriptor)
        #icRefs = self.reportDescriptor.json_descriptor()[0].get('inputControls')
        icRefs = self.reportDescriptor.getInputControls()
        for ic in icRefs:
            if isinstance(ic, dict):
                ic = InputControlDescriptor(ic)
            self.ics.append(ic)
            
        return self.ics
    '''
    def inputControls(self):
        if not self._report:
            self.report()
        
        self.reportParameterAdapter = self.reportParameterAdapter or\
        self._report.reportParameters()
        
        try:
            inputControls = self.reportParameterAdapter.get()
            #print "InputControls ", inputControls.content
            ics = json.loads(inputControls.content).get('inputControl')
            for ic in ics:
                ic = InputControlDescriptor(ic)
                self.ics.append(ic)
                
        except NoContent, e:
            print "No Content"
            pass
            
        return self.ics
    
    def inputControlsValues(self):
        if not self._report:
            self.report()
        
        self.reportParameterAdapter = self.reportParameterAdapter or\
        self._report.reportParameters()
        
        try:
            inputControls = self.reportParameterAdapter.values().get()
            print "InputControls ", inputControls.content
            ics = json.loads(inputControls.content).get('inputControlState')
            for ic in ics:
                ic = InputControlDescriptor(ic)
                self.icsValues.append(ic)
                
        except NoContent, e:
            print "No Content"
            pass
            
        return self.icsValues
    
    def updateInputControls(self):
        if not self._report:
            self.report()
        
        self.reportParameterAdapter = self.reportParameterAdapter or\
        self._report.reportParameters()
        self.reportParameterAdapter.setParameter(self.params)
        values = self.reportParameterAdapter.values()
        
        res = values.update().content
        
        if not json.loads(res).get('inputControlState'):
            raise InputControlUpdateError("Update inputControls Error")
        print res
        return self
        
        
    def downloadJRXML(self, withattach=False):
            
        if self.jrxmlDescriptor:
            return self
            
        if not self.d:
            self.details()
        
        try:
            jrxml_uri = self.reportDescriptor.json_descriptor()[0]\
                .get('jrxml').get('jrxmlFile').get('uri')
        except AttributeError, e:
            jrxml_uri = self.reportDescriptor.json_descriptor()[0]\
                .get('jrxml').get('jrxmlFileReference').get('uri')
        
        if not self.dlb:
            self.dlb = DownloadBinary(self.session, jrxml_uri)
        
        if not self.jrxmlDescriptor:
            self.jrxmlDescriptor = self.dlb.downloadBinary(file=True).getDescriptor()
        
        if withattach:
            self.getAttachments()
        
        return self
    
    def _downloadAttachments(self, name, filepath):
        if name not in self.attachDescriptor.keys():
            attach = DownloadBinary(self.session, filepath)
            self.attachDescriptor[name] = attach.downloadBinary(file=True)\
                                            .getDescriptor().content 
        return self
    
    def getDescriptor(self):
        return self.reportDescriptor
        
    def getJrxmlDescriptor(self):
        if not self.jrxmlDescriptor:
            raise ReportJRXMLError("Download jrxml first. Use method name: downloadJRXML")
            
        self.getJrxmlProperties()
        
        return dict(self.jrxmlDescriptor.json_descriptor()[0].items() + self.jrxml.items())
        
    def getFields(self, doc, isSubDataset=False, name=''):
        f = self.jrxml.get('field', None)
        if not self.jrxml.get('fields'):
            if isSubDataset and name:
                if not self.jrxml['subDatasets'][name].get('field'):
                    self.jrxml['subDatasets'][name]['field'] = {}
                f = self.jrxml['subDatasets'][name]['field']
            else:
                f = self.jrxml['field'] = {}
                
            fields = doc.get('field',[])#doc["jasperReport"]["field"]
            if not isinstance(fields, list):
                fields = [fields]

            for d in fields:
                f[d['@name']] = {}
                for key, value in d.items():
                    f[d['@name']][key.replace('@','')] = value
                    #ldict[d['@name']][key.replace('@','')] = value
                #self.jrxml['field'][d['@name']] = d['@class']
        #getSubDataSet()
        #print "doc {}".format(self.jrxml['field'])
        return self.jrxml and f
        
    def getProperties(self, doc, isSubDataset=False, name=''):
        p = self.jrxml.get('properties', None)
        if not self.jrxml.get('properties'):
            #doc = xmltodict.parse(self.jrxmlDescriptor.json_descriptor()[0].get('content'))
            if isSubDataset and name:
                if not self.jrxml['subDatasets'][name].get('properties'):
                    self.jrxml['subDatasets'][name]['properties'] = {}
                p = self.jrxml['subDatasets'][name]['properties']
            else:
                p = self.jrxml['properties'] = {}
            
            prop = doc.get("property")
            if not isinstance(prop, list):
                prop = [prop]
                
            for d in prop:
                p[d['@name']] = {}
                for key, value in d.items():
                    p[d['@name']][key.replace('@','')] = value
                #self.jrxml['properties'][d['@name']] = d['@value']
            
        return self.jrxml and p
        
    def getQueryString(self, doc, isSubDataset=False, name=''):
        q = self.jrxml.get('queryString')
        if not self.jrxml.get('queryString'):
            queryString = doc.get("queryString")
            language = ""
            txt = ""
            if not isinstance(queryString, basestring) and queryString:
                txt = queryString.get('#text','')
                language = queryString.get('@language', '')
            elif queryString:
                txt = queryString
            
            if isSubDataset and name:
                q = self.jrxml['subDatasets'][name]
            else:
                q = self.jrxml
                  
            q['queryString'] = {'query': txt, 'language': language}
            
        return self.jrxml and q
    
    def getInputControls(self, doc, isSubDataset=False, name=''):
        ic = self.jrxml.get('inputControls')
        if not self.jrxml.get('inputControls'):
            if isSubDataset and name:
                if not self.jrxml['subDatasets'][name].get('inputControls'):
                    self.jrxml['subDatasets'][name]['inputControls'] = {}
                ic = self.jrxml['inputControls'][name]['inputControls']
            else:
                ic = self.jrxml['inputControls'] = {}
                
            #self.jrxml['inputControls'] = {}
            params = doc.get("parameter", [])
            if not isinstance(params, list):
                params = [params]
                
            for d in params:
                ic[d['@name']] = {}
                for key, value in d.items():
                    ic[d['@name']][key.replace('@','')] = value
   
        return self.jrxml and ic
    
    def getSubDataSet(self, doc):
        if not self.jrxml.get('subDatasets'):
            #doc = xmltodict.parse(self.jrxmlDescriptor.json_descriptor()[0].get('content'))
            self.jrxml['subDatasets'] = {}
            subquery = doc.get("subDataset", [])
            if not isinstance(subquery, list):
                subquery = [subquery]
                
            for d in subquery:
                self.jrxml['subDatasets'][d['@name']] = {}
                for key, value in d.items():
                    if key[0] == "@":
                        self.jrxml['subDatasets'][d['@name']][key.replace('@','')] = value
                        continue
                    {
                        "field": lambda x,y=False,z='': self.getFields(x,y,z),
                        "property": lambda x,y=False,z='': self.getProperties(x, y, z),
                        "queryString": lambda x,y=False,z='': self.getQueryString(x),
                        
                    }.get(key, lambda x,y=False,z='': x)(d, True, d['@name'])
                    
                    
                #self.jrxml['subquery'][d['@name']] = d['@class']
    
    def getJrxmlProperties(self):
        if not self.jrxmlDescriptor:
             raise ReportJRXMLError("Download jrxml first. Use method name: downloadJRXML")
        print self.jrxmlDescriptor.json_descriptor()[0].get('content')
        doc = xmltodict.parse(self.jrxmlDescriptor.json_descriptor()[0].get('content'))
        report = doc.get("jasperReport")
        if report:
           self._getJrxmlProperties(report)
        
        return self.jrxml

    def getJrxmlPropertiesFromLocalFile(self, file):
        #print self.jrxmlDescriptor.json_descriptor()[0].get('content')
        file_content = None
        with open(file, 'r') as f:
            file_content = f.read()
        print file_content
        if file_content:
            doc = xmltodict.parse(file_content)
            report = doc.get("jasperReport")
            if report:
                self._getJrxmlProperties(report)
        
        return self.jrxml
        
    def _getJrxmlProperties(self, report):
        if report.get('field'):
            self.getFields(report)
        if report.get("property"):
            self.getProperties(report)
        if report.get("queryString"):
            self.getQueryString(report)
        if report.get("parameter"):
            self.getInputControls(report)
        if report.get("subDataset"):
            self.getSubDataSet(report)
            
        return self
    
    def change_image_location(self, file_content, root_path):
        print file_content
        if file_content:
            doc = xmltodict.parse(file_content)
            report = doc.get("jasperReport")
            #images = doc.get("imageExpression")
            images = report.get("background").get("band")
            print "ImageExpression: {}".format(images)
    #get details, jrxml file and attachemnts
    def get(self):
        self.downloadJRXML(withattach=True)
        
        return self
    
    def getDatabaseName(self):
        desc = self.details().getDescriptor()
        
        
    def getAttachments(self):
        if not self.reportDescriptor:
            raise ReportNotFoundError()
            
        files = self.reportDescriptor.json_descriptor()[0].get('resources').get('resource')
        for file in files:
            name = file.get('name')
            try:
                self._downloadAttachments(name, file.get('file').get('fileReference').get('uri'))
            except AttributeError, e:
                self._downloadAttachments(name, file.get('file').get('fileResource').get('uri'))
                
        return self.attachDescriptor
    
    def updateField(self, name, value):
        if not self.patchDescriptor:
            self.patchDescriptor = PatchDescriptor()
        
        self.patchDescriptor.field(name, value)
        
        return self
    
    def updateExpression(self, expression):
        if not self.patchDescriptor:
            self.patchDescriptor = PatchDescriptor()
        
        self.patchDescriptor.expression(expression)
        
        return self
        
    def runUpdateReportDescriptor(self):
        if not self.resource:
            self.resource= self.session.resourcesService().resource(self.path)
        
        self.resource.patchResource(self.patchDescriptor)
        
        return self
    
    def createQueryResource(self, query, label,language='sql', dataSourceURI=None):
        cquery = ClientQuery()
        cquery.setQuery(query)
        cquery.setDataSourceURI(dataSourceURI)
        cquery.setLanguage(language)
        cquery.setDescription("query 1 description")
        cquery.setLabel(label)
        if not self.resource:
            self.resource = self.session.resourcesService().resource(self.path + "_files")
            
        res = self.resource.createNew(cquery)
        print res.result.content
        return self
        
        
        
    
    