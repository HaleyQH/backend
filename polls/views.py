from django.http import HttpResponse, FileResponse, StreamingHttpResponse
from django.shortcuts import render
from bson.objectid import ObjectId
from rest_framework.decorators import action
# Create your views here.
from .models import UserModel
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


# from rest_framework_mongoengine.viewsets import ModelViewSet


class UserViewSet(ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'])
    def query(self, request):
        theme = self.request.query_params.get('theme', None)
        query = self.request.query_params.get('query', None)
        data = [{'title': '基于深度学习的视频字幕技术研究',
                 'author': '刘千会',
                 'video': 'E:\\video.mp4',
                 }, {
                    'title': '基于深度学习的视频字幕技术研究',
                    'author': '刘千会',
                    'video': 'E:\\video.webm',
                }]
        return Response(data)

        # theme = self.request.query_params.get('theme', None)
        # query = self.request.query_params.get('query', None)
        # queryset = {
        #     'author': lambda x: UserModel.objects.all().filter(author=x),
        #     'title': lambda x: UserModel.objects.all().filter(title=x),
        # }[theme](query)
        #
        #
        # serializer = UserSerializer(queryset, many=True, context={'request': request})
        # return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def video(self, request):
        video = self.request.query_params.get('video', None)
        data = open(video, 'rb')
        return StreamingHttpResponse(data, content_type='video/mp4')
