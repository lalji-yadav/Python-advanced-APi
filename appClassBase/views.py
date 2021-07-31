from django.shortcuts import render

# Create your views here.
from .models import Tech
from .serializers import TechSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics

from django.contrib.auth.models import User
from rest_framework import permissions



# class TechList(APIView):
#     def get(self, request, format=None):
#         obj = Tech.objects.all()
#         objSer = TechSerializer(obj, many=True)
#         return Response(objSer.data)
#
#     def post(self, request, format=None):
#         objSer = TechSerializer(data=request.data)
#         if objSer.is_valid():
#             objSer.save()
#             return Response(objSer.data, status=status.HTTP_201_CREATED)
#         return Response(objSer.errors, status=status.HTTP_400_BAD_REQUEST)

class TechList(generics.ListCreateAPIView):
    queryset = Tech.objects.all()
    serializer_class = TechSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TechDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tech.objects.all()
    serializer_class = TechSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class TechDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Tech.objects.get(pk=pk)
#         except Tech.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         obj = self.get_object(pk)
#         objSer = TechSerializer(obj)
#         return Response(objSer.data)
#
#     def put(self, request, pk, format=None):
#         obj = self.get_object(pk)
#         objSer = TechSerializer(obj, data=request.data)
#         if objSer.is_valid():
#             objSer.save()
#             return Response(objSer.data)
#         return Response(objSer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         obj = self.get_object(pk)
#         obj.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# def perform_create(self, serializer):
#     serializer.save(owner=self.request.user)

