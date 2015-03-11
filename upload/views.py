#encoding:utf-8
from django.http.response import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from qiniu import Auth


@csrf_exempt
def upload_callback(request):
    print request
    return HttpResponse(json.dumps({'foo': 'bar'}), content_type="application/json")

ACCESS_KEY = "5vnrmvpnIqY-q7gTKsd-Pdw12jDcCaYUYbmpzqEh"
SECRET_KEY = "QmfYBTeRr9UWnxk-8RJbsFD98lB0ZR_mdQHekFWM"
def upload_token():
    _token = ''  # 以_token为key 记录　该请求的　响应路径
    q = Auth(ACCESS_KEY, SECRET_KEY)
    # 上传策略仅指定空间名和上传后的文件名，其他参数仅为默认值
    token = q.upload_token('wm-test', None, 7200, {'insertOnly':1,
                                                   'callbackUrl':"http://298074.cicp.net:59295/upload/callback/", 
                                                   'callbackBody':"name=$(fname)&hash=$(etag)&size=$(imageInfo.width)x$(imageInfo.height)&token=%s"%_token, 
                                                   })
    return token



# def get_dnurl(key):
#     base_url = qiniu.rs.make_base_url('wm-test.u.qiniudn.com', key)
 
