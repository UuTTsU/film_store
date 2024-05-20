from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Film
from .serializers import FilmSerializer
from django.http import Http404
from django.http import HttpResponse
from .utils import Redis

class SelectFilmViews(APIView):
    def get(self, request):
        cached_data = Redis.get('CarAPICall')
        if cached_data:
            return Response(cached_data)
        films = Film.objects.all()
        serializer = FilmSerializer(films, many=True)
        Redis.set('CarAPICall', serializer.data)
        return Response(serializer.data)

class CreateFilmViews(APIView):
    def post(self, request):
        serializer = FilmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteFilmViews(APIView):
    def delete(self, request, pk, format=None):
        try:
            film = Film.objects.get(pk=pk)
        except Film.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        film.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def home(request):
    return HttpResponse("Welcome to the Film Store API")