from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


@api_view(['GET', 'POST'])
def student_list(request, format=None):
    if request.method == 'GET':
        obj = Student.objects.all()
        objSer = StudentSerializer(obj, many=True)
        print(objSer)
        return Response(objSer.data)

    elif request.method == 'POST':
        objSer = StudentSerializer(data=request.data)
        if objSer.is_valid():
            objSer.save()
            return Response(objSer.data, status=status.HTTP_201_CREATED)
        return Response(objSer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        obj = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        objSer = StudentSerializer(obj)
        return Response(objSer.data)

    elif request.method == 'PUT':
        objSer = StudentSerializer(obj, data=request.data)
        if objSer.is_valid():
            objSer.save()
            return Response(objSer.data)
        return Response(objSer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
