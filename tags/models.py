from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
# What tag applied to what object 

class Tag(models.Model):
    label= models.CharField(max_length=255)

class TaggedItam(models.Model):
    tag= models.ForeignKey(Tag, on_delete=models.CASCADE)
    #Type (product, video, article)
    #ID
    content_type=models.ForeignKey(ContentType,on_delete=models.CASCADE )
    object_id= models.PositiveIntegerField()
    content_object= GenericForeignKey()