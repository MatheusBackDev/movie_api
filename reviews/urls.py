from django.urls import path
from . import views


urlpatterns = [
    path('reviews/', views.ReviewListCreateView.as_view(), name='review_get_post'),
    path('reviews/<int:pk>/', views.ReviewDetailUpdateDeleteView.as_view(), name='review_get_put_delete'),
]
