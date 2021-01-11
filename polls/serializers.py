# from mongoengine import ObjectIdField
# from rest_framework_mongoengine import serializers

from rest_framework import serializers
from .models import UserModel
# class UserSerializer(serializers.DocumentSerializer):
#
#     class Meta:
#         model = UserModel
#         field = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # _id = ObjectIdField()
    class Meta:
        model = UserModel
        fields = '__all__'
        # fields = ('url','author','title','content',)

# class UserDetailSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#             model = UserModel
#             fields = ('video',)

# class UserDetailSerializer(serializers.DocumentSerializer):
#     class Meta:
#         model = UserModel
#         field = '__all__'