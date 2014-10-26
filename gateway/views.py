#encoding:utf-8
'''
Created on Oct 6, 2014

@author: liuxue
'''
import json

from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render

from gateway.forms import GatewayForm, MethodForm, ServerForm, AppkeyForm
from .models import Method, Appkey, Server
'''
json demo
            _json = { "statusCode":"200", 
            "message":"success", 
            "navTabId":"method-list", 
            "rel":"", 
            "callbackType":"closeCurrent", 
            "forwardUrl":"http://www.baidu.com", 
            "confirmMsg":"hello" }
'''
def response_json(**kwargs):
    json = { "statusCode":"200", 
            "message":"success", 
            "navTabId":"",#"method-list", 
            "rel":"", 
            "callbackType":"",#"closeCurrent", 
            "forwardUrl":"http://www.baidu.com", 
            "confirmMsg":"hello" }
    if kwargs:
        json.update(kwargs)
        if kwargs.has_key('message'):
            json.update({'statusCode':"300"})
    
    return json

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
def _parse_url(request):
    params = request.POST.dict()
    v_dict = {}
    u_dict = {}
    for k, v in params.items():
        if k.startswith('urls'):
            _k, _v = k.split('.')
            if _v == 'version':
                v_dict.update({
                          _k:v
                          })
            elif _v == 'suburl':
                u_dict.update({_k:v})
            else:
                pass
    
    url = {}
    for k, v in v_dict.items():
        url.update({v: u_dict[k]})
    
    return url

def method_add(request):
    '''
    @param name:  
    @param version: 
    @param url: 
    
    '''

    if request.method == 'POST':
        
        method = Method()
        method.name = request.POST['name']
        qs0 = Method.objects.filter(name=method.name)
        if qs0:
            _json = response_json(message='same name already exist')
        else:    
            method.desc = request.POST['desc']
            server_id = request.POST['server.id']
            method.server = Server.objects.get(id=server_id)
            # url 
            url = _parse_url(request)
            
            method.url.update(url)
            
            _json = response_json(navTabId="method-list", callbackType='closeCurrent')
            method.save()
            
        return HttpResponse(json.dumps(_json))
    else:
        f = MethodForm()
        return render(request, 'method.html', {'form':f, 'action':reverse('method-add')})    

def method_modify(request, method_id):
    '''
    @param obj_id: method id
    @param param: other attribute
    '''
    method = Method.objects.get(id=method_id)
    if request.method == 'POST':
        method.name = request.POST['name']
        qs0 = Method.objects.filter(name=method.name, id__ne=method_id)
        if qs0:
            _json = response_json(message='same name already exist')
            
        else:
            method.desc = request.POST['desc']
            server_id = request.POST['server.id']
            method.server = Server.objects.get(id=server_id)
            # url 
            url = _parse_url(request)            
            method.url.update(url)
            
            _json = response_json(navTabId="method-list", callbackType='closeCurrent')            
            method.save()
                
        return HttpResponse(json.dumps(_json))
    else:
        
        return render(request, 'method.html', {'method':method, 'action':reverse('method-modify', args=[method_id])})  

def method_list(request):
    '''
    list the server_id 's method
    '''
    methods = Method.objects.all()
    return render(request, 'method_list.html', {'methods':methods})

def methods(request):
    '''
    '''
    methods = Method.objects.all()
    return render(request, 'methods.html', {'methods':methods})
    
def server_add(request):
    '''
    @param name: 
    @param ip
    @param host: 
    '''
    if request.method == 'POST':
        f = ServerForm(request.POST)
        if f.is_valid():
            
            
            server = Server()
            server.name = f.cleaned_data['name']
            server.desc = f.cleaned_data['desc']
            server.ip = f.cleaned_data['ip']
            server.port = f.cleaned_data['port']
            
            qs0 = Server.objects.filter(name=server.name)
            qs1 = Server.objects.filter(ip=server.ip, port=server.port)
            if qs0:
                _json = response_json(message='same name already exist')
            elif qs1:
                _json = response_json(message='same ip or port already exist')
            else:
                _json = response_json(navTabId="server-list", callbackType='closeCurrent')
                server.save()
                
            return HttpResponse(json.dumps(_json))
        else:
            _json = response_json(navTabId='', message=f.errors.values())
            return HttpResponse(json.dumps(_json))
    else:
        f = ServerForm()
        return render(request, 'server.html', {'form':f, 'action':reverse('server-add')})  

