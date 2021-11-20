from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer


class TodoListViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    model = Todo