#encoding:utf-8

from mongoengine import Document, StringField, DateTimeField, DictField
from mongoengine import signals
from utils.dbutil import update_modified
# Create your models here.
class UploadConfig(Document):
    name = StringField(max_length=40, unique=True, required=True)
    method_name = StringField(max_length=40)
    
    bucket = StringField(max_length=40)
    default_policy = DictField(default={})
    callback_url = StringField(max_length=128)
    callback_body = StringField(max_length=128)
    
    download_domain = StringField(max_length=128)
    
    access_key = StringField(max_length=128)
    secret_key = StringField(max_length=128)
    
    created_at = DateTimeField(required=True)
    update_at = DateTimeField(required=True)
    
    
signals.pre_save.connect(update_modified) 