def server_modify(request, server_id):
    '''
    '''
    server = Server.objects.get(id=server_id)
    if request.method == 'GET':        
        return render(request, 'server.html', {'server':server, 'action':reverse('server-modify', args=[server_id])})
    else:
        
        f = ServerForm(request.POST)
        if f.is_valid():
            server.desc = f.cleaned_data['desc']
            server.ip = f.cleaned_data['ip']
            server.port = f.cleaned_data['port']
            qs0 = Server.objects.filter(name=server.name, id__ne=server_id)
            qs1 = Server.objects.filter(ip=server.ip, port=server.port, id__ne=server_id)
            if qs0:
                _json = response_json(message='same name already exist')
            elif qs1:
                _json = response_json(message='same ip or port already exist')
            else:
                server.save()
                _json = response_json(navTabId='server-list', callbackType='closeCurrent')
        
        else:
            _json = response_json(navTabId='', message=f.errors.values())

        return HttpResponse(json.dumps(_json))
        
def server_list(request):
    '''
    '''
    servers = Server.objects.all()
    return render(request, 'server_list.html', {'servers':servers})

def servers(request):
    servers = Server.objects.all()
    return render(request, 'servers.html', {'servers':servers})

def _parse_access(request):
    params = request.POST.dict()
    m_dict = {}
    v_dict = {}
    for k, v in params.items():
        if k.startswith('access'):
            _k, _v = k.split('.')
            if _v == 'method':
                m_dict.update({_k:v})
            elif _v == 'version':
                v_dict.update({_k:v})
            else:
                pass
    
    access = {}
    for k, v in m_dict.items():
        access.update({v: v_dict[k]})
    
    msg = []
    if access:
        aks = access.keys()
        mds = Method.objects.filter(name__in=aks)
        
        for a in aks:
            method = None
            for m in mds:
                if m.name == a:
                    method = m
                    
            if method:
                v = access[a]
                if method.url.has_key(v):
                    pass
                else:
                    msg.append('no name %s with version%s'% (a, v))
            else:
                msg.append('no name %s'% a)
            
    return access, ','.join(msg)

def appkey_add(request):
    '''
    @param name: 
    @param secert_key: 
    '''
    if request.method == 'GET':        
        return render(request, 'appkey.html', {'action':reverse('appkey-add')})
    else:
        
        f = AppkeyForm(request.POST)
        if f.is_valid():
            appkey = Appkey()
            appkey.desc = request.POST['desc']
            appkey.secert_key = request.POST['secert_key']
            appkey.name = request.POST['name']
            qs0 = Appkey.objects.filter(name=appkey.name)
            if qs0:
                _json = response_json(message='same name already exist')
            else:
                #access 
                access, msg = _parse_access(request)  
                if msg:
                    _json = response_json(message=msg)
                else:                 
                    appkey.access.update(access)
                    
                    appkey.save()
                    _json = response_json(navTabId='appkey-list', callbackType='closeCurrent')
        
        else:
            _json = response_json(message=f.errors.values())

        return HttpResponse(json.dumps(_json))

def appkey_modify(request, appkey_id):
    '''
    @param : 
    '''
    appkey = Appkey.objects.get(id=appkey_id)
    if request.method == 'GET':        
        return render(request, 'appkey.html', {'appkey':appkey, 'action':reverse('appkey-modify', args=[appkey_id])})
    else:
        
        f = AppkeyForm(request.POST)
        if f.is_valid():
            appkey.desc = request.POST['desc']
            appkey.secert_key = request.POST['secert_key']
            appkey.name = request.POST['name']
            qs0 = Appkey.objects.filter(name=appkey.name, id__ne=appkey_id)
            if qs0:
                _json = response_json(message='same name already exist')
            else:
                #access 
                access, msg = _parse_access(request)   
                if msg:
                    _json = response_json(message=msg)
                else:             
                    appkey.access.update(access)
                    
                    appkey.save()
                    _json = response_json(navTabId='appkey-list', callbackType='closeCurrent')
        
        else:
            _json = response_json(message=f.errors.values())

        return HttpResponse(json.dumps(_json))

def appkey_list(request):
    appkeys = Appkey.objects.all()
    return render(request, 'appkey_list.html', {'appkeys':appkeys})