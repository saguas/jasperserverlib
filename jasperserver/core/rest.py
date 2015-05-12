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

import urllib, base64
import requests
from exceptions import StatusException
from resource_services import ResourcesServices as rs
from reportingService import ReportingService as rps
import pprint
import logging
#import jasperserver as js
from session import Session
#import time

#_logger = logging.getLogger(jasperserver.__name__)
#js.set_logging(js.LOG_LEVELS['debug'])
pp = pprint.PrettyPrinter(indent=4)

_logger = logging.getLogger('jasperserver')

class Client(object):
    """
    Create a REST connection, with authentification
    This class implements Login service in JasperServer using the session cookie and the RESTful interface.
    """
    #headers = {
       #'User-Agent': 'JasperServer-Python',
    #}

    def __init__(self, url, username='jasperadmin', password='jasperadmin', resume=False, BasicAuth=False):
        print "in rest.py url {}".format(url)
        self.result = {}
        self.headers = {'User-Agent': 'JasperServer-Python'}
        self._url = url
        self._rest_url = url + '/rest'
        self.session = Session()
        self.content = None
        if BasicAuth:
            self.headers.update({"Authorization": "Basic " + base64.b64encode((username + ":" + str(password)).encode('ascii'))})
        if not resume:
            self._login(username, password)
        self.rs = None
        self.rps = None

    def _login(self, username, password):
        # Send POST authentification and retrieve the cookie
        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        headers.update(self.headers)
        params = {
                'j_username': username,
                'j_password': password,
        }

        #_logger.info("jasperserver _login request headers: {}".format(headers))
        response = requests.post(self._rest_url + '/login', data=params, headers=headers)
        statuscode = response.status_code
        if statuscode in StatusException:
            #raise JsException('Logging Error')
            raise StatusException[statuscode]()
            return self
        
       # _logger.info("jasperserver _login response headers: {}".format(response.headers))
        #if response.headers.get('set-cookie'):
        self.headers['Cookie'] = response.headers['set-cookie']
        
        self.session.setSessionId(self.headers['Cookie'])
        
        self.result["content"] = None
        self.result["response"] = None
        
        return self

    def logout(self):
        self.get(self._url + "/logout.html", params={'showPasswordChange':'null'})
        return self
        
    def resume(self, cookie):
        self.headers['Cookie'] = cookie
        _logger.info("jasperserver rest resume method called {}".format(cookie))
        self.session.setSessionId(self.headers['Cookie'])
        self.result["content"] = None
        self.result["response"] = None
        
        return self

    def get(self, url, params=''):
        # Send a http GET query
        headers = {}
        headers.update(self.headers)
        response = requests.get(self._clean_url(url), params=params, headers=headers)
        statuscode = response.status_code
        if statuscode in StatusException:
            raise StatusException[statuscode]()

        self.content = response.content
        self.response = response
        self.result["content"] = self.content
        self.result["response"] = self.response
        
        return self

    def put(self, url, data='', files='', uri='', params=''):
        # Send a single or multipart content
        headers = {}
        headers.update(self.headers)
        if files:
            data = {'ResourceDescriptor': data}
            files = {uri: open(files)}

        response = requests.put(self._clean_url(url), data=data, files=files, headers=headers)
        statuscode = response.status_code
        if statuscode in StatusException:
            raise StatusException[statuscode]()

        self.content = response.content
        self.result["content"] = self.content
        self.result["response"] = None
        
        return self

    def post(self, url, data='', files='', uri='', params=''):
        # Send a single or multipart content
        #if files:
        #    data = {'ResourceDescriptor': data}
        #    files = {uri: open(files)}

        headers = {}
        headers.update(self.headers)
        response = requests.post(self._clean_url(url), data=data, files=files, headers=headers, params=params)
        statuscode = response.status_code
        if statuscode in StatusException:
            raise StatusException[statuscode]()
        
        self.content = response.content
        self.result["content"] = self.content
        self.result["response"] = None
        
        return self
            
    def patch(self, url, data='', files='', uri='', params=''):
        # Send a single or multipart content
        #if files:
        #    data = {'ResourceDescriptor': data}
        #    files = {uri: open(files)}

        headers = {}
        headers.update(self.headers)
        response = requests.patch(self._clean_url(url), data=data, files=files, headers=headers, params=params)
        statuscode = response.status_code
        if statuscode in StatusException:
            raise StatusException[statuscode]()

        self.content = response.content
        self.result["content"] = self.content
        self.result["response"] = None
        
        return self

    def delete(self, url, params=''):
        # Delete a content
        headers = {}
        headers.update(self.headers)
        response = requests.delete(self._clean_url(url), headers=headers, params=params)
        statuscode = response.status_code
        if statuscode in StatusException:
            raise StatusException[statuscode]()

        self.content = response.content
        self.result["content"] = self.content
        self.result["response"] = None
        
        return self
        
        #type: "content" or "response"
    def getResult(self, rtype=None):
        return self.result.get(rtype.lower()) if rtype else self.result
        
    def resourcesService(self, makeNew=False):
        if not self.rs or makeNew:
            self.rs = rs(self)
        return self.rs
    
    def reportingService(self, makeNew=False):
        if not self.rps or makeNew:
            self.rps = rps(self)
        return self.rps

    def clearResources(self):
        self.rs = None
        return self

    def clearReporting(self):
        self.rps = None
        return self

    @staticmethod
    def _clean_url(url):
        return urllib.quote(url.replace('//', '/').replace('http:/', 'http://'), safe=':/')

    def __str__(self, ):
        return '%s Cookie: %s' % (self._url, self.headers.get('Cookie', ''))

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
