#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.abspath("./src/"))

from api import MoiKrugApi
from pretty import pp
from get_companys import CompanYGetter

def cb(response):
    pp(response)
    api.stop()

if __name__ == '__main__':
    api = MoiKrugApi()
    api.req(("positions", 979227173), cb)
    api.start()
    cp = CompanYGetter("companys.csv", city=679)
    cp.start_process()
