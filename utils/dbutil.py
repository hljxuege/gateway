#encoding:utf-8
'''
Created on Mar 11, 2015

@author: liuxue
'''
import redis
from django.conf import settings

r = redis.StrictRedis(host='localhost', port=6379, db=0)


def utc_to_localtime(utc_datetime):
    return utc_datetime + settings.EIGHT

import datetime

def update_modified(sender, document):
    if not document.created_at:     
        document.created_at = datetime.datetime.now()

    document.update_at = datetime.datetime.now()