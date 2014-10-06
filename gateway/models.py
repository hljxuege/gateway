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
    url = DictField()

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
    access = DictField()

