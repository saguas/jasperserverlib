# -*- coding: utf-8 -*-


def setHeader(key, value, connect):
    
    #if key not in connect.headers.keys():
    #headers = {key: value}
    #connect.headers.update(headers)
    connect.headers.update({key: value})

def removeHeader(key, connect):
    if key in connect.headers.keys():
        del connect.headers[key]
