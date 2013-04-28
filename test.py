#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.abspath("./src/"))

from krug import MoiKrugApi
from pretty import pp

def cb(response):
    pp(response)
    api.stop()

if __name__ == '__main__':
    api = MoiKrugApi()
    api.req(("staff", 548669435), cb)
    api.start()
