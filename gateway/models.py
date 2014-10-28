#encoding:utf-8
'''
Created on Oct 6, 2014

@author: liuxue
'''
from mongoengine import Document, StringField, IntField, DateTimeField, \
DictField, ReferenceField, BooleanField
import datetime

class Server(Document):
    name = StringField(max_length=40, unique=True, required=True)
    desc = StringField(max_length=40, required=True)
    ip = StringField(max_length=40, required=True)
    port = IntField(max_value=9999, min_value=1000, required=True)
    created_at = DateTimeField(required=True)
    update_at = DateTimeField(required=True)
    
    
    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.now()
        self.update_at = datetime.datetime.now()
        return super(Server, self).save(*args, **kwargs)

    
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
    
    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.now()
        self.update_at = datetime.datetime.now()
        return super(Method, self).save(*args, **kwargs)
    
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
    desc = StringField(max_length=40)
    access = DictField(default={})
    created_at = DateTimeField(required=True)
    update_at = DateTimeField(required=True)
    
    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.now()
        self.update_at = datetime.datetime.now()
        return super(Appkey, self).save(*args, **kwargs)
    