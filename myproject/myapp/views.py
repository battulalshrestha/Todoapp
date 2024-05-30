from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from myapp.models import Todo
from myapp.serializers import TodoModelSerializer
class TodoViewset(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
