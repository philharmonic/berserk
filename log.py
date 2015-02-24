'''
Created on Dec 20, 2012

@author: kermit
'''

import logging

def initialize():
    logging.basicConfig(filename='berserk.log',
                        level=logging.INFO,
                        format='%(asctime)s %(message)s')

def log(something):
    print(something)
    logging.info(something)

def log_server(something):
    log('Server: {}'.format(something))

def log_client(something):
    log('Client: {}'.format(something))

initialize()
