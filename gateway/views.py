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

from gateway.forms import GatewayForm, MethodForm, ServerForm
from models import Method, Appkey, Server


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

def method_add(request):
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
        return render(request, 'method.html', {'form':f, 'action':reverse('method-add')})    

def method_modify(request, obj_id):
    '''
    @param obj_id: method id
    @param param: other attribute
    '''
    method = get_object_or_404(Method, id=obj_id)
    if request.method == 'POST':
        f = MethodForm(request.POST)
        if f.is_valid():
            return render(request, 'index.html')
    else:
        f = MethodForm()
        return render(request, 'method.html', {'method':method, 'action':reverse('method-modify')})  

def method_list(request, server_id):
    '''
    list the server_id 's method
    '''
    return render(request, 'method_list.html')
    
def server_add(request):
    '''
    @param name: 
    @param ip
    @param host: 
    '''
    if request.method == 'POST':
        _json = { "statusCode":"304", 
                "message":"success", 
                "navTabId":"", 
                "rel":"", 
                "callbackType":"", 
                "forwardUrl":"http://www.baidu.com", 
                "confirmMsg":"hello" }
        f = ServerForm(request.POST)
        if f.is_valid():
            server = Server()
            server.name = f.cleaned_data['name']
            server.desc = f.cleaned_data['desc']
            server.ip = f.cleaned_data['ip']
            server.port = f.cleaned_data['port']
            
            server.save()
                
            return HttpResponse(json.dumps(_json))
        else:
            _json = { "statusCode":"200", 
                "message":f.errors.values(), 
                "navTabId":"", 
                "rel":"", 
                "callbackType":"", 
                "forwardUrl":"http://www.baidu.com", 
                "confirmMsg":"" }
            return HttpResponse(json.dumps(_json))
    else:
        f = ServerForm()
        return render(request, 'server.html', {'form':f, 'action':reverse('server-add')})  

def server_modify(request):
    '''
    '''
    name = request.GET['name']
    
    if request.method == 'GET':
        
        server = Server.objects.get(name=name)
        return render(request, 'server.html', {'server':server, 'action':reverse('server-modify')+'?name='+name})
    else:
        _json = { "statusCode":"200", 
                "message":'', 
                "navTabId":"", 
                "rel":"", 
                "callbackType":"", 
                "forwardUrl":"http://www.baidu.com", 
                "confirmMsg":"" }
        
        f = ServerForm(request.POST)
        if f.is_valid():
            server = Server.objects.get(name=name)
            server.desc = f.cleaned_data['desc']
            server.ip = f.cleaned_data['ip']
            server.port = f.cleaned_data['port']
            server.save()
            _json.update({
                          'message':'success'
                          })
            return HttpResponse(json.dumps(_json))
        else:
            _json.update({
                          'message':f.errors.values()
                          })

            return HttpResponse(json.dumps(_json))
        
def server_list(request):
    '''
    '''
    servers = Server.objects.all()
    return render(request, 'server_list.html', {'servers':servers})
  
def appkey_add(request):
    '''
    @param name: 
    @param secert_key: 
    '''
    pass

def appkey_modify(request, obj_id):
    '''
    @param : 
    '''