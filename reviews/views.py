from rest_framework import generics
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from permissions import GlobalPermissionClass


class ReviewListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
