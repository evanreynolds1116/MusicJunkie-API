from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
# STATUS USER FOR DESTROY/UPDATE METHODS
from rest_framework import status
from musicapp.models import UserSpotify
from .user import UserSerializer


class UserSpotifySerializer(serializers.HyperlinkedModelSerializer):

    user = UserSerializer()

    class Meta:
        model = UserSpotify
        url = serializers.HyperlinkedIdentityField(
            view_name='user_spotify',
            lookup_field='id'
        )
        fields = ('id', 'url', 'user', 'display_name', 'spotify_id', 'profile_picture')
        depth = 2

class UserSpotifyView(ViewSet):

    def retrieve(self, request, pk=None):
        try: 
            user_spotify = UserSpotify.objects.get(pk=pk)
            serializer = UserSpotifySerializer(
                user_spotify, context={'request': request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):

        user_spotify = UserSpotify.objects.all()
        serializer = UserSpotifySerializer(
            user_spotify, many=True, context={'request': request})
        return Response(serializer.data)