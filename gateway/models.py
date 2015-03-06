#encoding:utf-8
'''
Created on Oct 6, 2014

@author: liuxue
'''
from mongoengine import Document, StringField, IntField, DateTimeField, \
DictField, ReferenceField, BooleanField
from mongoengine import signals
import datetime

def update_modified(sender, document):
    if not document.created_at:     
        document.created_at = datetime.datetime.now()

    document.update_at = datetime.datetime.now()

class Server(Document):
    name = StringField(max_length=40, unique=True, required=True)
    desc = StringField(max_length=40, required=True)
    ip = StringField(max_length=40, required=True)
    port = IntField(max_value=9999, min_value=1000, required=True)
    created_at = DateTimeField(required=True)
    update_at = DateTimeField(required=True)

    
class Method(Document):
    '''
    {
        'name':name,
        'url':{
                'v1':'/url/url/',
                'v2':'/url/url2/',
                'v3':'/url/url3/',
                ...
        }
    
    }
    '''
    name = StringField(max_length=40, unique=True)
    desc = StringField(max_length=40)
    server = ReferenceField(Server)
    url = DictField()
    need_login = BooleanField(required=True, default=False)
    created_at = DateTimeField(required=True)
    update_at = DateTimeField(required=True)

    
class Appkey(Document):
    '''
    {
        'name':name,
        'access':{
                'method_id':v,
                ...
        }
    }
    '''
    name = StringField(max_length=40, unique=True)
    secert_key = StringField(max_length=40)
    session_time = IntField(default=1200)# seconds
    desc = StringField(max_length=40)
    access = DictField(default={})
    created_at = DateTimeField(required=True)
    update_at = DateTimeField(required=True)

class UploadConfig(Document):
    name = StringField(max_length=40, unique=True)
    bucket = StringField(max_length=40)
    policy = DictField(default={})
    callback_url = StringField(max_length=128)
    callback_body = StringField(max_length=128)
    download_domain = StringField(max_length=128)
    created_at = DateTimeField(required=True)
    update_at = DateTimeField(required=True)
    
    
signals.pre_save.connect(update_modified)    
    
import settings
def utc_to_localtime(utc_datetime):
    return utc_datetime + settings.EIGHT