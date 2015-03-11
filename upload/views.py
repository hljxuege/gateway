#encoding:utf-8
import json

from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from qiniu import Auth

from upload.models import UploadConfig
from utils.dbutil import r
from gateway.views import gateway


@csrf_exempt
def upload_callback(request):
    token = request.POST['toekn']
    exits = r.exists(token)
    code = 1 
    if exits:
        code = 0
        set_method_name = r.get(token)
        
    return gateway(request)

ACCESS_KEY = "5vnrmvpnIqY-q7gTKsd-Pdw12jDcCaYUYbmpzqEh"
SECRET_KEY = "QmfYBTeRr9UWnxk-8RJbsFD98lB0ZR_mdQHekFWM"
def upload_token(request):
    name = request.GET['name']
    config = UploadConfig.objects.get(name=name)
    config.callback_url
    config.callback_body
    default_policy = config.default_policy
    
    policy = default_policy
    
    ex = 7200
    
    _token = ''  # 以_token为key 记录　该请求的　响应路径
    policy.update({'insertOnly':1,
               'callbackUrl':"http://298074.cicp.net:59295/upload/callback/", 
               'callbackBody':"name=$(fname)&hash=$(etag)&size=$(imageInfo.width)x$(imageInfo.height)&token=%s"%_token, 
               })

    r.setex(_token, 'SET_XXX_METHOD', ex)
    q = Auth(ACCESS_KEY, SECRET_KEY)
    # 上传策略仅指定空间名和上传后的文件名，其他参数仅为默认值
    token = q.upload_token('wm-test', None, ex, policy)
    return token



# def get_dnurl(key):
#     base_url = qiniu.rs.make_base_url('wm-test.u.qiniudn.com', key)
 
