#encoding:utf-8
'''
Created on Oct 6, 2014

@author: liuxue
'''
import json

from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from gateway.forms import GatewayForm
from models import Method, Appkey


def _parse_request(request):
    
    if request.method == 'POST':
        form = GatewayForm(request.POST)
        q = request.POST

    else:
        form = GatewayForm(request.GET)
        q = request.GET
    
    if form.is_valid():
        pass
    else :
        raise ValidationError(form.errors)
    
    method = q['method']
    version = q['version']
    appkey = q['appkey']
    nonce = q['nonce']
    sign = q['sign']
    return appkey, method, version, nonce, sign

def gateway(request):
    '''
    @note: 
        nonce 随机数 时间段内唯一
        sign 签名：参数+nonce进行签名算法
        appkey 应用标识
        method 方法名称
        version 方法的版本号
        params 一系列方法的请求参数
    '''
    try:
        _appkey, _method, _version, _nonce, _sign = _parse_request(request)
        
        #check nonce
        pass
        
        #check sign
        
        #get method
        method = get_object_or_404(Method, name=_method)
        
        #get appkey
        appkey = get_object_or_404(Appkey, name=_appkey)
        
        if method.url.has_key(_version):
            url = method.url[_version]
        else:
            raise Exception('no url found')
        
        data = {'status':0, 'msg':'ok'}
    except Exception, e:
        data = {'status':-1, 'msg':str(e)}
    return HttpResponse(json.dumps(data))
    