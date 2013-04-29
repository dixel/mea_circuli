#/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado import ioloop
from tornado import httpclient
import re

YURL = "http://moikrug.ru/companies/all/?submitted=1&city_did=%d&page=%d"
COOKIE = "Session_id=noauth:1367149129; yandexuid=4408014941367149129; mkrs=qdv9599hn0v3bnbderpto5uik1"

class CompanYGetter(object):
    def __init__(self, result, yurl = YURL, cookie = COOKIE, city = 679):
        self.yurl = YURL
        self.cookie = COOKIE
        self.res_file = result
        self.cnt = 0
        self.res = []
        self.pool = dict([(k, False) for k in range(5)]) # pool size = 5
        self.city = city
        self.page = 1
        self.traverse = True
        self.companys = []

    def start_process(self):
        self.client = httpclient.AsyncHTTPClient()
        self.headers = {"Cookie": self.cookie}
        for k in self.pool:
            self.request(k, self.page)
        ioloop.IOLoop.instance().start()

    def request(self, worker, page):
        url = self.yurl % (self.city, page)
        request = httpclient.HTTPRequest(
            url = url,
            headers = self.headers,
            connect_timeout=310,
            request_timeout=310
            )
        self.pool[worker] = True
        try:
            current = self.page
            print "requesting: %s" % url
            self.client.fetch(request, lambda r: self._handle_request(r, worker))
        except:
            self.pool[worker] = False
            self._dispatch(worker, current)
        self.page += 1

    def _dispatch(self, worker, page):
        if not self.traverse:
            if self._pool_free():
                f = open(self.res_file, 'a+')
                f.write(",".join(self.companys))
                f.close()
                ioloop.IOLoop.instance().stop()
        else:
            self.request(worker, page)

    def _pool_free(self):
        if True in self.pool.values():
            return False
        else:
            return True

    def _handle_request(self, res, worker):
        if not res.error:
            companys = set(re.findall("(?<=http://moikrug.ru/companies/)\d+", res.body))
            print "found: %s" % companys
            if len(companys) == 0:
                self.traverse = False
            else:
                for i in companys:
                    self.companys.append(i)
        self.pool[worker] = False
        self._dispatch(worker, self.page)
