#/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado import ioloop
from tornado import httpclient

YURL = "http://moikrug.ru/companies/all/?submitted=1&page="
COOKIE = "Session_id=noauth:1367149129; yandexuid=4408014941367149129; mkrs=qdv9599hn0v3bnbderpto5uik1"

class CompanYGetter(object):
    def __init__(self):
        self.cnt = 0
        self.res = []
        self.traverse = True
    def process_pages(self):
        pg = 1
        client = httpclient.AsyncHTTPClient()
        headers = {"Cookie": COOKIE}
        while self.traverse and pg < 100:
            url = "".join([YURL, str(pg)])
            request = httpclient.HTTPRequest(
                url = url,
                headers = headers)
            client.fetch(request, self._handle_request)
            pg += 1
        ioloop.IOLoop.instance().start()
    def _handle_request(self, res):
        print res
        self.traverse = False
        ioloop.IOLoop.instance().stop()
