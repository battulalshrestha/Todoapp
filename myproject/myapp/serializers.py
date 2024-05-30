from rest_framework import serializers 
from myapp.models import Todo
class TodoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
        
