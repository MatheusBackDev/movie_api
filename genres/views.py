# import json
# from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import get_object_or_404
# from django.http import JsonResponse
from genres.models import Genre
from rest_framework import generics
from genres.serializers import GenreSerializer
from rest_framework.permissions import IsAuthenticated
from permissions import GlobalPermissionClass


class GenreListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


# ------------------------ Function Based View --------------------------
# @csrf_exempt
# def genre_create_list_view(request):
#     if request.method == 'GET':
#         genres = Genre.objects.all()
#         data = [{'id': genre.id, 'name': genre.name} for genre in genres]
#         return JsonResponse(data, safe=False)

#     elif request.method == 'POST':
#         data = json.loads(request.body.decode('utf-8'))
#         new_genre = Genre(name=data['name'])
#         new_genre.save()
#         return JsonResponse(
#             {'id': new_genre.id, 'name': new_genre.name},
#             status=201,
#         )


# @csrf_exempt
# def genre_detail_update_delete_view(request, pk):
#     genre = get_object_or_404(Genre, pk=pk)

#     if request.method == 'GET':
#         data = {'id': genre.id, 'name': genre.name}
#         return JsonResponse(data)

#     elif request.method == 'PUT':
#         data = json.loads(request.body.decode('utf-8'))
#         genre.name = data['name']
#         genre.save()
#         return JsonResponse(
#             {'id': genre.id, 'name': genre.name},
#             status=201,
#         )

#     elif request.method == 'DELETE':
#         genre.delete()
#         return JsonResponse(
#             {'message': 'Gênero excluído com succeso!'},
#             status=204,
#         )
# -----------------------------------------------------------------------
