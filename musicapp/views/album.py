"""View module for handling requests about park areas"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User
from musicapp.models import Album, UserSpotify
from rest_framework.decorators import action

class AlbumSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Album
        url = serializers.HyperlinkedIdentityField(
            view_name='album',
            lookup_field='id'
        )
        fields = ('id', 'album_artist', 'album_name', 'album_image', 'album_rating', 'album_id', 'user', 'user_id')
        depth = 2

class Albums(ViewSet):

    def create(self, request):

        # user = User.objects.get(pk=request.auth.user.id)   

        new_album = Album()
        new_album.user = request.auth.user
        # new_album.user_id = request.data["user_id"]
        new_album.album_artist = request.data["album_artist"]
        new_album.album_name = request.data["album_name"]
        new_album.album_image = request.data["album_image"]
        new_album.album_rating = request.data["album_rating"]
        new_album.album_id = request.data["album_id"]

        new_album.save()

        serializer = AlbumSerializer(
            new_album, context={'request': request})
    
        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        try: 
            album = Album.objects.get(pk=pk)
            serializer = AlbumSerializer(
                album, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):

        albums = Album.objects.filter(user=request.auth.user)
        serializer = AlbumSerializer(
            albums,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)

    def destroy(self, request, pk=None):

        try:
            album = Album.objects.get(pk=pk)
            album.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Album.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):

        album = Album.objects.get(pk=pk)
        # album.album_artist = request.data["album_artist"]
        # album.album_name = request.data["album_name"]
        # album.album_image = request.data["album_image"]
        album.album_rating = request.data["album_rating"]
        album.save()
        serializer = AlbumSerializer(
                album, context={'request': request})

        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
