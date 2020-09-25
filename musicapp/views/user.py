from django.http import HttpResponseServerError
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import serializers
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        url = serializers.HyperlinkedIdentityField(
            view_name='user',
            lookup_field='id'
        )
        fields = ('id', 'url', 'username')


class UserView(ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()


    # def retrieve(self, request, pk=None):
    #     try:
    #         queryset = User.objects.all()
    #         user = get_object_or_404(queryset, pk=pk)
    #         serializer = UserSerializer(user, context={'request': request})
    #         return Response(serializer.data)
    #     except Exception as ex:
    #         return HttpResponseServerError(ex)

    # def list(self, request):
    #     serializer = UserSerializer(queryset, many=True, context={'request', request})
    #     return Response(serializer.data)