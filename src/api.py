#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado import ioloop
from tornado import httpclient
from simplejson import loads

METHOD_MAPPING = {
    "staff": "company/staff?ids=",
    "positions": "person/positions?ids="
}

rec_count = 0

class MoiKrugApi(object):
    def __init__(self, 
            url="http://api.moikrug.ru/v1/", 
            token= "84935bc75606497ba24936057643b2a8"):
        self.url = url
        self.headers = {"Authorization:": "OAuth %s" % token}
        self.client = httpclient.AsyncHTTPClient()

    def req(self, req, callback, *args, **kwargs):
        url = self._get_url(req)
        request = httpclient.HTTPRequest(
            url = url,
            headers = self.headers)
        self.client.fetch(request, callback=lambda res: 
                self._handle_request(res, callback, *args, **kwargs))

    def start(self):
        ioloop.IOLoop.instance().start()

    def stop(self):
        ioloop.IOLoop.instance().stop()
        
    def _handle_request(self, response, callback, *args, **kwargs):
        callback(loads(response.body), *args, **kwargs)

    def _get_url(self, req):
        method = req[0]
        par = req[1]
        if type(par) == 'list':
            params = ", ".join(params)
        else:
            params = str(par)
        return "".join([self.url, METHOD_MAPPING.get(method, "my?test="), params])
