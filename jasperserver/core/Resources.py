# -*- coding: utf-8 -*-
##############################################################################
#
#    jasperserver library module for OpenERP
#    Copyright (C) 2012 SYLEAM ([http://www.syleam.fr]) Christophe CHAUVET
#
#    This file is a part of jasperserver library
#
#    jasperserver library is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    jasperserver library is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see [http://www.gnu.org/licenses/].
#
##############################################################################
import os
import json
import pprint
#from StringIO import StringIO

#from ResourceDescriptor import *
from common import setHeader, removeHeader
from resources_mime_type import ResourceFilesMimeType as rmt
from resource_search_param import ResourceSearchParameter as rsp
from ResourcesTypeResolverUtil import ResourcesTypeResolverUtil as ru
from resource_media_types import *
from PatchItem import PatchItem
from ClientFile import ClientFile
from RunReportAdapter import RunReportAdapter
from ReportParametersAdapter import ReportParametersAdapter


pp = pprint.PrettyPrinter(indent=4)

try:
    from lxml import etree
except ImportError:
    import xml.etree.cElementTree as etree


class Resources (object):
    '''
    an Resources instance implements resources service in JasperServer. You need an open session js_connect to use this service.
    the path is the URI to browse. This class implements resources service in JasperServer.
    You need an open session *js_connect* to use this service.
    *path* is the URI to browse.
    '''

    def __init__(self, js_connect):
        self._connect = js_connect
        self.url = js_connect._rest_url + '_v2/resources'
        self.params = {}

    def search(self):
        '''
        Browse the path. When used without arguments, it gives the list of resources in the folder specified in the URL.
        With the arguments, you can search for terms in the resource names or descriptions, search for all resources of a given *wstype*, and specify whether to search in subfolders.
        The *recursive* parameter is only used if a search criteria is specified (either *q* or *wstype*).
        This method return each found resource : name, type and uri in a dictionnary.
        '''
        setHeader('accept',rmt.JSON,self._connect)
        
        #params = {'q': description,
        #     'type': wstype,
        #     'recursive': recursive,
        #     'limit': item_max
        #}
        self.result = self._connect.get(self.url, params=self.params)
        
        return self
    
    def parameter(self, rsp_type, rsp_value):
        
        self.params[rsp_type] = rsp_value
        
        return self
    
    def getResult(self):
        
        result = self.result
        
        try:
            result = json.loads(result)
        except ValueError, e:
            pass
        
        return result


