'''
Created on Dec 20, 2012

@author: kermit
'''

import logging

def initialize():
    logging.basicConfig(filename='berserk.log',
                        level=logging.DEBUG,
                        format='%(asctime)s %(message)s')

def log(something):
    print(something)
    logging.info(something)

initialize()
