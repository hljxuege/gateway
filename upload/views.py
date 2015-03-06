#encoding:utf-8
from django.http.response import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from qiniu import Auth
from qiniu.services.storage.uploader import put_file


@csrf_exempt
def upload_callback(request):
    print request
    return HttpResponse(json.dumps({'foo': 'bar'}), content_type="application/json")

ACCESS_KEY = "5vnrmvpnIqY-q7gTKsd-Pdw12jDcCaYUYbmpzqEh"
SECRET_KEY = "QmfYBTeRr9UWnxk-8RJbsFD98lB0ZR_mdQHekFWM"
def upload_token():
    q = Auth(ACCESS_KEY, SECRET_KEY)
    # 上传策略仅指定空间名和上传后的文件名，其他参数仅为默认值
    token = q.upload_token('wm-test', None, 7200, {'insertOnly':1,
                                                   'callbackUrl':"http://298074.cicp.net:59295/upload/callback/", 'callbackBody':"name=$(fname)&hash=$(etag)&size=$(imageInfo.width)x$(imageInfo.height)"})
    return token

def upload():
    pass


# def get_dnurl(key):
#     base_url = qiniu.rs.make_base_url('wm-test.u.qiniudn.com', key)
 
if __name__ == '__main__':
    u_t = upload_token()
    print u_t
    key = '1.jpg'
    ret, info = put_file(u_t, key, '/home/liuxue/Downloads/mahua-logo.jpg', check_crc=True)
    print(info)
    assert ret['key'] == key
    key = '1.jpg'
#     print upload_pic(u_t, key, '/home/liuxue/Downloads/mahua-logo.jpg')
#     print get_dnurl(key)