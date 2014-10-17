#encoding:utf-8
'''
Created on Oct 6, 2014

@author: liuxue
'''
from django import forms
from .models import Server

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
    
    def clean(self):
        cleaned_data = super(ServerForm, self).clean()
        msg = ''
        same_name_server = Server.objects.filter(name=cleaned_data['name'])
        same_iport_server = Server.objects.filter(ip=cleaned_data['ip'], port=cleaned_data['port'])
        if same_name_server:
            msg = '%s already exist'%cleaned_data['name']
        if same_iport_server:
            msg = '%s %s already exist'%(cleaned_data['ip'], cleaned_data['port'])
        
        if msg:
            raise forms.ValidationError(msg)
        
        return cleaned_data