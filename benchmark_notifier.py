'''
Created on Nov 6, 2012

@author: kermit
'''

import time
from datetime import datetime

import SOAPpy

def notify_master(host='http://localhost:8088/', message="done", data=None):
#    p = SOAPpy.SOAPProxy(host)
#    try:
#        p.done(results="")
#    except AttributeError:
#        pass
    p = SOAPpy.SOAPProxy(host)
    try:
        p.done(results=data)
    except AttributeError:
        pass
