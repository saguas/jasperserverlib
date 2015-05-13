# -*- coding: utf-8 -*-
##############################################################################
#
#    jasperserverlib library module for Frappe
#    Copyright (C) 2015 Luis Fernandes
#
#    This file is a part of jasperserverlib library
#
#    jasperserverlib library is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    jasperserverlib library is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see [http://www.gnu.org/licenses/].
#
##############################################################################

from StringIO import StringIO
import json

try:
    from lxml import etree
except ImportError:
    import xml.etree.cElementTree as etree


class User(object):
    """
    Manage user inside the JasperServer
    """

    def __init__(self, js_connect):
        self._connect = js_connect
        self.url = js_connect._rest_url + '_v2/users'
    
    def search_json(self, query=''):
        headers = {'accept': 'application/json'}
        self._connect.headers.update(headers)
        
        res_json = self._connect.get(self.url, 'search=' + query)
        
        del self._connect.headers['accept']
        
        return json.loads(res_json)

    def create(self, login, user):
        """
        Create a new user, if exists it return status 403
        """
        
        headers = {'Content-type': 'application/json'}
        self._connect.headers.update(headers)
        
        res = self._connect.put(self.url + '/' + login, data=json.dumps(user))
        
        del self._connect.headers['Content-type']

        return res 

    def modify(self, login, user):
        """
        Modify an existent user, if not found return 404 not found
        """
        return self.create(login, user)

    def delete(self, login):
        """
        Delete user with the specied login.
        """
        return self._connect.delete(self.url + '/' + login)


class Role(object):
    """
    The role service allows administrators to view, create, edit, and delete role definitions. However, the role service does not define role membership
    """

    def __init__(self, js_connect):
        self._connect = js_connect
        self.url = js_connect._rest_url + '/role/'

    def search(self, query=''):
        """
        The Search method for the role service returns a list of roles
        that match the search string. Without query, all roles are listed.
        """
        list_roles = []
        content = self._connect.get(self.url + query)
        if content:
            tree = etree.XML(content)
            for role in tree.xpath('/roles/role/roleName'):
                list_roles.append(role.text)

        return list_roles

    def create(self, rolename):
        """
        Create a new role
        """
        role_rolename = 'ROLE_' + rolename.upper()
        root = etree.Element('role')
        etree.SubElement(root, 'externallyDefined').text = 'false'
        etree.SubElement(root, 'roleName').text = role_rolename

        return self._connect.put(self.url, data=etree.tostring(root))

    def modify(self, rolename):
        """
        Modify an existent role
        """
        if 'ROLE_' in rolename:
            role_rolename = rolename

        else:
            role_rolename = 'ROLE_' + rolename.upper()

        root = etree.Element('role')
        etree.SubElement(root, 'externallyDefined').text = 'false'
        etree.SubElement(root, 'roleName').text = role_rolename

        return self._connect.post(self.url + '/' + role_rolename, data=etree.tostring(root))

    def delete(self, rolename):
        """
        Delete an existent role, if not found return 404 not found
        """
        if 'ROLE_' in rolename:
            role_rolename = rolename

        else:
            role_rolename = 'ROLE_' + rolename.upper()

        return self._connect.delete(self.url + '/' + role_rolename)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
