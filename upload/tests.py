#encoding:utf-8
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""


from qiniu import Auth
from qiniu.services.storage.uploader import put_file

ACCESS_KEY = "5vnrmvpnIqY-q7gTKsd-Pdw12jDcCaYUYbmpzqEh"
SECRET_KEY = "QmfYBTeRr9UWnxk-8RJbsFD98lB0ZR_mdQHekFWM"
def upload_token():
    q = Auth(ACCESS_KEY, SECRET_KEY)
    # 上传策略仅指定空间名和上传后的文件名，其他参数仅为默认值
    token = q.upload_token('wm-test', None, 7200, {'callbackUrl':"http://298074.cicp.net:59295/upload/callback/", 'callbackBody':"name=$(key)&fname=$(fname)&hash=$(etag)&size=$(imageInfo.width)x$(imageInfo.height)", \
                                                   'saveKey':'aaa$(year)$(mon)$(day)$(hour)$(min)$(sec).jpg', 
                                                   'mimeType':'image/jpg'})
    return token

def upload():
    pass


# def get_dnurl(key):
#     base_url = qiniu.rs.make_base_url('wm-test.u.qiniudn.com', key)
 
if __name__ == '__main__':
#     u_t = upload_token()
#     print u_t
#     key = '1.jpg'
#     ret, info = put_file(u_t, None, '/home/liuxue/Downloads/mahua-logo.jpg', check_crc=True)
#     print(info)
#     print ret

    import requests    
     
    q = Auth(ACCESS_KEY, SECRET_KEY)
     
    bucket = 'wm-test'
    key = '1.jpg'
    base_url = 'http://%s/%s?imageView2/1/w/200/h/200/interlace/1' % (bucket + '.u.qiniudn.com', key)
    private_url = q.private_download_url(base_url, expires=3600)
    print(private_url)
    r = requests.get(private_url)
    print  r.status_code 