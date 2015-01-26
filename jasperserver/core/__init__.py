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

from resource_media_types import *
from resource_services import ResourcesServices
from rest import Client
from exceptions import JsException

        
def session(url, username='jasperadmin', password='jasperadmin', resume=False):
    #try:
    client = Client(url, username, password, resume)
    return client
    #except JsException:
    #    print 'Error Authentification FAIL!'
    #    sys.exit(1)
        

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
