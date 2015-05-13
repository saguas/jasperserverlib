# -*- coding: utf-8 -*-
##############################################################################
#
#    jasperserverlib library module for OpenERP
#    Copyright (C) 2012 SYLEAM ([http://www.syleam.fr]) Christophe CHAUVET
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

from ResourceLookupDescriptor import ResourceLookupDescriptor

class ResourceDescriptor(ResourceLookupDescriptor):
    
    def __init__(self, resourceDescriptor={}):
        super(ResourceDescriptor, self).__init__([resourceDescriptor])