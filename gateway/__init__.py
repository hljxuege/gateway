from mongoengine import connect
connect('gateway')
# from mongoengine import Document, StringField, IntField, DateTimeField, \
# DictField, ReferenceField
# import datetime
# class Base(Document):
#     created_at = DateTimeField(required=True)
#     update_at = DateTimeField(required=True)
#     
#     meta = {'allow_inheritance': True}
#     
#     def save(self, *args, **kwargs):
#         if not self.created_at:
#             self.created_at = datetime.datetime.now()
#         self.update_at = datetime.datetime.now()
#         return super(Base, self).save(*args, **kwargs)
# 
# class Server(Base):
#     name = StringField(max_length=40, unique=True, required=True)
#     desc = StringField(max_length=40, required=True)
#     ip = StringField(max_length=40, required=True)
#     port = IntField(max_value=9999, required=True)
# 
#     
# class Method(Base):
#     '''
#     {
#         'name':name,
#         'url':{
#                 'v1':'/url/url/',
#                 'v2':'/url/url2/',
#                 'v3':'/url/url3/',
#                 ...
#         }
#     
#     }
#     '''
#     name = StringField(max_length=40, unique=True)
#     desc = StringField(max_length=40)
#     server = ReferenceField(Server)
#     url = DictField()
# 
# class Appkey(Base):
#     '''
#     {
#         'name':name,
#         'access':{
#                 'method_id':v,
#                 ...
#         }
#     }
#     '''
#     name = StringField(max_length=40, unique=True)
#     secert_key = StringField(max_length=40)
#     desc = StringField(max_length=40)
#     access = DictField(default={})
# 
# 
# if __name__ == '__main__':
#     a = Appkey.objects[0]
#     a.name = 'n12'
#     a.secert_key = 's20'
#     a.access = {}
#     a.save()
#     
#     s = Server.objects[0]
#     s.name = 's'
#     s.ip = '127.0.0.1'
#     s.desc = 'desc'
#     s.port = 20
#     s.save()
#     
#     m = Method.objects.get(id=u'5443b249ff3fce15c19a66ca')
#     m.name = 'm'
#     m.desc = 'desc'
#     m.server = s
#     m.url.update({
#                   'v3':'a/a/dad/ad'
#                   })
#     m.save()
#     print m.url
#     print m.id
#     
#     