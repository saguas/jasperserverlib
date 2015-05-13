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


class JsException(Exception):
    """
    Global error for JasperQuery
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

###
## Error start with 4XX
##

class NoContent(JsException):
    """
    Error 204
    """
    def __init__(self, value='No Content'):
        self.value = value

class LicenceExpiredOrNotValid(JsException):
    """
    Error 302
    """
    def __init__(self, value='Licence Expired Or Not Valid'):
        self.value = value

class BadRequest(JsException):
    """
    Error 400
    """
    def __init__(self, value='Bad Request'):
        self.value = value


class Unauthorized(JsException):
    """
    Error 401
    """
    def __init__(self, value='Unauthorized'):
        self.value = value

class PaymentRequired(JsException):
    """
    Error 402
    """
    def __init__(self, value='Payment Required'):
        self.value = value

class Forbidden(JsException):
    """
    Error 403
    """
    def __init__(self, value='Forbidden'):
        self.value = value


class NotFound(JsException):
    """
    Raise this when error 404
    """
    def __init__(self, value='Not Found'):
        self.value = value

class MethodNotAllowed(JsException):
    """
    Raise this when error 405
    """
    def __init__(self, value='Method Not Allowed'):
        self.value = value

class NotAcceptable(JsException):
    """
    Raise this when error 406
    """
    def __init__(self, value='Not Acceptable'):
        self.value = value
        
class ProxyAthenticationRequired(JsException):
    """
    Raise this when error 407
    """
    def __init__(self, value='Proxy Athentication Required'):
        self.value = value

class RequestTimeOut(JsException):
    """
    Raise this when error 408
    """
    def __init__(self, value='Request Time-Out'):
        self.value = value

class Conflict(JsException):
    """
    Raise this when error 409
    """
    def __init__(self, value='Conflict'):
        self.value = value
        
class Gone(JsException):
    """
    Raise this when error 410
    """
    def __init__(self, value='Gone'):
        self.value = value
        
class LengthRequired(JsException):
    """
    Raise this when error 411
    """
    def __init__(self, value='Length Required'):
        self.value = value
        
class PreconditionFailed(JsException):
    """
    Raise this when error 412
    """
    def __init__(self, value='Precondition Failed'):
        self.value = value
        
class RequestEntityTooLarge(JsException):
    """
    Raise this when error 413
    """
    def __init__(self, value='Request Entity Too Large'):
        self.value = value
        
class RequestURITooLarge(JsException):
    """
    Raise this when error 414
    """
    def __init__(self, value='Request-URI Too Large'):
        self.value = value
        
class UnsupportedMediaType(JsException):
    """
    Raise this when error 415
    """
    def __init__(self, value='Unsupported Media Type'):
        self.value = value
        
class  RequestedRangeNotSatisfiable(JsException):
    """
    Raise this when error 416
    """
    def __init__(self, value='Requested Range Not Satisfiable'):
        self.value = value
        
class  ExpectationFailed(JsException):
    """
    Raise this when error 417
    """
    def __init__(self, value='Expectation Failed'):
        self.value = value
        
#Server Errors
class  InternalServerError(JsException):
    """
    Raise this when error 500
    """
    def __init__(self, value='Internal Server Error'):
        self.value = value
        
class  Not_Implemented(JsException):
    """
    Raise this when error 501
    """
    def __init__(self, value='Not Implemented'):
        self.value = value
        
class  BadGateway(JsException):
    """
    Raise this when error 502
    """
    def __init__(self, value='BadGateway'):
        self.value = value
        
class  ServiceUnavailable(JsException):
    """
    Raise this when error 503
    """
    def __init__(self, value='Service Unavailable'):
        self.value = value
        
class  GatewayTimeOut(JsException):
    """
    Raise this when error 504
    """
    def __init__(self, value='Gateway Time-Out'):
        self.value = value

class  HTTPVersionNotSupported(JsException):
    """
    Raise this when error 505
    """
    def __init__(self, value='HTTP Version Not Supported'):
        self.value = value


#custom 

class PathError(Exception):
    def __init__(self, message="Path is a necessary param"):

        # Call the base class constructor with the parameters it needs
        super(PathError, self).__init__(message)

        # Now for your custom code...
        self.message = message
        
class ResourceContentError(Exception):
    def __init__(self, message="Path is a necessary param"):

        # Call the base class constructor with the parameters it needs
        super(ResourceContentError, self).__init__(message)

        # Now for your custom code...
        self.message = message
        
class ReportNotFoundError(Exception):
    def __init__(self, message="Report not found. Try get report first."):

        # Call the base class constructor with the parameters it needs
        super(ReportNotFoundError, self).__init__(message)

        # Now for your custom code...
        self.message = message
        
class ReportRunError(Exception):
    def __init__(self, message="Report run error."):

        # Call the base class constructor with the parameters it needs
        super(ReportRunError, self).__init__(message)

        # Now for your custom code...
        self.message = message
        
class ReportJRXMLError(Exception):
    def __init__(self, message="Report jrxml error."):

        # Call the base class constructor with the parameters it needs
        super(ReportJRXMLError, self).__init__(message)

        # Now for your custom code...
        self.message = message
        
class InputControlUpdateError(Exception):
    def __init__(self, message="Report jrxml error."):

        # Call the base class constructor with the parameters it needs
        super(InputControlUpdateError, self).__init__(message)

        # Now for your custom code...
        self.message = message
# We can use StatusException as:
# status = '404'
# if status in StatusException:
#    raise StatusException[status]()
StatusException = {
    204: NoContent,
    302: LicenceExpiredOrNotValid,
    400: BadRequest,
    401: Unauthorized,
    402: PaymentRequired,
    403: Forbidden,
    404: NotFound,
    405: MethodNotAllowed,
    406: NotAcceptable,
    407: ProxyAthenticationRequired,
    408: RequestTimeOut,
    409: Conflict,
    410: Gone,
    411: LengthRequired,
    412: PreconditionFailed,
    413: RequestEntityTooLarge,
    414: RequestURITooLarge,
    415: UnsupportedMediaType,
    416: RequestedRangeNotSatisfiable,
    417: ExpectationFailed,
    #server Errors
    500: InternalServerError,
    501: Not_Implemented,
    502: BadGateway,
    503: ServiceUnavailable,
    504: GatewayTimeOut,
    505: HTTPVersionNotSupported
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
