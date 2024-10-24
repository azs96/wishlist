from django.db import models

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Item(models.Model):
  name = models.CharField(max_length=200)
  memo = models.TextField(null=True, blank=True)
  price = models.IntegerField(default=0) # todo minとmaxにする？

  image = models.ImageField(upload_to='images/uploaded/', default=None, null=True, blank=True)

  detail_main = ImageSpecField(
    source = "image",
    processors = [ResizeToFill(640,640)],
    format = "jpeg",
    options = {"quality": 80}
  )

  purchased = models.BooleanField(default=False)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name