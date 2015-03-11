#encoding:utf-8
'''
Created on Mar 11, 2015

@author: liuxue
'''
import os

import django.core.handlers.wsgi
import tornado.httpserver
import tornado.ioloop
from tornado.options import options, define, parse_command_line
import tornado.web
import tornado.wsgi

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gateway.settings")
from django.conf import settings

DEBUG = True
settings.DEBUG = DEBUG


if django.VERSION[1] > 5:
    django.setup()
    
define('port', type=int, default=8080)

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello from tornado')

def main():
    
    parse_command_line()
    wsgi_app = tornado.wsgi.WSGIContainer(
        django.core.handlers.wsgi.WSGIHandler())
    tornado_app = tornado.web.Application(
    [
      ('/hello-tornado', HelloHandler),
      (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': settings.STATICFILES_DIRS[0]}),
      ('.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
      ], **{'DEBUG':DEBUG})
    server = tornado.httpserver.HTTPServer(tornado_app)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()