class Resource (object):
    '''
    an Resource instance implements resource service in JasperServer. you need an open session js_connect to use this service. *path* is the folder where methods will be used.
    '''

    def __init__(self, js_connect, path=''):
        self._connect = js_connect
        self.path = path
        self.url = js_connect._rest_url + '_v2/resources' + path
        self.params = {}
        
    def details(self):
        
        setHeader('accept','application/json',self._connect)
        self.result = self._connect.get(self.url, params=self.params)
        
        return self
    
    def parameter(self, rsp_type, rsp_value):
        
        self.params[rsp_type] = rsp_value
        
        return self
    
    def downloadBinary(self, file=True):
        
        #removeHeader('accept', self._connect)
        
        if not file:
            setHeader('accept','application/repository.file+json',self._connect)
        
        self.result = self._connect.get(self.url, params=self.params)
        
        #removeHeader('accept', self._connect)
        
        return self
        
    def serverInfo(self):
        setHeader('accept','application/json',self._connect)
        
        self.result = self._connect.get(self._connect._rest_url+"_v2/serverInfo")
        self.content = self.result.content
		
        return self
        
    def getResult(self):
        
        result = self.result
        
        try:
            result = json.loads(result)
        except ValueError, e:
            pass
        
        return result

    def createNew(self, resource):
        '''
        Create a simple resource or a resource with an attached file.
        *wsType* : type of the resource (see jasper web service documentation).
        If you send a file resource, you need an *uri_jrxmlfile*.
        '''
        rd = self.build_resourceDescriptor(resource)
        print rd
        self.result = self._connect.post(self.url, data=rd, params=self.params)
        return self
    
    def createOrUpdate(self, resource):
        '''
        Create a simple resource or a resource with an attached file.
        *wsType* : type of the resource (see jasper web service documentation).
        If you send a file resource, you need an *uri_jrxmlfile*.
        '''
        rd = self.build_resourceDescriptor(resource)
        self.result = self._connect.put(self.url, data=rd, params=self.params)
        return self
        
    def patchResource(self, patchDescriptor):
        #mimetype = ru.getMimeType(resourcename)
        setHeader('Content-type',rmt.JSON,self._connect)
        #rd = {'version': patchDescriptor.getVersion(), "patch":[]}
        rd = patchDescriptor.toString()
        
        print rd
        
        self.result = self._connect.patch(self.url, data=rd)
        
        return self
        
    def copyFrom(self, copyfrom):
        setHeader('Content-Location',copyfrom,self._connect)
        self.result = self._connect.post(self.url, params=self.params)
        return self
        
    def moveFrom(self, movefrom):
        setHeader('Content-Location',movefrom,self._connect)
        self.result = self._connect.put(self.url, params=self.params)
        return self
        
    def uploadFileBase64(self, resource):
        #setHeader('Content-Type', rmt.REPOSITORYFILEJSON, self._connect)
        #rd = resource.toString()
        rd = self.build_resourceDescriptor(resource)
        self.result = self._connect.post(self.url, data=rd, params=self.params)
        return self
    
    def uploadFileStream(self, resource):
        mimetype = resource.getMimeType()
        setHeader('Content-Type', mimetype, self._connect)
        setHeader('Content-Description', resource.getDescription(), self._connect)
        setHeader('Content-Disposition', "attachment; filename=%s" % resource.getLabel() , self._connect)
        pp.pprint(self._connect.headers)
        files = {"file": resource.getContent()}
        self.result = self._connect.post(self.url, files=files, params=self.params)
        return self
    
    def build_resourceDescriptor(self, resource):
        # Build the resource descriptor in resourceDescriptor tags XML
        # Returns a tuple with the string of the resourceDescriptor, and the uri of the file resource.
        mimetype = ru.getMimeType(resource)
        setHeader('Content-type',RESOURCE_MEDIA_TYPE_PREFIX + mimetype + '+json',self._connect)
        setHeader('accept',rmt.JSON,self._connect)
        #url = self.url + "?" + urllib.urlencode({"create Folder":False})
        return resource.toString()

    def delete(self):
        '''
        Delete a resource in the current path
        '''
        self._connect.delete(self.url, params=self.params)


class Report(object):
    '''
    This class implements the new rest_v2 service, only for running a report in the reports units path.
    '''

    def __init__(self, js_connect, path):
        self._connect = js_connect
        #self.url = js_connect._rest_url + '_v2/reports' + path + '/'
        self.reportUnitUri = path

    def run(self, name, output_format='pdf', page='', onepagepersheet=''):
        '''
        Create a report with rest_V2 service. you can export a specific *page* and select one page per sheet if you choose an XLS format.
        Return the binary content.
        '''
        params = None
        if page:
            params = {'page': page}
        if onepagepersheet:
            params['onePagePerSheet'] = onepagepersheet

        return self._connect.get(self.url + name + '.' + output_format, params=params)
    
    def prepareForRun(self, format, pages):
        return RunReportAdapter(self._connect, self.reportUnitUri, format, pages)
    
    def reportParameters(self, mandatoryId='', *otherIds):
        ids = None
        if mandatoryId:
            ids = [mandatory]
            for count, id in enumerate(otherIds):
                ids.append(id)
        return ReportParametersAdapter(self._connect, self.reportUnitUri, ids)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
