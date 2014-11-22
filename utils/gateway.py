#encoding:utf-8
'''
Created on Nov 22, 2014

@author: liuxue
'''
from hashlib import sha1
import binascii
import hmac
import urllib
import uuid
import time
def get_gateway_sign(base_url, secret_key, args):
    base_str = urllib.quote(base_url).replace("/", "%2F")
    args_str = urllib.quote(urllib.urlencode(sorted(args.items(), key=lambda t:t[0])))
    url_str = '%s%s'%(base_str, args_str)
    hashed = hmac.new(secret_key, url_str, sha1)
    # The signature
    return binascii.b2a_base64(hashed.digest())[:-1]

def get_url(gateway_url, serverkey, appsecret, method, api_version, **kwargs):
    nonce = '%s'%uuid.uuid1()
    timestamp = '%s'%int(time.time())
    p = {'serverkey':str(serverkey),
         'method':method,
         'api_version':api_version,
         'timestamp':timestamp,
         'nonce':nonce
         }
    p.update(kwargs)
    print p
    sign = get_gateway_sign(gateway_url, appsecret, p)
    query = urllib.urlencode(p)
    request_url = '%s?%s&%s'%(gateway_url, query, urllib.urlencode(dict(sign=sign)))
    return request_url