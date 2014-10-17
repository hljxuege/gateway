#encoding:utf-8
'''
Created on Oct 6, 2014

@author: liuxue
'''
from django import forms
class GatewayForm(forms.Form):
    method = forms.CharField()
    version = forms.CharField()
    appkey = forms.CharField()
    nonce = forms.CharField()
    sign = forms.CharField()

class MethodForm(forms.Form): 
    name = forms.CharField()
    version = forms.CharField()
    url = forms.CharField()   
    
class ServerForm(forms.Form):
    name = forms.CharField()
    desc = forms.CharField()
    ip = forms.IPAddressField()
    port = forms.IntegerField()