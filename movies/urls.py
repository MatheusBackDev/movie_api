from django.urls import path
from . import views


urlpatterns = [
    path('movies/', views.MovieListCreateView.as_view(), name='movie_get_post'),
    path('movies/<int:pk>/', views.MovieDetailUpdateDeleteView.as_view(), name='movie_get_put_delete'),
    path('stats/movies/', views.MovieStatsView.as_view(), name='stats_movies_get'),
]
