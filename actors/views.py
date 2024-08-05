from rest_framework import generics
from actors.models import Actor
from actors.serializers import ActorSerializer
from rest_framework.permissions import IsAuthenticated
from permissions import GlobalPermissionClass


class ActorListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
