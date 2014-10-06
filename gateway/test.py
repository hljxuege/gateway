'''
Created on Oct 6, 2014

@author: liuxue
'''
from gateway.models import Method, Appkey
method = Method()
method.name='liuxue'
method.url={'2':'v/v/v/v', 'a1':'v1'}
method.save()

appkey = Appkey()
appkey.name='201'
appkey.access = {method.id:'1'}
appkey.save()
