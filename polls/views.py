from django.http import HttpResponse, FileResponse, StreamingHttpResponse
from django.shortcuts import render
from bson.objectid import ObjectId
from rest_framework.decorators import action
# Create your views here.
from 检索组pip包.源代码.search_utils import get_suggestion, search
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
        theme = self.request.query_params.getlist('theme[]', None)
        theme=','.join(theme)
        query = self.request.query_params.get('query', None)
        data = search(query, theme=theme)
        return Response(data)

        # data = [{'title': '基于深度学习的视频字幕技术研究',
        #          'author': '刘千会',
        #          'video': 'E:\\video.mp4',
        #          }, {
        #             'title': '基于深度学习的视频字幕技术研究',
        #             'author': '刘千会',
        #             'video': 'E:\\video.webm',
        #         }]
        # return Response(data)

    @action(detail=False, methods=['get'])
    def hint(self, request):
        query = self.request.query_params.get('query', None)
        data = get_suggestion(query)
        return Response(data)
