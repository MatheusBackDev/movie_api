from django.urls import path
from . import views


urlpatterns = [
    path('genres/', views.GenreListCreateView.as_view(), name='genre_get_post'),
    path('genres/<int:pk>/', views.GenreDetailUpdateDeleteView.as_view(), name='genre_get_put_delete'),
]
