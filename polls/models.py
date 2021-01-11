from bson import ObjectId
from django.db import models
import mongoengine


# Create your models here.
#
# class UserModel(mongoengine.Document):
#     video = mongoengine.StringField(max_length=500)
#     author = mongoengine.StringField(max_length=100)
#     title = mongoengine.StringField(max_length=50)
#     content = mongoengine.StringField(max_length=500)
#
#     class Meta:
#         db_table = 'IR'


class UserModel(models.Model):
    video = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    content = models.CharField(max_length=500)

    class Meta:
        db_table = 'db'
# from mongoengine import connect
#
# connect('test', host='127.0.0.1')
# userModel = UserModel(title = 'aaa',author='aaa',content='nnn',video='999')
# userModel.save()
# print(userModel.id)
# print(userModel.id == str(userModel.id))
# print(str(userModel.id))
