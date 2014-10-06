#encoding:utf-8
'''
Created on Oct 6, 2014

@author: liuxue
'''
from djangotoolbox.fields import DictField
from django.db import models
class Method(models.Model):
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
    name = models.CharField(max_length=40, unique=True)
    desc = models.CharField(max_length=40)
    server = models.ForeignKey('Server')
    url = DictField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Appkey(models.Model):
    '''
    {
        'name':name,
        'access':{
                'method_id':v,
                ...
        }
    }
    '''
    name = models.CharField(max_length=40, unique=True)
    secert_key = models.CharField(max_length=40)
    desc = models.CharField(max_length=40)
    access = DictField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Server(models.Model):
    name = models.CharField(max_length=40, unique=True)
    desc = models.CharField(max_length=40)
    ip = models.CharField(max_length=40)
    port = models.IntegerField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
