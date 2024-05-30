from django.db import models
class Todo(models.Model):
    title = models.CharField(max_length=30)
    des = models.TextField()
    image =models.FileField(upload_to="media/",max_length=200,null=True,default=None)
    is_completed = models.BooleanField(default=False)
# Create your models here. 
   