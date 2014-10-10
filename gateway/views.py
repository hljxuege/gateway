#encoding:utf-8
'''
Created on Oct 6, 2014

@author: liuxue
'''
import json

from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from gateway.forms import GatewayForm, MethodForm
from models import Method, Appkey


def index(request):
    return render(request, 'index.html')

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
    @param: nonce 随机数 时间段内唯一
    @param:sign 签名：参数+nonce进行签名算法
    @param: appkey 应用标识
    @param: method 方法名称
    @param: version 方法的版本号
    @param: params 一系列方法的请求参数
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
            uri = method.url[_version]
        else:
            raise Exception('no url found')
        
        #get server's ip and host
        pass
        
        # combine ip port uri
        pass
    
        #request 
        pass
        #proess return
        
        data = {'status':0, 'msg':'ok'}
    except Exception, e:
        data = {'status':-1, 'msg':str(e)}
    return HttpResponse(json.dumps(data))

def add_method(request):
    '''
    @param name:  
    @param version: 
    @param url: 
    
    '''
    
    if request.method == 'POST':
        f = MethodForm(request.POST)
        if f.is_valid():
            return render(request, 'index.html')
    else:
        f = MethodForm()
        return render(request, 'method.html', {'form':f, 'action':reverse('add_method')})    

def modify_method(request, obj_id):
    '''
    @param obj_id: method id
    @param param: other attribute
    '''
    pass

def add_server(request):
    '''
    @param name: 
    @param ip
    @param host: 
    '''
    pass

def modify_server(request, obj_id):
    '''
    '''
    pass

def add_appkey(request):
    '''
    @param name: 
    @param secert_key: 
    '''
    pass

def modify_appkey(request, obj_id):
    '''
    @param : 
    '''