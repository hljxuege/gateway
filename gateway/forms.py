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
    